import { User } from "./User"
import { Cart } from "./Cart"
 
class Sale {
    
    constructor(user, startDate, endDate, cart, totalPrice) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.totalPrice = totalPrice;
        //Remove the totalPrice and change it to something like %discount or a flat rate that is taken off
    }

    getUser() {
        return this.user;
    }

    getStartDate() {
        return this.startDate;
    }

    getEndDate() {
        return this.endDate;
    }

    getCart() {
        return this.cart;
    }

    getTotalPrice() {
        return this.totalPrice;
    }
}
