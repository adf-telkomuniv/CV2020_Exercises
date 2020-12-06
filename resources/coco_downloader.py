import requests

def download_coco():
    URL  = "https://docs.google.com/uc?export=download"
    id   = "19MkP4HWQHUIrAI8mMMGkF8AYBp67VVK4"
    dest = "coco_captioning.zip"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, dest)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, dest):
    CHUNK_SIZE = 32768

    with open(dest, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
