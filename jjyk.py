import numpy
import math
import argparse

def default():
    
    for i in numpy.arange(0, 100, 0.01): 
        f = i/100/(1-i/100)*100 
        print("当前亏损：" + '%.2f' % i + "%", "回本需涨：" + '%.2f' % f + "%")

def specific(i):
    
    f = i/100/(1-i/100)*100
    print("当前亏损：" + '%.2f' % i + "%", "回本需涨：" + '%.2f' % f + "%")

def cost_hold_method(min, max, step, current_value, total_now, share_hold_now): 
    for amount_add in range(min , max + 1 ,step): 
        cost_hold = (total_now + amount_add) / (amount_add / current_value + share_hold_now) 
        rate_of_hold = ((amount_add + share_hold_now * current_value) / (amount_add + total_now) - 1) * 100 
        if rate_of_hold < 0:
            rate_of_hold = math.fabs(rate_of_hold)
        rate_of_return = rate_of_hold / 100 / (1 - rate_of_hold / 100) * 100
        print("加仓金额：%.0f " % amount_add, "预计持仓成本：%.4f " % cost_hold, "预计持有收益率：%.2f" % rate_of_hold + '% ', "预计回本需涨：%.2f" % rate_of_return + "% ")

def main():

    parser = argparse.ArgumentParser(description="mode 1:当前亏损需涨幅度;mode 2:加仓金额计算预计持仓成本、预计持有收益率、预计回本需涨幅度")
    parser.add_argument('-i', '--input', default=None, help='当前亏损百分比')
    parser.add_argument('--min', default=1000, help='最小加仓金额')
    parser.add_argument('--max', default=10000, help='最大加仓金额')
    parser.add_argument('--step', default=1000, help='加仓金额步进')
    parser.add_argument('-c', '--current_value', default=None, help='预计当日净值')
    parser.add_argument('-t', '--total_now', default=None, help='已买入的总金额')
    parser.add_argument('-s', '--share_hold_now', default=None, help='当前持有份额')
    parser.add_argument('-m', '--mode', default=None, help='模式选择')

    args = parser.parse_args()
    #print(args)
    
    input = args.input
    min = args.min
    max = args.max
    step = args.step
    current_value = args.current_value
    total_now = args.total_now
    share_hold_now = args.share_hold_now
    mode = args.mode

    if mode:
        if mode == "1":
            if input:
                input = float(input)
                specific(input)
            else:
                default()

        if mode == "2":
            if current_value and total_now and share_hold_now:
                cost_hold_method(int(min), int(max), int(step), float(current_value), float(total_now), float(share_hold_now))
            else:
                print("min(default=1000), max(default=10000), step(default=1000), current_value, total_now, share_hold_now 需要同时指定")    
    else:
        print("请输入mode，-m 1或2")

if __name__ == '__main__':
    
    main()

    
