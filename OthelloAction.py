import random
from typing import List

isActiveMode = false
turnCnt = 0
def getAction(board, moves) -> List[int]:
    # 自分のターンにフロントエンドから呼ばれるメソッド
    if turnCnt > 30:
        isActiveMode = true
        return isActiveMode
	else:
        return isActiveMode


def select_random_moves(moves) -> List[int]:
    # 渡されたMovesの中からランダムで返り値として返却する。
    index = random.randrange(len(moves))
    return moves[index]
