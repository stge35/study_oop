from app.domain.member.dto.request.create_member_dto import CreateMemberDto


class CreateAdminDto(CreateMemberDto):

    name = "최명진 법무사 사무소"
    personal_number = "286-30-00784"
    phone_number = "031-903-7360"

    def __init__(self, password: str, member_id : int):
        super().__init__(
            name = CreateAdminDto.name,
            password = self.password,
            personal_number = CreateAdminDto.personal_number,
            phone_number = CreateAdminDto.phone_number,
            member_id = self.member_id
        )


    pass
