#include "pitches.h"
 
// notes in the melody:
int melody[] = {
  NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5, NOTE_C6};
int duration = 500;  // 500 miliseconds
int pin=8;
void setup() {
 
}
 
void loop() {  
  for (int thisNote = 0; thisNote < 8; thisNote++) {
    // pin8 output the voice, every scale is 0.5 sencond
    tone(pin, melody[thisNote], duration);
     
    // Output the voice after several minutes
    delay(1000);
  }
   
  // restart after two seconds 
  delay(2000);
}