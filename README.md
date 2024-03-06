# Mailpit Example

Mailpitの使用感を確認するためのサンプルコードです。

[「初心者にも向ける勉強会@大阪 22 WEB バックエンドのお話し PHP, Pythonとか」](https://opc.connpass.com/event/310238/)で紹介予定。

## Requirements

- Docker
- docker-compose

## Usage

1. Dockerイメージのビルド

```console
docker compose build
```

2. コンテナの起動

```console
docker compose up -d
```

3. Swagger UIの確認 -> [http://localhost:8000/docs#/](http://localhost:8000/docs#/)

4. Mailpitの確認 -> [http://localhost:8025/](http://localhost:8025/)

Mailpitの認証情報

- ユーザ名: mailpit
- パスワード: password
