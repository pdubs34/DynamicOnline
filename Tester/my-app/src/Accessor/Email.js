class Email {

    constructor(email) {
        this.email = email;
    }

    getEmail() {
        return this.email;
    }

    addEmail(newEmail) {
        //TODO: Add and email to email list
        this.email.add(newEmail);
    }
}
