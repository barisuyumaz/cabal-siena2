#include <Keyboard.h>


#if ARDUINO > 10605
#include <Mouse.h>
#endif  //ARDUINO > 10605
#include <MouseTo.h>



String incomingByte;
String x;
int xplus = 1366;
int yplus = 768;
String y;
void setup() {
  Keyboard.begin();
  Mouse.begin();
  MouseTo.setCorrectionFactor(0.6738); // orjinali 0.6738 ornjinal 36
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) { 
      incomingByte = Serial.readStringUntil("\n");
      if (incomingByte.toInt() < 0){//KEYBOARD CONTROL
        
    
          if (incomingByte.toInt() == -1){
            Keyboard.print("1");            
          }
          
          else if (incomingByte.toInt() == -2){
            Keyboard.print("2");
          }  
                  
          else if (incomingByte.toInt() == -3){
            Keyboard.print("3V");        
          }  
             
          else if (incomingByte.toInt() == -4){
            Keyboard.print("4V");          
          }
          
          else if (incomingByte.toInt() == -5){
            Keyboard.print("5V");                    
          } 
        
          else if (incomingByte.toInt() == -6){
            Keyboard.print("6V");         
          }
           
          else if (incomingByte.toInt() == -7){
            Keyboard.print("7");
          }
           
          else if (incomingByte.toInt() == -8){
            Keyboard.print("8");            
          }
          
          else if (incomingByte.toInt() == -9){
            Keyboard.print("9");            
          }
          
          else if (incomingByte.toInt() == -10){
            Keyboard.print("0");            
          }
           
          else if (incomingByte.toInt() == -11){
            Keyboard.print("-");            
          }

          else if (incomingByte.toInt() == -12){
            Keyboard.print("=");            
          }          
          
          else if (incomingByte.toInt() == -13){ //yalap şalap vur
            
            for(int i = 0; i<3 ; i++){
            
            Keyboard.print("Z");
            delay(200);
            Keyboard.print("3");
            delay(1200);
            Keyboard.print("Z");
            delay(200);
            Keyboard.print("4");
            delay(1200);   
            Keyboard.print("Z");
            delay(200);
            Keyboard.print("5");
            delay(1200);          
            }
          }
          else if (incomingByte.toInt() == -14){
            Mouse.click();         
          }          
          else if (incomingByte.toInt() == -15){
            Keyboard.press(KEY_ESC);
            delay(250);  
            Keyboard.release(KEY_ESC);          
          } 
          else if (incomingByte.toInt() == -16){
            Keyboard.print("Z");         
          }             
          else if (incomingByte.toInt() == -17){
            Keyboard.print("3");
            Keyboard.print("Z");      
          }   
          else if (incomingByte.toInt() == -18){
            Keyboard.print("4");
            Keyboard.print("Z");        
          }   
          else if (incomingByte.toInt() == -19){
            Keyboard.print("5");
            Keyboard.print("Z");           
          }   
          else if (incomingByte.toInt() == -20){
            Keyboard.print("6");
            Keyboard.print("Z");         
          }       
          else if (incomingByte.toInt() == -21){
            Keyboard.press(KEY_F5);
            delay(250);
            Keyboard.release(KEY_F5);
            delay(750);
            Keyboard.press(KEY_ESC);
            delay(250);  
            Keyboard.release(KEY_ESC);
            delay(1250);
            Keyboard.print("Z"); 
          }
          else if (incomingByte.toInt() == -22){
            Keyboard.press(KEY_F6);
                
            delay(250);
            Keyboard.release(KEY_F6);
            //Keyboard.print("-");        
          }  
          else if (incomingByte.toInt() == -23){
            Keyboard.press(KEY_F7);
            delay(250);
            Keyboard.release(KEY_F7);            
          }  
          else if (incomingByte.toInt() == -24){
            Keyboard.press(KEY_F8);
            delay(250);
            Keyboard.release(KEY_F8);            
          }   
          else if (incomingByte.toInt() == -25){
            Keyboard.press(KEY_F9);
            delay(250);
            Keyboard.release(KEY_F9);            
          }
          else if (incomingByte.toInt() == -26){ // baslangictan - ikiz kulelere kadar part1-1



            
             delay(1000); // 1sn
             
            koordinat_gonder(568,560); //1sn
            Mouse.click();
            delay(1000); // 1sn
            
            
            Keyboard.print("8");
            delay(1000);
            Keyboard.print("9");
            delay(1000);
            Keyboard.press(KEY_F7);
            delay(250);
            Keyboard.release(KEY_F7);
              

          
             delay(1300); //1sn
             
             koordinat_gonder(47,391); // 1sn
             delay(1000);
             
             Mouse.click();
             
             delay(5000); // 5 sn
             
             Keyboard.press(KEY_ESC);
             delay(250);  
             Keyboard.release(KEY_ESC);  
             koordinat_gonder(582,395); // 1sn
             delay(1000);   
             Mouse.click();
             
             
              for (int i = 0; i < 4; i++) {
                delay(500);
                Keyboard.print("1");
                delay(1500);  // 4sn
              }
             
             koordinat_gonder(582,395); // 1sn
             delay(1000);   
             Mouse.click();
             delay(1000);
             Keyboard.print("1");
             
             koordinat_gonder(1342,141); // 1sn 
             Mouse.click();
             delay(5000); // 5sn
             koordinat_gonder(582,175); // 1sn
             Mouse.click();
             delay(3000); //3 sn
             koordinat_gonder(988,132); // 1sn
             Keyboard.print("1");
             delay(750); // 0.75sn
             koordinat_gonder(1362,598); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn
             koordinat_gonder(1169,512); //1sn
             Keyboard.print("1");
             delay(750); // 0.75sn  
             
          }  
          else if (incomingByte.toInt() == -27){
            delay(750); //0.75sn
            koordinat_gonder(989,48); //1sn
            Mouse.click();
            delay(4500); // 4.5 sn
            Keyboard.print("1");
            delay(1000); // 1sn
             koordinat_gonder(321,209); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn  
             koordinat_gonder(99,202); //1sn
             Keyboard.print("1");
             delay(750); // 0.75sn     
             koordinat_gonder(501,399); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn 
            Keyboard.press(KEY_F6);
            delay(250);
            Keyboard.release(KEY_F6);                        
                         
          }     
          else if (incomingByte.toInt() == -28){
            Keyboard.press(KEY_F4);
            delay(250);
            Keyboard.release(KEY_F4);                               
          }
          else if (incomingByte.toInt() == -29){
            Keyboard.press(KEY_F3);
            delay(250);
            Keyboard.release(KEY_F3);                               
          } 
          else if (incomingByte.toInt() == -30){
             koordinat_gonder(299,186); //1sn
             Keyboard.print("1");
             delay(750); // 0.75sn     
             koordinat_gonder(238,350); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn    
             koordinat_gonder(602,383); //1sn
             Mouse.click();
             delay(1500); // 1.5sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(290,690); //1sn
             Keyboard.print("1");
             delay(750); // 0.75sn    
             koordinat_gonder(447,726); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn       
          }
          else if (incomingByte.toInt() == -31){
             koordinat_gonder(765,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn      
             koordinat_gonder(324,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(612,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(947,524); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn  
             
              //MASANIN ORAYA GELDİN
             koordinat_gonder(735,433); //1sn
             Mouse.click();
             delay(1000); // 1sn 
             Keyboard.print("1");
             delay(1000); // 1sn
             Keyboard.press(KEY_ESC);
             delay(250);  
             Keyboard.release(KEY_ESC);  
             koordinat_gonder(735,433); //1sn
             Mouse.click();
             delay(1000); // 1sn 
             Keyboard.print("1");
             delay(1000); // 1sn 
             //MASANIN ORADA İŞİN BİTTİ
             
             koordinat_gonder(28,445); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(227,666); //1sn
             Keyboard.print("2");
             delay(1000); // 1sn 
             koordinat_gonder(206,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(206,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn
             Keyboard.print("Z");
          }  
          else if (incomingByte.toInt() == -32){
             koordinat_gonder(209,125); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn    
             koordinat_gonder(149,311); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn            
             koordinat_gonder(809,349); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn

            
            Keyboard.press(KEY_RIGHT_ARROW);
            delay(240);  
            Keyboard.release(KEY_RIGHT_ARROW);  
    
          }



           
          else if (incomingByte.toInt() == -33){  //DGNDEN ÇIKMAK İÇİN
            koordinat_gonder(1293,121); //1sn
            delay(300);
            Mouse.click();
            delay(1000);
            koordinat_gonder(638,450); //1sn
            Mouse.click();
            delay(1000);
          }       
          else if (incomingByte.toInt() == -34){
            koordinat_gonder(644,324); //1sn
            Mouse.click();
          }      
          else if (incomingByte.toInt() == -35){
            koordinat_gonder(405,203); //1sn
            Mouse.click();
            delay(1500);
            koordinat_gonder(738,595); //1sn
            Mouse.click();
            delay(1000);
          }
          else if (incomingByte.toInt() == -36){ // baslangictan - ikiz kulelere kadar oluncepart_2
             delay(1000); // 1sn
             Keyboard.print("8");
             delay(1000);
             Keyboard.print("9");
             delay(1000);
             Keyboard.press(KEY_F7);
             delay(250);
             Keyboard.release(KEY_F7);
             delay(1300); //1sn
             
             koordinat_gonder(47,391); // 1sn
             delay(1000);        
             Mouse.click();
             delay(5000); // 5 sn
             koordinat_gonder(1342,141); // 1sn 
             Mouse.click();
             delay(5000); // 5sn
             koordinat_gonder(582,175); // 1sn
             Mouse.click();
             delay(3000); //3 sn
             koordinat_gonder(988,132); // 1sn
             Keyboard.print("1");
             delay(750); // 0.75sn
             koordinat_gonder(1362,598); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn
             koordinat_gonder(1169,512); //1sn
             Keyboard.print("1");
             delay(750); // 0.75sn  
             
          }  
          else if (incomingByte.toInt() == -37){
             koordinat_gonder(765,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn      
             koordinat_gonder(324,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(612,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(947,524); //1sn
             Keyboard.print("2");
             delay(750); // 0.75sn  
    
             
             koordinat_gonder(28,445); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(227,666); //1sn
             Keyboard.print("2");
             delay(1000); // 1sn 
             koordinat_gonder(206,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             koordinat_gonder(206,767); //1sn
             Keyboard.print("1");
             delay(1000); // 1sn 
             Keyboard.print("Z");
          }
          else if (incomingByte.toInt() == -38){
            koordinat_gonder(680,507); //1sn
            Mouse.click();
          }  
                                                                            
      }
      
      else {                        //MOUSE CONTROL
          x = incomingByte;
          y = incomingByte;
          x.remove(4,4);
          y.remove(0,4);
          MouseTo.setTarget(0, 0); 
          while (MouseTo.move() == false) {}
          delay(500);
          MouseTo.setTarget(x.toInt()+3,y.toInt()+3  ,0);
          while (MouseTo.move() == false) {}
          delay(250);
          Mouse.click();  // kolon tıklatma burdada sekteye uğrayacak
          delay(400);
          Keyboard.print("1"); // kolon tıklatma için bozulmuş oldu şuan
          delay(500);
      }

  }
}







void koordinat_gonder(int kor1x, int kor2y){
          MouseTo.setTarget(0, 0); 
          while (MouseTo.move() == false) {}
          delay(500);
          MouseTo.setTarget(kor1x+3, kor2y+3 ,0);//+3
          while (MouseTo.move() == false) {}
          delay(250);
          //Mouse.click();  // kolon tıklatma burdada sekteye uğrayacak
          //delay(400);
          //Keyboard.print("1"); // kolon tıklatma için bozulmuş oldu şuan
          //delay(500);  
}





  
