#include <Servo.h>

Servo myservo;   

int pos = 0;
int cm = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT); 
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  return pulseIn(echoPin, HIGH);
}


void setup() {
  digitalWrite(12,LOW);
  myservo.attach(9); 
  Serial.begin(9600);
}

void loop() {
   cm = 0.01723 * readUltrasonicDistance(6, 7);

   Serial.print("Distance: ");
   Serial.print(cm);
   Serial.println(" cm");

   if (cm > 5 && cm < 30) { // Only activate if a real object is detected
      Serial.println("Object detected! Opening gate...");

      // open the gate
      for (pos = 0; pos <= 90; pos += 1) { 
         myservo.write(pos);             
         delay(15);                       
      }
      // hold gate open
      delay(1000);

      // close the gate
      for (pos = 90; pos >= 0; pos -= 1) { 
         myservo.write(pos);
         delay(15);                                     
      }
      // gate cannot open again for 3 seconds
      delay(3000);
   }                          
}