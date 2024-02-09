import pyglet
import random


window = pyglet.window.Window(width=1024, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()


numbers = random.sample(range(1, 100), 19) + [37]
random.shuffle(numbers)


current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 37:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        x = i * 50 + 20
        y = window.height // 2
        outer_radius = 30
        inner_radius = 15
        num_spikes = 5

        if i == current_index and not search_complete:
            color = (255, 0, 0)  
        elif i == found_index:
            color = (0, 255, 0) 
        else:
            color = (200, 200, 200)
        
        pyglet.shapes.Star(x, y, outer_radius, inner_radius, num_spikes, color=color, batch=batch).draw()
        label = pyglet.text.Label(str(number), x=x+outer_radius//5, y=y+inner_radius//5, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()