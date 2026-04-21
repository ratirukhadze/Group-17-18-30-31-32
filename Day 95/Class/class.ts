interface user {
    name: string;
    age: number;
    ownPiano: boolean;
}
let object: user = {
    name: "Rati",
    age: 20,
    ownPiano: true
}


function rati({saxeli, gvari, asaki}: {saxeli: string, gvari: string, asaki: number}) {
    console.log(saxeli);
    console.log(gvari);
    console.log(asaki);
}