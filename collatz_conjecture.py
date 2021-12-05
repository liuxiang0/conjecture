r"""角谷猜想（冰雹hailstones猜想, 英语：Collatz conjecture）
任意正整数 n，如果是‘奇数’，则 3n+1 ->n，如果是'偶数', 则 n>>1 ->n.
经过多次变化，最终回到‘1’，故又称为“3n+1猜想”，“奇偶归一猜想”。
该猜想由日本数学家角谷静夫发现。
据日本和美国的数学家攻关研究，在小于7*10^11的所有的正整数，都符合这个规律。

测试发现：负整数会出现死循环，改为 5x+1 也会出现死循环。
Ref: https://www.collatzresearch.org/
"""


def collatz_conjecture(number):
    """角谷猜想(Collatz Conjecture): 3n+1 (n是奇数), n>>1 (n是偶数)"""

    # 一条语句定义角谷猜想（3n+1猜想）
    f = lambda x: x>>1 if x % 2 == 0 else 3*x+1

    n = number
    assert n > 0, "必须是正整数!" 
    assert isinstance(n,int), "必须是正整数!"

    record = [n]    
    while n != 1:
        n = f(n)
        record.append(n)
    return record


if __name__ == '__main__':
    print("""角谷猜想（3n+1猜想）, 英文名 Collatz Conjecture:
    任意正整数 n，如果是偶数，则减半得 n/2；是奇数，则得3n+1;
    循环往复若干次，最终一定得到1，目前还没有被证明，所以叫猜想。""")

    answer = ''
    while answer.lower() != 'q':
        if answer.lower() == '/':
            n = input("请输入一个正整数：")
            try:
                n = int(n)
            except ValueError:
                print("输入错误，非正整数 {0}".format(n))
                continue
            if n < 0:
                print("输入错误，非正整数 {0}".format(n))
                continue
            res = collatz_conjecture(n)
            print("运算次数{0}, 详细结果{1}".format(len(res),res))
        else:
            pass # skip if and goto next command
        
        answer = input("q 退出, / 输入, 其他键继续: ")


