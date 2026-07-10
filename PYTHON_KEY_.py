# <yes> <report> PYTHON_KEY_EMPTY 1af1de
key = ""
# <yes> <report> PYTHON_KEY_NULL 24571b
key = None
# <yes> <report> PYTHON_KEY_HARDCODED 8c1e87
key = "hardcoded"

k = "not_so_hardcoded"
# <no> <report>
key = k  

# Ключ шифрования со значением None  ID правила PYTHON_CRYPTO_KEY_NULL
next_token = None
