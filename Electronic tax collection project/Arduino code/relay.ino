/*
   SIM800L SMS RELAY v2.0
   Arduino Uno (ATmega328P)
  CODED BY: KIPNGETICH E. TOWETT
*/

#include <SoftwareSerial.h>
SoftwareSerial gsm_sim800(3, 2); // (Rx,Tx  > Tx,Rx)

char usertext; //the SMS read by SIM800l
String command; //the command equivalent to the read SMS, usertext
int relay = 4; // Output for Relay Control

boolean low; //for SMS sending control purpose to only allow SIM800l to send one SMS instead of flooding the user’s phone with low moisture messages.

void setup() {
  Serial.begin(9600); //begin serial communication at 9600 baud rate
  gsm_sim800.begin(9600);

  while (!gsm_sim800.available()) {
    gsm_sim800.println("AT"); //initiate handshake between Arduino and SIM800l
    delay(1000); //time in milliseconds that the program has to wait before moving on to the next line of code
    Serial.println("Connecting...");
  }
  Serial.println("Connected!");
  gsm_sim800.println("AT+CMGF=1");  //Set SMS to Text Mode
  delay(100);
  gsm_sim800.println("AT+CNMI=1,2,0,0,0");  //Procedure to handle newly arrived messages
  delay(100);
  gsm_sim800.println("AT+CMGL=\"REC UNREAD\""); // Read Unread Messages
  delay(100);

  digitalWrite(relay, HIGH); // Initial state of the relay
  pinMode(relay, OUTPUT);
  low = true;
}

void loop()
{
  int sensor = analogRead(A0);//get the input from the sensor
  int mapped_value = map(sensor, 1020, 450, 0, 100); //Maps sensor value to the range 0 to 100%

  //gsm_sim800.println("AT+CMGDA=\"DEL ALL\"");// deletes messages in the inbox
  //delay(1000);

  if ((low) && (mapped_value < 70) && (digitalRead(relay) == HIGH)) {

    gsm_sim800.println("AT+CMGS=\"+254713209745\"");//phone number which receives texts from the system
    serial_comm();
    gsm_sim800.print("Moisture level below 70%"); //text content
    serial_comm();
    gsm_sim800.write(26);
    delay(500);

    low = false;//avoids repetitive sending of "low moisture" messages

  }

  // Serial Buffer
  while (gsm_sim800.available()) {

    usertext = gsm_sim800.read(); //reads text received from the user
    command += usertext; //stores the text from the user in string command
  }
  delay(1000);

  command.toUpperCase(); // toggles the Received Message to uppercase letters

  //turn RELAY ON or OFF
  if (command.indexOf("OFF") > -1) {
    digitalWrite(relay, HIGH);
    low = true;

    if (digitalRead(relay) == HIGH) {

      gsm_sim800.println("AT+CMGS=\"+254713209745\"");//phone number which receives texts from the system
      serial_comm();
      gsm_sim800.print("Motor stopped running. Moisture level is "); //text content
      gsm_sim800.print(mapped_value); //text content
      gsm_sim800.print("%."); //text content
      serial_comm();

      gsm_sim800.write(26);

      delay(1000);
    }
  }

  if (command.indexOf("ON") > -1) {
    digitalWrite(relay, LOW); //relay is active low hence state LOW activates it

    gsm_sim800.println("AT+CMGS=\"+254713209745\"");//phone number which receives texts from the system
    serial_comm();
    gsm_sim800.print("Motor started pumping. Moisture level is "); //text content
    gsm_sim800.print(mapped_value); //text content
    gsm_sim800.print("%"); //text content
    serial_comm();
    gsm_sim800.write(26);

    delay(100);
  }

  if (command.indexOf("LEVEL") > -1) {

    gsm_sim800.println("AT+CMGS=\"+254713209745\"");//phone number which receives texts from the system
    serial_comm();
    gsm_sim800.print("Moisture level: "); //text content
    gsm_sim800.print(mapped_value); //text content
    gsm_sim800.print("%"); //text content
    serial_comm();
    gsm_sim800.write(26);

    delay(100);
  }

  delay(50);

  command = "";

  if ((mapped_value > 80)&&(digitalRead(relay)== LOW)) {
    digitalWrite(relay, HIGH);
    low = true;

    gsm_sim800.println("AT+CMGS=\"+254713209745\"");//phone number which receives texts from the system
    serial_comm();
    gsm_sim800.print("Motor stopped running. Moisture level is "); //text content
    gsm_sim800.print(mapped_value); //text content
    gsm_sim800.print("%"); //text content
    serial_comm();
    gsm_sim800.write(26);

    delay(500);
  }
}

void serial_comm()
{
  delay(500);
  while (Serial.available())
  {
    gsm_sim800.write(Serial.read());//forward what Serial received to Software Serial Port
  }
  while (gsm_sim800.available())
  {
    Serial.write(gsm_sim800.read());//Forward what Software Serial received to Serial Port

  }
}
