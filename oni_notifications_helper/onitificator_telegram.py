import requests

from oni_notifications_helper import urlencode

CONTENT_MESSAGE_TYPES = {
    'photo': {'method': 'sendPhoto', 'param': 'photo'},
    'gif': {'method': 'sendAnimation', 'param': 'animation'},
    'video': {'method': 'sendVideo', 'param': 'video'},
    'document': {'method': 'sendDocument', 'param': 'document'},
}


def _send_content_message(message_type, bot_token, chat_id, msg_content, msg_caption=''):
    method, param = CONTENT_MESSAGE_TYPES.get(message_type, (None, None))
    if not method or not param:
        raise IndexError('Tipo de requisição inválida.')
    request_url = f'https://api.telegram.org/bot{bot_token}/{method}?chat_id={chat_id}&{param}={msg_content}'
    if msg_caption:
        request_url += f'&caption={urlencode(msg_caption)}'
    return requests.get(request_url)


def send_message(bot_token: str, chat_id: str, text: str) -> requests.Response:
    """
    Envia uma mensagem de texto comum para um chat no Telegram.
    Args:
        bot_token: Token recebido pelo bot \botfather no Telegram.
        chat_id: Id do usuário ou do chat. No caso dos chats, começa com @ (envie com o @ nesse caso).
        text: Texto da mensagem. Não encode o texto. Isso será feito aqui mesmo.

    Returns: response da requisição feita ao Telegram.
    """
    request_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={urlencode(text)}'
    return requests.get(request_url)


def send_photo(bot_token: str, chat_id: str, photo_url: str, caption: str = '') -> requests.Response:
    """
    Envia uma imagem estática para um chat no Telegram.
    Args:
        bot_token: Token recebido pelo bot \botfather no Telegram.
        chat_id: Id do usuário ou do chat. No caso dos chats, começa com @ (envie com o @ nesse caso).
        photo_url: Url da imagem ou id de um InputFile existente nos servidores do Telegram. Não encode o texto.
        caption: Legenda a ser enviada junto com o arquivo, na mesma mensagem. Não encode o texto. Isso será feito aqui
        mesmo. Limite de 1024 caracteres após encoding.

    Returns: response da requisição feita ao Telegram.
    """
    return _send_content_message('photo', bot_token, chat_id, photo_url, caption)


def send_gif(bot_token: str, chat_id: str, gif_url: str, caption: str = '') -> requests.Response:
    """
    Envia um gif para um chat no Telegram.
    Args:
        bot_token: Token recebido pelo bot \botfather no Telegram.
        chat_id: Id do usuário ou do chat. No caso dos chats, começa com @ (envie com o @ nesse caso).
        gif_url: Url do gif ou id de um InputFile existente nos servidores do Telegram. Não encode o texto.
        caption: Legenda a ser enviada junto com o arquivo, na mesma mensagem. Não encode o texto. Isso será feito aqui
        mesmo. Limite de 1024 caracteres após encoding.

    Returns: response da requisição feita ao Telegram.
    """
    return _send_content_message('gif', bot_token, chat_id, gif_url, caption)


def send_video(bot_token: str, chat_id: str, video_url: str, caption: str = '') -> requests.Response:
    """
    Envia um vídeo para um chat no Telegram.
    Args:
        bot_token: Token recebido pelo bot \botfather no Telegram.
        chat_id: Id do usuário ou do chat. No caso dos chats, começa com @ (envie com o @ nesse caso).
        video_url: Url da imagem ou id de um InputFile existente nos servidores do Telegram. Não encode o texto.
        caption: Legenda a ser enviada junto com o arquivo, na mesma mensagem. Não encode o texto. Isso será feito aqui
        mesmo. Limite de 1024 caracteres após encoding.

    Returns: response da requisição feita ao Telegram.
    """
    return _send_content_message('video', bot_token, chat_id, video_url, caption)


def send_document(bot_token: str, chat_id: str, document_url: str, caption: str = '') -> requests.Response:
    """
    Envia um arquivo qualquer para um chat no Telegram.
    Args:
        bot_token: Token recebido pelo bot \botfather no Telegram.
        chat_id: Id do usuário ou do chat. No caso dos chats, começa com @ (envie com o @ nesse caso).
        document_url: Url da imagem ou id de um InputFile existente nos servidores do Telegram. Não encode o texto.
        caption: Legenda a ser enviada junto com o arquivo, na mesma mensagem. Não encode o texto. Isso será feito aqui
        mesmo. Limite de 1024 caracteres após encoding.

    Returns: response da requisição feita ao Telegram.
    """
    return _send_content_message('document', bot_token, chat_id, document_url, caption)
