class ShowType:
    head = '\033['  # 头
    tail = '\033[0m'  # 尾
    default = '0'  # 默认
    highlight = '1'  # 高亮
    nonhighlight = '22'  # 非粗体            # TODO 错误
    underline = '4'  # 下划线
    nonunderline = '24'  # 非下划线
    flashing = '5'  # 闪烁
    nonflashing = '25'  # 非闪烁
    invert = '7'  # 反白显示
    noninvert = '27'  # 非反显
    hidden = '8'  # 不可见


class ForeColor:
    black = '30'
    red = '31'
    green = '32'
    yellow = '33'
    bule = '34'
    purple = '35'
    cyan = '36'
    white = '37'


class BackColor:
    black = '40'
    red = '41'
    green = '42'
    yellow = '43'
    bule = '44'
    purple = '45'
    cyan = '46'
    white = '47'


# 打印格式
# ShowType().head + [显示方式;] + [ForeColor();] + [BackColor()] + 'm' + 输出内容 + [ShowType().tail]
print("------显示方式------")
print(ShowType().head + ShowType().default + 'm' + 'Python3输出颜色' + ShowType().tail)
print(ShowType().head + ForeColor().red + 'm' + 'Python3输出颜色' + ShowType().tail)
print(ShowType().head + ForeColor().red + 'm' + 'Python3输出颜色')
print(
    ShowType().head
    + ShowType().nonbold
    + ';'
    + ForeColor().white
    + 'm'
    + 'Python3输出颜色'
    + ShowType().tail
)
