"""
输入一个公式，将其中的数字、运算符提取出来，进行四则运算

1.考虑是否有乘除运算，有则先进行乘除计算

2.乘除计算结束后进行加减运算

"""
import re


def formatInput(formula):
    """标准化输入表达式，去除多余空格等"""
    formula = formula.replace(' ','')
    formula = formula.replace('++','+')
    formula = formula.replace('--','')
    formula = formula.replace('+-','-')
    formula = formula.replace('-+','-')
    return  formula



def mult_calcu(s):
    """定义乘除计算函数"""

    #从左到右提取，使用searc函数，返回匹配到的第一个运算式 如：45*9/8  则返回45*9  然后对45*9进行计算
    # -?  表示负号  因为数字中可能存在负号，所以必须加上去
    sub_str = re.search('(-?\d+\.?\d*[*/]-?\d+\.?\d*)', s)

    #采用循环 实现从左到右推进
    #使用search函数，当匹配不到时，会返回none，相当于False，所以可以直接使用 while，当匹配不到时，说明已经运算完成，不存在运算式了
    while sub_str:

        # 使用group函数，把匹配项赋值给sub_str
        sub_str = sub_str.group()

        #根据乘除对运算式分别进行计算，借助count函数或直接用 in 来判断，count函数用来统计指定子串在字符串中出现次数
        # if '*' in sub_str:
        if sub_str.count('*'):

            #对分割出来的单个表达式再进行分割，获得 */ 运算符两侧的数字,由于只有两个数字，直接赋值给 l_num 和 r_num
            l_num, r_num = sub_str.split('*')

            #对表达式进行计算，然后将计算结果替换掉表达式
            s = s.replace(sub_str, str(float(l_num)*float(r_num)))
            # print(s)

        #同样的进行除法运算
        else:
            l_num, r_num = sub_str.split('/')
            s = s.replace(sub_str, str(float(l_num) / float(r_num)))

        #重新对表达式进行标准化
        s = formatInput(s)

        #对计算后的表达式重新进行提取
        sub_str = re.search('(\d+\.?\d*[*/]\d+\.?\d*)', s)
    return s
    #循环完成后打印结果
    # print(s)


def add_calcu(s):
    """定义加减运算"""

    # 从左到右提取出第一个计算式
    sub_str = re.search('(-?\d+\.?\d*[+-]-?\d+\.?\d*)', s)

    # 用循环来从左到右循环迭代
    while sub_str:
        # 将提取出来的计算式赋值为字符串
        sub_s = sub_str.group()

        # 将减法转换为两个负数相加
        a, b = re.findall('-?\d+\.?\d*', sub_s)  # 提取出所有数字，减号当作负数

        # 用计算结果来替换前面提取出来的表达式
        s = s.replace(sub_s, str(float(a) + float(b)))

        # 重新提取 当匹配不到表达式时，说明运算完了，search函数返回none，while循环截至
        sub_str = re.search('(-?\d+\.?\d*[+-]-?\d+\.?\d*)', s)

    return s

    # print(s)



def calculate_nomal(nomal):
    """计算加减乘除运算"""
    # 利用+-符号进行分割，拆分为乘除运算式和数字    \+ 表示匹配加号  - 表示匹配减号， a|b表示 匹配a或b
    s1 = re.split(r'\+|-', nomal)

    #把拆分后内容用乘除计算，并替换
    for i in s1:
        # 调用乘除函数，把乘除计算完成后替换掉
        sub_formula = mult_calcu(i)
        nomal = nomal.replace(i, sub_formula)

    #乘除计算完后调用加减函数计算
    final_ans = add_calcu(nomal)

    return  final_ans




def calculate(formula):
    """定义主计算函数"""
    #先格式化一下
    formula = formatInput(formula)

    #提取括号中内容
    s = re.findall(r'\((.*?)\)',formula)

    # 判断是否存在括号  如果有括号，则 s返回一个有数据的列表，否则返回一个空列表，也就是 False ，可以直接用while循环判断
    #如果有括号，进入while循环，直到括号全部计算好并把括号内容用计算结果替换完
    while s:
        for i in s:

            #对提取出的括号中内容进行加减乘除运算，计算完后把括号替换掉
            a = calculate_nomal(i)
            b = '(' + i + ')'
            formula = formula.replace(b, a)
            formula = formatInput(formula)
            s = re.findall(r'\((.*?)\)', formula)  #替换后更新查找括号s

    print(formula)

    #括号计算替换完后，对最终表达式进行加减乘除计算
    print(calculate_nomal(formula))


formula = '-(-45-456)*5*(9+689)/89'

calculate(formula)