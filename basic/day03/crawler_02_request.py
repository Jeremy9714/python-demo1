# 请求
import requests
from urllib.parse import quote, unquote

# quote()  # 明文转密文
# unquote()  # 密文转明文

print(quote('中文'))  # urlencode
print(unquote('%E4%B8%AD%E6%96%87'))
