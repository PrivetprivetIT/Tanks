import weapons_collection
from tkinter import*
import world
import tanks_collection
import texture


KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

SPACE = 32
ENTER = 13
E = 69

FPS = 60

def update():
    tanks_collection.update()
    weapons_collection.update()
    weapons_collection.update_nuclear()

    player = tanks_collection.get_player()

    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)

    world.update_map()
    w.after(1000//FPS, update)

def key_press(event):

    player = tanks_collection.get_player()

    if player.is_destroyed():
        return

    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()

    elif event.keycode == KEY_UP:
        world.move_camera(delta_x = 0, delta_y = -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(delta_x = 0, delta_y = 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(delta_x = -5, delta_y = 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(delta_x = 5, delta_y = 0)

    elif event.keycode == ENTER:
        tanks_collection.spawn()
    elif event.keycode == SPACE:
        player.fire()
    elif event.keycode == E:
        player.nuclear_boom()

def load_textures():
    texture.load('tank_up', '../img/tank_up.png')
    texture.load('tank_down', '../img/tank_down.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')

    texture.load('tank_up_player', '../img/tank_up_player.png')
    texture.load('tank_down_player', '../img/tank_down_player.png')
    texture.load('tank_left_player', '../img/tank_left_player.png')
    texture.load('tank_right_player', '../img/tank_right_player.png')

    texture.load(world.BRICK, '../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    texture.load(world.MISSLE, '../img/bonus.png')

    texture.load('missile_up', '../img/missile_up.png')
    texture.load('missile_down', '../img/missile_down.png')
    texture.load('missile_left', '../img/missile_left.png')
    texture.load('missile_right', '../img/missile_right.png')

    texture.load('rocket_up', '../img/rocket_up.png')
    texture.load('rocket_down', '../img/rocket_down.png')
    texture.load('rocket_left', '../img/rocket_left.png')
    texture.load('rocket_right', '../img/rocket_right.png')

    texture.load('tank_destroy', '../img/tank_destroy.png')

    print(texture._frames)

w = Tk()

load_textures()

w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT,
              bg = '#8ccb5e')
canv.pack()

world.initialaze(canv)

tanks_collection.initialize(canv)
weapons_collection.initialize(canv)

w.bind('<KeyPress>', key_press)

update()
w.mainloop()