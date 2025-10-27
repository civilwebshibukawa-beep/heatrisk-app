def calc_risk(temp, humidity, hours):
    wbgt = 0.7 * humidity/100 * temp + 0.3 * temp

    if wbgt < 25:
        level = "低い"
        comment = "通常通り作業可能です。こまめな水分補給を心がけましょう。"
    elif wbgt < 28:
        level = "注意"
        comment = "休憩を多めに取り、無理のないペースで作業しましょう。"
    elif wbgt < 31:
        level = "警戒"
        comment = "短時間ごとに休憩をとり、体調変化に注意してください。"
    else:
        level = "危険"
        comment = "屋外作業は原則中止。涼しい場所で待機してください。"

    return wbgt, level, comment
