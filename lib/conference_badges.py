def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    messages = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return messages

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    assignments = assign_rooms(names)
    for assign in assignments:
        print(assign)

        
