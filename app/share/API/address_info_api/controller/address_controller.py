from app.share.API.address_info_api.dto.request.address_request_dto import RequestAddressDto
from app.share.API.address_info_api.dto.response.address_response_dto import AddressResponseDto
from app.share.API.address_info_api.service.address_service import AddressService
from app.share.validation.business_exception import BusinessException


class AddressController:
    def __init__(self, service = AddressService):
        self.service = service

    def search_address(self, keyword: str) -> list[AddressResponseDto]:

        try:
            request_dto = RequestAddressDto(keyword)

            addresses = self.service.search_address_from_api(request_dto)

            return [AddressResponseDto.from_entity(addr) for addr in addresses]

        except BusinessException as e:
            raise
