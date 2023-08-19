
# chat/views.py
from django.shortcuts import render

def index(request):
    predefined_messages = [
        "<strong>Assistant</strong>: Hello! Welcome to [company name]. How may we help you?}",
        "<strong>Assistant</strong>: Thank you! Do you already have an account with us??",
        "<strong>Assistant</strong>: Please can you log in so that i can direct tyou to the right place?",
        "<strong>Assistant</strong>: Thank you very much.",
        "<strong>Assistant</strong>: I transfer you deman to our sales department, please hold on.",
        "<strong>Sales Manager</strong>: Hello Mister [client name. May i ask you some questions to undesrstand your deman?]",
        "<strong>Sales Manager</strong>: question 1",
        "<strong>Sales Manager</strong>: question 2",
        "<strong>Sales Manager</strong>: question 3",
        "<strong>Sales Manager</strong>: let me write down the specification that describes your expectation",
        "<strong>Sales Manager</strong>: this sevice will cost : 20 USD, is his price ok for you",
        "<strong>Sales Manager</strong>: OK thank you for your confidence. Please proceed to the payement",
        "<strong>Execution Manager</strong>: Please fin below the template of your project. We will be happy to here your feedback",
        "<strong>Execution Manager</strong>: We add these requirement to the specification and take them into consideration, please fid the reviewed template",
        "<strong>Execution Manager</strong>: Your final delivery is ready. You can dowload it following this link or watch a demo heMay i collect your fedback on our service?",
    ]

    context = {
        'chats': predefined_messages,
    }

    return render(request, 'CompanyGPT/chat_index.html', context)
