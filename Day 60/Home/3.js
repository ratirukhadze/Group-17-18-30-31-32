
const hotel = {
    hotelName: "Grand Palace",
    stars: 5,
    location: "Tbilisi",
    guestReviews: {
        guest1: "Excellent service!",
        guest2: "Very clean and comfortable.",
        guest3: "Great location and friendly staff."
    }
};


console.log("Hotel properties and values:");
for (const key in hotel) {
    console.log(`${key}:`, hotel[key]);
}


console.log("Has 'spa' property:", hotel.hasOwnProperty('spa'));


const additionalInfo = { roomsCount: 120 };
const updatedHotel = Object.assign({}, hotel, additionalInfo);
console.log("Updated hotel with roomsCount:", updatedHotel);


Object.freeze(updatedHotel);
updatedHotel.stars = 3; 
console.log("After attempting to change stars:", updatedHotel.stars);


console.log("Is hotel object frozen?", Object.isFrozen(updatedHotel));