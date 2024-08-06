# # ProductCreateProductRequest
The CreateProductRequest message is used to create a new product within the system. It contains various fields that allow specifying the details and attributes of the product.

## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** | Represents the ID of the tenant associated with the product.  | [optional]
**entity_type**| **str** | Specifies the type of entity for the product.  | [optional]
**entity_code**| **str** | Indicates the code of the entity associated with the product.  | [optional]
**code**| **str** | Represents the unique code or identifier for the product.  | [optional]
**is_configurable**| **bool** | Specifies whether the product has variants or not.  | [optional]
**variant_attributes**| **List[str]** | Contains a list of attributes specific to the product variants.  | [optional]
**is_virtual**| **bool** | Indicates whether the product is virtual or not.  | [optional]
**is_giftcard**| **bool** | Specifies whether the product is a gift card or not.  | [optional]
**has_configurator**| **bool** |   | [optional]
**url_key**| [**ProductLocalizedText**](ProductLocalizedText.md) |   | [optional]
**max_saleable_quantity**| **int** | Specifies the maximum quantity that can be sold for the product in each order.  | [optional]
**media_variant_attributes**| **List[str]** |   | [optional]
**attributes**| [**Dict[str, ProtobufAny]**](ProtobufAny.md) | Contains a map of additional attributes associated with the product, where the key is the attribute name and the value is any type of value.  | [optional]
**variants**| [**Dict[str, ProductProductVariant]**](ProductProductVariant.md) | Represents a map of product variants associated with the product, where the key is the variant ID or code, and the value is a ProductVariant message.  | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

