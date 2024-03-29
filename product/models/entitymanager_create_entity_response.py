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
from pydantic import BaseModel
from pydantic import Field
from product.models.entitymanager_attribute_write_errors import EntitymanagerAttributeWriteErrors
from product.models.entitymanager_entity import EntitymanagerEntity
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EntitymanagerCreateEntityResponse(BaseModel):
    """
    EntitymanagerCreateEntityResponse
    """ # noqa: E501
    attribute_write_errors: Optional[EntitymanagerAttributeWriteErrors] = Field(default=None, alias="attributeWriteErrors")
    entity: Optional[EntitymanagerEntity] = None
    __properties: ClassVar[List[str]] = ["attributeWriteErrors", "entity"]

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
        """Create an instance of EntitymanagerCreateEntityResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attribute_write_errors
        if self.attribute_write_errors:
            _dict['attributeWriteErrors'] = self.attribute_write_errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict['entity'] = self.entity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EntitymanagerCreateEntityResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributeWriteErrors": EntitymanagerAttributeWriteErrors.from_dict(obj.get("attributeWriteErrors")) if obj.get("attributeWriteErrors") is not None else None,
            "entity": EntitymanagerEntity.from_dict(obj.get("entity")) if obj.get("entity") is not None else None
        })
        return _obj


