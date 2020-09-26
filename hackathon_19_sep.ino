void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char msg = Serial.read();
    Serial.print("This is what I received: ");
    Serial.println(msg);

    switch (msg) {
      case 'A':
      case 'a':
        analogWrite(9, 0);
        break;
      case 'B':
      case 'b':
        analogWrite(9, 25);
        break;
      case 'C':
      case 'c':
        analogWrite(9, 50);
        break;
      case 'D':
      case 'd':
        analogWrite(9, 100);
        break;
      case 'E':
      case 'e':
        analogWrite(9, 125);
        break;
      case 'F':
      case 'f':
        analogWrite(9, 150);
        break;
      case 'G':
      case 'g':
        analogWrite(9, 175);
        break;
      case 'H':
      case 'h':
        analogWrite(9, 200);
        break;
      case 'I':
      case 'i':
        analogWrite(9, 225);
        break;
      case 'J':
      case 'j':
        analogWrite(9, 250);
        break;
    }
  }
}
