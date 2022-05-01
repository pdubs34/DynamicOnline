import { Cart } from "./Cart"
import { Category } from "./Category"
import { Image } from "./Image"

class Item {

    constructor(name, manufacturer, description, dimensions, weight, rating, SKU, image, basePrice) {
        this.name = name;
        this.manufacturer = manufacturer;
        this.description = description;
        this.dimensions = dimensions;
        this.weight = weight;
        this.rating = rating;
        this.SKU = SKU;
        this.image = image;
        this.basePrice = basePrice;
    }

    // Item that is in a cart
    constructor(name, manufacturer, description, dimensions, weight, rating, SKU, image, basePrice, cart, category) {
        this.name = name;
        this.manufacturer = manufacturer;
        this.description = description;
        this.dimensions = dimensions;
        this.weight = weight;
        this.rating = rating;
        this.SKU = SKU;
        this.image = image;
        this.basePrice = basePrice;
        this.cart = cart;
        this.category = category;
    }

    getName() {
        return this.name;
    }

    getManufacturer() {
        return this.manufacturer;
    }

    getDescription() {
        return this.description;
    }

    getDimensions() {
        return this.dimensions;
    }

    getWeight() {
        return this.weight;
    }

    getRating() {
        return this.rating;
    }

    getSKU() {
        return this.SKU;
    }

    getImage() {
        return this.image;
    }

    getBasePrice() {
        return this.basePrice;
    }

    getCart() {
        return this.cart;
    }
    
    getCategory() {
        return this.category;
    }

    getItemByName(itemName) {
        //TODO: Add code to access database, get relevant values to fulfill the constraints of a new item
        return newItem;
    }

    getPriceAfterSale(itemName) {
        //TODO: Calculate the new price of the item based on whether or not it is on sale
    }
}
