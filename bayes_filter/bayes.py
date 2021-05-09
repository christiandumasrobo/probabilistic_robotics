from Door import Door

door = Door(True)
print('True door state: ', door.state)
print('First observation(True is open, False is closed): ', door.observe())
door.push()
print('First action performed, push')
print('Second observation: ', door.observe())
