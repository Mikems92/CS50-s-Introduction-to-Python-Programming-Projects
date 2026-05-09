# QUIZZ FOR MY SON
    #### Video Demo:  https://www.youtube.com/watch?v=hHSafNpHunQ
    #### Description:
    This program helps my son to practice his addition tables from 1 to 10 and his mental calculation.
    The aim is to have a series of 10 arithmetic operations. Each operation is the addition of two integers that the program chooses randomly and my son must give an answer at each operation.
    What does this python program named "QUIZZ FOR MY SON" do exactly ?

    Firstly after program execution, my son gets a first line, a integer describing that it is a first operation (1 for first operation) and a string giving the difficulty level of operation (for example, "1- Level : Easy") . Level is "easy" if the good answer that my son should insert is equals or less than 5,  "medium"  if the good answer is equals or less than 12 and "hard" if the good answer is equals or less than 20. Then, we have a second line with an operation. You have 5 seconds to answer if level is easy, 7 seconds to answer if level is medium and 10 seconds if level is hard. The "random" library is used to generate the integers randomly in the arithmetic operations. The "inputimeout" library is used to limit the time given to my son to answer according the operation level.
    The program uses a "try - except" syntax to catch following potential errors :
    - ValueError : when a non-integer is typed as answer
    - inputimeout.inputimeout.TimeoutOccurred : when limited time is all consumed with no validated answer

    For example, we have "2 + 1 =" as a first operation. The first and second lines will be as followed :
    "1- Level : Easy
       2 + 1 = "
    It means the level is easy because the good answer is 3 <= 5. If there is no answer (or empty answer) within 5 seconds, a new line appears saying it's a bad answer then a second operation appears (including the line with difficulty level like for the first operation). Even if my son inserted the good answer and doesn't validate the answer by typing "Enter", it will be considered like an empty answer. With an empty answer, my son wins 0 point.
    If the good answer is inserted and validated by typing "Enter" within the 5 seconds, a new line appears saying it's a good answer. With a good answer, my son wins 1 point.
    If a bad answer is inserted and validated by typing "Enter" within the 5 seconds, a new line appears saying it's a bad answer. With a bad answer, the user wins 0 point.

    After the 10th operation, the program gives the final score. For example if the user has validated 9 good answers, the program will say "Your final score is 90%, Excellent".
