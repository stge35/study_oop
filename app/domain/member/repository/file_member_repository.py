import json
import os.path
from typing import List
from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.entity.member import Member

from app.domain.member.repository.member_interface import MemberInterface

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

    def _save_data(self, data: List[dict]):

        with open(self.file_path, "w", encoding = "utf-8") as f :
            return json.dump(data, f, ensure_ascii=False, indent=4)

    def _read_data(self) -> List[dict]:

        with open(self.file_path, "r", encoding = "utf-8") as f:
            return json.load(f)


