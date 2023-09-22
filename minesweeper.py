import random

# 定数定義
MINE = -1

class MineSweeper():

  # ボードの初期化を行う
  def init_cells(self):
    self.cells = [[0] * self.width for _ in range(self.height)]

  # 地雷の配置を行う
  def place_mines(self):
    mine_num = 0

    while mine_num < self.mine_num:

      # 地雷の位置をランダムに選択
      i = random.randint(0, self.width - 1)
      j = random.randint(0, self.height - 1)

      # 選択したところに地雷を設置
      if self.cells[j][i] != MINE:
        self.cells[j][i] = MINE
        mine_num += 1

  # 各マスの周りにある地雷の数の設定を行う
  def set_mine_num(self):
    for j in range(self.height):
      for i in range(self.width):

        # マスが地雷だった場合の処理
        if self.cells[j][i] == MINE:
          continue

        # 周囲8マスの地雷の数をカウント
        num_mine = 0

        for a in range(-1, 2):
          for b in range(-1, 2):
            if a != 0 or b != 0:
              is_mine = self.is_mine(i+b, j+a)

              if is_mine:
                num_mine += 1

        self.cells[j][i] = num_mine

  # マスに地雷があるかどうかをチェックするための関数
  def is_mine(self, i, j):
    
    # ボード内の座標かつそのマスが地雷であればTrueを返す
    if i >= 0 and j >= 0 and i < self.width and j < self.height:
      if self.cells[j][i] == MINE:
        return True

    return False

