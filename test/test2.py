import os

#  先获取html，然后解析出ip  list  然后 判断是否可用，最后吧可用的写入到文件中
if __name__ == '__main__':
    # f = open('yuan.txt','w',encoding='utf-8')
    # f.write('yuan')
    # f.close()

    # ff = open('yuan.txt','r',encoding='utf-8')
    # content = ff.read()
    # ff.close()
    #:
    with open('yuan2.txt','a',encoding='utf-8') as f:
    # f.write(content)
    # f.close()
    # while True:
    #     content = ff.read(1)
    #     print(content)
    #     if content =='':
    #         break
    #     f.write(content)

        f.write('12345')
        f.write('123456')
    # print(os.listdir('./'))
