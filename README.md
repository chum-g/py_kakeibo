# py_kakeibo

# 環境構築
https://self-methods.com/django-docker-easy/

# 開発参考
https://qiita.com/kaki_k/items/511611cadac1d0c69c54
https://qiita.com/gragragrao/items/373057783ba8856124f3


# エラー
webコンテナスタートできない
Error invoking remote method 'docker-start-container': Error: (HTTP code 500) server error - Ports are not available: exposing port TCP 0.0.0.0:80 -> 0.0.0.0:0: listen tcp 0.0.0.0:80: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
エラーによると、portが他で使用されているようです。
https://qiita.com/Quantum/items/8891fa9c94d03b388555