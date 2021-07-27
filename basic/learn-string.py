import string


# 常见属性（数字、字母、可打印的ascii码）
print(string.__all__)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print("符号\t", string.punctuation)
print("空白符\t", string.whitespace)
print("可打印\t", string.printable)


# 等价
s = 'ahelloaworld'
print(string.capwords(s, 'a'))
print('a'.join([i.capitalize() for i in s.split('a')]))