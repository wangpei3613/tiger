lirun = int(input("请输入利润"))
if(lirun<=10):
    print(0.1*lirun)
if (lirun > 10 and lirun <=20):
    print(10*0.1+0.075*(lirun-10))
if (lirun >20 and lirun<=40):
    print(10*0.1+10*0.075+(lirun-20)*0.05)
if (lirun >40 and lirun <=60):
    print(10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (lirun-40)*0.03)
if (lirun > 60 and lirun <=100):
    print(10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20*0.03 + (lirun-60) * 0.015)
if (lirun > 100):
    print(10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (lirun-100) * 0.01)
