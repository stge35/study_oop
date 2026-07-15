import json
import os.path
from typing import List, Optional
from app.domain.member.entity.member import Member
from app.domain.member.repository.member_interface import MemberInterface
from app.share.utils.data_encryptor import DataEncryptor


# BASE_SAVE_DIR = os.path.

class FileMemberRepository(MemberInterface):

    # 초기화

    def __init__(self, file_path : str = "members.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            self._save_data([])

    def save_member(self, member: Member) -> Member:

        all_member = self._read_data()

        if member.member_id is None:
            member.member_id = len(all_member) + 1

        member_dict = member.__dict__

        all_member.append(member_dict)

        self._save_data(all_member)

        print("저장 성공")

        return member

    def find_all_member(self) -> list[Member]:

        raw_data_list = self._read_data()
        members = []

        for data in raw_data_list:
            decrypted_p_num = DataEncryptor.decrypt(data['personal_number'])

            member = Member(
                member_id = data['member_id'],
                name = data['name'],
                password = data['password'],  # 비밀번호는 단방향이라 복호화 불가 (그대로 둠)
                personal_number = decrypted_p_num,  # ⭕ 복원된 평문 주입
                phone_number = data['phone_number']
            )
            members.append(member)

        return members

    def find_by_name(self, name: str) -> list[Member]:
        """[1단계] 사용자가 화면에서 이름으로 검색할 때 쓰는 함수"""
        all_members = self._read_data()
        results = []

        for data in all_members:
            if data['name'] == name:
                decrypted_p_num = DataEncryptor.decrypt(data['personal_number'])

                member_entity = Member.to_member(
                    member_id = data['member_id'],
                    name = data['name'],
                    password = data['password'],
                    personal_number = decrypted_p_num,
                    phone_number = data['phone_number']
                )
                results.append(member_entity)

        return results

    def find_by_id(self, member_id: int) -> Member | None:

        all_members = self._read_data()
        for data in all_members:
            if data['member_id'] == member_id:

                decrypted_p_num = DataEncryptor.decrypt(data['personal_number'])

                return Member.to_member(
                    member_id = data['member_id'],
                    name = data['name'],
                    password = data['password'],
                    personal_number = decrypted_p_num,
                    phone_number = data['phone_number']
                )
        return None

    def exists_by_name(self, name: str) -> bool:
        all_members = self._read_data()

        for data in all_members:
            if data.get("name") == name:
                return True

        return False


    def _save_data(self, data: List[dict]):

        with open(self.file_path, "w", encoding = "utf-8") as f :
            return json.dump(data, f, ensure_ascii = False, indent = 4)

    def _read_data(self) -> List[dict]:

        with open(self.file_path, "r", encoding = "utf-8") as f:
            return json.load(f)


