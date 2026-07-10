import base64
import keyring
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class DataEncryptor:


    _SERVICE_NAME = "MyLawFirmApp"
    _KEY_NAME = "SecretKey"

    @classmethod
    def _get_secret_key(cls) -> bytes:

        saved_key = keyring.get_password(cls._SERVICE_NAME, cls._KEY_NAME)

        if not saved_key:
            raise ValueError(
                "보안 에러: 최초 1회 인증 키 등록이 필요합니다.")

        key_bytes = saved_key.encode('utf-8')
        if len(key_bytes) != 32:
            raise ValueError(
                f"등록된 키가 32 바이트가 아닙니다. {len(key_bytes)}"
            )
        return key_bytes

    @classmethod
    def encrypt(cls, plain_text: str) -> str:
        if not plain_text:
            return ""

        secret_key = cls._get_secret_key()

        cipher = AES.new(secret_key, AES.MODE_CBC)

        raw_data = plain_text.encode('utf-8')
        padded_data = pad(raw_data, AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_data)

        combined_bytes = cipher.iv + encrypted_bytes
        return base64.b64encode(combined_bytes).decode('utf-8')

    @classmethod
    def decrypt(cls, encrypted_text: str) -> str:
        if not encrypted_text:
            return ""

        try:
            secret_key = cls._get_secret_key()
            combined_bytes = base64.b64decode(encrypted_text.encode('utf-8'))

            iv = combined_bytes[:16]
            encrypted_bytes = combined_bytes[16:]

            cipher = AES.new(secret_key, AES.MODE_CBC, iv)
            decrypted_padded = cipher.decrypt(encrypted_bytes)

            return unpad(decrypted_padded, AES.block_size).decode('utf-8')

        except Exception as e:
            raise ValueError(f"복호화 실패 (암호화 키가 유실되었거나 데이터가 오염됨 : {str(e)}")