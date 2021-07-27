from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import base64


def gen_keypair():
    # 生成密钥对
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )
    public_key = private_key.public_key()

    # 序列化
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),  # 无密码
        # encryption_algorithm=serialization.BestAvailableEncryption(b'password'),  # 添加密码
    )
    public_pem = public_key.public_bytes(
        encodingserialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    # 写入文件
    with open('private.pem', 'wb') as f:
        f.write(private_pem)
    with open('public.pem', 'wb') as f:
        f.write(public_pem)


def load_pem_file(file, is_private: bool):
    with open(file, 'rb') as f:
        if is_private:
            private_key = serialization.load_pem_private_key(
                data=f.read(),
                password=None,
                backend=default_backend(),
            )
            return private_key
        else:
            public_key = serialization.load_pem_public_key(
                data=f.read(), backend=default_backend()
            )
            return public_key


def rsa_sign(message: bytes, private_key, is_base64: bool) -> bytes:
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    signature = (
        base64.b64encode(signature) if is_base64 else signature
    )  # 转base64的字节串bytes(传输, 展示, 存储)
    return signature


def rsa_verify(signature: bytes, message: bytes, public_key, is_base64: bool) -> bool:
    signature = base64.b64decode(signature) if is_base64 else signature
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        return True
    except Exception as e:
        print(e)
        return False


def getsrc(msgid: str, sysid: str, timestamp: str, body: str):
    src = (
        "gbp-msg-id:"
        + msgid
        + "\r\n"
        + "gbp-sys-id:"
        + sysid
        + "\r\n"
        + "gbp-timestamp:"
        + timestamp
        + "\r\n"
        + body
    )
    return src


if __name__ == "__main__":
    msg = getsrc("11111", "000000S001", "2021-07-22+18:00:00", "abc123").encode()

    signature = rsa_sign(msg, load_pem_file("private.pem", True), True)
    print(type(signature), signature)

    print(rsa_verify(signature, msg, load_pem_file("public.pem", False), True))
