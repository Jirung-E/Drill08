from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.vx = random.randint(3, 7)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        # self.x += self.vx
        self.x += 5


class Ball:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = 599
        self.vy = random.randint(30, 70) / 10
        if random.randint(0, 1) == 0:
            self.image = load_image('ball21x21.png')
            self.radius = 21//2
        else:
            self.image = load_image('ball41x41.png')
            self.radius = 41//2

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y < 50 + self.radius:
            self.y == 50 + self.radius
        else:
            self.y -= self.vy


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global balls
    global world

    running = True
    grass = Grass()
    team = [ Boy() for _ in range(11) ]
    balls = [ Ball() for _ in range(20) ]
    
    world = []
    world.append(grass)
    world += team
    world += balls


def render_world():
    clear_canvas()
    for e in world:
        e.draw()
    update_canvas()


def update_world():
    for e in world:
        e.update()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
