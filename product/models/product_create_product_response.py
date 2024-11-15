# coding: utf-8

"""
    Product Service

    Introducing our revolutionary Product Management Service! Designed to streamline your product inventory and elevate customer experiences, our cutting-edge protobuf service is a game-changer in the world of efficient product management.  With our service, you can effortlessly create new products, allowing you to quickly bring your ideas to life and expand your catalog. Retrieve product information in a snap, providing accurate and personalized details to your customers based on their specific needs and preferences.  Stay ahead of the competition by easily updating product information, ensuring your catalog is always up-to-date and optimized. Seamlessly remove products from your inventory when needed, maintaining a clean and relevant product selection.  Enhance the visual appeal of your products with our advanced media gallery functionalities. Effortlessly add and update captivating images and videos to showcase your products in the best possible light, engaging your customers and driving conversions.  Personalization is key in today's market, and our service enables you to offer unique options to your customers. Easily create and manage lists of customizable options for your products, providing flexibility and tailoring to individual preferences.  Attributes play a vital role in defining products, and our service empowers you to effectively manage them. From bulk attribute creation to listing and retrieving attribute options, our service ensures your product information is rich and comprehensive.  Our service extends its capabilities to entity management, allowing you to effortlessly handle different entities and create customized options lists associated with them. This provides further flexibility and customization options for your product offerings.  When it comes to bulk updates, our service has you covered. Effortlessly update multiple products simultaneously, saving you time and streamlining your operations.  Finding specific products and variants is a breeze with our service. Quickly locate products based on their unique stock keeping unit (SKU) values, ensuring efficient inventory management and smooth order fulfillment.  Experience a new level of efficiency and productivity with our Product Management Service. Unlock the full potential of streamlined product management and empower your business to thrive in today's competitive market. Try our service today and elevate your product management to new heights!

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from product.models.product_attribute_response_error import ProductAttributeResponseError
from product.models.product_product_response_error import ProductProductResponseError
from typing import Optional, Set
from typing_extensions import Self

class ProductCreateProductResponse(BaseModel):
    """
    The CreateProductResponse message is used to provide a response after creating a product within the system. It includes fields that indicate the success of the product creation and any errors encountered during the process.
    """ # noqa: E501
    success: Optional[StrictBool] = Field(default=None, description="Indicates whether the product creation was successful or not.")
    id: Optional[StrictStr] = Field(default=None, description="Represents the ID of the created product.")
    product_errors: Optional[List[ProductProductResponseError]] = Field(default=None, description="Contains a list of ProductResponseError messages, indicating any errors related to the product creation.", alias="productErrors")
    attribute_errors: Optional[List[ProductAttributeResponseError]] = Field(default=None, description="Contains a list of AttributeResponseError messages, indicating any errors related to the attributes of the product.", alias="attributeErrors")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "id", "productErrors", "attributeErrors"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProductCreateProductResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in product_errors (list)
        _items = []
        if self.product_errors:
            for _item_product_errors in self.product_errors:
                if _item_product_errors:
                    _items.append(_item_product_errors.to_dict())
            _dict['productErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_errors (list)
        _items = []
        if self.attribute_errors:
            for _item_attribute_errors in self.attribute_errors:
                if _item_attribute_errors:
                    _items.append(_item_attribute_errors.to_dict())
            _dict['attributeErrors'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductCreateProductResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "success": obj.get("success"),
            "id": obj.get("id"),
            "productErrors": [ProductProductResponseError.from_dict(_item) for _item in obj["productErrors"]] if obj.get("productErrors") is not None else None,
            "attributeErrors": [ProductAttributeResponseError.from_dict(_item) for _item in obj["attributeErrors"]] if obj.get("attributeErrors") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


