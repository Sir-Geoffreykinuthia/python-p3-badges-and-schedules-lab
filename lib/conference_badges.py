def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start=1):
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {index}!")
    return room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room_assignment in assign_rooms(names):
        print(room_assignment)










# def badge_maker(name):
#     return f"Hello, my name is {name}."

# def batch_badge_creator(names):
#     return [badge_maker(name) for name in names]

# def assign_rooms(names):
#     return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]

# def printer(names):
#     for badge in batch_badge_creator(names):
#         print(badge)
#     for room_assignment in assign_rooms(names):
#         print (room_assignment)
    
