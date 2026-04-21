function loveCalculator() {
    let name1 = prompt("შეიყვანეთ კაცის სახელი:"); 

    let name2 = prompt("შეიყვანეთ ქალის სახელი:");
    
    let percentag = Math.floor(Math.random() * 101); 
    
    alert(`${name1} და ${name2}, თქვენი სიყვარულის პროცენტია ${percentag}`);
}






loveCalculator();