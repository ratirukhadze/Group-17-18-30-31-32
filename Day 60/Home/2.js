
const sportsClub = {
    clubName: "Dinamo Tbilisi",
    sportType: "Football",
    foundedYear: 1925,
    achievements: {
        title1: {
            name: "Soviet Top League",
            year: 1964
        },
        title2: {
            name: "Soviet Cup",
            year: 1976
        },
        title3: {
            name: "UEFA Cup Winners' Cup",
            year: 1981
        }
    }
};


console.log(Object.keys(sportsClub));


console.log(Object.values(sportsClub));


console.log(sportsClub.hasOwnProperty('sponsors'));


const updatedSportsClub = Object.assign({}, sportsClub, { stadiumCapacity: 55000 });
console.log(updatedSportsClub);


Object.freeze(updatedSportsClub);
updatedSportsClub.clubName = "Changed Name"; 
console.log(updatedSportsClub.clubName); 


console.log(Object.isFrozen(updatedSportsClub));