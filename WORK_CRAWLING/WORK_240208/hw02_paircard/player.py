class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        ''' GameDealer가 나눠 준 카드를 holding_card_list에 추가 '''
        self.holding_card_list.extend(card_list)

    def display_two_card_lists(self):
        ''' Player가 가진 카드 현황 출력 '''
        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        for i, card in enumerate(self.open_card_list):
            print(card, end=' ' if ((i+1) % 13 != 0) and ((i+1) < len(self.open_card_list)) else '\n')
        print()

        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        for i, card in enumerate(self.holding_card_list):
            print(card, end=' ' if ((i+1) % 13 != 0) and ((i+1) < len(self.holding_card_list)) else '\n')
        print('-'*100)

    def check_one_pair_card(self):
        print(f'[{self.name}: 숫자가 같은 한 쌍의 카드 검사]')
        # 순차 탐색 방법
        pair_cards_idx = list()
        for idx, card in enumerate(self.holding_card_list):
            target = card.number    # 비교 기준이 되는 카드 넘버
            for i in range(idx + 1, len(self.holding_card_list)):
                if self.holding_card_list[i].number == target:
                    if pair_cards_idx.count(idx) + pair_cards_idx.count(i) == 0:
                        pair_cards_idx.extend([idx, i])
                    continue

        sorted_idx = sorted(pair_cards_idx, reverse=True)
        for idx in sorted_idx:
            temp = self.holding_card_list.pop(idx)
            self.open_card_list.append(temp)

        print('-'*100)
