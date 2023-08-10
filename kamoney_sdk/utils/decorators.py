def Private(func):
    def wrapper(*args, **kwargs):
        # Checando se a secret key foi fornecida para assinar as requisições
        if isinstance(args[0].keys['public_key'], str) == False or isinstance(args[0].keys['private_key'], str):
            raise Exception("Instantiate the sdk with your public and private key to call a private method")
        return func(*args, **kwargs)
    
    return wrapper