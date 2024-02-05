from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle,Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

class Renderer(Window):
    def __init__(self):
        super().__init__ (720,720,"Solar System Simulation")
        self.batch = Batch()
        self.x =[5,2,3,4,1,6]
        self.bars = []
        for e,i in enumerate(self.x):
            self.bars.append(Rectangle(80+e*100,100,80,i*100, color=hex_to_rgb('#8CEB34'), batch=self.batch))

    def on_update(self, deltatime):
        #n = len(self.x)
        if len(self.x) > 1:
            mid = len(self.x) // 2  # หาตำแหน่งกลางของ array
            left_half = self.x[:mid]  # แบ่ง array เป็นครึ่งแรก
            right_half = self.x[mid:]  # แบ่ง array เป็นครึ่งหลัง
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    self.x[k] = left_half[i]
                    i += 1
                else:
                    self.x[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                self.x[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                self.x[k] = right_half[j]
                j += 1
                k += 1
                self.bars = []       
                for e,i in enumerate(self.x):
                    self.bars.append(Rectangle(80+e*100,100,80,i*100, color=hex_to_rgb('#8CEB34'), batch=self.batch))
                return

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 3)
run()
