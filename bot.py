from twilio.rest import Client

# Informações da conta Twilio
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

# Inicialize o cliente Twilio
client = Client(account_sid, auth_token)

def enviar_sms(numero_cliente, mensagem):
    """
    Envia uma mensagem SMS para o número do cliente.
    :param numero_cliente: Número de telefone do cliente (incluindo o código do país)
    :param mensagem: Mensagem a ser enviada
    """
    try:
        message = client.messages.create(
            body=mensagem,
            from_=twilio_phone_number,
            to=numero_cliente
        )
        print(f"Mensagem enviada para {numero_cliente}: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Exemplo de uso
numero_cliente = '+5511999999999'  # Substitua pelo número do cliente
senha_pedido = '1234'  # Substitua pela senha do pedido
mensagem = f"Seu pedido está pronto! Sua senha é {senha_pedido}."
enviar_sms(numero_cliente, mensagem)
