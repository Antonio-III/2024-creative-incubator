int ledPin = 11;  // LED connected to pin 11
int btnPin = 2;   // Button connected to pin 2
int state = LOW;  // LED state

void setup() {
  pinMode(ledPin, OUTPUT);      // Set LED as an output
  pinMode(btnPin, INPUT_PULLUP); // Enable internal pull-up resistor
}

void loop() {

  if (state == LOW) {  // Button pressed
    state = !state;  // Toggle LED state
    digitalWrite(ledPin, state);
    delay(300);  // Debounce delay
  }
}