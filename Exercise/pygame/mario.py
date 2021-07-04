# Mario example originally from: https://github.com/Mechachleopteryx/python-cheatsheet
# However it didn't receive the keys as it was out-of-the box (on my Python 3.8)
# I fixed it by checking the pressed keys and adding them to a set one by one, see "run"
# Use the arrow keys to move Mario.
# Twenkid, 4.7.2021

import collections, dataclasses, enum, io, itertools as it, pygame as pg, urllib.request
from random import randint

P = collections.namedtuple('P', 'x y')          # Position
D = enum.Enum('D', 'n e s w')                   # Direction
SIZE, MAX_SPEED = 50, P(5, 10)                  # Screen size, Speed limit

def main():
    def get_screen():
        pg.init()
        return pg.display.set_mode(2 * [SIZE*16])
    def get_images():
        url = 'https://gto76.github.io/python-cheatsheet/web/mario_bros.png'
        img = pg.image.load(io.BytesIO(urllib.request.urlopen(url).read()))
        return [img.subsurface(get_rect(x, 0)) for x in range(img.get_width() // 16)]
    def get_mario():
        Mario = dataclasses.make_dataclass('Mario', 'rect spd facing_left frame_cycle'.split())
        return Mario(get_rect(1, 1), P(0, 0), False, it.cycle(range(3)))
    def get_tiles():
        positions = [p for p in it.product(range(SIZE), repeat=2) if {*p} & {0, SIZE-1}] + \
            [(randint(1, SIZE-2), randint(2, SIZE-2)) for _ in range(SIZE**2 // 10)]
        return [get_rect(*p) for p in positions]
    def get_rect(x, y):
        return pg.Rect(x*16, y*16, 16, 16)
    run(get_screen(), get_images(), get_mario(), get_tiles())

def run(screen, images, mario, tiles):
    clock = pg.time.Clock()
    while all(event.type != pg.QUIT for event in pg.event.get()):
        keys = {pg.K_UP: D.n, pg.K_RIGHT: D.e, pg.K_DOWN: D.s, pg.K_LEFT: D.w}        
        pressed = {keys.get(i) for i, on in enumerate(pg.key.get_pressed()) if on}
        #if keys[pygame.K_UP]:
        
        keyPressed = pg.key.get_pressed()
        '''
        if keyPressed[pg.K_RIGHT]: pressed = {D.e} #{'e'}# {'D.e'}
        if keyPressed[pg.K_LEFT]: pressed = {D.w}  #{'w'} #{'D.w'}       
        if keyPressed[pg.K_UP]: pressed = {D.n} #{'n'} #{'D.n'} 
        if keyPressed[pg.K_DOWN]: pressed = {D.s} #'}  #{'s'} #{'D.s'} 
        '''
        
        if keyPressed[pg.K_RIGHT]: pressed.add(D.e) #{'e'}# {'D.e'}
        if keyPressed[pg.K_LEFT]: pressed.add(D.w)  #{'w'} #{'D.w'}       
        if keyPressed[pg.K_UP]: pressed.add(D.n) #{'n'} #{'D.n'} 
        if keyPressed[pg.K_DOWN]: pressed.add(D.s) #'}  #{'s'} #{
        
        #print(keyPressed)
        print(pressed)
        update_speed(mario, tiles, pressed)
        update_position(mario, tiles)
        draw(screen, images, mario, tiles, pressed)
        clock.tick(28)

def update_speed(mario, tiles, pressed):
    x, y = mario.spd
    #print(D.e, pressed)
    x += 2 * ((D.e in pressed) - (D.w in pressed))
    print(x)
    x -= x // abs(x) if x else 0
    y += 1 if D.s not in get_boundaries(mario.rect, tiles) else (D.n in pressed) * -10
    mario.spd = P(*[max(-limit, min(limit, s)) for limit, s in zip(MAX_SPEED, P(x, y))])
    #print(mario.spd)

def update_position(mario, tiles):
    p = mario.rect.topleft
    larger_speed = max(abs(s) for s in mario.spd)
    for _ in range(larger_speed):
        mario.spd = stop_on_collision(mario.spd, get_boundaries(mario.rect, tiles))
        p = P(*[a + s/larger_speed for a, s in zip(p, mario.spd)])
        mario.rect.topleft = p

def get_boundaries(rect, tiles):
    deltas = {D.n: P(0, -1), D.e: P(1, 0), D.s: P(0, 1), D.w: P(-1, 0)}
    return {d for d, delta in deltas.items() if rect.move(delta).collidelist(tiles) != -1}

def stop_on_collision(spd, bounds):
    return P(x=0 if (D.w in bounds and spd.x < 0) or (D.e in bounds and spd.x > 0) else spd.x,
             y=0 if (D.n in bounds and spd.y < 0) or (D.s in bounds and spd.y > 0) else spd.y)

def draw(screen, images, mario, tiles, pressed):
    print("draw")
    def get_frame_index():
        if D.s not in get_boundaries(mario.rect, tiles):
            return 4
        return next(mario.frame_cycle) if {D.w, D.e} & pressed else 6
    screen.fill((85, 168, 255))
    mario.facing_left = (D.w in pressed) if {D.w, D.e} & pressed else mario.facing_left
    screen.blit(images[get_frame_index() + mario.facing_left * 9], mario.rect)
    for rect in tiles:
        screen.blit(images[18 if {*rect.topleft} & {0, (SIZE-1)*16} else 19], rect)
    pg.display.flip()

if __name__ == '__main__':
    main()
