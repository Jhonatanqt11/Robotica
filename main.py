# This is a sample Python script.
import chess
from stockfish import  Stockfish
import serial, time
#import RPI.GPIO as GPIO
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = chess.Board()
    #arduino = serial.Serial('COM3', 9600)
    time.sleep(2)
    while(board.is_checkmate() == False):
        stockfish1 = Stockfish("./stockfish/stockfish-windows-x86-64-avx2.exe")
        stockfish1.set_depth(20)
        stockfish1.set_skill_level(20)
        move1 = input('Enter the posotion of the piece: ')
        #arduino.write(move1)
        time.sleep(5)
        move2 = input('Enter the position of the square: ')
        #arduino.write(move2)
        move = move1 + move2
        board.push_san(move)
        print(board)
        time.sleep(5)
        stockfish1.set_fen_position(board.fen())
        moveIA = stockfish1.get_best_move()
        piece = moveIA[0] + moveIA[1]
        square = moveIA[2] + moveIA[3]
        #arduino.write(piece)
        time.sleep(10)
        #arduino.write(square)
        time.sleep(5)
        board.push_san(moveIA)
        print(board)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
