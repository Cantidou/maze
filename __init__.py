maze = []

with open('maze.csv', 'r') as MAZE_FILE:
    for line in MAZE_FILE:
        line = line.strip()
        file_split = line.split(';')
        maze.append(file_split)

# End position
maze[len(maze) - 2][len(maze) - 2] = 'E'

# Start position
maze[1][1] = '@'

crossroads = []

def step():
    for i in range(0, len(maze)):
        if '@' in maze[i]:
            def check_step():
                variants = []
                if maze[i - 1][maze[i].index('@')] == '0':  # if it can go UP
                    variants.append('UP')
                if maze[i + 1][maze[i].index('@')] == '0':  # if it can go DOWN
                    variants.append('DOWN')
                if maze[i][maze[i].index('@') + 1] == '0':  # if it can go RIGHT
                    variants.append('RIGHT')
                if maze[i][maze[i].index('@') - 1] == '0':  # if it can go LEFT
                    variants.append('LEFT')
                if len(variants) == 0:
                    variants = ['END']

                return variants

            def make_step(func: list):
                print(func)
                if len(func) == 1:
                    match func[0]:
                        case 'UP':
                            maze[i - 1][maze[i].index('@')] = '@'
                            maze[i][maze[i].index('@')] = 'X'
                        case 'DOWN':
                            maze[i + 1][maze[i].index('@')] = '@'
                            maze[i][maze[i].index('@')] = 'X'
                        case 'RIGHT':
                            maze[i][maze[i].index('@') + 1] = '@'
                            maze[i][maze[i].index('@')] = 'X'
                        case 'LEFT':
                            maze[i][maze[i].index('@') - 1] = '@'
                            maze[i][maze[i].index('@') + 1] = 'X'
                if len(func) > 1:
                    crossroads.append([i, maze[i].index('@')])
                    match func[0]:
                        case 'UP':
                            maze[i - 1][maze[i].index('@')] = '@'
                            maze[i][maze[i].index('@')] = 'X'
                        case 'DOWN':
                            maze[i + 1][maze[i].index('@')] = '@'
                            maze[i][maze[i].index('@')] = 'X'
                        case 'RIGHT':
                            maze[i][maze[i].index('@') + 1] = '@'
                            maze[i][maze[i].index('@')] = 'X'
                        case 'LEFT':
                            maze[i][maze[i].index('@') - 1] = '@'
                            maze[i][maze[i].index('@') + 1] = 'X'
                if func[0] == 'END':
                    maze[i][maze[i].index('@')] = 'X'
                    maze[crossroads[0][0]][crossroads[0][1]] = '@'
                    del crossroads[0]
                print(crossroads)

            make_step(check_step())
            break


for i in range(1, 635):
    step()

for i in maze:
    print(i)
