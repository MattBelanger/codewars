def extract_names(names, num):
    if (num == 1):
        return names[0]
    elif (num == 2):
        return names[0] + ' and ' + names[1]
    elif (num == 3):
        return extract_names(names, 1) + ', ' + extract_names(names[1:], 2)
    elif (num >= 4):
        return ', '.join(names[0:2]) + ' and ' + str(num - 2) + ' others'

def likes(names):
    num_likes = len(names)
    
    if (num_likes == 0):
        return 'no one likes this'
    elif (num_likes == 1):
        return extract_names(names, 1) + ' likes this'
    elif (num_likes > 1):
        return extract_names(names, num_likes) + ' like this'