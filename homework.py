words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for i in words:
    if i[len(i)-1] == 'e':
        i + 'd'
        past_tense.append(i)
    else: 
        i + 'ed'
        past_tense.append(i)

print(past_tense)