# coding: utf-8

"""
    Product Service

    API for managing products

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from product.models.entitymanager_get_attribute_options_request_option import EntitymanagerGetAttributeOptionsRequestOption
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EntitymanagerGetAttributeOptionsRequest(BaseModel):
    """
    EntitymanagerGetAttributeOptionsRequest
    """ # noqa: E501
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    option_ids: Optional[List[EntitymanagerGetAttributeOptionsRequestOption]] = Field(default=None, alias="optionIds")
    __properties: ClassVar[List[str]] = ["tenantId", "optionIds"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntitymanagerGetAttributeOptionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in option_ids (list)
        _items = []
        if self.option_ids:
            for _item in self.option_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['optionIds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EntitymanagerGetAttributeOptionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "optionIds": [EntitymanagerGetAttributeOptionsRequestOption.from_dict(_item) for _item in obj.get("optionIds")] if obj.get("optionIds") is not None else None
        })
        return _obj


