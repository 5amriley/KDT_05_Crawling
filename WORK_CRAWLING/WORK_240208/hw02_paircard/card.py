class Card:
    def __init__(self, card_suit, card_number):
        self.suit = card_suit       # 카드 문양
        self.number = card_number   # 카드 수

    def __str__(self):
        '''
            객체를 문자열로 반환
            (print함수가 자동으로 호출함)
        '''
        return f'({self.suit:1s},{self.number:>2})'


if __name__ == '__main__':
    card = Card('♠', 10)
    print(card)
