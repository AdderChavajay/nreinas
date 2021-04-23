#librerira utilizado numpy

import os
import numpy as np

print('Juego de N reinas')
option = 0
RESET = 0
PLAY = 1
SEE_RESULT = 2
EXIT = 99
TOTAL_QUEENS_ADDED = 0
matrixTable = np.zeros((8, 8))

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def printMainMenu():
  os.system('cls')
  print('99 - Salir')
  print('1 - Jugar')
  print('2 - Ver juego resuelto')

def printPlayMenu():
  optionGame = 1
  coordenates = [0, 0]
  while optionGame != EXIT:
    addToMatrix(coordenates)
    printTable()
    print('Y')
    print('\n\n99 - Salir')
    print('0 - Reset')
    optionGame = input('X, Y: ')
    coordenates = optionGame.split(',')
    try:
      optionGame = int(optionGame)
    except:
      optionGame = -1
    os.system('cls')

def printTable():
  print('\n   1  2  3  4  5  6  7  8   X')
  for i in range(8):
    row = str(i + 1) + ' '
    for j in range(8):
      if matrixTable[i][j] == 1:
        row += '|X '
      else:
        row += '|  '
    print(row + '|')

def verifyIsThereAOne(array):
  for item in array:
    if item == 1:
      return True
      break
  return False

def verifyDiagonal(matrix, col, row):
  nDiag = col - row
  diagonal = matrix.diagonal(nDiag)
  diag1 = verifyIsThereAOne(diagonal)
  nDiag = -7 + (col + row)
  diagonal = np.rot90(matrix).diagonal(nDiag)
  diag2 = verifyIsThereAOne(diagonal)
  return (diag1 or diag2)
  

def addToMatrix(coordenates):
  global TOTAL_QUEENS_ADDED
  try:
    gameError = False
    x, y = coordenates
    for row in range(8):
      if gameError:
        break
      for col in range(8):
        gameError = (((int(x) - 1) == col or (int(y) - 1) == row) and (matrixTable[row][col] == 1))
        if gameError:
          prRed('No se puede agregar la reina en esa posicion')
          break
        elif (int(x) - 1) == col and (int(y) - 1) == row:
          gameError = verifyDiagonal(matrixTable, col, row)
          if gameError:
            prRed('No se puede agregar la reina en esa posicion')
            break
          else:
            matrixTable[row][col] = 1
            TOTAL_QUEENS_ADDED += 1
            break
    if TOTAL_QUEENS_ADDED == 8:
      prGreen('Ha resulto el juego')
  except (ex):
    print('error de datos ' + ex)
    

def playGame():
  os.system('cls')
  printPlayMenu()

def choseMenu(input):
  if input == PLAY:
    playGame()
  elif input == SEE_RESULT:
    print('wait, in development')
  printMainMenu()

while int(option) != EXIT:
  printMainMenu()
  choseMenu(option)
  option = int(input('Opcion: '))