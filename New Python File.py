def setup():
    size(600, 600)
    frameRate(5)


def draw():
    for x in range(0,600,20):
        for y  in range (0,600,20):
            rotate(5)
            triangle(random(0,10),random(0,10),random(0,10),20,10,10)
            line(x,y, x+random(-20,20), y+random(-20,20))
            ellipse(x,y,5,5)
            
    saveFrame('afbeelding13.jpg')
    
    
