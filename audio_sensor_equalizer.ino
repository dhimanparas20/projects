//-----------------------------------------------------------------
// Arduino code to make Equalizer using LED and Sound Sensor.     |
// Code by paras Dhiman Ken_kaneki_69 dhimanparas20               |
//-----------------------------------------------------------------

//===================================================================
// Pin configuration
// A0: Audio sensor, D1: Light1, D2: Light2, D3: Light3, D4: Light4 and so on till D8.
//===================================================================

// Configure your variables here:
int r1 = 583;     // Starting threshold of Light1
int r2 = 586;     // Starting threshold of Light2
int r3 = 589;     // Starting threshold of Light3
int r4 = 592;     // Starting threshold of Light4
int r5 = 595;     // Starting threshold of Light5
int r6 = 598;     // Starting threshold of Light6
int r7 = 601;     // Starting threshold of Light7
int r8 = 604;     // Starting threshold of Light8

int t1 = 60 ;     // Time gap for second light to turn on.
int t2 = 50 ;     // Time gap for second light to turn off


void setup() {                // Defining pins
Serial.begin(9600);  
pinMode(A0, INPUT);
pinMode(D0, INPUT); 
pinMode(D1, OUTPUT);
pinMode(D2, OUTPUT); 
pinMode(D3, OUTPUT);
pinMode(D4, OUTPUT);
pinMode(D5, OUTPUT);
pinMode(D6, OUTPUT);
pinMode(D7, OUTPUT);
pinMode(D8, OUTPUT);
}

// universal on/off control function.
void l(char p, int c){        //p stands for pin number and c stand for on or off command
  if (c == 1){
    digitalWrite(p,HIGH);     //on command
    delay(t1);
  }
  else if (c == 0){  
    digitalWrite(p,LOW);      //off command
    delay(t2);
  }
}

void loop() {                 // Drawing patterns
  int ard = analogRead(A0);   // Storing analog read values to a variable "ard".
  Serial.print(ard);          // Print read values on monitor
  Serial.print("\n");
  if(ard >=r1 && ard <r2){
     l(D1,1);
     l(D1,0);
  }
  else if(ard>=r2 && ard<r3){
    l(D1,1);
    l(D2,1);
    l(D2,0);
    l(D1,0);
  }
  else if (ard>=r3 && ard<r4){
    l(D1,1);
    l(D2,1);
    l(D3,1);
    l(D3,0);
    l(D2,0);
    l(D1,0);
  }
  else if (ard>=r4 && ard<r5){
    l(D1,1);
    l(D2,1);
    l(D3,1);
    l(D4,1);
    l(D4,0);
    l(D3,0);
    l(D2,0);
    l(D1,0);
  }
  else if (ard>=r5 && ard<r6){
    l(D1,1);
    l(D2,1);
    l(D3,1);
    l(D4,1);
    l(D5,1);
    l(D5,0);
    l(D4,0);
    l(D3,0);
    l(D2,0);
    l(D1,0);
  }
  else if (ard>=r6 && ard<r7){
    l(D1,1);
    l(D2,1);
    l(D3,1);
    l(D4,1);
    l(D5,1);
    l(D6,1);
    l(D6,0);
    l(D5,0);
    l(D4,0);
    l(D3,0);
    l(D2,0);
    l(D1,0);
  }
  else if(ard >=r7 && ard <r8){
    l(D1,1);
    l(D2,1);
    l(D3,1);
    l(D4,1);
    l(D5,1);
    l(D6,1);
    l(D7,1);
    l(D7,0);
    l(D6,0);
    l(D5,0);
    l(D4,0);
    l(D3,0);
    l(D2,0);
    l(D1,0);
  }
  else if(ard>=r8){
    l(D1,1);
    l(D2,1);
    l(D3,1);
    l(D4,1);
    l(D5,1);
    l(D6,1);
    l(D7,1);
    l(D8,1);
    l(D8,0);
    l(D7,0);
    l(D6,0);
    l(D5,0);
    l(D4,0);
    l(D3,0);
    l(D2,0);
    l(D1,0);
  }
} 
