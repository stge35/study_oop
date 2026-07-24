import requests

from app.share.API.address_info_api.dto.request.address_request_dto import RequestAddressDto
from app.share.API.address_info_api.entity.address import Address
from app.share.validation.business_exception import BusinessException
from app.share.validation.error_code import ErrorCode


class AddressService:
    ADDRESS_INFO_CONFIRM_KEY = ""
    API_URL = "https://business.juso.go.kr/addrlink/addrLinkApi.do"

    def search_address_from_api(self, dto: RequestAddressDto) -> list[Address]:


        params = {
            "confmKey": self.ADDRESS_INFO_CONFIRM_KEY,
            "currentPage": "1",
            "countPerPage": "10",
            "keyword": dto.keyword,
            "resultType": "json"
        }
        try:
            response = requests.get(self.API_URL, params = params, timeout = 5)
            response.raise_for_status()
            data = response.json()

            results = data.get("results", {})
            common = results.get("common", {})

            error_code = ErrorCode.ADDRESS_ERROR
            error_msg = ErrorCode.ADDRESS_ERROR

            if error_code != "0":
                raise BusinessException(f"주소 API 오류{error_code}: {error_msg}")

            juso_list = results.get("juso", [])
            addresses = []

            for item in juso_list:
                address = Address(
                    zip_code = item.get("zipNo", ""),
                    road_address = item.get("roadAddr", ""),
                    detail_address = "",
                    building_name = item.get("bdNm", "")
                )
                addresses.append(address)

            return addresses
        except requests.RequestException:
            raise BusinessException(ErrorCode.INVALID_INPUT_VALUE, "주소 검색 서비스 연계 오류")

    def save_selected_address(self, address: Address) -> "Address":
        return self.repository.save(address)