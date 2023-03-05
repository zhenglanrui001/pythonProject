#1
board = [
    ["*","*","*","*","*"],
    ["*","o","#"," ","*"],
    [" "," ","P"," "," "],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
for _ in range(31):
    game.move("a")
print(game)

#2
board = [
    ["*","*"," ","*","*"],
    ["*","o"," "," ","*"],
    ["*","#","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("w")
print(game)

#3
board = [
    ["*","*"," ","*","*"],
    ["*","o"," "," ","*"],
    ["*","#","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(31):
    game.move("w")
print(game)

#4
board = [
    ["*","*"," ","*","*"],
    ["*","o"," "," ","*"],
    ["*","#","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("s")
print(game)

#5
board = [
    ["*","*"," ","*","*"],
    ["*","o"," "," ","*"],
    ["*","#","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(31):
    game.move("s")
print(game)

#6
board = [
    ["*","*","*","*","*"],
    ["*","o"," "," ","*"],
    [" "," ","P","#"," "],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("d")
print(game)

#7
board = [
    ["*","*","*","*","*"],
    ["*","o"," "," ","*"],
    [" ","#","P"," "," "],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("a")
print(game)

#8
board = [
    ["*","*"," ","*","*"],
    ["*","o","#"," ","*"],
    [" "," ","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("w")
print(game)

#9
board = [
    ["*","*"," ","*","*"],
    ["*","o"," "," ","*"],
    ["*"," ","P"," ","*"],
    ["*"," ","#"," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("s")
print(game)

#10
board = [
    ["*","*","*","*","*"],
    ["*","o","#"," ","*"],
    ["*"," ","P"," "," "],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("d")
print(game)

#11
board = [
    ["*","*","*","*","*"],
    ["*","o","#"," ","*"],
    [" "," ","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("a")
print(game)

#12
board = [
    ["*","*"," ","*","*"],
    ["*","o"," "," ","*"],
    ["*","#","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("w")
print(game)

#13
board = [
    ["*","*","*","*","*"],
    ["*","o"," "," ","*"],
    ["*","#","P"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*"," ","*","*"]
]
game = Sokoban(board)
for _ in range(6):
    game.move("s")
print(game)

#14
board = [
    ["*","*","*","*","*","*","*","*"],
    ["*"," "," "," "," "," "," ","*"],
    ["*","P"," ","#"," "," "," ","*"],
    ["*","*","*","*","*"," ","#","*"],
    ["*","o"," "," "," "," "," ","*"],
    ["*"," "," "," "," "," ","o","*"],
    ["*","*","*","*","*","*","*","*"]
]
game = Sokoban(board)
print(game.is_complete())

#15
board = [
    ["*","*","*","*","*","*","*","*"],
    ["*"," "," "," "," "," "," ","*"],
    ["*"," "," "," "," "," "," ","*"],
    ["*","*","*","*","*"," "," ","*"],
    ["*"," ","P"," "," "," "," ","*"],
    ["*"," "," "," "," "," "," ","*"],
    ["*","*","*","*","*","*","*","*"]
]
game = Sokoban(board)
print(game.is_complete())

#16
board = [
    [" "," "," "],
    [" ","P"," "],
    [" "," "," "]
]
game = Sokoban(board)
print(game.is_complete())

#17
board = [
    ["o","#"," "],
    [" ","P"," "],
    [" ","#","o"]
]
game = Sokoban(board)
print(game.is_complete())

#18
board = [
    [" "," "," "],
    ["P","#","o"],
    [" "," "," "]
]
game = Sokoban(board)
print(game.is_complete())
game.move("d")
print(game.is_complete())

#19
board = [
    ["*","*","*","*","*"],
    ["*","o"," "," ","*"],
    [" "," ","P","#"," "],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
print(game.is_complete())

#20
board = [
    ["*","*","*","*","*"],
    ["*","o"," "," ","*"],
    ["#"," ","P","#","o"],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
print(game.is_complete())

#21
board = [
    ["*","*","*","*","*"],
    ["*","#"," "," ","*"],
    [" "," ","P"," "," "],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
print(game.is_complete())

#22
board = [
    ["*","*","*","*","*"],
    ["*","*","*","*","*"],
    ["*","*","P","*","8"],
    ["*","*","*","*","*"],
    ["*","*","*","*","*"]
]
game = Sokoban(board)
print(game.is_complete())

#23
board = [
    [" "," "," "],
    ["P","#","o"],
    [" "," "," "]
]
game = Sokoban(board)
game.move("d")
print(game.is_complete())
game.undo()
print(game.is_complete())

#24
board = [
    [" "," "," "],
    ["P","#","o"],
    [" "," "," "]
]
game = Sokoban(board)
game.move("d")
print(game.is_complete())
game.restart()
print(game.is_complete())