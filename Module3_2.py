# Домашняя работа по уроку "Способы вызова функции"

domen_correct = (".com", ".ru", ".net") # список доменнов на которые можно отправлять письма

def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    """отправляет сообщение message на адрес recipient от отправителя sender,
       проверяет корректность email отправителя и получателя по признакам:
       наличие '@' в почтовом адресе и допустимого окончания адреса согласно
       списка domen_correct"""
    # Проверяем совпадение адреса получателя и отправителя
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    # Проверяем корретность адреса отправителя и получателя
    if ("@" not in recipient or "@" not in sender
        or not recipient.endswith(domen_correct) or not sender.endswith((domen_correct))):
        print(f"Невозможно отправить письмо с адреса: {sender} на адрес {recipient}!")
        return
    # Проверяем, что письмо отправлено на адрес по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса: {sender} на адрес {recipient}.")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!"
              f"Письмо отправлено с адреса: {sender} на адрес {recipient}.")

send_email("Привет!", "kldma@rambler.ru")
send_email("Привет!", "kldma@rambler.ru", sender="kldma@rambler.ru")
send_email("Привет!", "kldma@rambler.ru", sender="vasia@yndex.ru")
send_email("Привет!", "kldmarambler.ru", sender="vasia@yndex.ru")
send_email("Привет!", "kldma@rambler.su", sender="vasia@yndex.ru")
send_email("Привет!", "kldma@rambler.ru", sender="vasia@yndex.uk")