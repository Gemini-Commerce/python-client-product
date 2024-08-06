# # ProductCreateProductResponse
The CreateProductResponse message is used to provide a response after creating a product within the system. It includes fields that indicate the success of the product creation and any errors encountered during the process.

## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success**| **bool** | Indicates whether the product creation was successful or not.  | [optional]
**id**| **str** | Represents the ID of the created product.  | [optional]
**product_errors**| [**List[ProductProductResponseError]**](ProductProductResponseError.md) | Contains a list of ProductResponseError messages, indicating any errors related to the product creation.  | [optional]
**attribute_errors**| [**List[ProductAttributeResponseError]**](ProductAttributeResponseError.md) | Contains a list of AttributeResponseError messages, indicating any errors related to the attributes of the product.  | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

