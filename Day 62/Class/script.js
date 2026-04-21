


fruits = ["apple", "orangea", "banana", "kiwi", "grapee"];
 citruss = fruits.slice(1, 3); 
 fruitStrings = fruits.join('-'); 
function processFruits(arr) {
    citruss = arr.slice(1, 3);
   fruitStrings = arr.join('-');
return fruitStrings;
}
console.log(processFruits(fruits)); 