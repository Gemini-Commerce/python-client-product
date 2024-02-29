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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from product.models.product_assets_entry_metadata import ProductAssetsEntryMetadata
from product.models.product_localized_asset import ProductLocalizedAsset
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProductAssetsEntry(BaseModel):
    """
    ProductAssetsEntry
    """ # noqa: E501
    id: Optional[StrictStr] = None
    asset_grn: Optional[StrictStr] = Field(default=None, alias="assetGrn")
    localized_asset_grn: Optional[ProductLocalizedAsset] = Field(default=None, alias="localizedAssetGrn")
    locales: Optional[List[StrictStr]] = None
    position: Optional[StrictInt] = None
    metadata: Optional[List[ProductAssetsEntryMetadata]] = None
    __properties: ClassVar[List[str]] = ["id", "assetGrn", "localizedAssetGrn", "locales", "position", "metadata"]

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
        """Create an instance of ProductAssetsEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of localized_asset_grn
        if self.localized_asset_grn:
            _dict['localizedAssetGrn'] = self.localized_asset_grn.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductAssetsEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "assetGrn": obj.get("assetGrn"),
            "localizedAssetGrn": ProductLocalizedAsset.from_dict(obj.get("localizedAssetGrn")) if obj.get("localizedAssetGrn") is not None else None,
            "locales": obj.get("locales"),
            "position": obj.get("position"),
            "metadata": [ProductAssetsEntryMetadata.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None
        })
        return _obj


