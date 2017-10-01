from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

app = Flask(__name__)
# The following codes will connect to the database
# and query it for data, so that it can be presented on the
# HTML page
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Fake Restaurants
# restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
#
# restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {
#     'name': 'Blue Burgers', 'id': '2'}, {'name': 'Taco Hut', 'id': '3'}]
#
#
# # Fake Menu Items
# items = [{'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
#           'price': '$5.99', 'course': 'Entree', 'id': '1'},
#        {'name': 'Chocolate Cake', 'description': 'made with Dutch Chocolate',
#           'price': '$3.99', 'course': 'Dessert', 'id': '2'},
#          {'name': 'Caesar Salad',
#           'description': 'with fresh organic vegetables',
#           'price': '$5.99', 'course': 'Entree', 'id': '3'},
#          {'name': 'Iced Tea', 'description': 'with lemon',
#           'price': '$.99', 'course': 'Beverage', 'id': '4'},
#          {'name': 'Spinach Dip',
#           'description': 'creamy dip with fresh spinach',
#           'price': '$1.99', 'course': 'Appetizer', 'id': '5'}]
# item = {'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
#         'price': '$5.99', 'course': 'Entree'}


@app.route('/restaurants/')
def allRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurants/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('allRestaurants'))
    else:
        return render_template('newRestaurant.html')


@app.route('/restaurants/<int:restaurant_id>/edit',  methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            session.add(editedRestaurant)
            session.commit()
            return redirect(url_for('allRestaurants'))
    else:
        return render_template(
            'editRestaurant.html', restaurant=editedRestaurant)


@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    deletedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        return redirect(url_for('allRestaurants'))
    else:
        return render_template(
            'deleteRestaurant.html', restaurant=deletedRestaurant)


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    return render_template('newMenuItem.html')


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    return render_template('editMenuItem.html', item=item)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deleteMenuItem.html', item=item)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
