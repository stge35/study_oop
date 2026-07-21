import copy
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

    def update_member(self, member: Member) -> None:

        # 1. 파일에서 현재 영구 저장되어 있는 전체 회원 목록([{}, {}, ...])을 읽어 온다.
        all_members: list[dict]= self._read_data()

        # 2. 파일 목록에서 수정 대상 회원의 위치(인덱스)와 기존 딕셔너리를 찾습니다.
        target_index: int = -1
        existing_member_dict: Optional[dict] = None

        for index, m_dict in enumerate(all_members):
            if m_dict.get('member_id') == member.member_id:
                target_index = index
                existing_member_dict = m_dict
                break

        # 3. 수정할 회원이 파일 내에 없으면 예외를 던져 작업을 중단한다.
        if target_index == -1 or existing_member_dict is None:
            raise ValueError(f"저장소 에러: ID {member.member_id}번 회원이 존재하지 않습니다.")

        # 4. [안전장치] 전달 받은 member 객체의 데이터 중 None 아닌(실제 수정된) 값만
        #    기존 파일 데이터 (existing_member_dict)에 부분 업데이트(patch) 합니다.
        update_member_dict = copy.deepcopy(existing_member_dict)

        # member 객체에서 None이 아닌 필드만 골라내어 딕셔너리를 갱신
        for key, value in member.__dict__.items():
            if value is not None:
                update_member_dict[key] = value

        # 5. 기존 리스트의 해당 위치에 안전하게 가공된 딕셔너리를 교체
        all_members[target_index] = update_member_dict

        self._save_data(all_members)
        print(f"업데이트 성공 {member.member_id}")

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
                address = data['address'],
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
                    address = data['address'],
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
                    address = data['address'],
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


