(V2) 4 Degrees of Freedom Robotic Arm on Custom robot base powered by XRP

<img width="811" height="466" alt="Screenshot 2026-07-31 at 10 17 01 PM" src="https://github.com/user-attachments/assets/80adf379-1dde-40a7-ba33-98f8f8a776d5" />

About - This project was created during Hack Club's Macondo program. It uses a custom made chassis and adds onto it by using 4 MG995 servo motors and various different 3d printed objects to make a 4 degree of freedom robotic arm ontop of the robot. Throughout the next couple months, there will be many updates/upgrades to the software used to control the robot and will likely use a bluetooth webtool that is unique (but will first start using something like pestol.ink) and there will be updates to the hardware used (ex: custom board, new grabbing mechanisms, different chassis look, etc.)

Helpful links
XRP Code Editor - https://xrpcode.wpi.edu

OnShape CAD (full V2) (DISCLAIMER - the CAD model for the XRP wheel and the motor were not created by me)- https://cad.onshape.com/documents/8c0d30bc27f93aca9cecb3c5/w/34c3822477bc31986b632ba4/e/a49cac85e221fc7f59d26fd0
OnShape CAD (V1/V1.5 Claw) - https://cad.onshape.com/documents/94cab965c461ea71e610c3a8/w/6c71823ed011eed3911d8ce7/e/d39e55db9d4270f620e11d48

Orb Game Piece used to test claw (called "Rubble") - https://www.printables.com/model/1251185-2025-xrp-game-orbit-odyssey/files 

Instructions for V2 - 
1) Print out all pieces on OnShape file (wheel and wheel retainer and gear and grabber should have 2 of each) with the exception of the XRP motor and XRP included wheel; ideally out of Basic PLA
2) Take the base and the XRP motors with the sensor side being on the lower part of the motor area like picture below
   <img width="442" height="273" alt="Screenshot 2026-08-01 at 11 01 27 PM" src="https://github.com/user-attachments/assets/071c5fb8-8b02-4399-84d0-770056252db7" />
3) Place the motor retainers onto the top of the motor and line up the holes
4) Screw the retainer onto the drive base using 4 (2 per retainer) M3 6mm buttonhead screws
5) Attach the XRP board to the center of the robot base with the barrel-jack connector facing away from the wall using 4 M3 4mm screws using a M3 nut as a standoff between the board and the base
6) Connect the provided XRP battery to the board and plug in the left and right motors to the left and right motor slots on the board
7) Place battery in the area enclosed by the rectangle, should make battery sit at an angle
8) Then assemble the arm battery packs by make 2 sets of 2 2AA battery holders connected in series (Red wire of one connected to the Black of the Other) and then connect the two sets in parallel by connect the reds together and then the blacks together
9) Move these batteries to the area that is also occupied by the barrel-jack connector
10) Then attach the servo platform to the base using 4 M3 25mm socketheads
11) Attach the power rails of a breadboard to either side of the longer part of this servo platform
12) Attach a MG995 motor using 4 M3 4mm screws
13) Attach Servo horn (4 point) using included screw (all other servos need the circular horn)
14) Attach Joint 1 to the the servo horn using included screws where the slot for the motor wires should be facing the front (where the back is the numbers 1208)
15) Press another MG995 into the the square area with motor wire protect on the side of the slot
16) Replace the back plate on the servo for arm support bracket and do so for one more MG995
17) Slide the second joint by first sliding the bracket onto the support bracket and then orient it on the face of the servo horn, secure using included screws
18) Secure the second MG995 motor using 4 M3 6mm screws
19) Secure the third MG995 motor using 4 M3 4mm screws
20) Secure the claw onto the third MG995 by using the same method as the second joint
21) Insert the final motor into the claw shroud in a parallel manner to the arm and secure using 4 M3 4mm screws
22) Attach the two gears pointing forward and secure the one powered using included screws and the one that is static by placing it on the "pin" and then using the gear retainer and 1 M3 4mm screw to retain
23) Attach the claw grabbers were ends should be pointing towards each other and secure to the gears using 4 M3 6mm screws
    I think I missed a lot of steps in the in betweens (WORK IN PROGRESS)


Additional Electronics -
Follow the diagram, servo motor signal wires go to any of the 4 signal wires on the board for the way that you have configured as each motor
Additionally, this diagram doesn't take into account the use of a breadboard; distinct positive and negative lines have been made for a little ease of understanding.
<img width="636" height="365" alt="Screenshot 2026-07-29 at 11 29 17 PM" src="https://github.com/user-attachments/assets/750d6db5-0526-4979-a061-6bb8d70edd1c" />

