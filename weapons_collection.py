from units import Missile, Rocket

_missiles = []
_rockets = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv

def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)

def nuclear_boom(owner):
    r = Rocket(_canvas, owner)
    _rockets.append(r)

def update():
    start = len(_missiles) - 1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()

def update_nuclear():
    start = len(_rockets) - 1
    for i in range(start, -1, -1):
        if _rockets[i].is_destroyed():
            del _rockets[i]
        else:
            _rockets[i].update()

def check_missiles_collection(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
        if missile.intersects(tank):
            missile.destroy()
            tank.damage(25)
            return

def check_rockets_collection(tank):
    for rocket in _rockets:
        if rocket.get_owner() == tank:
            continue
        if rocket.intersects(tank):
            rocket.destroy()
            tank.damage(100)
            return