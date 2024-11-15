# product_client
Introducing our revolutionary Product Management Service! Designed to streamline your product inventory and elevate customer experiences, our cutting-edge protobuf service is a game-changer in the world of efficient product management.

With our service, you can effortlessly create new products, allowing you to quickly bring your ideas to life and expand your catalog. Retrieve product information in a snap, providing accurate and personalized details to your customers based on their specific needs and preferences.

Stay ahead of the competition by easily updating product information, ensuring your catalog is always up-to-date and optimized. Seamlessly remove products from your inventory when needed, maintaining a clean and relevant product selection.

Enhance the visual appeal of your products with our advanced media gallery functionalities. Effortlessly add and update captivating images and videos to showcase your products in the best possible light, engaging your customers and driving conversions.

Personalization is key in today's market, and our service enables you to offer unique options to your customers. Easily create and manage lists of customizable options for your products, providing flexibility and tailoring to individual preferences.

Attributes play a vital role in defining products, and our service empowers you to effectively manage them. From bulk attribute creation to listing and retrieving attribute options, our service ensures your product information is rich and comprehensive.

Our service extends its capabilities to entity management, allowing you to effortlessly handle different entities and create customized options lists associated with them. This provides further flexibility and customization options for your product offerings.

When it comes to bulk updates, our service has you covered. Effortlessly update multiple products simultaneously, saving you time and streamlining your operations.

Finding specific products and variants is a breeze with our service. Quickly locate products based on their unique stock keeping unit (SKU) values, ensuring efficient inventory management and smooth order fulfillment.

Experience a new level of efficiency and productivity with our Product Management Service. Unlock the full potential of streamlined product management and empower your business to thrive in today's competitive market. Try our service today and elevate your product management to new heights!

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 2.1.0
- Generator version: 7.9.0
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

import product
from product.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product.Configuration(
    host = "https://product.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductAddMediaGalleryEntryRequest() # ProductAddMediaGalleryEntryRequest | 

    try:
        # Add Media Gallery Entry
        api_response = api_instance.add_media_gallery_entry(body)
        print("The response of ProductApi->add_media_gallery_entry:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductApi->add_media_gallery_entry: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://product.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProductApi* | [**add_media_gallery_entry**](docs/ProductApi.md#add_media_gallery_entry) | **POST** /product.Product/AddMediaGalleryEntry | Add Media Gallery Entry
*ProductApi* | [**bulk_add_assets_entries**](docs/ProductApi.md#bulk_add_assets_entries) | **POST** /product.Product/BulkAddAssetsEntries | Bulk Add Assets Entries
*ProductApi* | [**bulk_delete_products**](docs/ProductApi.md#bulk_delete_products) | **POST** /product.Product/BulkDeleteProducts | Bulk Delete Products
*ProductApi* | [**bulk_enhance_product_data_with_ai**](docs/ProductApi.md#bulk_enhance_product_data_with_ai) | **POST** /product.Product/BulkEnhanceProductDataWithAI | Bulk Enhance Product Data With AI
*ProductApi* | [**bulk_remove_assets_entries**](docs/ProductApi.md#bulk_remove_assets_entries) | **POST** /product.Product/BulkRemoveAssetsEntries | Bulk Remove Assets Entries
*ProductApi* | [**bulk_update_assets_entries**](docs/ProductApi.md#bulk_update_assets_entries) | **POST** /product.Product/BulkUpdateAssetsEntries | Bulk Update Assets Entries
*ProductApi* | [**bulk_update_v2**](docs/ProductApi.md#bulk_update_v2) | **POST** /product.Product/BulkUpdateV2 | Bulk Update Products
*ProductApi* | [**create_attribute_options**](docs/ProductApi.md#create_attribute_options) | **POST** /product.Product/CreateAttributeOptions | Create Attribute Options
*ProductApi* | [**create_entity**](docs/ProductApi.md#create_entity) | **POST** /product.Product/CreateEntity | Create Entity
*ProductApi* | [**create_options_list**](docs/ProductApi.md#create_options_list) | **POST** /product.Product/CreateOptionsList | Create Options List
*ProductApi* | [**create_product_with_ai**](docs/ProductApi.md#create_product_with_ai) | **POST** /product.Product/CreateProductWithAI | Create Product With AI
*ProductApi* | [**get_attribute_option**](docs/ProductApi.md#get_attribute_option) | **POST** /product.Product/GetAttributeOption | Get Attribute Option
*ProductApi* | [**get_attribute_options**](docs/ProductApi.md#get_attribute_options) | **POST** /product.Product/GetAttributeOptions | Get Attribute Options
*ProductApi* | [**get_entity**](docs/ProductApi.md#get_entity) | **POST** /product.Product/GetEntity | Get Entity Details
*ProductApi* | [**get_options_list**](docs/ProductApi.md#get_options_list) | **POST** /product.Product/GetOptionsList | Get Options List
*ProductApi* | [**get_product**](docs/ProductApi.md#get_product) | **POST** /product.Product/GetProduct | Get Product
*ProductApi* | [**get_product_by_code**](docs/ProductApi.md#get_product_by_code) | **POST** /product.Product/GetProductByCode | Get Product By Code
*ProductApi* | [**get_product_by_url_key**](docs/ProductApi.md#get_product_by_url_key) | **POST** /product.Product/GetProductByUrlKey | Get Product By Url Key
*ProductApi* | [**get_product_data_in_review**](docs/ProductApi.md#get_product_data_in_review) | **POST** /product.Product/GetProductDataInReview | Get Product Data In Review
*ProductApi* | [**list_attribute_options**](docs/ProductApi.md#list_attribute_options) | **POST** /product.Product/ListAttributeOptions | List Attribute Options
*ProductApi* | [**list_entities**](docs/ProductApi.md#list_entities) | **POST** /product.Product/ListEntities | List Entities
*ProductApi* | [**list_options_lists**](docs/ProductApi.md#list_options_lists) | **POST** /product.Product/ListOptionsLists | List Options Lists
*ProductApi* | [**list_products**](docs/ProductApi.md#list_products) | **POST** /product.Product/ListProducts | List Products
*ProductApi* | [**list_products_by_ids**](docs/ProductApi.md#list_products_by_ids) | **POST** /product.Product/ListProductsByIds | List Products By Ids
*ProductApi* | [**list_products_by_sku**](docs/ProductApi.md#list_products_by_sku) | **POST** /product.Product/ListProductsBySku | List Products By Sku
*ProductApi* | [**list_variants_by_sku**](docs/ProductApi.md#list_variants_by_sku) | **POST** /product.Product/ListVariantsBySku | List Product Variants By Sku
*ProductApi* | [**product_bulk_create_attribute**](docs/ProductApi.md#product_bulk_create_attribute) | **POST** /product.Product/BulkCreateAttribute | 
*ProductApi* | [**product_bulk_update**](docs/ProductApi.md#product_bulk_update) | **POST** /product.Product/BulkUpdate | 
*ProductApi* | [**product_create_attribute_group**](docs/ProductApi.md#product_create_attribute_group) | **POST** /product.Product/CreateAttributeGroup | 
*ProductApi* | [**product_create_product**](docs/ProductApi.md#product_create_product) | **POST** /product.Product/CreateProduct | 
*ProductApi* | [**product_create_product_v2**](docs/ProductApi.md#product_create_product_v2) | **POST** /product.Product/CreateProductV2 | 
*ProductApi* | [**product_delete**](docs/ProductApi.md#product_delete) | **POST** /product.Product/Delete | 
*ProductApi* | [**product_delete_attribute**](docs/ProductApi.md#product_delete_attribute) | **POST** /product.Product/DeleteAttribute | 
*ProductApi* | [**product_delete_product**](docs/ProductApi.md#product_delete_product) | **POST** /product.Product/DeleteProduct | 
*ProductApi* | [**product_get_attribute_group**](docs/ProductApi.md#product_get_attribute_group) | **POST** /product.Product/GetAttributeGroup | 
*ProductApi* | [**product_list_attribute_groups**](docs/ProductApi.md#product_list_attribute_groups) | **POST** /product.Product/ListAttributeGroups | 
*ProductApi* | [**product_update_attribute**](docs/ProductApi.md#product_update_attribute) | **POST** /product.Product/UpdateAttribute | 
*ProductApi* | [**product_update_attribute_group**](docs/ProductApi.md#product_update_attribute_group) | **POST** /product.Product/UpdateAttributeGroup | 
*ProductApi* | [**product_update_product**](docs/ProductApi.md#product_update_product) | **POST** /product.Product/UpdateProduct | 
*ProductApi* | [**product_update_product_v2**](docs/ProductApi.md#product_update_product_v2) | **POST** /product.Product/UpdateProductV2 | 
*ProductApi* | [**remove_media_gallery_entry**](docs/ProductApi.md#remove_media_gallery_entry) | **POST** /product.Product/RemoveMediaGalleryEntry | Remove Media Gallery Entry
*ProductApi* | [**update_attribute_options**](docs/ProductApi.md#update_attribute_options) | **POST** /product.Product/UpdateAttributeOptions | Update Attribute Options
*ProductApi* | [**update_data_to_be_reviewed**](docs/ProductApi.md#update_data_to_be_reviewed) | **POST** /product.Product/GetEnhanceProductDataWithAIStatus | Get Enhance Product Data With AI Status
*ProductApi* | [**update_data_to_be_reviewed_0**](docs/ProductApi.md#update_data_to_be_reviewed_0) | **POST** /product.Product/UpdateDataToBeReviewed | Update Data To Be Reviewed
*ProductApi* | [**update_media_gallery_entry**](docs/ProductApi.md#update_media_gallery_entry) | **POST** /product.Product/UpdateMediaGalleryEntry | Update Media Gallery Entry
*ProductApi* | [**update_options_list**](docs/ProductApi.md#update_options_list) | **POST** /product.Product/UpdateOptionsList | Update Options List
*ProductApi* | [**update_product_with_ai**](docs/ProductApi.md#update_product_with_ai) | **POST** /product.Product/UpdateProductWithAI | Update Product With AI


## Documentation For Models

 - [AttributeInReviewString](docs/AttributeInReviewString.md)
 - [BulkUpdateAssetsEntriesRequestUpdateEntity](docs/BulkUpdateAssetsEntriesRequestUpdateEntity.md)
 - [EntitymanagerAiContext](docs/EntitymanagerAiContext.md)
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
 - [GetEnhanceProductDataWithAIStatusResponseJob](docs/GetEnhanceProductDataWithAIStatusResponseJob.md)
 - [ListProductsRequestFilter](docs/ListProductsRequestFilter.md)
 - [ProductAddMediaGalleryEntryRequest](docs/ProductAddMediaGalleryEntryRequest.md)
 - [ProductAddMediaGalleryEntryResponse](docs/ProductAddMediaGalleryEntryResponse.md)
 - [ProductAssetData](docs/ProductAssetData.md)
 - [ProductAssets](docs/ProductAssets.md)
 - [ProductAssetsEntry](docs/ProductAssetsEntry.md)
 - [ProductAssetsEntryMetadata](docs/ProductAssetsEntryMetadata.md)
 - [ProductAttributeInReview](docs/ProductAttributeInReview.md)
 - [ProductAttributeInReviewError](docs/ProductAttributeInReviewError.md)
 - [ProductAttributeInReviewJobStatus](docs/ProductAttributeInReviewJobStatus.md)
 - [ProductAttributeInReviewJobType](docs/ProductAttributeInReviewJobType.md)
 - [ProductAttributeInReviewSource](docs/ProductAttributeInReviewSource.md)
 - [ProductAttributeResponseError](docs/ProductAttributeResponseError.md)
 - [ProductAttributeToEnrich](docs/ProductAttributeToEnrich.md)
 - [ProductAttributeToEnrichType](docs/ProductAttributeToEnrichType.md)
 - [ProductBulkAddAssetsEntriesRequest](docs/ProductBulkAddAssetsEntriesRequest.md)
 - [ProductBulkAddAssetsEntriesResponse](docs/ProductBulkAddAssetsEntriesResponse.md)
 - [ProductBulkDeleteProductsRequest](docs/ProductBulkDeleteProductsRequest.md)
 - [ProductBulkEnhanceProductDataWithAIRequest](docs/ProductBulkEnhanceProductDataWithAIRequest.md)
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
 - [ProductCreateProductWithAIRequest](docs/ProductCreateProductWithAIRequest.md)
 - [ProductCreateProductWithAIResponse](docs/ProductCreateProductWithAIResponse.md)
 - [ProductDataInReview](docs/ProductDataInReview.md)
 - [ProductDeleteProductRequest](docs/ProductDeleteProductRequest.md)
 - [ProductDeleteRequest](docs/ProductDeleteRequest.md)
 - [ProductDeleteResponse](docs/ProductDeleteResponse.md)
 - [ProductEnrichAction](docs/ProductEnrichAction.md)
 - [ProductFieldMask](docs/ProductFieldMask.md)
 - [ProductGetEnhanceProductDataWithAIStatusRequest](docs/ProductGetEnhanceProductDataWithAIStatusRequest.md)
 - [ProductGetEnhanceProductDataWithAIStatusResponse](docs/ProductGetEnhanceProductDataWithAIStatusResponse.md)
 - [ProductGetProductByCodeRequest](docs/ProductGetProductByCodeRequest.md)
 - [ProductGetProductByCodeResponse](docs/ProductGetProductByCodeResponse.md)
 - [ProductGetProductByUrlKeyRequest](docs/ProductGetProductByUrlKeyRequest.md)
 - [ProductGetProductByUrlKeyResponse](docs/ProductGetProductByUrlKeyResponse.md)
 - [ProductGetProductDataInReviewRequest](docs/ProductGetProductDataInReviewRequest.md)
 - [ProductGetProductDataInReviewResponse](docs/ProductGetProductDataInReviewResponse.md)
 - [ProductGetProductRequest](docs/ProductGetProductRequest.md)
 - [ProductGetProductResponse](docs/ProductGetProductResponse.md)
 - [ProductLanguageCode](docs/ProductLanguageCode.md)
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
 - [ProductTranslateAction](docs/ProductTranslateAction.md)
 - [ProductUpdateAssetEntryPayload](docs/ProductUpdateAssetEntryPayload.md)
 - [ProductUpdateDataToBeReviewedRequest](docs/ProductUpdateDataToBeReviewedRequest.md)
 - [ProductUpdateMediaGalleryEntryRequest](docs/ProductUpdateMediaGalleryEntryRequest.md)
 - [ProductUpdateProductRequest](docs/ProductUpdateProductRequest.md)
 - [ProductUpdateProductRequestV2](docs/ProductUpdateProductRequestV2.md)
 - [ProductUpdateProductResponse](docs/ProductUpdateProductResponse.md)
 - [ProductUpdateProductWithAIRequest](docs/ProductUpdateProductWithAIRequest.md)
 - [ProductUpdateProductWithAIResponse](docs/ProductUpdateProductWithAIResponse.md)
 - [ProductentitymanagerLocalizedText](docs/ProductentitymanagerLocalizedText.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [TranslateActionAttributeCodesToTranslate](docs/TranslateActionAttributeCodesToTranslate.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


