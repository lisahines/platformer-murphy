# Here is my code, from the end of the session.
class Game:
    bx_sz = 50
    data = {1:[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,1,1,1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,2,0,0,0,0],
               [0,0,2,0,0,0,0,0,0,1,1,1,0,0,0,0,2,0,2,0,0,0,0,2,0],
               [0,0,0,0,2,0,0,2,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0],
               [0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1],
               [0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1],
               [1,1,1,1,1,3,3,1,1,1,1,1,1,1,3,3,1,1,1,1,1,3,3,1,1]],
    }
    def __init__(self):
        self.level = Game.data[1]
        self.scr_x = 0
        self.scr_y = height - (len(self.level)*Game.bx_sz)
    def at_loc(self, x, y):
        i = (y - self.scr_y) // Game.bx_sz
        j = (x - self.scr_x) // Game.bx_sz
        return self.level[int(i)][int(j)]
    def update(self):
        num_bx = height // Game.bx_sz
        st = len(self.level) - num_bx
        en = len(self.level)
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if self.level[i][j] == 0:
                    fill("#99FF99")
                elif self.level[i][j] == 1:
                    fill("#000000")
                elif self.level[i][j] == 2:
                    fill("#FFF700")
                else:
                    fill("#FF4800")
                rect(j * Game.bx_sz + self.scr_x, i * Game.bx_sz + self.scr_y, Game.bx_sz, Game.bx_sz)
    def handle_coins(self, player):
        i = int((player.y - self.scr_y) // Game.bx_sz)
        j = int((player.x - self.scr_x) // Game.bx_sz)
        mxi = min(i+2, len(self.level))
        mni = max(0, i)
        mxj = min(j+2, len(self.level[0]))
        mnj = max(0, j)
        for p in range(mni, mxi):
            for q in range(mnj, mxj):
                if self.level[p][q] == 2:
                    player.coins += 1
                    self.level[p][q] = 0

class Player:
    def __init__(self):
        self.x = width / 2
        self.y = 0
        self.w = Game.bx_sz
        self.h = Game.bx_sz
        self.vx = 0
        self.vy = 0
        self.lives = 3
        self.coins = 0
        self.img = None
    def loose_life(self):
        self.lives -= 1
        self.x = width / 2
        self.y = 0
        self.w = Game.bx_sz
        self.h = Game.bx_sz
        self.vx = 0
        self.vy = 0
        self.img = None
    def update(self):
        global g
        fill("#FF0000")
        rect(self.x, self.y, self.w, self.h)
        if self.x >= 0 and self.x + self.w <= width and self.y >= 0 and self.y + self.h <= height:
            corners = self.hit_block()
            if corners == [False, False, False, False]: #no corners
                self.x += self.vx
                self.y += self.vy
            elif corners == [True, False, False, False]: #top left
                self.x += self.vx
                if self.vy >= 0: self.y += self.vy
            elif corners == [False, True, False, False]: #top right
                self.x += self.vx
                if self.vy >= 0: self.y += self.vy
            elif corners == [False, False, True, False]: #bottom left
                self.x += self.vx
                if self.vy <= 0: self.y += self.vy
            elif corners == [False, False, False, True]: #bottom right
                self.x += self.vx
                if self.vy <= 0: self.y += self.vy
            elif corners == [True, False, True, False]: #top left, bottom left
                if self.vx >= 0: self.x += self.vx
                self.y += self.vy
            elif corners == [False, True, False, True]: #top right, bottom right
                if self.vx <= 0: self.x += self.vx
                self.y += self.vy
            elif corners == [True, True, False, False]: #top left, top right
                self.x += self.vx
                if self.vy >= 0: self.y += self.vy
            elif corners == [False, False, True, True]: #bottom left, bottom right
                self.x += self.vx
                if self.vy <= 0: self.y += self.vy
            elif corners == [True, True, True, False]: #top left, top right, bottom left
                if self.vx >= 0: self.x += self.vx
                if self.vy >= 0: self.y += self.vy
            elif corners == [True, True, False, True]: #top left, top right, bottom right
                if self.vx <= 0: self.x += self.vx
                if self.vy >= 0: self.y += self.vy
            elif corners == [True, False, True, True]: #top left, bottom left, bottom right
                if self.vx >= 0: self.x += self.vx
                if self.vy <= 0: self.y += self.vy
            elif corners == [False, True, True, True]: #top right, bottom right, bottom left
                if self.vx <= 0: self.x += self.vx
                if self.vy <= 0: self.y += self.vy
            else: #You are trapped
                print("The player is touching all corners")
            if self.vy < 5:
                self.vy += 0.1
        else:
            if self.x <= 0:
                self.x = 0
            elif self.x + self.w >= width:
                self.x = width - self.w
            if self.y <= 0:
                self.y = 0
            elif self.y + self.h >= height:
                self.loose_life()
        if abs(self.vx) > 0.05:
            self.vx *= 0.8
        else:
            self.vx = 0
        if g.scr_x < 0:
            if self.x <= width / 3:
                g.scr_x += 1
                self.x += 1
        if (width - g.scr_x) // g.bx_sz < len(g.level[0])-1:
            if self.x >= width / 3 * 2:
                g.scr_x -= 1
                self.x -= 1
        if g.scr_y < 0:
            if self.y <= height / 2:
                g.scr_y += 1
                self.y += 1
        if (height - g.scr_y) // g.bx_sz < len(g.level):
            if self.y >= height / 2:
                g.scr_y -= 1
                self.y -= 1
        g.handle_coins(self)
        fill("#BCB600")
        textSize(20)
        text("Coins: "+str(self.coins),0,20)
        fill("#F7A100")
        text("Lives: "+str(self.lives),0,40)

    def hit_block(self):
        global g
        u_l = g.at_loc(self.x, self.y) == 1
        u_r = g.at_loc(self.x + self.w, self.y) == 1
        b_l = g.at_loc(self.x, self.y + self.h) == 1
        b_r = g.at_loc(self.x + self.w, self.y + self.h) == 1
        return [u_l, u_r, b_l, b_r]
        
    def move(self, dir):
        if dir == "left":
            self.vx = -5
        if dir == "right":
            self.vx = 5
        if dir == "up":
            self.vy = -3

def setup():
    global g, p
    size(1000,700)
    noStroke()
    g = Game()
    p = Player()

def draw():
    global g, p
    g.update()
    p.update()

def keyPressed():
    global g, p
    if keyCode == UP:
        p.move("up")
    if keyCode == DOWN:
        p.move("down")
    if keyCode == LEFT:
        p.move("left")
    if keyCode == RIGHT:
        p.move("right") 
