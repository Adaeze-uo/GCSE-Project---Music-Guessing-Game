import random
import re
import time

Player_Username = "Xaviour"
Player_Password = "Mojang"
Player_GameCode = "Chem1a"
print('Since we only allow authorized players to play,\nwe must check you are an authorized player.')
time.sleep(2)
print('\nPlease enter your player details when prompted')
time.sleep(2)


def Login():
  Username_Login = input('Please enter your player username: ')

  if Username_Login == Player_Username:
     Password_Login = input('Please enter your password linked to your username: ')
     if Password_Login == Player_Password:
       Gamecode_Login = input('Please enter your GameCode your received when you registered your account: ')
       if Gamecode_Login == Player_GameCode:
         print('If you got this far with no errors then your username, password and GameCode are correct.')
         print('You will be directed to the menu.')
         time.sleep(2)
  else:
    print('Your Username, Password and/or GameCode login is incorrect, please enter your detail(s) again .')
    Login()


Login()


def Main_Menu():
  print('Welcome to the Game Menu!')
  time.sleep(1)
  print('\nPlease pick on of the following options below:')
  time.sleep(1)  
  print('1.Start Game \n2.Show current player scoreboard') 
  choice = input()
  if choice == "1":
    print('Okay the game will start in a couple moments')
    time.sleep(1)
    print('.')  
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(2)
    Game_Mode = "Easy"
    Player_Wins = 0
    EasyL_Player_Score = 0
    MediumL_Player_Score = 0
    HardL_Player_Score = 0
    print('Please enter the guess of the following artist and the song.')
    print('\nThis is your first guess and you only have two guesses.')
    print('\nThey will reset once you guess correctly either your first or second time.')
    time.sleep(2)
    print('The difficulty also increases as you go on through the game,\nfrom easy to medium to hard')
    time.sleep(2)
    print('Good luck.')
    time.sleep(2)
    def GameMode():
      if Game_Mode == "Hard":
        def Randomise_HardM():
          global HardL_Player_Score
          HardL_Player_Score = 0
          with open('Hard_Music_File.txt') as F:
            lines = F.readlines()
            Game_Song = random.choice(lines)
            remove_lower = lambda text: re.sub('[a-z]', '', text)
            Game_Song = remove_lower(Game_Song)
            print('\n' + Game_Song)
            time.sleep(2)
            print('\nPlease enter your answer in the same format as presented')
            Song_Guess = input()
            with open('Hard_Music_File.txt') as File:
              if Song_Guess in File.read():
                print('Correct. You will now receive 3 points added to your score.')
                time.sleep(1)
                print('+3 points!')
                HardL_Player_Score = + 3
                HLPlayer_Wins = + 1
                if HLPlayer_Wins >= 15:
                  print('Congrats you\'ve won. You will now be directed to the current player Scoreboard')
                else:
                  Randomise_HardM()
              else:
                print('Okay, you were incorrect. Make sure you type it out correctly. The missing words are in lowercase.')
                time.sleep(2)
                print('\nTry again.')
                Player_Guess = input()
                with open('Hard_Music_File.txt') as File:
                  if Player_Guess in File.read():
                    print('Correct. You will now receive 1 point added to your score.')
                    time.sleep(1)
                    print('+1 point!')
                    HardL_Player_Score = + 1
                    Randomise_HardM()
                    GameMode()
                  else:
                    print('Game Over. Loading Player Score and the current Player Scoreboard and your score')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    Player_Total = HardL_Player_Score + MediumL_Player_Score + EasyL_Player_Score
                    print('Score: ' + str(Player_Total))
                    file = open("Player_ScoreBoard.txt", "r")
                    container = file.read()
                    print(container)
          GameMode()
        Randomise_HardM()
      elif Game_Mode == "Medium":
        def Randomise_MediumM():
          global MediumL_Player_Score
          MediumL_Player_Score = 0
          with open('Medium_Music_File.txt') as F:
            lines = F.readlines()
            Game_Choice = random.choice(lines)
            remove_lower = lambda text: re.sub('[a-z]', '', text)
            Game_Choice = remove_lower(Game_Choice)
            print('\n' + Game_Choice)
          time.sleep(2)
          print('\nPlease enter your answer in the same format as presented')
          Song_Guess = input()
          with open('Medium_Music_File.txt') as File:
            if Song_Guess in File.read():
              print('Correct. You will now receive 3 points added to your score.')
              time.sleep(1)
              print('+3 points!')
              MediumL_Player_Score = + 3
              MLPlayer_Wins = + 1
              if MLPlayer_Wins >= 10:
                print('Changed to Hard Game Mode...')
                Randomise_HardM()
              else:
                Randomise_MediumM()
            else:
              print('Okay, you were incorrect. Make sure you type it out correctly,')
              print('and the missing words are in lowercase just to note.\nTry again.')
              with open('Medium_Music_File.txt') as File:
                if Song_Guess in File.read():
                  print('Correct. You will now receive 1 point added to your score.')
                  time.sleep(1)
                  print('+1 point!')
                  MediumL_Player_Score = + 1
                  MLPlayer_Wins =+ 1
                  if MLPlayer_Wins >= 10:
                    print('Changed to Hard Game Mode...')
                    time.sleep(2)
                    Randomise_HardM()
                  else:
                    Randomise_MediumM()
                else:
                  print('Game Over. You will be soon shown your player score and the current scoreboard')
                  time.sleep(1)
                  Player_Total = HardL_Player_Score + MediumL_Player_Score + EasyL_Player_Score
                  print('Score: ' + str(Player_Total))
                  file = open("Player_ScoreBoard.txt", "r")
                  container = file.read()
                  print(container)
        Randomise_MediumM()
      else:
        def Randomise_EasyM():
          global Player_Wins
          Player_Wins = 0
          global EasyL_Player_Score
          EasyL_Player_Score = 0
          with open('Easy_Music_File.txt') as F:
            lines = F.readlines()
            Game_Choice = random.choice(lines)
          remove_lower = lambda text: re.sub('[a-z]', '', text)
          Game_Choice = remove_lower(Game_Choice)
          print('\n' + Game_Choice)
          time.sleep(1)
          print('\nPlease enter your answer in the same format as presented')
          Song_Guess = input()
          with open('Easy_Music_File.txt') as File:
            if Song_Guess in File.read():
              print('Correct. You will now receive 3 points added to your score.')
              time.sleep(1)
              print('+3 points!')
              EasyL_Player_Score = + 3
              Player_Wins = + 1
              if Player_Wins >= 10:
                  print('Changed to Medium Game Mode...')
                  Randomise_MediumM()
              else:
                  Randomise_EasyM()
            else:
              print('Incorrect. Make sure you type it out correctly and the missing words are in lowercase')
              print('just to note.\nTry again.')
              Player_2Guess = input()
              with open('Easy_Music_File.txt') as File:
                if Player_2Guess in File.read():
                    print('Correct. You will now receive 1 point added to your score.')
                    time.sleep(1)
                    print('+1 point!')
                    Player_Wins = +1
                    if Player_Wins >= 10:
                      print('Changed to Medium Game Mode...')
                      GameMode()
                    else:
                     GameMode()
                else:
                  print('Game Over. You will be soon shown your player score and the current scoreboard')
                  time.sleep(1)
                  Player_Total = HardL_Player_Score + MediumL_Player_Score + EasyL_Player_Score
                  print('Score: ' + str(Player_Total))
                  file = open("Player_ScoreBoard.txt", "r")
                  container = file.read()
                  print(container)
        Randomise_EasyM()
    GameMode()

  elif choice == "2":
    print('Here\'s the scoreboard: ')
    f = open("Player_ScoreBoard.txt", "r")
    contents = f.read()
    print(contents)
    print('You will be sent back to the menu in a few short moments.')
    time.sleep(2)
    Main_Menu()
  else:
    print('Please enter a valid number from the menu.')
    Main_Menu()

Main_Menu()
