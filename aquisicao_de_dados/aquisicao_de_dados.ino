const int s0 = 8;
const int s1 = 9;
const int s2 = 12;
const int s3 = 11;
const int out = 10;

//Pinos dos leds
int pinoledverm = 2;
int pinoledverd = 3;
int pinoledazul = 4;

//Variaveis que armazenam o valor das cores
int red = 0;
int green = 0;
int blue = 0;

void setup()
{
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(out, INPUT);
  pinMode(pinoledverm, OUTPUT);
  pinMode(pinoledverd, OUTPUT);
  pinMode(pinoledazul, OUTPUT);
  Serial.begin(9600);
  digitalWrite(s0, HIGH);
  digitalWrite(s1, HIGH);
}

void loop()
{
  color(); //Chama a rotina que le as cores
  //Mostra no serial monitor os valores detectados
  char c;
  if (Serial.available()){
    c = Serial.read();
      Serial.println("-------------------NOVO----------------------");
    for (int a = 0; a < 100; a++) {
      Serial.print(red, DEC);
      Serial.print(',');
      //Serial.print(" Verde : ");
      Serial.print(green, DEC);
      // Serial.print(" Azul : ");
      Serial.print(',');
      Serial.print(blue, DEC);
      Serial.print(",");
      Serial.print(c);
      Serial.println();
      delay(1);
    }
    //Aguarda 2 segundos, apaga os leds e reinicia o processo
    delay(200);
  }
}

void color()
{
  //Rotina que le o valor das cores
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  //count OUT, pRed, RED
  red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
  digitalWrite(s3, HIGH);
  //count OUT, pBLUE, BLUE
  blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
  digitalWrite(s2, HIGH);
  //count OUT, pGreen, GREEN
  green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
}


