# product
API for managing products

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-product.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-product.git`)

Then import the package:
```python
import product
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import product
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import product
from product.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product.Configuration(
    host = "https://product.api.gogemini.io"
)



# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductAddMediaGalleryEntryRequest() # ProductAddMediaGalleryEntryRequest | 

    try:
        api_response = api_instance.product_add_media_gallery_entry(body)
        print("The response of ProductApi->product_add_media_gallery_entry:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductApi->product_add_media_gallery_entry: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://product.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProductApi* | [**product_add_media_gallery_entry**](docs/ProductApi.md#product_add_media_gallery_entry) | **POST** /product.Product/AddMediaGalleryEntry | 
*ProductApi* | [**product_bulk_add_assets_entries**](docs/ProductApi.md#product_bulk_add_assets_entries) | **POST** /product.Product/BulkAddAssetsEntries | Assets endpoints
*ProductApi* | [**product_bulk_create_attribute**](docs/ProductApi.md#product_bulk_create_attribute) | **POST** /product.Product/BulkCreateAttribute | 
*ProductApi* | [**product_bulk_delete_products**](docs/ProductApi.md#product_bulk_delete_products) | **POST** /product.Product/BulkDeleteProducts | 
*ProductApi* | [**product_bulk_remove_assets_entries**](docs/ProductApi.md#product_bulk_remove_assets_entries) | **POST** /product.Product/BulkRemoveAssetsEntries | 
*ProductApi* | [**product_bulk_update**](docs/ProductApi.md#product_bulk_update) | **POST** /product.Product/BulkUpdate | 
*ProductApi* | [**product_bulk_update_assets_entries**](docs/ProductApi.md#product_bulk_update_assets_entries) | **POST** /product.Product/BulkUpdateAssetsEntries | 
*ProductApi* | [**product_bulk_update_v2**](docs/ProductApi.md#product_bulk_update_v2) | **POST** /product.Product/BulkUpdateV2 | 
*ProductApi* | [**product_create_attribute_group**](docs/ProductApi.md#product_create_attribute_group) | **POST** /product.Product/CreateAttributeGroup | 
*ProductApi* | [**product_create_attribute_options**](docs/ProductApi.md#product_create_attribute_options) | **POST** /product.Product/CreateAttributeOptions | 
*ProductApi* | [**product_create_entity**](docs/ProductApi.md#product_create_entity) | **POST** /product.Product/CreateEntity | 
*ProductApi* | [**product_create_options_list**](docs/ProductApi.md#product_create_options_list) | **POST** /product.Product/CreateOptionsList | 
*ProductApi* | [**product_create_product**](docs/ProductApi.md#product_create_product) | **POST** /product.Product/CreateProduct | 
*ProductApi* | [**product_create_product_v2**](docs/ProductApi.md#product_create_product_v2) | **POST** /product.Product/CreateProductV2 | 
*ProductApi* | [**product_delete**](docs/ProductApi.md#product_delete) | **POST** /product.Product/Delete | 
*ProductApi* | [**product_delete_attribute**](docs/ProductApi.md#product_delete_attribute) | **POST** /product.Product/DeleteAttribute | 
*ProductApi* | [**product_delete_product**](docs/ProductApi.md#product_delete_product) | **POST** /product.Product/DeleteProduct | 
*ProductApi* | [**product_get_attribute_group**](docs/ProductApi.md#product_get_attribute_group) | **POST** /product.Product/GetAttributeGroup | 
*ProductApi* | [**product_get_attribute_option**](docs/ProductApi.md#product_get_attribute_option) | **POST** /product.Product/GetAttributeOption | 
*ProductApi* | [**product_get_attribute_options**](docs/ProductApi.md#product_get_attribute_options) | **POST** /product.Product/GetAttributeOptions | 
*ProductApi* | [**product_get_entity**](docs/ProductApi.md#product_get_entity) | **POST** /product.Product/GetEntity | 
*ProductApi* | [**product_get_options_list**](docs/ProductApi.md#product_get_options_list) | **POST** /product.Product/GetOptionsList | 
*ProductApi* | [**product_get_product**](docs/ProductApi.md#product_get_product) | **POST** /product.Product/GetProduct | 
*ProductApi* | [**product_get_product_by_code**](docs/ProductApi.md#product_get_product_by_code) | **POST** /product.Product/GetProductByCode | 
*ProductApi* | [**product_get_product_by_url_key**](docs/ProductApi.md#product_get_product_by_url_key) | **POST** /product.Product/GetProductByUrlKey | 
*ProductApi* | [**product_list_attribute_groups**](docs/ProductApi.md#product_list_attribute_groups) | **POST** /product.Product/ListAttributeGroups | Attribute Groups endpoints
*ProductApi* | [**product_list_attribute_options**](docs/ProductApi.md#product_list_attribute_options) | **POST** /product.Product/ListAttributeOptions | 
*ProductApi* | [**product_list_entities**](docs/ProductApi.md#product_list_entities) | **POST** /product.Product/ListEntities | 
*ProductApi* | [**product_list_options_lists**](docs/ProductApi.md#product_list_options_lists) | **POST** /product.Product/ListOptionsLists | 
*ProductApi* | [**product_list_products**](docs/ProductApi.md#product_list_products) | **POST** /product.Product/ListProducts | 
*ProductApi* | [**product_list_products_by_ids**](docs/ProductApi.md#product_list_products_by_ids) | **POST** /product.Product/ListProductsByIds | 
*ProductApi* | [**product_list_products_by_sku**](docs/ProductApi.md#product_list_products_by_sku) | **POST** /product.Product/ListProductsBySku | 
*ProductApi* | [**product_list_variants_by_sku**](docs/ProductApi.md#product_list_variants_by_sku) | **POST** /product.Product/ListVariantsBySku | 
*ProductApi* | [**product_remove_media_gallery_entry**](docs/ProductApi.md#product_remove_media_gallery_entry) | **POST** /product.Product/RemoveMediaGalleryEntry | 
*ProductApi* | [**product_update_attribute**](docs/ProductApi.md#product_update_attribute) | **POST** /product.Product/UpdateAttribute | 
*ProductApi* | [**product_update_attribute_group**](docs/ProductApi.md#product_update_attribute_group) | **POST** /product.Product/UpdateAttributeGroup | 
*ProductApi* | [**product_update_attribute_options**](docs/ProductApi.md#product_update_attribute_options) | **POST** /product.Product/UpdateAttributeOptions | rpc GetAttributeOptionByCode (product.entitymanager.GetAttributeOptionByCodeRequest) returns (product.entitymanager.GetAttributeOptionByCodeResponse) {}
*ProductApi* | [**product_update_media_gallery_entry**](docs/ProductApi.md#product_update_media_gallery_entry) | **POST** /product.Product/UpdateMediaGalleryEntry | 
*ProductApi* | [**product_update_options_list**](docs/ProductApi.md#product_update_options_list) | **POST** /product.Product/UpdateOptionsList | 
*ProductApi* | [**product_update_product**](docs/ProductApi.md#product_update_product) | **POST** /product.Product/UpdateProduct | 
*ProductApi* | [**product_update_product_v2**](docs/ProductApi.md#product_update_product_v2) | **POST** /product.Product/UpdateProductV2 | 


## Documentation For Models

 - [BulkUpdateAssetsEntriesRequestUpdateEntity](docs/BulkUpdateAssetsEntriesRequestUpdateEntity.md)
 - [EntitymanagerAttribute](docs/EntitymanagerAttribute.md)
 - [EntitymanagerAttributeGroup](docs/EntitymanagerAttributeGroup.md)
 - [EntitymanagerAttributeOption](docs/EntitymanagerAttributeOption.md)
 - [EntitymanagerAttributeOptionErrors](docs/EntitymanagerAttributeOptionErrors.md)
 - [EntitymanagerAttributeOptionSwatch](docs/EntitymanagerAttributeOptionSwatch.md)
 - [EntitymanagerAttributeWriteError](docs/EntitymanagerAttributeWriteError.md)
 - [EntitymanagerAttributeWriteErrors](docs/EntitymanagerAttributeWriteErrors.md)
 - [EntitymanagerBulkCreateAttributeRequest](docs/EntitymanagerBulkCreateAttributeRequest.md)
 - [EntitymanagerBulkCreateAttributeResponse](docs/EntitymanagerBulkCreateAttributeResponse.md)
 - [EntitymanagerCreateAttributeGroupRequest](docs/EntitymanagerCreateAttributeGroupRequest.md)
 - [EntitymanagerCreateAttributeOptionsRequest](docs/EntitymanagerCreateAttributeOptionsRequest.md)
 - [EntitymanagerCreateAttributeOptionsResponse](docs/EntitymanagerCreateAttributeOptionsResponse.md)
 - [EntitymanagerCreateEntityResponse](docs/EntitymanagerCreateEntityResponse.md)
 - [EntitymanagerCreateOptionsListRequest](docs/EntitymanagerCreateOptionsListRequest.md)
 - [EntitymanagerCreateOptionsListResponse](docs/EntitymanagerCreateOptionsListResponse.md)
 - [EntitymanagerDeleteAttributeRequest](docs/EntitymanagerDeleteAttributeRequest.md)
 - [EntitymanagerEntity](docs/EntitymanagerEntity.md)
 - [EntitymanagerEntityIdentifier](docs/EntitymanagerEntityIdentifier.md)
 - [EntitymanagerEntityRequest](docs/EntitymanagerEntityRequest.md)
 - [EntitymanagerGetAttributeGroupRequest](docs/EntitymanagerGetAttributeGroupRequest.md)
 - [EntitymanagerGetAttributeOptionRequest](docs/EntitymanagerGetAttributeOptionRequest.md)
 - [EntitymanagerGetAttributeOptionResponse](docs/EntitymanagerGetAttributeOptionResponse.md)
 - [EntitymanagerGetAttributeOptionsRequest](docs/EntitymanagerGetAttributeOptionsRequest.md)
 - [EntitymanagerGetAttributeOptionsRequestOption](docs/EntitymanagerGetAttributeOptionsRequestOption.md)
 - [EntitymanagerGetAttributeOptionsResponse](docs/EntitymanagerGetAttributeOptionsResponse.md)
 - [EntitymanagerGetAttributeOptionsResponseOption](docs/EntitymanagerGetAttributeOptionsResponseOption.md)
 - [EntitymanagerGetOptionsListRequest](docs/EntitymanagerGetOptionsListRequest.md)
 - [EntitymanagerGetOptionsListResponse](docs/EntitymanagerGetOptionsListResponse.md)
 - [EntitymanagerListAttributeGroupsRequest](docs/EntitymanagerListAttributeGroupsRequest.md)
 - [EntitymanagerListAttributeGroupsResponse](docs/EntitymanagerListAttributeGroupsResponse.md)
 - [EntitymanagerListAttributeOptionsRequest](docs/EntitymanagerListAttributeOptionsRequest.md)
 - [EntitymanagerListAttributeOptionsResponse](docs/EntitymanagerListAttributeOptionsResponse.md)
 - [EntitymanagerListEntitiesRequest](docs/EntitymanagerListEntitiesRequest.md)
 - [EntitymanagerListEntitiesResponse](docs/EntitymanagerListEntitiesResponse.md)
 - [EntitymanagerListOptionsListsRequest](docs/EntitymanagerListOptionsListsRequest.md)
 - [EntitymanagerListOptionsListsResponse](docs/EntitymanagerListOptionsListsResponse.md)
 - [EntitymanagerOptionsList](docs/EntitymanagerOptionsList.md)
 - [EntitymanagerRenderAs](docs/EntitymanagerRenderAs.md)
 - [EntitymanagerTypes](docs/EntitymanagerTypes.md)
 - [EntitymanagerUpdateAttributeGroupRequest](docs/EntitymanagerUpdateAttributeGroupRequest.md)
 - [EntitymanagerUpdateAttributeGroupRequestPayload](docs/EntitymanagerUpdateAttributeGroupRequestPayload.md)
 - [EntitymanagerUpdateAttributeOptionsRequest](docs/EntitymanagerUpdateAttributeOptionsRequest.md)
 - [EntitymanagerUpdateAttributeOptionsResponse](docs/EntitymanagerUpdateAttributeOptionsResponse.md)
 - [EntitymanagerUpdateAttributeRequest](docs/EntitymanagerUpdateAttributeRequest.md)
 - [EntitymanagerUpdateAttributeRequestPayload](docs/EntitymanagerUpdateAttributeRequestPayload.md)
 - [EntitymanagerUpdateOptionsListRequest](docs/EntitymanagerUpdateOptionsListRequest.md)
 - [EntitymanagerUpdateOptionsListResponse](docs/EntitymanagerUpdateOptionsListResponse.md)
 - [ListProductsRequestFilter](docs/ListProductsRequestFilter.md)
 - [ProductAddMediaGalleryEntryRequest](docs/ProductAddMediaGalleryEntryRequest.md)
 - [ProductAddMediaGalleryEntryResponse](docs/ProductAddMediaGalleryEntryResponse.md)
 - [ProductAssetData](docs/ProductAssetData.md)
 - [ProductAssets](docs/ProductAssets.md)
 - [ProductAssetsEntry](docs/ProductAssetsEntry.md)
 - [ProductAssetsEntryMetadata](docs/ProductAssetsEntryMetadata.md)
 - [ProductAttributeResponseError](docs/ProductAttributeResponseError.md)
 - [ProductBulkAddAssetsEntriesRequest](docs/ProductBulkAddAssetsEntriesRequest.md)
 - [ProductBulkAddAssetsEntriesResponse](docs/ProductBulkAddAssetsEntriesResponse.md)
 - [ProductBulkDeleteProductsRequest](docs/ProductBulkDeleteProductsRequest.md)
 - [ProductBulkRemoveAssetsEntriesRequest](docs/ProductBulkRemoveAssetsEntriesRequest.md)
 - [ProductBulkUpdateAssetsEntriesRequest](docs/ProductBulkUpdateAssetsEntriesRequest.md)
 - [ProductBulkUpdateAssetsEntriesResponse](docs/ProductBulkUpdateAssetsEntriesResponse.md)
 - [ProductBulkUpdateRequest](docs/ProductBulkUpdateRequest.md)
 - [ProductBulkUpdateRequestPayload](docs/ProductBulkUpdateRequestPayload.md)
 - [ProductBulkUpdateRequestV2](docs/ProductBulkUpdateRequestV2.md)
 - [ProductBulkUpdateRequestV2Payload](docs/ProductBulkUpdateRequestV2Payload.md)
 - [ProductBulkUpdateResponse](docs/ProductBulkUpdateResponse.md)
 - [ProductBulkUpdateResponseResponse](docs/ProductBulkUpdateResponseResponse.md)
 - [ProductBulkUpdateResponseV2](docs/ProductBulkUpdateResponseV2.md)
 - [ProductBulkUpdateResponseV2Response](docs/ProductBulkUpdateResponseV2Response.md)
 - [ProductCreateProductRequest](docs/ProductCreateProductRequest.md)
 - [ProductCreateProductRequestV2](docs/ProductCreateProductRequestV2.md)
 - [ProductCreateProductResponse](docs/ProductCreateProductResponse.md)
 - [ProductCreateProductResponseV2](docs/ProductCreateProductResponseV2.md)
 - [ProductDeleteProductRequest](docs/ProductDeleteProductRequest.md)
 - [ProductDeleteRequest](docs/ProductDeleteRequest.md)
 - [ProductDeleteResponse](docs/ProductDeleteResponse.md)
 - [ProductFieldMask](docs/ProductFieldMask.md)
 - [ProductGetProductByCodeRequest](docs/ProductGetProductByCodeRequest.md)
 - [ProductGetProductByCodeResponse](docs/ProductGetProductByCodeResponse.md)
 - [ProductGetProductByUrlKeyRequest](docs/ProductGetProductByUrlKeyRequest.md)
 - [ProductGetProductByUrlKeyResponse](docs/ProductGetProductByUrlKeyResponse.md)
 - [ProductGetProductRequest](docs/ProductGetProductRequest.md)
 - [ProductGetProductResponse](docs/ProductGetProductResponse.md)
 - [ProductListProductsByIdsRequest](docs/ProductListProductsByIdsRequest.md)
 - [ProductListProductsByIdsResponse](docs/ProductListProductsByIdsResponse.md)
 - [ProductListProductsBySkuRequest](docs/ProductListProductsBySkuRequest.md)
 - [ProductListProductsBySkuResponse](docs/ProductListProductsBySkuResponse.md)
 - [ProductListProductsRequest](docs/ProductListProductsRequest.md)
 - [ProductListProductsResponse](docs/ProductListProductsResponse.md)
 - [ProductListVariantsBySkuRequest](docs/ProductListVariantsBySkuRequest.md)
 - [ProductListVariantsBySkuResponse](docs/ProductListVariantsBySkuResponse.md)
 - [ProductLocalizedAsset](docs/ProductLocalizedAsset.md)
 - [ProductLocalizedText](docs/ProductLocalizedText.md)
 - [ProductMediaGallery](docs/ProductMediaGallery.md)
 - [ProductMediaGalleryEntry](docs/ProductMediaGalleryEntry.md)
 - [ProductMediaGalleryEntryMetadata](docs/ProductMediaGalleryEntryMetadata.md)
 - [ProductProductEntity](docs/ProductProductEntity.md)
 - [ProductProductResponseError](docs/ProductProductResponseError.md)
 - [ProductProductVariant](docs/ProductProductVariant.md)
 - [ProductRemoveMediaGalleryEntryRequest](docs/ProductRemoveMediaGalleryEntryRequest.md)
 - [ProductUpdateAssetEntryPayload](docs/ProductUpdateAssetEntryPayload.md)
 - [ProductUpdateMediaGalleryEntryRequest](docs/ProductUpdateMediaGalleryEntryRequest.md)
 - [ProductUpdateProductRequest](docs/ProductUpdateProductRequest.md)
 - [ProductUpdateProductRequestV2](docs/ProductUpdateProductRequestV2.md)
 - [ProductUpdateProductResponse](docs/ProductUpdateProductResponse.md)
 - [ProductentitymanagerLocalizedText](docs/ProductentitymanagerLocalizedText.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


