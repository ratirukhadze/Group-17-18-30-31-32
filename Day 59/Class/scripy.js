function Flight(flightId, land, takeoff, time, destination) {
    this.flightId = flightId;
    this.land = land;
    this.takeoff = takeoff;
    this.time = time;
    this.destination = destination;
}
let flight1 = new Flight("AI202", "Delhi", "Chhatrapati Shivaji Maharaj International Airport", "2 hours", "Mumbai");


console.log(`Flight ID: ${flight1.flightId}, land: ${flight1.land}, takeoff: ${flight1.takeoff}, time: ${flight1.time}, destination: ${flight1.destination}`);

