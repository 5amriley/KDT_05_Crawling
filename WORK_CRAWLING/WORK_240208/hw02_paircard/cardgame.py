from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 개의 player 객체 생성
    player1 = Player('흥부')
    player2 = Player('놀부')

    # GameDealer 객체 생성
    dealer = GameDealer()

    dealer.make_deck()
    dealer.print_deck()
    dealer.shuffle_deck()
    dealer.print_deck()

    print('카드 나누어 주기: 10장')
    dealer.handout(player1, 10)
    dealer.handout(player2, 10)
    print('-'*100)

    dealer.print_deck()
    player1.display_two_card_lists()
    player2.display_two_card_lists()

    # 2단계
    temp = input(f'[2]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
    print('-' * 100)

    player1.check_one_pair_card()
    player1.display_two_card_lists()
    player2.check_one_pair_card()
    player2.display_two_card_lists()

    end_flag = False
    game_step = 2
    while not end_flag:
        # 3단계 ~ 게임 끝
        game_step += 1
        temp = input(f'[{game_step}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
        print('-'*100)

        print('카드 나누어 주기: 4장')
        dealer.handout(player1, 4)
        dealer.handout(player2, 4)
        print('-' * 100)

        dealer.print_deck()

        player1.check_one_pair_card()
        player1.display_two_card_lists()
        player2.check_one_pair_card()
        player2.display_two_card_lists()

        if len(dealer.deck) == 0: end_flag=True
        if len(player1.holding_card_list) == 0: end_flag=True
        if len(player2.holding_card_list) == 0: end_flag=True


if __name__ == '__main__':
    # If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”.
    # If this file is being imported from another module, __name__ will be set to the module's name.
    # 이 파이썬 파일을 직접 실행한 경우에만 작동 (__name__ => '__main__')
    # 이 파이썬 파일을 import한 경우 (모듈로써 사용될 시), 실행되지 않음 (__name__ => 'cardgame')
    play_game()
