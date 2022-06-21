#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>
#include <LiquidCrystal.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

// initialize LCD with the arduino pin number it is connected to
const int rs = 7, en = 6, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

Servo serv;
int servPOS = 0;

boolean flag = true;

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);

  //set up rfid
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
  delay(4);       // Optional delay. Some board do need more time after init to be ready, see Readme
  //mfrc522.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader details
}

void loop() {
  // Print a message to the LCD.
  lcd.print("Toll Booth!");
  // set the cursor to column 0, line 1
  lcd.setCursor(0, 1);

  // Print a message to the LCD.
  lcd.print("Scan card to pay");
  // set the cursor to column 0, line 0
  lcd.setCursor(0, 0);

  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    lcd.clear();
    // Print a message to the LCD.
    lcd.print("Card detected!");
    // set the cursor to column 0, line 1
    lcd.setCursor(0, 1);
    delay(5000);
    flag = true;
    return;
  }

  String content = "";
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
    lcd.clear();
    // Print a message to the LCD.
    lcd.print("Please wait");
    // set the cursor to column 0, line 1
    lcd.setCursor(0, 1);
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();

  if (flag) {
    Serial.println(content);

    while (!Serial.available()) {
      ;
    }
    String registered = "";
    registered = Serial.readStringUntil('\n');
    int reg = registered.toInt();

    if (registered == "R") {
      Serial.println("bal");

      while (!Serial.available()) {
        ;
      }
      String acc_bal = "";
      acc_bal = Serial.readStringUntil('\n');
      int bal = acc_bal.toInt();
      int toll = 50;

      if (toll <= bal) {
        lcd.clear();
        // Print a message to the LCD.
        lcd.print("Toll charges:");
        // set the cursor to column 0, line 1
        lcd.setCursor(0, 1);
        lcd.print("Ksh. 50");
        lcd.setCursor(0, 0);
        delay(5000);

        // set the cursor to column 0, line 1
        int new_bal = bal - toll;
        Serial.println(new_bal);

        lcd.clear();
        // Print a message to the LCD.
        lcd.print("New balance:");
        // set the cursor to column 0, line 1
        lcd.setCursor(0, 1);
        lcd.print("Ksh. " + String(new_bal));
        lcd.setCursor(0, 0);
        delay(5000);
        lcd.clear();
      }

      else {
        lcd.clear();
        lcd.print("Insufficient!!!!");
        // set the cursor to column 0, line 1
        lcd.setCursor(0, 1);
        lcd.print("Top up account");
        lcd.setCursor(0, 0);
        delay(5000);
        lcd.clear();
      }
    }
    else {
      lcd.clear();
      // Print a message to the LCD.
      lcd.print("Unregistered card!!!");
      // set the cursor to column 0, line 1
      lcd.setCursor(0, 1);
      lcd.print("Call customer care");
      lcd.setCursor(0, 0);
      delay(5000);
      lcd.clear();
    }
  }

  flag = false;

}
