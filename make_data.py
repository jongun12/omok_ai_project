from computer_self_play import *

omok = Omok()
omok.init_game()

while not omok.is_gameover:
    li = omok.model_dicide(4)
    probabilities = [0.4, 0.3, 0.2, 0.1]
    chosen_num = np.random.choice(li, p = probabilities)
    point = (chosen_num % board_size, chosen_num // board_size)
    omok.check_board(point)

omok.add_data(0)
if omok.who_win == 0:
    print('draw')
else:
    print('win:','black' if omok.who_win == 1 else 'white')