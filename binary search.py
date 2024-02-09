import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1024, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

numbers = sorted(random.sample(range(1, 100), 19) + [37])


left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 37:
            found = True
        elif numbers[mid] < 37:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True


pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):     
        x = i * 50 + 20
        y = window.height // 2
        outer_radius = 30
        inner_radius = 15
        num_spikes = 5

        if left <= i <= right and not search_complete:
            color = (100, 100,255)  
        elif i == mid and not search_complete:
            color = (255, 0, 0)  
        elif found and i == mid:
            color = (0, 255, 0)  
        else:
            color = (214, 208, 193)  
        
        pyglet.shapes.Star(x, y, outer_radius, inner_radius, num_spikes, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+outer_radius//5, y=y+inner_radius//5, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()