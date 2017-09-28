from flask import Flask
app = Flask(__name__)


@app.route('/restaurants/')
def allRestaurants():
    return "This shows all the restaurants"


@app.route('/restaurants/new')
def newRestaurant():
    return "This makes a new restaurants"


@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This edits restaurants"


@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This deletes restaurants"


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    return "This shows restaurant menus"


@app.route('/restaurants/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
    return "This adds new restaurant menu"


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This edits restaurant menu"


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "This deletes restaurant menu"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
