shouldGoToStart = True
shouldGoUp = False
shouldGoDown = False
isFoodAhead = False
isFirstGoingToStart = True
isGoingToStartFromEnd = False

def bot_do(snake, game_size_y, next_dir, food, game_size_x):
    global isFoodAhead
    global shouldGoToStart
    global shouldGoUp
    global shouldGoDown
    global isFirstGoingToStart
    global isGoingToStartFromEnd

    if not food == ["x", "x"]:
        if food[0] > snake[0][0]: isFoodAhead = True
        else: isFoodAhead = False

    #handle end of gameboard
    if snake[0][0] == game_size_x-1:
        if snake[0][1] == game_size_y-1:
            shouldGoToStart = True
            shouldGoUp = False
            isGoingToStartFromEnd = True
            return "A"
        else:
            shouldGoToStart = True
            shouldGoUp = False
            return "S"

    if snake[0][1] == game_size_y-1:
        if shouldGoToStart:
            if isGoingToStartFromEnd:
                if not snake[0][0] == 0: return "A"

    if shouldGoToStart:
        #go to start
        #go to the start for the first time
        if not snake[0][1] == game_size_y - 1:
        #need to go down one to get to correct start
            if next_dir == "W":
                if [snake[0][0]-1, snake[0][1]] in snake:
                    shouldGoToStart = False
                    shouldGoUp = True
                    shouldGoDown = False
                    return "D"
                else: return "A"
            else: return "S"
        else:
            #need to go to left
            if [snake[0][0]-1, snake[0][1]] in snake:
                shouldGoToStart = False
                shouldGoUp = True
                shouldGoDown = False
                return "D"
            else:
                if next_dir == "D": return  "W"
                else:
                    if snake[0][0] == 0:
                        shouldGoUp = True
                        shouldGoToStart = False
                        isFirstGoingToStart = False
                        return "W"
                    else: return "A"
    else:
        if shouldGoUp:
            if snake[0][1] == 0:
                shouldGoUp = False
                shouldGoDown = True
                return "D"
            else: return "W"
        if shouldGoDown:
            if snake[0][1] == game_size_y-2:
                if isFoodAhead:
                    shouldGoDown = False
                    shouldGoUp = True
                    return "D"
                else:
                    shouldGoDown = False
                    shouldGoToStart = True
                    return "S"
            else: return "S"