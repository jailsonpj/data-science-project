import random

class Point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<%s, %s>' % (self.x,self.y)

class Reward(Point):

    def __init__(self,x,y,name):
        super(Reward,self).__init__(x,y)
        self.name = name

    def __str__(self):
        return '<%s, %s>: %s' % (self.x,self.y,self.name)
    def __repr__(self):
        return '<Reward> %s' % str(self)

class Robo(Point):

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print("Movimento Proibido")

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print("Movimento Proibido")
    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print("Movimento Proibido")

    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print("Movimento Proibido")

def check_reward(robot,rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("O Robô achou a recompensa: %s" % reward.name)
            ok = True

    return ok


if __name__ == "__main__":
    r1 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
    r2 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
    r3 = Reward(random.randint(0,10),random.randint(0,10),'arma')
    rewards = [r1,r2,r3]
    robot = Robo(random.randint(0,10),random.randint(0,10))

    for i in range(10):
        move = input("digite up,down,left,right para o movimento: ")
        if move == 'up':
            robot.move_up()
        elif move == 'down':
            robot.move_down
        elif move == 'left':
            robot.move_left
        elif move == 'right':
            robot.move_right
        else:
            print("Movimento Invalido!")
            continue
        check_reward(robot,rewards)

    '''
    rewards = [r1,r2]
    print(check_reward(robot,rewards))
    robot.move_left()
    print(check_reward(robot,rewards))'''
    print(r1)
    print(rewards)
