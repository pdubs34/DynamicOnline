class Image {

    constructor(title, description, fileLocation) {
        this.title = title;
        this.description = description;
        this.fileLocation = fileLocation;
    }

    getTitle() {
        return this.title;
    }

    getDescription() {
        return this.description;
    }

    getFileLocation() {
        return this.fileLocation;
    }
}
