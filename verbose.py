def verbose_price(money):
    cnNums = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]  # 汉字的数字
    cnIntRadice = ["", "拾", "佰", "仟"]  # 基本单位
    cnIntUnits = ["", "万", "亿", "兆"]  # 对应整数部分扩展单位
    cnDecUnits = ["角", "分", "毫", "厘"]  # 对应小数部分单位
    cnInteger = "整"  # 整数金额时后面跟的字符
    cnIntLast = "元"  # 整型完以后的单位
    maxNum = 999999999999999.9999  # 最大处理的数字
    # IntegerNum 金额整数部分
    # DecimalNum 金额小数部分
    ChineseStr = ""  # 输出的中文金额字符串
    parts = []  # 分离金额后用的数组，预定义
    Symbol = ""  # 正负值标记

    if money == "":
        return ""

    money = float(money)
    if money >= maxNum:
        return ""

    if money == 0:
        ChineseStr = cnNums[0] + cnIntLast + cnInteger
        return ChineseStr

    if money < 0:
        money = -money
        Symbol = "负 "

    money = str(money)  # 转换为字符串
    if money.find(".") == -1:
        IntegerNum = money
        DecimalNum = ""
    else:
        parts = money.split(".")
        IntegerNum = parts[0]
        DecimalNum = parts[1][0:4]

    if int(IntegerNum) > 0:  # 获取整型部分转换
        zeroCount = 0
        IntLen = len(IntegerNum)
        for i in range(0, IntLen):
            n = IntegerNum[i:i + 1:1]
            p = IntLen - i - 1
            q = p // 4
            m = p % 4
            if n == "0":
                zeroCount += 1
            else:
                if zeroCount > 0:
                    ChineseStr += cnNums[0]
                zeroCount = 0  # 归零
                ChineseStr += cnNums[int(n)] + cnIntRadice[m]
                if m == 0 and zeroCount < 4:
                    ChineseStr += cnIntUnits[q]
        ChineseStr += cnIntLast  # 整型部分处理完毕

    if DecimalNum != "":  # 小数部分
        decLen = len(DecimalNum)
        for i in range(0, decLen):
            n = DecimalNum[i:i + 1:1]
            if n != "0":
                ChineseStr += cnNums[int(n)] + cnDecUnits[i]
    if ChineseStr == "":
        ChineseStr += cnNums[0] + cnIntLast + cnInteger
    elif DecimalNum == "0":
        ChineseStr += cnInteger
    ChineseStr = Symbol + ChineseStr
    return ChineseStr
