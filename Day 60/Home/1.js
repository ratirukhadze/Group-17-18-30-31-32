
const university = {
    name: "Tbilisi State University",
    departments: 10,
    website: "https://www.tsu.ge",
    ratings: {
        student1: 4.5,
        student2: 4.8,
        student3: 4.2
    }
};


for (const key in university) {
    console.log(`${key}:`, university[key]);
}


console.log('Has scholarship property:', university.hasOwnProperty('scholarship'));


const updatedUniversity = Object.assign({}, university, { studentsCount: 15000 });
console.log('With studentsCount:', updatedUniversity);


Object.freeze(university);
university.name = "Changed University"; 
console.log('After freeze attempt:', university.name);


console.log('Is frozen:', Object.isFrozen(university));





