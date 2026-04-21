let Person = {
    name: 'Jack James',
    age: 30,
    proffesion: 'Software Engineer',
    country: 'USA',
    greet: function() {
        console.log(`Hello, my name is ${this.name}, I am ${this.age} years old, working as a ${this.proffesion} in ${this.country}.`);
    }
}


let book = {
    title: 'The Great Gatsby',
    author : 'F. Scott Fitzgerald',
    year: 1925,
    genre: 'Fiction',
    price: 10.99,

sasa: function() {
    console.log(`The book "${this.title}" was written by ${this.author} in ${this.year}. It is a ${this.genre} novel priced at $${this.price}.`);
}
};