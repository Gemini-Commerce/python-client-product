# product.ProductApi

All URIs are relative to *https://product.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_media_gallery_entry**](ProductApi.md#add_media_gallery_entry) | **POST** /product.Product/AddMediaGalleryEntry | Add Media Gallery Entry
[**bulk_add_assets_entries**](ProductApi.md#bulk_add_assets_entries) | **POST** /product.Product/BulkAddAssetsEntries | Bulk Add Assets Entries
[**bulk_delete_products**](ProductApi.md#bulk_delete_products) | **POST** /product.Product/BulkDeleteProducts | Bulk Delete Products
[**bulk_enhance_product_data_with_ai**](ProductApi.md#bulk_enhance_product_data_with_ai) | **POST** /product.Product/BulkEnhanceProductDataWithAI | Bulk Enhance Product Data With AI
[**bulk_remove_assets_entries**](ProductApi.md#bulk_remove_assets_entries) | **POST** /product.Product/BulkRemoveAssetsEntries | Bulk Remove Assets Entries
[**bulk_update_assets_entries**](ProductApi.md#bulk_update_assets_entries) | **POST** /product.Product/BulkUpdateAssetsEntries | Bulk Update Assets Entries
[**bulk_update_v2**](ProductApi.md#bulk_update_v2) | **POST** /product.Product/BulkUpdateV2 | Bulk Update Products
[**create_attribute_options**](ProductApi.md#create_attribute_options) | **POST** /product.Product/CreateAttributeOptions | Create Attribute Options
[**create_entity**](ProductApi.md#create_entity) | **POST** /product.Product/CreateEntity | Create Entity
[**create_options_list**](ProductApi.md#create_options_list) | **POST** /product.Product/CreateOptionsList | Create Options List
[**create_product_with_ai**](ProductApi.md#create_product_with_ai) | **POST** /product.Product/CreateProductWithAI | Create Product With AI
[**get_attribute_option**](ProductApi.md#get_attribute_option) | **POST** /product.Product/GetAttributeOption | Get Attribute Option
[**get_attribute_options**](ProductApi.md#get_attribute_options) | **POST** /product.Product/GetAttributeOptions | Get Attribute Options
[**get_entity**](ProductApi.md#get_entity) | **POST** /product.Product/GetEntity | Get Entity Details
[**get_options_list**](ProductApi.md#get_options_list) | **POST** /product.Product/GetOptionsList | Get Options List
[**get_product**](ProductApi.md#get_product) | **POST** /product.Product/GetProduct | Get Product
[**get_product_by_code**](ProductApi.md#get_product_by_code) | **POST** /product.Product/GetProductByCode | Get Product By Code
[**get_product_by_url_key**](ProductApi.md#get_product_by_url_key) | **POST** /product.Product/GetProductByUrlKey | Get Product By Url Key
[**get_product_data_in_review**](ProductApi.md#get_product_data_in_review) | **POST** /product.Product/GetProductDataInReview | Get Product Data In Review
[**list_attribute_options**](ProductApi.md#list_attribute_options) | **POST** /product.Product/ListAttributeOptions | List Attribute Options
[**list_entities**](ProductApi.md#list_entities) | **POST** /product.Product/ListEntities | List Entities
[**list_options_lists**](ProductApi.md#list_options_lists) | **POST** /product.Product/ListOptionsLists | List Options Lists
[**list_products**](ProductApi.md#list_products) | **POST** /product.Product/ListProducts | List Products
[**list_products_by_ids**](ProductApi.md#list_products_by_ids) | **POST** /product.Product/ListProductsByIds | List Products By Ids
[**list_products_by_sku**](ProductApi.md#list_products_by_sku) | **POST** /product.Product/ListProductsBySku | List Products By Sku
[**list_variants_by_sku**](ProductApi.md#list_variants_by_sku) | **POST** /product.Product/ListVariantsBySku | List Product Variants By Sku
[**product_bulk_create_attribute**](ProductApi.md#product_bulk_create_attribute) | **POST** /product.Product/BulkCreateAttribute | 
[**product_bulk_update**](ProductApi.md#product_bulk_update) | **POST** /product.Product/BulkUpdate | 
[**product_create_attribute_group**](ProductApi.md#product_create_attribute_group) | **POST** /product.Product/CreateAttributeGroup | 
[**product_create_product**](ProductApi.md#product_create_product) | **POST** /product.Product/CreateProduct | 
[**product_create_product_v2**](ProductApi.md#product_create_product_v2) | **POST** /product.Product/CreateProductV2 | 
[**product_delete**](ProductApi.md#product_delete) | **POST** /product.Product/Delete | 
[**product_delete_attribute**](ProductApi.md#product_delete_attribute) | **POST** /product.Product/DeleteAttribute | 
[**product_delete_product**](ProductApi.md#product_delete_product) | **POST** /product.Product/DeleteProduct | 
[**product_get_attribute_group**](ProductApi.md#product_get_attribute_group) | **POST** /product.Product/GetAttributeGroup | 
[**product_list_attribute_groups**](ProductApi.md#product_list_attribute_groups) | **POST** /product.Product/ListAttributeGroups | 
[**product_update_attribute**](ProductApi.md#product_update_attribute) | **POST** /product.Product/UpdateAttribute | 
[**product_update_attribute_group**](ProductApi.md#product_update_attribute_group) | **POST** /product.Product/UpdateAttributeGroup | 
[**product_update_product**](ProductApi.md#product_update_product) | **POST** /product.Product/UpdateProduct | 
[**product_update_product_v2**](ProductApi.md#product_update_product_v2) | **POST** /product.Product/UpdateProductV2 | 
[**remove_media_gallery_entry**](ProductApi.md#remove_media_gallery_entry) | **POST** /product.Product/RemoveMediaGalleryEntry | Remove Media Gallery Entry
[**update_attribute_options**](ProductApi.md#update_attribute_options) | **POST** /product.Product/UpdateAttributeOptions | Update Attribute Options
[**update_data_to_be_reviewed**](ProductApi.md#update_data_to_be_reviewed) | **POST** /product.Product/GetEnhanceProductDataWithAIStatus | Get Enhance Product Data With AI Status
[**update_data_to_be_reviewed_0**](ProductApi.md#update_data_to_be_reviewed_0) | **POST** /product.Product/UpdateDataToBeReviewed | Update Data To Be Reviewed
[**update_media_gallery_entry**](ProductApi.md#update_media_gallery_entry) | **POST** /product.Product/UpdateMediaGalleryEntry | Update Media Gallery Entry
[**update_options_list**](ProductApi.md#update_options_list) | **POST** /product.Product/UpdateOptionsList | Update Options List
[**update_product_with_ai**](ProductApi.md#update_product_with_ai) | **POST** /product.Product/UpdateProductWithAI | Update Product With AI


# **add_media_gallery_entry**
> ProductAddMediaGalleryEntryResponse add_media_gallery_entry(body)

Add Media Gallery Entry

The AddMediaGalleryEntry endpoint allows users to add a new media entry to the gallery of a specific product. To make a request to this endpoint, users need to provide the necessary information in the specified format. The request includes the tenant_id to specify the relevant tenant, the product_id to identify the target product, and the asset_grn which represents the globally unique identifier for the media asset being added. Additionally, the position field indicates the desired position of the media entry within the gallery, allowing users to control the order in which the media items are displayed. The metadata field, which is a repeated field, provides the option to include additional metadata associated with the media entry. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_add_media_gallery_entry_request import ProductAddMediaGalleryEntryRequest
from product.models.product_add_media_gallery_entry_response import ProductAddMediaGalleryEntryResponse
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
    except Exception as e:
        print("Exception when calling ProductApi->add_media_gallery_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAddMediaGalleryEntryRequest**](ProductAddMediaGalleryEntryRequest.md)|  | 

### Return type

[**ProductAddMediaGalleryEntryResponse**](ProductAddMediaGalleryEntryResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_add_assets_entries**
> ProductBulkAddAssetsEntriesResponse bulk_add_assets_entries(body)

Bulk Add Assets Entries

The BulkAddAssetsEntries endpoint allows users to add assets. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_add_assets_entries_request import ProductBulkAddAssetsEntriesRequest
from product.models.product_bulk_add_assets_entries_response import ProductBulkAddAssetsEntriesResponse
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
    body = product.ProductBulkAddAssetsEntriesRequest() # ProductBulkAddAssetsEntriesRequest | 

    try:
        # Bulk Add Assets Entries
        api_response = api_instance.bulk_add_assets_entries(body)
        print("The response of ProductApi->bulk_add_assets_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->bulk_add_assets_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkAddAssetsEntriesRequest**](ProductBulkAddAssetsEntriesRequest.md)|  | 

### Return type

[**ProductBulkAddAssetsEntriesResponse**](ProductBulkAddAssetsEntriesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_products**
> object bulk_delete_products(body)

Bulk Delete Products

This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_delete_products_request import ProductBulkDeleteProductsRequest
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
    body = product.ProductBulkDeleteProductsRequest() # ProductBulkDeleteProductsRequest | 

    try:
        # Bulk Delete Products
        api_response = api_instance.bulk_delete_products(body)
        print("The response of ProductApi->bulk_delete_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->bulk_delete_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkDeleteProductsRequest**](ProductBulkDeleteProductsRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enhance_product_data_with_ai**
> object bulk_enhance_product_data_with_ai(body)

Bulk Enhance Product Data With AI

The BulkEnhanceProductDataWithAI endpoint allows users to enhance product data using artificial intelligence (AI) capabilities. By making a request to this endpoint and providing the necessary input data, users can leverage AI algorithms to enrich and optimize product information. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_enhance_product_data_with_ai_request import ProductBulkEnhanceProductDataWithAIRequest
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
    body = product.ProductBulkEnhanceProductDataWithAIRequest() # ProductBulkEnhanceProductDataWithAIRequest | 

    try:
        # Bulk Enhance Product Data With AI
        api_response = api_instance.bulk_enhance_product_data_with_ai(body)
        print("The response of ProductApi->bulk_enhance_product_data_with_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->bulk_enhance_product_data_with_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkEnhanceProductDataWithAIRequest**](ProductBulkEnhanceProductDataWithAIRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_assets_entries**
> object bulk_remove_assets_entries(body)

Bulk Remove Assets Entries

The BulkRemoveAssetsEntries endpoint allows users to remove assets. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_remove_assets_entries_request import ProductBulkRemoveAssetsEntriesRequest
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
    body = product.ProductBulkRemoveAssetsEntriesRequest() # ProductBulkRemoveAssetsEntriesRequest | 

    try:
        # Bulk Remove Assets Entries
        api_response = api_instance.bulk_remove_assets_entries(body)
        print("The response of ProductApi->bulk_remove_assets_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->bulk_remove_assets_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkRemoveAssetsEntriesRequest**](ProductBulkRemoveAssetsEntriesRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_assets_entries**
> ProductBulkUpdateAssetsEntriesResponse bulk_update_assets_entries(body)

Bulk Update Assets Entries

The BulkUpdateAssetsEntries endpoint allows users to update assets. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_update_assets_entries_request import ProductBulkUpdateAssetsEntriesRequest
from product.models.product_bulk_update_assets_entries_response import ProductBulkUpdateAssetsEntriesResponse
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
    body = product.ProductBulkUpdateAssetsEntriesRequest() # ProductBulkUpdateAssetsEntriesRequest | 

    try:
        # Bulk Update Assets Entries
        api_response = api_instance.bulk_update_assets_entries(body)
        print("The response of ProductApi->bulk_update_assets_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->bulk_update_assets_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkUpdateAssetsEntriesRequest**](ProductBulkUpdateAssetsEntriesRequest.md)|  | 

### Return type

[**ProductBulkUpdateAssetsEntriesResponse**](ProductBulkUpdateAssetsEntriesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_v2**
> ProductBulkUpdateResponse bulk_update_v2(body)

Bulk Update Products

Version 2 of bulk updates for product attributes with enhanced payload structure and response format. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_update_request_v2 import ProductBulkUpdateRequestV2
from product.models.product_bulk_update_response import ProductBulkUpdateResponse
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
    body = product.ProductBulkUpdateRequestV2() # ProductBulkUpdateRequestV2 | 

    try:
        # Bulk Update Products
        api_response = api_instance.bulk_update_v2(body)
        print("The response of ProductApi->bulk_update_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->bulk_update_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkUpdateRequestV2**](ProductBulkUpdateRequestV2.md)|  | 

### Return type

[**ProductBulkUpdateResponse**](ProductBulkUpdateResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute_options**
> EntitymanagerCreateAttributeOptionsResponse create_attribute_options(body)

Create Attribute Options

Create attribute options with specified codes, values, and swatches. Returns created options and any associated errors.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_create_attribute_options_request import EntitymanagerCreateAttributeOptionsRequest
from product.models.entitymanager_create_attribute_options_response import EntitymanagerCreateAttributeOptionsResponse
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
    body = product.EntitymanagerCreateAttributeOptionsRequest() # EntitymanagerCreateAttributeOptionsRequest | 

    try:
        # Create Attribute Options
        api_response = api_instance.create_attribute_options(body)
        print("The response of ProductApi->create_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerCreateAttributeOptionsRequest**](EntitymanagerCreateAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerCreateAttributeOptionsResponse**](EntitymanagerCreateAttributeOptionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> EntitymanagerCreateEntityResponse create_entity(body)

Create Entity

The CreateEntity endpoint allows users to define and create a new entity with custom attributes, providing a flexible way to represent and manage different data structures within the system. By making a request to this endpoint, users can create a new entity that serves as an abstraction of a product or any other domain-specific object. This endpoint empowers users to define the specific attributes that compose the entity, such as color, composition, technical details, or any other relevant properties. Utilize the CreateEntity endpoint to dynamically extend and adapt your system's data model to accommodate diverse business requirements and efficiently manage various types of entities.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_create_entity_response import EntitymanagerCreateEntityResponse
from product.models.entitymanager_entity import EntitymanagerEntity
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
    body = product.EntitymanagerEntity() # EntitymanagerEntity | 

    try:
        # Create Entity
        api_response = api_instance.create_entity(body)
        print("The response of ProductApi->create_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerEntity**](EntitymanagerEntity.md)|  | 

### Return type

[**EntitymanagerCreateEntityResponse**](EntitymanagerCreateEntityResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_options_list**
> EntitymanagerCreateOptionsListResponse create_options_list(body)

Create Options List

The CreateOptionsList endpoint allows users to create an OptionList, which represents a list of predefined options for assigning to an attribute. By making a request to this endpoint with the provided request format, users can create a new OptionList by specifying the relevant tenant ID and providing the OptionList object containing the predefined options. This functionality facilitates efficient management and assignment of predefined attribute values, ensuring consistency and flexibility within the system.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_create_options_list_request import EntitymanagerCreateOptionsListRequest
from product.models.entitymanager_create_options_list_response import EntitymanagerCreateOptionsListResponse
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
    body = product.EntitymanagerCreateOptionsListRequest() # EntitymanagerCreateOptionsListRequest | 

    try:
        # Create Options List
        api_response = api_instance.create_options_list(body)
        print("The response of ProductApi->create_options_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_options_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerCreateOptionsListRequest**](EntitymanagerCreateOptionsListRequest.md)|  | 

### Return type

[**EntitymanagerCreateOptionsListResponse**](EntitymanagerCreateOptionsListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product_with_ai**
> ProductCreateProductWithAIResponse create_product_with_ai(body)

Create Product With AI

The CreateProductWithAI endpoint allows users to create a new product within the system using artificial intelligence (AI) capabilities. By sending a request to this endpoint and providing the necessary input data, users can leverage AI algorithms to enhance and optimize the product creation process.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_create_product_with_ai_request import ProductCreateProductWithAIRequest
from product.models.product_create_product_with_ai_response import ProductCreateProductWithAIResponse
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
    body = product.ProductCreateProductWithAIRequest() # ProductCreateProductWithAIRequest | 

    try:
        # Create Product With AI
        api_response = api_instance.create_product_with_ai(body)
        print("The response of ProductApi->create_product_with_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_product_with_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductCreateProductWithAIRequest**](ProductCreateProductWithAIRequest.md)|  | 

### Return type

[**ProductCreateProductWithAIResponse**](ProductCreateProductWithAIResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_option**
> EntitymanagerGetAttributeOptionResponse get_attribute_option(body)

Get Attribute Option

Retrieve attribute option details by providing the tenant ID, list code, and option ID. Returns the specified attribute option.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_get_attribute_option_request import EntitymanagerGetAttributeOptionRequest
from product.models.entitymanager_get_attribute_option_response import EntitymanagerGetAttributeOptionResponse
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
    body = product.EntitymanagerGetAttributeOptionRequest() # EntitymanagerGetAttributeOptionRequest | 

    try:
        # Get Attribute Option
        api_response = api_instance.get_attribute_option(body)
        print("The response of ProductApi->get_attribute_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_attribute_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetAttributeOptionRequest**](EntitymanagerGetAttributeOptionRequest.md)|  | 

### Return type

[**EntitymanagerGetAttributeOptionResponse**](EntitymanagerGetAttributeOptionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_options**
> EntitymanagerGetAttributeOptionsResponse get_attribute_options(body)

Get Attribute Options

Retrieve a list of attribute options based on the provided tenant ID and list code.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_get_attribute_options_request import EntitymanagerGetAttributeOptionsRequest
from product.models.entitymanager_get_attribute_options_response import EntitymanagerGetAttributeOptionsResponse
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
    body = product.EntitymanagerGetAttributeOptionsRequest() # EntitymanagerGetAttributeOptionsRequest | 

    try:
        # Get Attribute Options
        api_response = api_instance.get_attribute_options(body)
        print("The response of ProductApi->get_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetAttributeOptionsRequest**](EntitymanagerGetAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerGetAttributeOptionsResponse**](EntitymanagerGetAttributeOptionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> EntitymanagerEntity get_entity(body)

Get Entity Details

Retrieve details of an entity by providing the tenant ID and either entity data or entity ID. Returns information including ID, type, code, label, relationships, and attributes.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_entity import EntitymanagerEntity
from product.models.entitymanager_entity_request import EntitymanagerEntityRequest
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
    body = product.EntitymanagerEntityRequest() # EntitymanagerEntityRequest | 

    try:
        # Get Entity Details
        api_response = api_instance.get_entity(body)
        print("The response of ProductApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerEntityRequest**](EntitymanagerEntityRequest.md)|  | 

### Return type

[**EntitymanagerEntity**](EntitymanagerEntity.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_options_list**
> EntitymanagerGetOptionsListResponse get_options_list(body)

Get Options List

Retrieve option lists.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_get_options_list_request import EntitymanagerGetOptionsListRequest
from product.models.entitymanager_get_options_list_response import EntitymanagerGetOptionsListResponse
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
    body = product.EntitymanagerGetOptionsListRequest() # EntitymanagerGetOptionsListRequest | 

    try:
        # Get Options List
        api_response = api_instance.get_options_list(body)
        print("The response of ProductApi->get_options_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_options_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetOptionsListRequest**](EntitymanagerGetOptionsListRequest.md)|  | 

### Return type

[**EntitymanagerGetOptionsListResponse**](EntitymanagerGetOptionsListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> ProductGetProductResponse get_product(body)

Get Product

The GetProduct endpoint enables users to retrieve a product from the system. By sending a request to this endpoint, users can retrieve a product by providing its unique identifier.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_get_product_request import ProductGetProductRequest
from product.models.product_get_product_response import ProductGetProductResponse
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
    body = product.ProductGetProductRequest() # ProductGetProductRequest | 

    try:
        # Get Product
        api_response = api_instance.get_product(body)
        print("The response of ProductApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductRequest**](ProductGetProductRequest.md)|  | 

### Return type

[**ProductGetProductResponse**](ProductGetProductResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_by_code**
> ProductGetProductByCodeResponse get_product_by_code(body)

Get Product By Code

The GetProductByCode endpoint enables users to retrieve a product from the system. By sending a request to this endpoint, users can retrieve a product by providing its unique code.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_get_product_by_code_request import ProductGetProductByCodeRequest
from product.models.product_get_product_by_code_response import ProductGetProductByCodeResponse
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
    body = product.ProductGetProductByCodeRequest() # ProductGetProductByCodeRequest | 

    try:
        # Get Product By Code
        api_response = api_instance.get_product_by_code(body)
        print("The response of ProductApi->get_product_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_product_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductByCodeRequest**](ProductGetProductByCodeRequest.md)|  | 

### Return type

[**ProductGetProductByCodeResponse**](ProductGetProductByCodeResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_by_url_key**
> ProductGetProductByUrlKeyResponse get_product_by_url_key(body)

Get Product By Url Key

The GetProductByUrlKey endpoint enables users to retrieve a product from the system. By sending a request to this endpoint, users can retrieve a product by providing its unique url key.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_get_product_by_url_key_request import ProductGetProductByUrlKeyRequest
from product.models.product_get_product_by_url_key_response import ProductGetProductByUrlKeyResponse
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
    body = product.ProductGetProductByUrlKeyRequest() # ProductGetProductByUrlKeyRequest | 

    try:
        # Get Product By Url Key
        api_response = api_instance.get_product_by_url_key(body)
        print("The response of ProductApi->get_product_by_url_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_product_by_url_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductByUrlKeyRequest**](ProductGetProductByUrlKeyRequest.md)|  | 

### Return type

[**ProductGetProductByUrlKeyResponse**](ProductGetProductByUrlKeyResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_data_in_review**
> ProductGetProductDataInReviewResponse get_product_data_in_review(body)

Get Product Data In Review

The GetProductDataInReview endpoint allows users to retrieve product data that is currently under review. By making a request to this endpoint, users can access detailed information about the product data that is pending approval or review by authorized personnel. This functionality provides transparency and visibility into the product data review process, enabling users to track the status and progress of product data submissions.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_get_product_data_in_review_request import ProductGetProductDataInReviewRequest
from product.models.product_get_product_data_in_review_response import ProductGetProductDataInReviewResponse
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
    body = product.ProductGetProductDataInReviewRequest() # ProductGetProductDataInReviewRequest | 

    try:
        # Get Product Data In Review
        api_response = api_instance.get_product_data_in_review(body)
        print("The response of ProductApi->get_product_data_in_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_product_data_in_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductDataInReviewRequest**](ProductGetProductDataInReviewRequest.md)|  | 

### Return type

[**ProductGetProductDataInReviewResponse**](ProductGetProductDataInReviewResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attribute_options**
> EntitymanagerListAttributeOptionsResponse list_attribute_options(body)

List Attribute Options

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_list_attribute_options_request import EntitymanagerListAttributeOptionsRequest
from product.models.entitymanager_list_attribute_options_response import EntitymanagerListAttributeOptionsResponse
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
    body = product.EntitymanagerListAttributeOptionsRequest() # EntitymanagerListAttributeOptionsRequest | 

    try:
        # List Attribute Options
        api_response = api_instance.list_attribute_options(body)
        print("The response of ProductApi->list_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListAttributeOptionsRequest**](EntitymanagerListAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerListAttributeOptionsResponse**](EntitymanagerListAttributeOptionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities**
> EntitymanagerListEntitiesResponse list_entities(body)

List Entities

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_list_entities_request import EntitymanagerListEntitiesRequest
from product.models.entitymanager_list_entities_response import EntitymanagerListEntitiesResponse
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
    body = product.EntitymanagerListEntitiesRequest() # EntitymanagerListEntitiesRequest | 

    try:
        # List Entities
        api_response = api_instance.list_entities(body)
        print("The response of ProductApi->list_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListEntitiesRequest**](EntitymanagerListEntitiesRequest.md)|  | 

### Return type

[**EntitymanagerListEntitiesResponse**](EntitymanagerListEntitiesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_options_lists**
> EntitymanagerListOptionsListsResponse list_options_lists(body)

List Options Lists

The ListOptionsLists endpoint allows users to retrieve a list of OptionLists available in the system. By making a request to this endpoint with the provided request format, users can obtain all the OptionLists associated with the specified tenant. This functionality enables users to access and manage the predefined options available for various attributes within the system. Utilizing the ListOptionsLists endpoint provides a convenient way to retrieve and work with OptionLists, facilitating efficient management of attribute options and ensuring consistency in attribute values throughout the system.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_list_options_lists_request import EntitymanagerListOptionsListsRequest
from product.models.entitymanager_list_options_lists_response import EntitymanagerListOptionsListsResponse
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
    body = product.EntitymanagerListOptionsListsRequest() # EntitymanagerListOptionsListsRequest | 

    try:
        # List Options Lists
        api_response = api_instance.list_options_lists(body)
        print("The response of ProductApi->list_options_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_options_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListOptionsListsRequest**](EntitymanagerListOptionsListsRequest.md)|  | 

### Return type

[**EntitymanagerListOptionsListsResponse**](EntitymanagerListOptionsListsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> ProductListProductsResponse list_products(body)

List Products

The ListProducts endpoint provides users with the ability to retrieve a filtered list of products based on specific criteria. By including filter parameters in the request, users can customize the response to only include products that meet certain conditions, such as price range, category, availability, or any other relevant attributes. This endpoint empowers users to efficiently narrow down the product selection and retrieve tailored results.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_list_products_request import ProductListProductsRequest
from product.models.product_list_products_response import ProductListProductsResponse
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
    body = product.ProductListProductsRequest() # ProductListProductsRequest | 

    try:
        # List Products
        api_response = api_instance.list_products(body)
        print("The response of ProductApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListProductsRequest**](ProductListProductsRequest.md)|  | 

### Return type

[**ProductListProductsResponse**](ProductListProductsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products_by_ids**
> ProductListProductsByIdsResponse list_products_by_ids(body)

List Products By Ids

The ListProductsByIds endpoint allows users to retrieve a list of products based on provided IDs. By making a request to this endpoint and specifying a set of product IDs, users can retrieve detailed information about the corresponding products. This endpoint facilitates efficient retrieval of specific products, enabling applications to display accurate and targeted product information to users.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_list_products_by_ids_request import ProductListProductsByIdsRequest
from product.models.product_list_products_by_ids_response import ProductListProductsByIdsResponse
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
    body = product.ProductListProductsByIdsRequest() # ProductListProductsByIdsRequest | 

    try:
        # List Products By Ids
        api_response = api_instance.list_products_by_ids(body)
        print("The response of ProductApi->list_products_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_products_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListProductsByIdsRequest**](ProductListProductsByIdsRequest.md)|  | 

### Return type

[**ProductListProductsByIdsResponse**](ProductListProductsByIdsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products_by_sku**
> ProductListProductsBySkuResponse list_products_by_sku(body)

List Products By Sku

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_list_products_by_sku_request import ProductListProductsBySkuRequest
from product.models.product_list_products_by_sku_response import ProductListProductsBySkuResponse
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
    body = product.ProductListProductsBySkuRequest() # ProductListProductsBySkuRequest | 

    try:
        # List Products By Sku
        api_response = api_instance.list_products_by_sku(body)
        print("The response of ProductApi->list_products_by_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_products_by_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListProductsBySkuRequest**](ProductListProductsBySkuRequest.md)|  | 

### Return type

[**ProductListProductsBySkuResponse**](ProductListProductsBySkuResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_variants_by_sku**
> ProductListVariantsBySkuResponse list_variants_by_sku(body)

List Product Variants By Sku

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_list_variants_by_sku_request import ProductListVariantsBySkuRequest
from product.models.product_list_variants_by_sku_response import ProductListVariantsBySkuResponse
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
    body = product.ProductListVariantsBySkuRequest() # ProductListVariantsBySkuRequest | 

    try:
        # List Product Variants By Sku
        api_response = api_instance.list_variants_by_sku(body)
        print("The response of ProductApi->list_variants_by_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_variants_by_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListVariantsBySkuRequest**](ProductListVariantsBySkuRequest.md)|  | 

### Return type

[**ProductListVariantsBySkuResponse**](ProductListVariantsBySkuResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_create_attribute**
> EntitymanagerBulkCreateAttributeResponse product_bulk_create_attribute(body)



Allow creation of multiple attributes. If any attribute is invalid, an error will be returned with more details, and in the response body, the attributes created will be returned.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_bulk_create_attribute_request import EntitymanagerBulkCreateAttributeRequest
from product.models.entitymanager_bulk_create_attribute_response import EntitymanagerBulkCreateAttributeResponse
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
    body = product.EntitymanagerBulkCreateAttributeRequest() # EntitymanagerBulkCreateAttributeRequest | 

    try:
        api_response = api_instance.product_bulk_create_attribute(body)
        print("The response of ProductApi->product_bulk_create_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_create_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerBulkCreateAttributeRequest**](EntitymanagerBulkCreateAttributeRequest.md)|  | 

### Return type

[**EntitymanagerBulkCreateAttributeResponse**](EntitymanagerBulkCreateAttributeResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_update**
> ProductBulkUpdateResponse product_bulk_update(body)



This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_bulk_update_request import ProductBulkUpdateRequest
from product.models.product_bulk_update_response import ProductBulkUpdateResponse
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
    body = product.ProductBulkUpdateRequest() # ProductBulkUpdateRequest | 

    try:
        api_response = api_instance.product_bulk_update(body)
        print("The response of ProductApi->product_bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkUpdateRequest**](ProductBulkUpdateRequest.md)|  | 

### Return type

[**ProductBulkUpdateResponse**](ProductBulkUpdateResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create_attribute_group**
> EntitymanagerAttributeGroup product_create_attribute_group(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_attribute_group import EntitymanagerAttributeGroup
from product.models.entitymanager_create_attribute_group_request import EntitymanagerCreateAttributeGroupRequest
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
    body = product.EntitymanagerCreateAttributeGroupRequest() # EntitymanagerCreateAttributeGroupRequest | 

    try:
        api_response = api_instance.product_create_attribute_group(body)
        print("The response of ProductApi->product_create_attribute_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create_attribute_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerCreateAttributeGroupRequest**](EntitymanagerCreateAttributeGroupRequest.md)|  | 

### Return type

[**EntitymanagerAttributeGroup**](EntitymanagerAttributeGroup.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create_product**
> ProductCreateProductResponse product_create_product(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_create_product_request import ProductCreateProductRequest
from product.models.product_create_product_response import ProductCreateProductResponse
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
    body = product.ProductCreateProductRequest() # ProductCreateProductRequest | The CreateProductRequest message is used to create a new product within the system. It contains various fields that allow specifying the details and attributes of the product.

    try:
        api_response = api_instance.product_create_product(body)
        print("The response of ProductApi->product_create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductCreateProductRequest**](ProductCreateProductRequest.md)| The CreateProductRequest message is used to create a new product within the system. It contains various fields that allow specifying the details and attributes of the product. | 

### Return type

[**ProductCreateProductResponse**](ProductCreateProductResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create_product_v2**
> ProductCreateProductResponseV2 product_create_product_v2(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_create_product_request_v2 import ProductCreateProductRequestV2
from product.models.product_create_product_response_v2 import ProductCreateProductResponseV2
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
    body = product.ProductCreateProductRequestV2() # ProductCreateProductRequestV2 | 

    try:
        api_response = api_instance.product_create_product_v2(body)
        print("The response of ProductApi->product_create_product_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create_product_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductCreateProductRequestV2**](ProductCreateProductRequestV2.md)|  | 

### Return type

[**ProductCreateProductResponseV2**](ProductCreateProductResponseV2.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_delete**
> ProductDeleteResponse product_delete(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_delete_request import ProductDeleteRequest
from product.models.product_delete_response import ProductDeleteResponse
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
    body = product.ProductDeleteRequest() # ProductDeleteRequest | 

    try:
        api_response = api_instance.product_delete(body)
        print("The response of ProductApi->product_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductDeleteRequest**](ProductDeleteRequest.md)|  | 

### Return type

[**ProductDeleteResponse**](ProductDeleteResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_delete_attribute**
> object product_delete_attribute(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_delete_attribute_request import EntitymanagerDeleteAttributeRequest
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
    body = product.EntitymanagerDeleteAttributeRequest() # EntitymanagerDeleteAttributeRequest | 

    try:
        api_response = api_instance.product_delete_attribute(body)
        print("The response of ProductApi->product_delete_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_delete_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerDeleteAttributeRequest**](EntitymanagerDeleteAttributeRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_delete_product**
> object product_delete_product(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_delete_product_request import ProductDeleteProductRequest
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
    body = product.ProductDeleteProductRequest() # ProductDeleteProductRequest | 

    try:
        api_response = api_instance.product_delete_product(body)
        print("The response of ProductApi->product_delete_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_delete_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductDeleteProductRequest**](ProductDeleteProductRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_attribute_group**
> EntitymanagerAttributeGroup product_get_attribute_group(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_attribute_group import EntitymanagerAttributeGroup
from product.models.entitymanager_get_attribute_group_request import EntitymanagerGetAttributeGroupRequest
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
    body = product.EntitymanagerGetAttributeGroupRequest() # EntitymanagerGetAttributeGroupRequest | 

    try:
        api_response = api_instance.product_get_attribute_group(body)
        print("The response of ProductApi->product_get_attribute_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_attribute_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetAttributeGroupRequest**](EntitymanagerGetAttributeGroupRequest.md)|  | 

### Return type

[**EntitymanagerAttributeGroup**](EntitymanagerAttributeGroup.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_attribute_groups**
> EntitymanagerListAttributeGroupsResponse product_list_attribute_groups(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_list_attribute_groups_request import EntitymanagerListAttributeGroupsRequest
from product.models.entitymanager_list_attribute_groups_response import EntitymanagerListAttributeGroupsResponse
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
    body = product.EntitymanagerListAttributeGroupsRequest() # EntitymanagerListAttributeGroupsRequest | 

    try:
        api_response = api_instance.product_list_attribute_groups(body)
        print("The response of ProductApi->product_list_attribute_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_attribute_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListAttributeGroupsRequest**](EntitymanagerListAttributeGroupsRequest.md)|  | 

### Return type

[**EntitymanagerListAttributeGroupsResponse**](EntitymanagerListAttributeGroupsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_attribute**
> EntitymanagerAttribute product_update_attribute(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_attribute import EntitymanagerAttribute
from product.models.entitymanager_update_attribute_request import EntitymanagerUpdateAttributeRequest
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
    body = product.EntitymanagerUpdateAttributeRequest() # EntitymanagerUpdateAttributeRequest | 

    try:
        api_response = api_instance.product_update_attribute(body)
        print("The response of ProductApi->product_update_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerUpdateAttributeRequest**](EntitymanagerUpdateAttributeRequest.md)|  | 

### Return type

[**EntitymanagerAttribute**](EntitymanagerAttribute.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_attribute_group**
> EntitymanagerAttributeGroup product_update_attribute_group(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_attribute_group import EntitymanagerAttributeGroup
from product.models.entitymanager_update_attribute_group_request import EntitymanagerUpdateAttributeGroupRequest
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
    body = product.EntitymanagerUpdateAttributeGroupRequest() # EntitymanagerUpdateAttributeGroupRequest | 

    try:
        api_response = api_instance.product_update_attribute_group(body)
        print("The response of ProductApi->product_update_attribute_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_attribute_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerUpdateAttributeGroupRequest**](EntitymanagerUpdateAttributeGroupRequest.md)|  | 

### Return type

[**EntitymanagerAttributeGroup**](EntitymanagerAttributeGroup.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_product**
> ProductUpdateProductResponse product_update_product(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_update_product_request import ProductUpdateProductRequest
from product.models.product_update_product_response import ProductUpdateProductResponse
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
    body = product.ProductUpdateProductRequest() # ProductUpdateProductRequest | 

    try:
        api_response = api_instance.product_update_product(body)
        print("The response of ProductApi->product_update_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateProductRequest**](ProductUpdateProductRequest.md)|  | 

### Return type

[**ProductUpdateProductResponse**](ProductUpdateProductResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_product_v2**
> object product_update_product_v2(body)



### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_update_product_request_v2 import ProductUpdateProductRequestV2
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
    body = product.ProductUpdateProductRequestV2() # ProductUpdateProductRequestV2 | 

    try:
        api_response = api_instance.product_update_product_v2(body)
        print("The response of ProductApi->product_update_product_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_product_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateProductRequestV2**](ProductUpdateProductRequestV2.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_media_gallery_entry**
> object remove_media_gallery_entry(body)

Remove Media Gallery Entry

The RemoveMediaGalleryEntry endpoint allows users to remove a specific media entry from a product's gallery. By making a request to this endpoint and providing the tenant ID, product ID, and the unique identifier of the media entry, users can easily manage and update the visual content of a product's gallery. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_remove_media_gallery_entry_request import ProductRemoveMediaGalleryEntryRequest
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
    body = product.ProductRemoveMediaGalleryEntryRequest() # ProductRemoveMediaGalleryEntryRequest | 

    try:
        # Remove Media Gallery Entry
        api_response = api_instance.remove_media_gallery_entry(body)
        print("The response of ProductApi->remove_media_gallery_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->remove_media_gallery_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductRemoveMediaGalleryEntryRequest**](ProductRemoveMediaGalleryEntryRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_options**
> EntitymanagerUpdateAttributeOptionsResponse update_attribute_options(body)

Update Attribute Options

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_update_attribute_options_request import EntitymanagerUpdateAttributeOptionsRequest
from product.models.entitymanager_update_attribute_options_response import EntitymanagerUpdateAttributeOptionsResponse
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
    body = product.EntitymanagerUpdateAttributeOptionsRequest() # EntitymanagerUpdateAttributeOptionsRequest | 

    try:
        # Update Attribute Options
        api_response = api_instance.update_attribute_options(body)
        print("The response of ProductApi->update_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerUpdateAttributeOptionsRequest**](EntitymanagerUpdateAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerUpdateAttributeOptionsResponse**](EntitymanagerUpdateAttributeOptionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_to_be_reviewed**
> ProductGetEnhanceProductDataWithAIStatusResponse update_data_to_be_reviewed(body)

Get Enhance Product Data With AI Status

The GetEnhanceProductDataWithAIStatus endpoint allows users to retrieve the status of a product data enhancement process using artificial intelligence (AI) capabilities. By making a request to this endpoint and providing the necessary input data, users can check the progress and completion status of the AI-driven product data enhancement operation. This functionality provides visibility and transparency into the AI processing of product data, enabling users to monitor and track the status of the enhancement process.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_get_enhance_product_data_with_ai_status_request import ProductGetEnhanceProductDataWithAIStatusRequest
from product.models.product_get_enhance_product_data_with_ai_status_response import ProductGetEnhanceProductDataWithAIStatusResponse
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
    body = product.ProductGetEnhanceProductDataWithAIStatusRequest() # ProductGetEnhanceProductDataWithAIStatusRequest | 

    try:
        # Get Enhance Product Data With AI Status
        api_response = api_instance.update_data_to_be_reviewed(body)
        print("The response of ProductApi->update_data_to_be_reviewed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_data_to_be_reviewed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetEnhanceProductDataWithAIStatusRequest**](ProductGetEnhanceProductDataWithAIStatusRequest.md)|  | 

### Return type

[**ProductGetEnhanceProductDataWithAIStatusResponse**](ProductGetEnhanceProductDataWithAIStatusResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_to_be_reviewed_0**
> object update_data_to_be_reviewed_0(body)

Update Data To Be Reviewed

The UpdateDataToBeReviewed endpoint allows users to update product data that is pending review. By sending a request to this endpoint and providing the necessary input data, users can modify and enhance the product information that is currently under review. This functionality enables users to make changes to product data submissions and ensure that the information is accurate and up-to-date before final approval.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_update_data_to_be_reviewed_request import ProductUpdateDataToBeReviewedRequest
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
    body = product.ProductUpdateDataToBeReviewedRequest() # ProductUpdateDataToBeReviewedRequest | 

    try:
        # Update Data To Be Reviewed
        api_response = api_instance.update_data_to_be_reviewed_0(body)
        print("The response of ProductApi->update_data_to_be_reviewed_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_data_to_be_reviewed_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateDataToBeReviewedRequest**](ProductUpdateDataToBeReviewedRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_gallery_entry**
> object update_media_gallery_entry(body)

Update Media Gallery Entry

The UpdateMediaGalleryEntry endpoint allows users to modify and update a specific media entry within a product's gallery. By sending a request to this endpoint and providing the necessary information, users can efficiently update the media asset, position, and metadata associated with the entry. This operation is asynchronous and may complete after the response.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_update_media_gallery_entry_request import ProductUpdateMediaGalleryEntryRequest
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
    body = product.ProductUpdateMediaGalleryEntryRequest() # ProductUpdateMediaGalleryEntryRequest | 

    try:
        # Update Media Gallery Entry
        api_response = api_instance.update_media_gallery_entry(body)
        print("The response of ProductApi->update_media_gallery_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_media_gallery_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateMediaGalleryEntryRequest**](ProductUpdateMediaGalleryEntryRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_options_list**
> EntitymanagerUpdateOptionsListResponse update_options_list(body)

Update Options List

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.entitymanager_update_options_list_request import EntitymanagerUpdateOptionsListRequest
from product.models.entitymanager_update_options_list_response import EntitymanagerUpdateOptionsListResponse
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
    body = product.EntitymanagerUpdateOptionsListRequest() # EntitymanagerUpdateOptionsListRequest | 

    try:
        # Update Options List
        api_response = api_instance.update_options_list(body)
        print("The response of ProductApi->update_options_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_options_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerUpdateOptionsListRequest**](EntitymanagerUpdateOptionsListRequest.md)|  | 

### Return type

[**EntitymanagerUpdateOptionsListResponse**](EntitymanagerUpdateOptionsListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_with_ai**
> ProductUpdateProductWithAIResponse update_product_with_ai(body)

Update Product With AI

The UpdateProductWithAI endpoint allows users to update an existing product within the system using artificial intelligence (AI) capabilities. By sending a request to this endpoint and providing the necessary input data, users can leverage AI algorithms to enhance and optimize the product update process.

### Example

* Api Key Authentication (Authorization):

```python
import product
from product.models.product_update_product_with_ai_request import ProductUpdateProductWithAIRequest
from product.models.product_update_product_with_ai_response import ProductUpdateProductWithAIResponse
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
    body = product.ProductUpdateProductWithAIRequest() # ProductUpdateProductWithAIRequest | 

    try:
        # Update Product With AI
        api_response = api_instance.update_product_with_ai(body)
        print("The response of ProductApi->update_product_with_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_product_with_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateProductWithAIRequest**](ProductUpdateProductWithAIRequest.md)|  | 

### Return type

[**ProductUpdateProductWithAIResponse**](ProductUpdateProductWithAIResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

