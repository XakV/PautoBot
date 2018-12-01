/* LED Blink, Teensyduino Tutorial #1
   http://www.pjrc.com/teensy/tutorial.html
 
   This example code is in the public domain.
*/



// the setup() method runs once, when the sketch starts

void setup() {
  // initialize the digital pin as an output.
  for (int i = 2; i < 10; i++) { // chose pins 2-9 
  pinMode(i, OUTPUT); // Set the pins as outposts
 }
}

// Define function to turn off all LEDs at the same time
void allLEDsOff(void) {
for (int i = 2; i <10; i++) {
digitalWrite(i, LOW);   
 }
}

// Switch on LEDs in sequence from left to right
void loop() {
  for (int i = 2; i < 9; i++) { //Run loop once for each LED
     allLEDsOff(); // Turn off all LEDs
   digitalWrite(i, HIGH); // Turn on current LED
   delay(200); //Delay of 200 ms,
               // then repeat loop to move on to next LED
}
for (int i = 9; i > 2; i--) { // Light LEDs from right to left
  allLEDsOff();
  digitalWrite(i, HIGH);
  delay(200); 
 }
}
