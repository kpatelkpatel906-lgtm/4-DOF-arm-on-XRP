(V2) 4 Degrees of Freedom Robotic Arm on Custom robot base powered by XRP
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<img width="811" height="466" alt="Screenshot 2026-07-31 at 10 17 01 PM" src="https://github.com/user-attachments/assets/80adf379-1dde-40a7-ba33-98f8f8a776d5" />

About - This project was created during Hack Club's Macondo program. It uses a custom made chassis and adds onto it by using 4 MG995 servo motors and various different 3d printed objects to make a 4 degree of freedom robotic arm ontop of the robot. Throughout the next couple months, there will be many updates/upgrades to the software used to control the robot and will likely use a bluetooth webtool that is unique (but will first start using something like pestol.ink) and there will be updates to the hardware used (ex: custom board, new grabbing mechanisms, different chassis look, etc.)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Helpful links
-------------
**XRP Code Editor - https://xrpcode.wpi.edu**

OnShape CAD (full V2) **(DISCLAIMER - the CAD model for the XRP wheel and the motor were not created by me)**- https://cad.onshape.com/documents/8c0d30bc27f93aca9cecb3c5/w/34c3822477bc31986b632ba4/e/a49cac85e221fc7f59d26fd0
OnShape CAD (V1/V1.5 Claw) - https://cad.onshape.com/documents/94cab965c461ea71e610c3a8/w/6c71823ed011eed3911d8ce7/e/d39e55db9d4270f620e11d48

Orb Game Piece used to test claw (called "Rubble") - https://www.printables.com/model/1251185-2025-xrp-game-orbit-odyssey/files 

Instructions for V2
-------------------
1) Print out all pieces on OnShape file (wheel and wheel retainer and gear and grabber should have 2 of each) with the exception of the XRP motor and XRP included wheel; ideally out of Basic PLA
2) Take the base and the XRP motors with the sensor side being on the lower part of the motor area like picture below
   <img width="442" height="273" alt="Screenshot 2026-08-01 at 11 01 27 PM" src="https://github.com/user-attachments/assets/071c5fb8-8b02-4399-84d0-770056252db7" />
3) Place the motor retainers onto the top of the motor and line up the holes
4) Screw the retainer onto the drive base using 4 (2 per retainer) M3 6mm buttonhead screws
5) Attach the included wheel to both motors and use the included screw in the XRP kit to secure
6) Take the wheel and insert in onto the pegs on the sides of the robot
7) Take the wheel retainer and place on top of the hole and use 2 M3 4mm screws to secure
   Base should look like so -
   <img width="1143" height="399" alt="Screenshot 2026-08-06 at 10 49 15 PM" src="https://github.com/user-attachments/assets/0a1cb4d8-0de6-4aae-9f6c-719e01251822" />
9) Attach the XRP board to the center of the robot base with the barrel-jack connector facing away from the wall using 4 M3 4mm screws using a M3 nut as a standoff between the board and the base
10) Connect the provided XRP battery to the board and plug in the left and right motors to the left and right motor slots on the board
11) Place battery in the area enclosed by the rectangle, should make battery sit at an angle
12) Then assemble the arm battery packs by make 2 sets of 2 2AA battery holders connected in series (Red wire of one connected to the Black of the Other) and then connect the two sets in parallel by connect the reds together and then the blacks together
13) Move these batteries to the area that is also occupied by the barrel-jack connector
14) Then attach the servo platform to the base using 4 M3 25mm socketheads
15) Attach the power rails of a breadboard to either side of the longer part of this servo platform
16) Attach a MG995 motor using 4 M3 4mm screws
17) Attach Servo horn (4 point) using included screw (all other servos need the circular horn)
18) Attach Joint 1 to the the servo horn using included screws where the slot for the motor wires should be facing the front (where the back is the numbers 1208)
19) Press another MG995 into the the square area with motor wire protect on the side of the slot
20) Replace the back plate on the servo for arm support bracket and do so for one more MG995
21) Slide the second joint by first sliding the bracket onto the support bracket and then orient it on the face of the servo horn, secure using included screws
22) Secure the second MG995 motor using 4 M3 6mm screws
23) Secure the third MG995 motor using 4 M3 4mm screws
24) Secure the claw onto the third MG995 by using the same method as the second joint
25) Insert the final motor into the claw shroud in a parallel manner to the arm and secure using 4 M3 4mm screws
26) Attach the two gears pointing forward and secure the one powered using included screws and the one that is static by placing it on the "pin" and then using the gear retainer and 1 M3 4mm screw to retain
27) Attach the claw grabbers were ends should be pointing towards each other and secure to the gears using 4 M3 6mm screws
   Fully assembled claw looks something like this -
   <img width="1027" height="604" alt="Screenshot 2026-08-06 at 10 54 14 PM" src="https://github.com/user-attachments/assets/8537fd1f-15e3-41e1-8820-3182e261c1d9" />

Electronics instructions
------------------------
1) Take 2 2AA battery back holders and connect these two in series
2) Repeat step 1
3) Connect the two pairs of batteries together in series to get a total voltage 4 times that of a standard AA and current that is double that of a standard AA
   <img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/1aeeb0db-ade3-464d-98d7-c1428e274621" />
5) Take a power rail of the breadboard and insert 2 300uf 16V capacitors with the small side inside of the negative terminal
6) Then place the female side of a dupont connector and attach to the XRP servo pinout (specifically the signal wire)
7) Then place 4 sets of male to male jumper wires on the negative side
8) Repeat step 6 but for the positive side
9) Connect the negative wires to the brown colored slot on the servo extension wire
10) repeat step 8 but using positive wires and the red colored slot
11) Repeat step 8 but using the dupont connectors from step 5 and connect to the yellow slot on servo extension wires
12) Use enough slack on the cables using the servo extension wires to make sure that nothing gets caught when arm is in motion
13) Note - I would use some electrical tape with the jumper wires to ensure that nothing gets unplugged from random motion on the arm/drivebase

Additional Electronics help
---------------------------
Follow the diagram, servo motor signal wires go to any of the 4 signal wires on the board for the way that you have configured as each motor
Additionally, this diagram doesn't take into account the use of a breadboard; distinct positive and negative lines have been made for a little ease of understanding.
<img width="636" height="365" alt="Screenshot 2026-07-29 at 11 29 17 PM" src="https://github.com/user-attachments/assets/750d6db5-0526-4979-a061-6bb8d70edd1c" />

videos 
part 1 - https://youtu.be/mma-man9Brw
part 2 - https://youtube.com/shorts/A3m_HA8ld8k?feature=share
