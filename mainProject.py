from flask import Flask, render_template
app = Flask(__name__)


@app.route('/restaurants/')
def allRestaurants():
    return render_template('restaurants.html')


@app.route('/restaurants/new')
def newRestaurant():
    return render_template('newRestaurant.html')


@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html')


@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html')


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    return render_template('menu.html')


@app.route('/restaurants/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
    return render_template('newMenuItem.html')


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return render_template('editMenuItem.html')


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deleteMenuItem.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
