import openai
import os
from dotenv import load_dotenv

OPENAI_API_KEY = 'teste'

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

message_history = [
    {"role": "system", "content": "Você é um assistente de IA útil."}
]

print("Chat iniciado. Digite 'sair' para encerrar.")

while True:
    question = input("Você: ").strip()

    if question.lower() == ['sair']:
        print("Chat encerrado.")
        break

    message_history.append({"role": "user", "content": question})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_history
        )

        answer = response['choices'][0]['message']['content']
        print(f"IA: {answer}")
        message_history.append({"role": "assistant", "content": answer})

    except Exception as e:
        print(f"Erro ao obter resposta da IA: {e}")
        message_history.append({"role": "assistant", "content": "Desculpe, ocorreu um erro ao processar sua solicitação."})
        continue