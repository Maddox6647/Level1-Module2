"""
Create the classic Flappy Bird game!
"""

# 0. Do the other exercises in this folder before starting this one!

def setup():
    pass
    # 1. Use the size function to set the width and height of the program
    size(800, 800)
    # 2. Remove the comment (the '#') in the line below 
    global bg, bird, lower_pipe, upper_pipe, score
    score = 0
    # 3. Use the loadImage function to initialize the bg variable with the
    # flappyBackground.jpg image 
    bg = loadImage("flappyBackground.jpg")
    # 4. Resize the background to the width and height of the program
    bg.resize(800, 800)
    # 5. Use the Bird class defined below to create a Bird object.
    # The bird image is named 'bird.png'
    bird = Bird("bird.png", 30, 200)
    
    # 6. Use the Pipe class defined below to create 2 Pipe objects,
    # one pipe at the top and one at the bottom.
    # The pipe images are named, "topPipe.png" and "bottomPipe.png"  
    upper_pipe = Pipe("topPipe.png")
    lower_pipe = Pipe("bottomPipe.png")
    
    
    # 7. Call the reset_pipes function to set the initial positions
    # of the pipes
    reset_pipes(lower_pipe, upper_pipe)
def draw():
    pass
    # 8. Remove the comment (the '#') in the line below
    global bg, bird, lower_pipe, upper_pipe, score
    
    # 9. Use the background function to draw the game's background
    background(bg)
    # 10. Find the Bird class below and follow the instructions
    # there to complete the Bird class before continuing

    # 18. Call the bird's update and draw methods.
    # Is the bird displayed and move up when the mouse is clicked?
    bird.update()
    bird.draw()
    # 19. Call the upper and lower pipe's update methods.
    upper_pipe.update()
    lower_pipe.update()
    # 20. Call the upper and lower pipe's draw methods. 
    # Do the pipes move across the screen?
    upper_pipe.draw()
    lower_pipe.draw()
    # 21. Call the reset_pipes function defined below when the pipes
    # move past the screen to reset their position. 
    if upper_pipe.x <=  -upper_pipe.width:
        reset_pipes(upper_pipe, lower_pipe)
        score += 1
    # 22. Call the intersects_pipes function defined below to check if
    # the bird collided with one of the pipes. If there's a collision,
    # stop the game by calling noLoop()  
    if intersects_pipes(bird, lower_pipe, upper_pipe) == True:
        noLoop()
    # 23. End the game if the bird flies too low (hitting the ground)
    # OR flies too high (above the screen)
    
    if bird.y >= 800:
        noLoop()
    if bird.y <= 0:
        noLoop()

    textSize(32)
    text("score: " + str(score), 10, 30)
    fill(0, 0, 0)
    
    
class Bird:
    def __init__(self, image_file, bird_x, bird_y):
        self.x = bird_x
        self.y = bird_y
        self.width = 90
        self.height = ( 3 * self.width ) / 4
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
        self.yVelocity = -10
        
        # 11. Initialize a member variable for gravity (typically 1 to 5)
        self.gravity = 1
        # 12. Add a member variable for the distance the bird travels
        # upward when it flaps (jumps)
        self.distance = 10
    # 13. Create an update method that will update the bird's position
    # while the game runs
    def update(self):
        self.yVelocity += self.gravity
        self.y  += self.yVelocity
        # 14. Move the bird downward by the gravity member variable to make
        # it look like the bird is falling
        
        # 15. Use the boolean mousePressed variable to flap (jump) the bird
        # up by flap distance member variable the when the mouse is pressed
        if mousePressed:
            #self.y -= self.distance
            self.yVelocity = -10
            
    # 16. Create a draw method that shows the bird on the program
    def draw(self):
        # 17. Use the image function and the class's member variables to
        # draw the bird
        # image( <image>, <x positon>, <y position> )
        image(self.image, self.x, self.y)
class Pipe:
    pipe_gap = 209
    
    def __init__(self, image_file, pipe_y=0, pipe_height=0):
        self.x = width
        self.y = pipe_y
        self.width = 100
        self.height = pipe_height
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
    
    def update(self):
        self.x -= 8
    
    def draw(self):
        image(self.image, self.x, self.y)

    def teleport(self, pipe_y, pipe_height):
        self.x = width
        self.y = pipe_y
        self.height = pipe_height
        self.image.resize(self.width, self.height)
        

def reset_pipes(lower_pipe, upper_pipe):
    random_height = int((2 * random(height) / 3) + 50)
    upper_pipe.teleport(0, random_height)
    lower_pipe.teleport(random_height + Pipe.pipe_gap, height - random_height)
    
    
def intersects_pipes(bird, lower_pipe, upper_pipe):
    # Check upper pipe collision
    if (bird.x + bird.width >= upper_pipe.x and
        bird.x <= upper_pipe.x + upper_pipe.width and
        bird.y + bird.height >= upper_pipe.y and
        bird.y <= upper_pipe.y + upper_pipe.height):
        return True

    # Check lower pipe collision
    if (bird.x + bird.width >= lower_pipe.x and
        bird.x <= lower_pipe.x + lower_pipe.width and
        bird.y + bird.height >= lower_pipe.y and
        bird.y <= lower_pipe.y + lower_pipe.height):
        return True

    return False
