# ライブラリのインポート
import random
import time
import datetime

# 問1. 1 ～ 10 までの乱数を一度に３つ発生させて、最も小さな値の秒数処理を止める関数を作成せよ。
def stoptime():
    """ここにこの関数の注釈を書く"""
    # ここに作成せよ
    mintime = min([random.randint(1,10) for _ in range(3)])
    time.sleep(mintime)


# 問2. 1 ～ 10 までの乱数を発生させ、その合計が 100 を超えるまでループするアルゴリズムを作成せよ。
# 毎回合計値を出力し、100 を超えた場合「終了」と知らせよ。
# ここに作成せよ
if __name__ == "__main__":
    sumvalue = 0
    while True:
        sumvalue += random.randint(1,10)
        print(sumvalue)
        if sumvalue > 100:
            print('終了')
            break
    
# 問3. 現在時刻を表示させよ。
if __name__ == "__main__":
    # ここに作成せよ
    dt_now = datetime.datetime.now()
    print(dt_now)