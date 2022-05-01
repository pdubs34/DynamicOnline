import { State } from "./State"
import { Country } from "./Country"

class Address {

    constructor(street, city, state, zipCode, country) {
        this.street = street;
        this.city = city;
        this.state = state;
        this.zipCode = zipCode;
        this.country = country;
    }

    getStreet() {
        return this.street;
    }

    getCity() {
        return this.city;
    }

    getState() {
        return this.state;
    }

    gerZip() {
        return this.zipCode;
    }

    getCountry() {
        return this.country;
    }
}
