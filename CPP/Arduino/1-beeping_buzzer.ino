int buzzerPin=8; //definition digital 8 pins as pin to control the buzzer

void setup()
{
	pinMode(buzzerPin,OUTPUT); //Set digital 8 port mode, the OUTPUT for the output
}
void loop()
{  
	digitalWrite(buzzerPin,HIGH); //Set PIN 8 feet as HIGH = 5 v
	delay(1000);                   //Set the delay time，2000ms
	digitalWrite(buzzerPin,LOW);  //Set PIN 8 feet for LOW = 0 v
	delay(1000);                   //Set the delay time，2000ms
}