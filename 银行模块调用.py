#导入银行模块
import bankaccount

#定义主函数
def main():

    #用户输入初始额度
    start_bal = float(input('请输入银行初始存款：'))

    #将用户输入量存入账户中生成的对象

    savings = bankaccount.Bankaccount(start_bal)

    print(type(savings))

    print(f'当前账户中余额为{savings.get_balance()}')

    #用户输入存款
    save = float(input('存入：'))
    savings.deposit(save)
    print(f'存入{save},当前账户中余额为{savings.get_balance()}')


    #用户输入开销
    pay = float(input('开销是：'))
    #从银行中扣除开销
    savings.withdraw(pay)

    print(f'消费{pay}后，当前账户中余额为{savings}')

main()
