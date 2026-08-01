(V2) 4 Degrees of Freedom Robotic Arm on Custom robot base powered by XRP

<img width="811" height="466" alt="Screenshot 2026-07-31 at 10 17 01 PM" src="https://github.com/user-attachments/assets/80adf379-1dde-40a7-ba33-98f8f8a776d5" />

About - This project was created during Hack Club's Macondo program. It uses a custom made chassis and adds onto it by using 4 MG995 servo motors and various different 3d printed objects to make a 4 degree of freedom robotic arm ontop of the robot. Throughout the next couple months, there will be many updates/upgrades to the software used to control the robot and will likely use a bluetooth webtool that is unique (but will first start using something like pestol.ink) and there will be updates to the hardware used (ex: custom board, new grabbing mechanisms, different chassis look, etc.)

Helpful links
XRP Code Editor - https://xrpcode.wpi.edu

OnShape CAD - 

Orb Game Piece used to test claw (called "Rubble") - https://www.printables.com/model/1251185-2025-xrp-game-orbit-odyssey/files 

Instructions

1) Create the XRP robot base using the instructions provided by SparkFun - https://xrpusersguide.readthedocs.io/en/latest/course/building.html





2) Take the 3d printed modular brackets with one M3 sized hole at the top and secure them to the front (ball bearings are considered the front of the robot) with a center to center distance of 4.5 cm on both side (the holes should make a square that is the width of the XRP by 4.5 centimeters)
3) Prepare 2 MG995 servos with the back support part in place of the normal back by using a philips head screwdriver and removing the 4 screws on the back of the cover, ensuring that the top of the servo doesn't fall off.
4) Attach the base to the 4 standoffs (modular brackets) using 4 M3 4mm screws
5) Attach the first MG995 servo to the base using 4 M3 6mm screws
6) Attach a circular horn to the servo with a press fit and then use a philips head screwdriver to secure the horn using the provided screw with the motors
7) Then take joint 1 and use the 2 provided screws to attach the arm joint to the horn of the first servo motor
8) Using another MG995 motor and 4 M3 4mm screws, attach the servo to the open spot on joint 1
9) Repeat step 6 for this motor as well
10) Attach joint 2 to the horn of the second servo motor using the included philips head screws
11) Attach the 3rd MG995 motor to the the end of joint 2 using 4 M3 10mm screws\
12) Repeat step 6 for the 3rd servo motor
13) Attach the final joint to the 3rd motor using included screws
14) Use 2 M3 6mm screws to connect Part 1 of the final joint to part 2 of the final joint ensure that the side that is getting connected is the opposite the side of the servo's wire and make sure the holes make a parallel line with part 1 of the final joint
15) Attach the final servo to this final joint using 4 M3 12mm screws
16) Repeat step 6 for the final servo


Electronics -
Follow the diagram, servo motor signal wires go to any of the 4 signal wires on the board for the way that you have configured as each motor
<img width="636" height="365" alt="Screenshot 2026-07-29 at 11 29 17 PM" src="https://github.com/user-attachments/assets/750d6db5-0526-4979-a061-6bb8d70edd1c" />

