#1 Variant
#1 задание
def BigWorld(My_text):
    MaxWorld = ''
    World = ''
    for i in range(My_text):
        if My_text[i] == ' ':
            if len(World) > len(MaxWorld):
                MaxWorld = World
            world = ''
        else:
            world += My_text[i]
    if len(World) > len(MaxWorld):
        MaxWorld = World
        
    return MaxWorld



My_text = input()
result = BigWorld(My_text)
print(result)
