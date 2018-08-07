#include <Servo.h>
 char lectura;
// Declaramos la variable para controlar el servo
Servo servoMotor;
 
void setup() {
  // Iniciamos el monitor serie para mostrar el resultado
  Serial.begin(9600);
 
  // Iniciamos el servo para que empiece a trabajar con el pin 9
  servoMotor.attach(13);
}
 
void loop() {
  if (Serial.available()>=1)
  {
    lectura = Serial.read();
    // Desplazamos a la posición 0º
    if (lectura == 'r'){
      servoMotor.write(2);
      // Esperamos 1 segundo
      //delay(1000);
    }

     else if (lectura == 's'){
      // Desplazamos a la posición 90º
      servoMotor.write(45);
      // Esperamos 1 segundo
      //delay(1000);
      }

    else if (lectura == 'd'){
    // Desplazamos a la posición 180º
    servoMotor.write(90);
    // Esperamos 1 segundo
    //delay(1000);
    }

    else if (lectura == 'l'){
      servoMotor.write(180);
    // Esperamos 1 segundo
    //delay(1000);
      }
    
  }
}
