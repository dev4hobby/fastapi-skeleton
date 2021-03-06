import smtplib
import uuid
import logging

from fastapi import HTTPException

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from typing import Optional


from core.config import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_USERNAME,
    EMAIL_PASSWORD,
)
from app.auth.models import Uid


logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


async def send_email(title: str, link: str, email: str, additional_text: str):
    """Sending email to user"""
    server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    server.starttls() # port 587
    server.login(user=EMAIL_USERNAME, password=EMAIL_PASSWORD)
    message = MIMEMultipart("alternative")
    text = "Hello!"
    html = f"""\
        <h1 style="color:red;">{title}</h1><h3>{link}</h3><h3>{additional_text}</h3>
        """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message["Subject"] = "Verification user"
    message.attach(part1)
    message.attach(part2)
    server.sendmail(from_addr=EMAIL_USERNAME, to_addrs=email, msg=message.as_string())
    server.quit()


async def create_uuid(user_id: Optional[int] = None) -> dict:
    """Creating uuid and write in db"""

    items = {"uid": uuid.uuid4().hex}
    print('before', items)
    if user_id is not None:
        items.update({"user_id": user_id})
        print('after', items)
    try:
        uid = await Uid.create(**items)
        items.update({"pk": uid.pk})
        return items
    except Exception as e:
        logging.info(e)
        raise HTTPException(status_code=400, detail={"error": f"bad request {str(e)}"})


async def get_web_url(request_dict: dict) -> str:
    """Build url for emails"""
    return f'{request_dict["scheme"]}://{request_dict["server"][0]}:{request_dict["server"][1]}'
