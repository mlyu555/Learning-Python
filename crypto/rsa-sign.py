from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import base64


def getsrc(msgid: str, sysid: str, timestamp: str, body: str):
    src = 'gbp-msg-id:' + msgid + '\r\n' + 'gbp-sys-id:' + sysid + '\r\n' + 'gbp-timestamp:' + timestamp + '\r\n' + body
    return src

def rsasign(message: bytes, private_key):
    with open(private_key, 'rb') as f:
        privkey = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
    signature = privkey.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    signature = base64.b64encode(signature).decode()
    return signature

def rsaverify(signature: str, message: bytes, public_key: str):
    with open(public_key, 'rb') as f:
        pubkey = serialization.load_pem_public_key(f.read(), backend=default_backend())
    try:
        pubkey.verify(
            base64.b64decode(signature),
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print('success')
    except Exception as e:
        print(f'failed: {type(e)}')



if __name__ == "__main__":
    msg = getsrc('11111', '000000S001', '2021-07-22+18:00:00', 'abc123').encode()
    print(msg)

    signature = rsasign(msg, 'private.pem')
    print(type(signature), signature)

    rsaverify(signature, msg, 'public.pem')
