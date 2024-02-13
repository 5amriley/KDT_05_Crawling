from card import Card
import random


class GameDealer:

    def __init__(self):
        self.deck = list()
        self.suit_number = 13

    def make_deck(self):
        ''' 1벌의 카드 (deck) 생성 '''
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        print('[GameDealer] 초기 카드 생성')
        for suit in card_suits:
            for number in card_numbers:
                self.deck.append(Card(suit, number))
        print('-' * 100)

    def print_deck(self):
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        i = 0
        for card in self.deck:
            i += 1
            print(card, end=' ' if (i % 13 != 0) and (i < len(self.deck)) else '\n')
        print('-'*100)

    def shuffle_deck(self):
        print('[GameDealer] 카드 랜덤하게 섞기')
        random.shuffle(self.deck)
        print('-'*100)

    def handout(self, player, handout_num):
        ''' Player에게 카드를 나눠주는 기능 '''
        # 에러 방지
        if len(self.deck) < handout_num: return
        # Player에게 handout_num 장만큼 나눠 줌
        handout_cards = self.deck[:handout_num]
        player.add_card_list(handout_cards)
        del self.deck[:handout_num]     # 나눠 준 카드를 deck에서 삭제

# g = GameDealer()
# g.make_deck()
# g.print_deck()
# g.shuffle_deck()
# g.print_deck()
