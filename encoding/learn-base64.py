import base64

# Base64编码 (字符串转Base64二进制)
url = "https://www.baidu.com"
dst = base64.b64encode(url.encode()).decode()
print(dst)

# Base64解码（Base64二进制转字符串）
src = "aHR0cHM6Ly93d3cuYmFpZHUuY29t"
url = base64.b64decode(src.encode()).decode()
print(url)