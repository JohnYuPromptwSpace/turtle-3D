import turtle
import math

class Cube:
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.vertices = []
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self.compute_vertices()
    
    def compute_vertices(self):
        x1, y1, z1 = self.corner1
        x2, y2, z2 = self.corner2
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        z_min, z_max = min(z1, z2), max(z1, z2)
        
        self.vertices = [
            (x_min, y_min, z_min),
            (x_max, y_min, z_min),
            (x_max, y_min, z_max),
            (x_min, y_min, z_max),
            (x_min, y_max, z_min),
            (x_max, y_max, z_min),
            (x_max, y_max, z_max),
            (x_min, y_max, z_max)
        ]
    
    def draw(self, player, drawer):
        projected = []
        for vertex in self.vertices:
            proj, zcam = player.project(vertex)
            projected.append((proj, zcam))
        
        for edge in self.edges:
            i, j = edge
            if projected[i][1] > 0 and projected[j][1] > 0:
                p1 = projected[i][0]
                p2 = projected[j][0]
                drawer.penup()
                drawer.goto(p1[0], p1[1])
                drawer.pendown()
                drawer.goto(p2[0], p2[1])

class Cube:
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.vertices = []
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self.compute_vertices()
    
    def compute_vertices(self):
        x1, y1, z1 = self.corner1
        x2, y2, z2 = self.corner2
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        z_min, z_max = min(z1, z2), max(z1, z2)
        
        self.vertices = [
            (x_min, y_min, z_min),
            (x_max, y_min, z_min),
            (x_max, y_min, z_max),
            (x_min, y_min, z_max),
            (x_min, y_max, z_min),
            (x_max, y_max, z_min),
            (x_max, y_max, z_max),
            (x_min, y_max, z_max)
        ]
    
    def draw(self, player, drawer):
        projected = []
        for vertex in self.vertices:
            proj, zcam = player.project(vertex)
            projected.append((proj, zcam))
        
        for edge in self.edges:
            i, j = edge
            if projected[i][1] > 0 and projected[j][1] > 0:
                p1 = projected[i][0]
                p2 = projected[j][0]
                drawer.penup()
                drawer.goto(p1[0], p1[1])
                drawer.pendown()
                drawer.goto(p2[0], p2[1])

class Player:
    def __init__(self, x=0, y=0, z=-50):
        self.x = x
        self.y = y
        self.z = z
        self.yaw = 0.0
        self.pitch = 0.0
        self.move_speed = 10
        self.rot_speed = math.radians(5)
        self.vy = 0
        
        self.pressed = [False] * 8
    
    def update(self):
        self.y += self.vy
        self.vy -= 1

    def forward_vector(self):
        fx = math.sin(-self.yaw)
        fy = 0
        fz = math.cos(-self.yaw)
        return fx, fy, fz

    def right_vector(self):
        rx = math.cos(-self.yaw)
        ry = 0
        rz = -math.sin(-self.yaw)
        return rx, ry, rz

    def project(self, vertex):
        dx = vertex[0] - self.x
        dy = vertex[1] - self.y
        dz = vertex[2] - self.z
        
        cos_y = math.cos(-self.yaw)
        sin_y = math.sin(-self.yaw)
        x1 = cos_y * dx - sin_y * dz
        z1 = sin_y * dx + cos_y * dz
        y1 = dy
        
        cos_p = math.cos(-self.pitch)
        sin_p = math.sin(-self.pitch)
        y2 = cos_p * y1 - sin_p * z1
        z2 = sin_p * y1 + cos_p * z1
        
        if z2 < 0.1:
            z2 = 0.1
        focal_length = 200
        screen_x = focal_length * x1 / z2
        screen_y = focal_length * y2 / z2
        return (screen_x, screen_y), z2

    def move_forward(self):
        fx, fy, fz = self.forward_vector()
        self.x += self.move_speed * fx
        self.y += self.move_speed * fy
        self.z += self.move_speed * fz

    def move_backward(self):
        fx, fy, fz = self.forward_vector()
        self.x -= self.move_speed * fx
        self.y -= self.move_speed * fy
        self.z -= self.move_speed * fz

    def strafe_left(self):
        rx, ry, rz = self.right_vector()
        self.x -= self.move_speed * rx
        self.z -= self.move_speed * rz

    def strafe_right(self):
        rx, ry, rz = self.right_vector()
        self.x += self.move_speed * rx
        self.z += self.move_speed * rz

    def turn_left(self):
        self.yaw += self.rot_speed

    def turn_right(self):
        self.yaw -= self.rot_speed

    def look_up(self):
        self.pitch -= self.rot_speed
        if self.pitch < math.radians(-89):
            self.pitch = math.radians(-89)

    def look_down(self):
        self.pitch += self.rot_speed
        if self.pitch > math.radians(89):
            self.pitch = math.radians(89)
    
    def jump(self):
        self.vy = 20

class EventHandler:
    def __init__(self, drawer, world_objects, player):
        self.drawer = drawer
        self.world_objects = world_objects
        self.player = player
        pass

    def on_w(self):
        self.player.move_forward()

    def on_s(self):
        self.player.move_backward()

    def on_a(self):
        self.player.strafe_left()

    def on_d(self):
        self.player.strafe_right()

    def on_left(self):
        self.player.turn_left()

    def on_right(self):
        self.player.turn_right()

    def on_up(self):
        self.player.look_up()

    def on_down(self):
        self.player.look_down()

    def on_space(self):
        self.player.jump()

    def on_q(self):
        self.player.q()