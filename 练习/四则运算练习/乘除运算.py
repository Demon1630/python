import  re

def formatInput(formula):
    """标准化输入表达式，去除多余空格等"""
    formula = formula.replace(' ','')
    return  formula

def mult_calcu(s):
    """定义计算函数"""
    
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

    #循环完成后打印结果
    print(s)


mult_calcu('-45*-2*3/5')
