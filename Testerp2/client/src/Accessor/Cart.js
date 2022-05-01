/* Cart class has a user to which it belongs to and a list of items 
which are in the cart */
import { User } from "./User"

class Cart {

    constructor(user, items) {
        this.user = user;
        this.items = items;
    }

    getUser() {
        return this.user;
    }

    getItems() {
        return this.items;
    }

    getSumOfItems() {
        //TODO: Add a method that gets the sum of all the items in the cart




        // var sum = 0;
        // const tempArray = this.items;
        // for(var i = 0; i < this.items.size; i++) {
        //     sum += tempArray[i].getPriceAfterSale(temp[i].itemId);
        // }
        // return sum;
    }

    addItem(itemName) {
        //TODO: Add an item to the cart
            
            // Add code to access database, get relevant values to fulfill the constraints of a new item
        
        // const newItem = getItemByName(itemName);
        // this.items.add(newItem);
    }
}
