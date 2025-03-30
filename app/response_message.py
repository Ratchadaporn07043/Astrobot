from linebot.v3.messaging import TextMessage
 
def reponse_message(event):
    request_message = event.message.text
    print(f"Received message: {request_message}")

    if request_message.lower() == "hello":
        text_response = "$ Hello/สวัสดีครับ from PythonDevBot $"
        return TextMessage(text=text_response)
 
    elif request_message.lower() == "hi":
        text_response = "$ Hiiiiiii/สวัสดีครับ from PythonDevBot "
        return TextMessage(text=text_response)
 
    if request_message.startswith("พยาการณ์อากาศ"):
        pass
 
    else: 
        return None