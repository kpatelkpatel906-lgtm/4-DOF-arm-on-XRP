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
    ARM instructions coming soon - very similar to that of V1 with some minor QOL improvements



Additional Electronics -
Follow the diagram, servo motor signal wires go to any of the 4 signal wires on the board for the way that you have configured as each motor
Additionally, this diagram doesn't take into account the use of a breadboard; distinct positive and negative lines have been made for a little ease of understanding.
<img width="636" height="365" alt="Screenshot 2026-07-29 at 11 29 17 PM" src="https://github.com/user-attachments/assets/750d6db5-0526-4979-a061-6bb8d70edd1c" />

