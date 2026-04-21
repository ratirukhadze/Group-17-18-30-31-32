
const cinema = {
    cinemaName: "Rustaveli Cinema",
    moviesCount: 8,
    location: "Tbilisi",
    movieReviews: {
        user1: "ძალიან კარგი გამოცდილება!",
        user2: "კარგი ფილმები და კომფორტული დარბაზი.",
        user3: "მომეწონა მომსახურება."
    }
};


for (let key in cinema) {
    console.log(`${key}:`, cinema[key]);
}


console.log("vipSeats" in cinema); 


const ticket = { ticketPrice: 15 };
const updatedCinema = Object.assign({}, cinema, ticket);
console.log(updatedCinema);

Object.freeze(updatedCinema);
updatedCinema.cinemaName = "Amirani Cinema"; 
console.log(updatedCinema.cinemaName); 


console.log(Object.isFrozen(updatedCinema)); 