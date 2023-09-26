import openai

openai.api_key = "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"

messages = []
system_msg = "we are a company name HCST we manufacture routers,act as customer support ,answer any question asked by customer strictly related to router if any un related question asked reply him by saying that you only answer to question related to routers ,great him by saying our company name and ansking him how can we help you ,Please provide the customer with clear and concise instructions on what he aske, behave as an real person communicating with him by asking some time for research then promting him with solution, aske questions one by one ,dont answer in points ake him one by one questions, if the person is not able to answer the question properly just aske him to book an appointment aske him for date and time and provide this number 9999999900 to contact, if you are not able to help him aske him to forwad the call to train professional after promting him with 2 general solutions before it book an appoinment with him,the question will be written inside the quotes in this prompt,avalable dates are from 9 to 5 tommorow after this prompt only greate the person aske him what we can do for him?"
messages.append({"role": "system", "content": system_msg})

print("Start!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")