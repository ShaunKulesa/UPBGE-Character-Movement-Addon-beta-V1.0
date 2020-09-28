import bge

#Call_Logic_Bricks
cont = bge.logic.getCurrentController()
own = cont.owner
#State_Sensors
Forward = cont.sensors['Forward']
Backward = cont.sensors['Backward']
Left = cont.sensors['Left']
Right = cont.sensors['Right']
Jump = cont.sensors['Jump']
#If
if Forward.positive:
    own.applyMovement((0, .1, 0), True)

if Backward.positive:
    own.applyMovement((0, -.1, 0), True)

if Left.positive:
    own.applyMovement((-0.1, 0, 0), True)
    
if Right.positive:
    own.applyMovement((0.1, 0, 0), True)

if Jump.positive:
    own.setLinearVelocity((0, 0, 5), True)