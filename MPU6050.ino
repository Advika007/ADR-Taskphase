#include <Wire.h>
#include <Servo.h>

//importing libraries and defining motors
Servo rprop; //right motor
Servo lprop; //left motor

long accX , accY , accZ; //These variables will store accelerometer value from the data of the MPU reading.
float gFx , gFy , gFz;   //These variables will store gravitational force value in each axes.

long gyrX , gyrY ,gyrZ; //These variables will store gyro value from the data of the MPU reading.
float rotX, rotY, rotZ; //These variables will store rotational speed or velocity value in each axes.

float Acceleration_angle[2];
float Gyro_angle[2];
float Total_angle[2];

float elapsedTime , time , timePrev; //
int i;
float radtodeg = 180/3.141592654;

float PID, pwmleft, pwmright, error, prev_error;
float pid_p=0;
float pid_i=0;
float pid_d=0;

//Defining PID constants
double kp= 4;
double ki= 0.008;
double kd= 2.8;

double throttle= 1200; //intial value of throttle to the motor
float desired_angle=0; //It is a one dimension rig set up , hence horizontal angle will be zero.


void setup() {
  Wire.begin();
  Wire.beginTransmission(0x68); //This is the I2C address of the MPU( b1101000/b1101001 is low/high logic)
  Wire.write(0x6B); //Accessing the register 6B - Power Management (This register allows user to configure the power mode and clock source. It also provides a bit for resetting the entire device, and a bit for disabling the temperature sensor.)
  Wire.write(0);//Setting SLEEP register to 0.
  Wire.endTransmission(true); //stop : boolean,true will send a stop message, releasing the bus after transmission. false will send a restart, keeping the connection active.
  Serial.begin(9600);
  rprop.attach(3); //attach the right motor to pin 3
  lprop.attach(5); //attach the left motor to pin 5

  time= millis(); //Count time in milliseconds
  //Writes a value in microseconds (uS) to the servo.On standard servos a parameter value of 1000 is fully counter-clockwise, 2000 is fully clockwise, and 1500 is in the middle
  lprop.writeMicroseconds(1000); 
  rprop.writeMicroseconds(1000);
  delay(7000); //Give some delay, 7s, to have time to connect the propellers and let everything start up
} 

void loop() {
  timePrev= time; //Previous time is actual time
  time= millis(); //actual time
  elapsedTime= (time- timePrev)/1000; 
  recordAccelRegisters();
  //Now we can apply the Euler formula.
  //The atan will calculate the arctangent.
  //The pow(a,b) will elevate the a value to the b power.
  //sqrt function will calculate the rooth square
  Acceleration_angle[0] = atan(gFy/sqrt(pow(gFx,2))+ (pow(gFz,2))*radtodeg); //for X axis data
  Acceleration_angle[1] = atan(-1*(gFx)/sqrt(pow(gFy,2) + pow(gFz,2)))*radtodeg; //for Y axis data
  recordGyroRegisters();

  //We can apply complementary filter.
  //in order to obtain degrees we have to multiply the degree/seconds value by the elapsedTime.
   /*---X axis angle---*/
   Total_angle[0] = 0.98 *(Total_angle[0] + rotX*elapsedTime) + 0.02*Acceleration_angle[0];
   /*---Y axis angle---*/
   Total_angle[1] = 0.98 *(Total_angle[1] + rotY*elapsedTime) + 0.02*Acceleration_angle[1];
  
  printData();
  delay(500);

  //Now we apply PID
//We will implement the PID with just one axis.
//Error caluculation
error = Total_angle[1] - desired_angle;

//Calculating proportional value of the PID
//We multiply proportional constant and error

pid_p= kp*error;

//The integral part should only act if we are close to the desired position but we want to fine tune the error.
//So we give an if operation for error between -2 and 2 degree.
if(-2< error < 2)
{
  pid_i = pid_i + (ki*error);
}

//The last part is derivative caluculation. 
//The derivate acts upon the speed of the error.
//The speed is the amount of error that produced in a certain amount of time divided by that time.
// We will use a variable called previous_error.
//We substract that value from the actual error and divide all by the elapsed time. 

pid_d= kd*((error- prev_error)/elapsedTime);

PID = pid_p + pid_i + pid_d; //For final PID values we sum each parts.

if(PID < -1000)
{
  PID=-1000;
}
if(PID > 1000)
{
  PID=1000;
}


//Finnaly we calculate the PWM width.
//We sum the desired throttle and the PID value
pwmleft = throttle + PID;
pwmright = throttle - PID;

//If the throttle value of 1300, if we sum the max PID value we would have 2300us and that will mess up the ESC.
//we map the PWM values 

//Right
if(pwmright < 1000)
{
  pwmright= 1000;
}
if(pwmright > 2000)
{
  pwmright=2000;
}
//Left
if(pwmleft < 1000)
{
  pwmleft= 1000;
}
if(pwmleft > 2000)
{
  pwmleft=2000;
}

lprop.writeMicroseconds(pwmleft);
rprop.writeMicroseconds(pwmright);
prev_error = error; //Remember to store the previous error.

}


void recordAccelRegisters()
{
Wire.beginTransmission(0x68); //I2C address of the MPU
Wire.write(0x3B); //Starting register for accelerometer reading
Wire.endTransmission(false);
Wire.requestFrom(0x68,6); //Request accel registers (3B-40)
//In this case we request 6 registers.
//Each value of acceleration is made out of two 8bits registers, low values and high values.
//For that we request the 6 of them and just make then sum of each pair. 
//For that we shift to the left the high values register (<<) and make an or (|) operation to add the low values.
while(Wire.available()< 6);
accX = Wire.read()<<8|Wire.read(); //Stores first two bytes to be positioned in accX
accY = Wire.read()<<8|Wire.read(); //Stores middle two bytes to be positioned in accY
accZ = Wire.read()<<8|Wire.read(); //Stores last two bytes to be positioned in accZ
processAccelData();

}
//To obtain the values of acceleration in "g" units
//We first have to divide the raw values that we have just read by 16384.0 
//because that is the value that the MPU6050 datasheet gives us
void processAccelData() {
  gFx = accX / 16384.0;
  gFy = accY / 16384.0;
  gFz = accZ / 16384.0;
}

void recordGyroRegisters() {
  Wire.beginTransmission(0x68); //I2C address of the MPU
  Wire.write(0x43); //Starting register for gyro reading
  Wire.endTransmission(false);
  Wire.requestFrom(0x68,4); //Request gyro registers (43-46)
  while(Wire.available()< 4);
  gyrX = Wire.read()<<8|Wire.read();
  gyrY = Wire.read()<<8|Wire.read(); 
 
  processGyroData();
}


void processGyroData() {
  //Now in order to obtain the gyro data in degrees/seconda 
  //we have to divide first the raw value by 131 
  //because this is the value that the datasheet gives us
  rotX = gyrX / 131.0;
  rotY = gyrY / 131.0;
  rotZ = gyrZ / 131.0;
}
 
void printData() {
  Serial.print("Gyro (deg)");
  Serial.print("X=");
  Serial.print(rotX);
  Serial.print("Y=");
  Serial.print(rotY);
  Serial.print("Z=");
  Serial.print(rotZ);
  Serial.print("Accel (g)");
  Serial.print("X=");
  Serial.print(gFx);
  Serial.print("Y=");
  Serial.print(gFy);
  Serial.print("Z=");
  Serial.print(gFz);
  Serial.print("PID VALUE");
  Serial.print(PID);
  Serial.print("RIGHT MOTOR PWM");
  Serial.print(pwmright);
  Serial.print("LEFT MOTOR PWM");
  Serial.print(pwmleft);
  
}
