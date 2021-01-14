from Parcial3_Client.services.services import generate_request, response_2_dict, generate_post, generate_put, \
    generate_delete
from constants import APP_NAME


def get_all_mensajes(token):
    # Llamo a la API.
    url = APP_NAME+"/server/mensajes"
    params = {}
    response = generate_request(url, token=token, params=params)
    if response:
        return response_2_dict(response)


def get_mensaje(id, token):
    url = APP_NAME+"/server/mensajes/" + id + "/"
    params = {}
    response = generate_request(url, token=token, params=params)
    if response:
        return response_2_dict(response)


def get_mensaje_filtered(token, params):
    url = APP_NAME+"/server/mensajes/"
    response = generate_request(url, token=token, params=params)
    if response:
        return response_2_dict(response)


def create_mensaje(mensaje, token):
    url = APP_NAME+"/server/mensajes/"
    response = generate_post(url, mensaje, token=token)
    return response

def update_mensaje(id, mensaje, token):
    url = APP_NAME+"/server/mensajes/" + id + "/"
    response = generate_put(url, mensaje, token=token)
    return response

def delete_mensaje(id, token):
    url = APP_NAME+"/server/mensajes/" + id + "/"
    response = generate_delete(url, token=token)
    return response


