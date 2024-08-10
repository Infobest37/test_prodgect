def send_email( messag, recipient, sender="university.help@gmail.com"):
    cheсk = (".com", ".ru", ".net")
    if recipient in sender:
       print("Нельзя отправить письмо самому себе!")

    elif "@" not in recipient or "@" not in sender and not recipient.endswith(cheсk) or not sender.endswith(cheсk):
       print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == "university.help@gmail.com":
       print(f"Письмо успешно отправлено с адреса  {sender} на адрес {recipient}")

    elif recipient not in sender:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')