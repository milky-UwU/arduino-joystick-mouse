const int PIN_X = A0;  
const int PIN_Y = A1;  
const int PIN_SW = 2;  

void setup() {
  Serial.begin(115200); 
  pinMode(PIN_SW, INPUT_PULLUP); 
}

void loop() {
  int x = analogRead(PIN_X);
  int y = analogRead(PIN_Y);
  int btn = digitalRead(PIN_SW);

  int inverted_y = 1023 - y; 

  Serial.print(x);
  Serial.print(",");
  Serial.print(inverted_y); 
  Serial.print(",");
  Serial.println(btn);

  delay(10);
}