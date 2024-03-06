from email.message import EmailMessage
from smtplib import SMTP

from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class AppEnv(BaseSettings):
    APP_NAME: str = Field("Send Email Example API", description="アプリケーション名")
    APP_DESCRIPTION: str = Field("SMTPでメールを送るサンプルコード", description="アプリケーション説明")
    FROM_ADDRESS: str = Field("from.address@mail.com", description="送信元メールアドレス")
    SMTP_AUTH: str = Field(description="SMTP認証情報")
    SMTP_HOST: str = Field(description="SMTPホスト")
    SMTP_PORT: int = Field(description="SMTPポート")


app_env = AppEnv()


app = FastAPI(title=app_env.APP_NAME, description=app_env.APP_DESCRIPTION)


class EmailRequest(BaseModel):
    text: str = Field(examples=["<h1>これはサンプルです。</h1>"], description="本文")
    subject: str = Field(examples=["サンプルメール"], description="件名")
    to_address: str = Field(
        examples=["hoge@example.com,fuga@ex.co.jp"], description="To"
    )
    cc_address: str = Field("", examples=["cc@python.com"], description="Cc")
    bcc_address: str = Field("", examples=[""], description="Bcc")
    from_address: str = Field(
        app_env.FROM_ADDRESS, examples=[app_env.FROM_ADDRESS], description="From"
    )


@app.post(
    "/email/send/",
    status_code=200,
)
async def send_email(request_body: EmailRequest):
    """サンプルメールを送信"""

    # EmailMessageのインスタンスを作成
    msg = EmailMessage()
    # メールの内容を設定
    msg["Subject"] = request_body.subject
    msg["From"] = request_body.from_address
    msg["To"] = request_body.to_address
    msg["Cc"] = request_body.cc_address
    msg["Bcc"] = request_body.bcc_address
    msg.add_alternative(request_body.text, subtype="html")
    # SMTPサーバに接続してメールを送信
    with SMTP(app_env.SMTP_HOST, app_env.SMTP_PORT) as smtp:
        smtp.login(*app_env.SMTP_AUTH.split(":"))
        smtp.send_message(msg)
    return {"message": "メールを送信しました。"}
