function Price(id, price, discount) {
    this.id = id;
    this.price = price;
    this.discount = discount;
    
    this.discountPrice = function() {
        return this.price - (this.price * this.discount / 100);
    };

}