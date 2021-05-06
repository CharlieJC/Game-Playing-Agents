from game import TicTacToe, TakeAway, Connect4
import time
# Let two versions compete against each other and report on the performance dierence, e.g., win-draw-lose rate, and resource consumption.

#compares the performance for a game, running two AI players at different depths
#returns a 3 tuple (winner,avg move time depth1, avg move time depth2)
def comparePerformanceDepth(game, depth1, depth2):
    depth_one_time = 0
    depth_one_moves = 0
    depth_two_time = 0
    depth_two_moves = 0
    while game.winner() == None:
        start = time.time_ns()
        game.process_ai_move_inefficient(depth1)
        stop = time.time_ns()
        depth_one_time += stop-start
        depth_one_moves += 1
        if game.winner() != None:
            break
        game.nextTurn()
        start = time.time_ns()
        game.process_ai_move(depth2)
        stop = time.time_ns()
        depth_two_time += stop-start
        depth_two_moves += 1
        if game.winner() != None:
            break
        game.nextTurn()
    # print(f'{depth_two_time/depth_two_moves}')
    return (game.winner(),depth_one_time/depth_one_moves, depth_two_time/depth_two_moves)


game = Connect4((False,False))
results = comparePerformanceDepth(game, 4, 4)

print(f'Average move time DFS: {results[1]}')
print(f'Average move time DLS: {results[2]}')
print(f'Winner: {results[0]}')
file1 = open("performance/results.csv","w")

file1.write(f'{results[0]},{results[1]},{results[2]}')