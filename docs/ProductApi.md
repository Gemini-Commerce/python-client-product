# product.ProductApi

All URIs are relative to *https://product.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_add_media_gallery_entry**](ProductApi.md#product_add_media_gallery_entry) | **POST** /product.Product/AddMediaGalleryEntry | 
[**product_bulk_add_assets_entries**](ProductApi.md#product_bulk_add_assets_entries) | **POST** /product.Product/BulkAddAssetsEntries | Assets endpoints
[**product_bulk_create_attribute**](ProductApi.md#product_bulk_create_attribute) | **POST** /product.Product/BulkCreateAttribute | 
[**product_bulk_delete_products**](ProductApi.md#product_bulk_delete_products) | **POST** /product.Product/BulkDeleteProducts | 
[**product_bulk_remove_assets_entries**](ProductApi.md#product_bulk_remove_assets_entries) | **POST** /product.Product/BulkRemoveAssetsEntries | 
[**product_bulk_update**](ProductApi.md#product_bulk_update) | **POST** /product.Product/BulkUpdate | 
[**product_bulk_update_assets_entries**](ProductApi.md#product_bulk_update_assets_entries) | **POST** /product.Product/BulkUpdateAssetsEntries | 
[**product_bulk_update_v2**](ProductApi.md#product_bulk_update_v2) | **POST** /product.Product/BulkUpdateV2 | 
[**product_create_attribute_group**](ProductApi.md#product_create_attribute_group) | **POST** /product.Product/CreateAttributeGroup | 
[**product_create_attribute_options**](ProductApi.md#product_create_attribute_options) | **POST** /product.Product/CreateAttributeOptions | 
[**product_create_entity**](ProductApi.md#product_create_entity) | **POST** /product.Product/CreateEntity | 
[**product_create_options_list**](ProductApi.md#product_create_options_list) | **POST** /product.Product/CreateOptionsList | 
[**product_create_product**](ProductApi.md#product_create_product) | **POST** /product.Product/CreateProduct | 
[**product_create_product_v2**](ProductApi.md#product_create_product_v2) | **POST** /product.Product/CreateProductV2 | 
[**product_delete**](ProductApi.md#product_delete) | **POST** /product.Product/Delete | 
[**product_delete_attribute**](ProductApi.md#product_delete_attribute) | **POST** /product.Product/DeleteAttribute | 
[**product_delete_product**](ProductApi.md#product_delete_product) | **POST** /product.Product/DeleteProduct | 
[**product_get_attribute_group**](ProductApi.md#product_get_attribute_group) | **POST** /product.Product/GetAttributeGroup | 
[**product_get_attribute_option**](ProductApi.md#product_get_attribute_option) | **POST** /product.Product/GetAttributeOption | 
[**product_get_attribute_options**](ProductApi.md#product_get_attribute_options) | **POST** /product.Product/GetAttributeOptions | 
[**product_get_entity**](ProductApi.md#product_get_entity) | **POST** /product.Product/GetEntity | 
[**product_get_options_list**](ProductApi.md#product_get_options_list) | **POST** /product.Product/GetOptionsList | 
[**product_get_product**](ProductApi.md#product_get_product) | **POST** /product.Product/GetProduct | 
[**product_get_product_by_code**](ProductApi.md#product_get_product_by_code) | **POST** /product.Product/GetProductByCode | 
[**product_get_product_by_url_key**](ProductApi.md#product_get_product_by_url_key) | **POST** /product.Product/GetProductByUrlKey | 
[**product_list_attribute_groups**](ProductApi.md#product_list_attribute_groups) | **POST** /product.Product/ListAttributeGroups | Attribute Groups endpoints
[**product_list_attribute_options**](ProductApi.md#product_list_attribute_options) | **POST** /product.Product/ListAttributeOptions | 
[**product_list_entities**](ProductApi.md#product_list_entities) | **POST** /product.Product/ListEntities | 
[**product_list_options_lists**](ProductApi.md#product_list_options_lists) | **POST** /product.Product/ListOptionsLists | 
[**product_list_products**](ProductApi.md#product_list_products) | **POST** /product.Product/ListProducts | 
[**product_list_products_by_ids**](ProductApi.md#product_list_products_by_ids) | **POST** /product.Product/ListProductsByIds | 
[**product_list_products_by_sku**](ProductApi.md#product_list_products_by_sku) | **POST** /product.Product/ListProductsBySku | 
[**product_list_variants_by_sku**](ProductApi.md#product_list_variants_by_sku) | **POST** /product.Product/ListVariantsBySku | 
[**product_remove_media_gallery_entry**](ProductApi.md#product_remove_media_gallery_entry) | **POST** /product.Product/RemoveMediaGalleryEntry | 
[**product_update_attribute**](ProductApi.md#product_update_attribute) | **POST** /product.Product/UpdateAttribute | 
[**product_update_attribute_group**](ProductApi.md#product_update_attribute_group) | **POST** /product.Product/UpdateAttributeGroup | 
[**product_update_attribute_options**](ProductApi.md#product_update_attribute_options) | **POST** /product.Product/UpdateAttributeOptions | rpc GetAttributeOptionByCode (product.entitymanager.GetAttributeOptionByCodeRequest) returns (product.entitymanager.GetAttributeOptionByCodeResponse) {}
[**product_update_media_gallery_entry**](ProductApi.md#product_update_media_gallery_entry) | **POST** /product.Product/UpdateMediaGalleryEntry | 
[**product_update_options_list**](ProductApi.md#product_update_options_list) | **POST** /product.Product/UpdateOptionsList | 
[**product_update_product**](ProductApi.md#product_update_product) | **POST** /product.Product/UpdateProduct | 
[**product_update_product_v2**](ProductApi.md#product_update_product_v2) | **POST** /product.Product/UpdateProductV2 | 


# **product_add_media_gallery_entry**
> ProductAddMediaGalleryEntryResponse product_add_media_gallery_entry(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductAddMediaGalleryEntryRequest() # ProductAddMediaGalleryEntryRequest | 

    try:
        api_response = api_instance.product_add_media_gallery_entry(body)
        print("The response of ProductApi->product_add_media_gallery_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_add_media_gallery_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAddMediaGalleryEntryRequest**](ProductAddMediaGalleryEntryRequest.md)|  | 

### Return type

[**ProductAddMediaGalleryEntryResponse**](ProductAddMediaGalleryEntryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_add_assets_entries**
> ProductBulkAddAssetsEntriesResponse product_bulk_add_assets_entries(body)

Assets endpoints

### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductBulkAddAssetsEntriesRequest() # ProductBulkAddAssetsEntriesRequest | 

    try:
        # Assets endpoints
        api_response = api_instance.product_bulk_add_assets_entries(body)
        print("The response of ProductApi->product_bulk_add_assets_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_add_assets_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkAddAssetsEntriesRequest**](ProductBulkAddAssetsEntriesRequest.md)|  | 

### Return type

[**ProductBulkAddAssetsEntriesResponse**](ProductBulkAddAssetsEntriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_create_attribute**
> EntitymanagerBulkCreateAttributeResponse product_bulk_create_attribute(body)



### Example


```python
import time
import os
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_delete_products**
> object product_bulk_delete_products(body)



### Example


```python
import time
import os
import product
from product.models.product_bulk_delete_products_request import ProductBulkDeleteProductsRequest
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
    body = product.ProductBulkDeleteProductsRequest() # ProductBulkDeleteProductsRequest | 

    try:
        api_response = api_instance.product_bulk_delete_products(body)
        print("The response of ProductApi->product_bulk_delete_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_delete_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkDeleteProductsRequest**](ProductBulkDeleteProductsRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_remove_assets_entries**
> object product_bulk_remove_assets_entries(body)



### Example


```python
import time
import os
import product
from product.models.product_bulk_remove_assets_entries_request import ProductBulkRemoveAssetsEntriesRequest
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
    body = product.ProductBulkRemoveAssetsEntriesRequest() # ProductBulkRemoveAssetsEntriesRequest | 

    try:
        api_response = api_instance.product_bulk_remove_assets_entries(body)
        print("The response of ProductApi->product_bulk_remove_assets_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_remove_assets_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkRemoveAssetsEntriesRequest**](ProductBulkRemoveAssetsEntriesRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

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



### Example


```python
import time
import os
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_update_assets_entries**
> ProductBulkUpdateAssetsEntriesResponse product_bulk_update_assets_entries(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductBulkUpdateAssetsEntriesRequest() # ProductBulkUpdateAssetsEntriesRequest | 

    try:
        api_response = api_instance.product_bulk_update_assets_entries(body)
        print("The response of ProductApi->product_bulk_update_assets_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_update_assets_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkUpdateAssetsEntriesRequest**](ProductBulkUpdateAssetsEntriesRequest.md)|  | 

### Return type

[**ProductBulkUpdateAssetsEntriesResponse**](ProductBulkUpdateAssetsEntriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_bulk_update_v2**
> ProductBulkUpdateResponseV2 product_bulk_update_v2(body)



### Example


```python
import time
import os
import product
from product.models.product_bulk_update_request_v2 import ProductBulkUpdateRequestV2
from product.models.product_bulk_update_response_v2 import ProductBulkUpdateResponseV2
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
    body = product.ProductBulkUpdateRequestV2() # ProductBulkUpdateRequestV2 | 

    try:
        api_response = api_instance.product_bulk_update_v2(body)
        print("The response of ProductApi->product_bulk_update_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_bulk_update_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBulkUpdateRequestV2**](ProductBulkUpdateRequestV2.md)|  | 

### Return type

[**ProductBulkUpdateResponseV2**](ProductBulkUpdateResponseV2.md)

### Authorization

No authorization required

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


```python
import time
import os
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create_attribute_options**
> EntitymanagerCreateAttributeOptionsResponse product_create_attribute_options(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerCreateAttributeOptionsRequest() # EntitymanagerCreateAttributeOptionsRequest | 

    try:
        api_response = api_instance.product_create_attribute_options(body)
        print("The response of ProductApi->product_create_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerCreateAttributeOptionsRequest**](EntitymanagerCreateAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerCreateAttributeOptionsResponse**](EntitymanagerCreateAttributeOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create_entity**
> EntitymanagerCreateEntityResponse product_create_entity(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerEntity() # EntitymanagerEntity | 

    try:
        api_response = api_instance.product_create_entity(body)
        print("The response of ProductApi->product_create_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerEntity**](EntitymanagerEntity.md)|  | 

### Return type

[**EntitymanagerCreateEntityResponse**](EntitymanagerCreateEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_create_options_list**
> EntitymanagerCreateOptionsListResponse product_create_options_list(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerCreateOptionsListRequest() # EntitymanagerCreateOptionsListRequest | 

    try:
        api_response = api_instance.product_create_options_list(body)
        print("The response of ProductApi->product_create_options_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_create_options_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerCreateOptionsListRequest**](EntitymanagerCreateOptionsListRequest.md)|  | 

### Return type

[**EntitymanagerCreateOptionsListResponse**](EntitymanagerCreateOptionsListResponse.md)

### Authorization

No authorization required

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


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductCreateProductRequest() # ProductCreateProductRequest | 

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
 **body** | [**ProductCreateProductRequest**](ProductCreateProductRequest.md)|  | 

### Return type

[**ProductCreateProductResponse**](ProductCreateProductResponse.md)

### Authorization

No authorization required

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


```python
import time
import os
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

No authorization required

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


```python
import time
import os
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

No authorization required

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


```python
import time
import os
import product
from product.models.entitymanager_delete_attribute_request import EntitymanagerDeleteAttributeRequest
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

No authorization required

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


```python
import time
import os
import product
from product.models.product_delete_product_request import ProductDeleteProductRequest
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

No authorization required

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


```python
import time
import os
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_attribute_option**
> EntitymanagerGetAttributeOptionResponse product_get_attribute_option(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerGetAttributeOptionRequest() # EntitymanagerGetAttributeOptionRequest | 

    try:
        api_response = api_instance.product_get_attribute_option(body)
        print("The response of ProductApi->product_get_attribute_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_attribute_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetAttributeOptionRequest**](EntitymanagerGetAttributeOptionRequest.md)|  | 

### Return type

[**EntitymanagerGetAttributeOptionResponse**](EntitymanagerGetAttributeOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_attribute_options**
> EntitymanagerGetAttributeOptionsResponse product_get_attribute_options(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerGetAttributeOptionsRequest() # EntitymanagerGetAttributeOptionsRequest | 

    try:
        api_response = api_instance.product_get_attribute_options(body)
        print("The response of ProductApi->product_get_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetAttributeOptionsRequest**](EntitymanagerGetAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerGetAttributeOptionsResponse**](EntitymanagerGetAttributeOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_entity**
> EntitymanagerEntity product_get_entity(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerEntityRequest() # EntitymanagerEntityRequest | 

    try:
        api_response = api_instance.product_get_entity(body)
        print("The response of ProductApi->product_get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerEntityRequest**](EntitymanagerEntityRequest.md)|  | 

### Return type

[**EntitymanagerEntity**](EntitymanagerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_options_list**
> EntitymanagerGetOptionsListResponse product_get_options_list(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerGetOptionsListRequest() # EntitymanagerGetOptionsListRequest | 

    try:
        api_response = api_instance.product_get_options_list(body)
        print("The response of ProductApi->product_get_options_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_options_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerGetOptionsListRequest**](EntitymanagerGetOptionsListRequest.md)|  | 

### Return type

[**EntitymanagerGetOptionsListResponse**](EntitymanagerGetOptionsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_product**
> ProductGetProductResponse product_get_product(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductGetProductRequest() # ProductGetProductRequest | 

    try:
        api_response = api_instance.product_get_product(body)
        print("The response of ProductApi->product_get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductRequest**](ProductGetProductRequest.md)|  | 

### Return type

[**ProductGetProductResponse**](ProductGetProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_product_by_code**
> ProductGetProductByCodeResponse product_get_product_by_code(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductGetProductByCodeRequest() # ProductGetProductByCodeRequest | 

    try:
        api_response = api_instance.product_get_product_by_code(body)
        print("The response of ProductApi->product_get_product_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_product_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductByCodeRequest**](ProductGetProductByCodeRequest.md)|  | 

### Return type

[**ProductGetProductByCodeResponse**](ProductGetProductByCodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_product_by_url_key**
> ProductGetProductByUrlKeyResponse product_get_product_by_url_key(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductGetProductByUrlKeyRequest() # ProductGetProductByUrlKeyRequest | 

    try:
        api_response = api_instance.product_get_product_by_url_key(body)
        print("The response of ProductApi->product_get_product_by_url_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_get_product_by_url_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductGetProductByUrlKeyRequest**](ProductGetProductByUrlKeyRequest.md)|  | 

### Return type

[**ProductGetProductByUrlKeyResponse**](ProductGetProductByUrlKeyResponse.md)

### Authorization

No authorization required

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

Attribute Groups endpoints

### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerListAttributeGroupsRequest() # EntitymanagerListAttributeGroupsRequest | 

    try:
        # Attribute Groups endpoints
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_attribute_options**
> EntitymanagerListAttributeOptionsResponse product_list_attribute_options(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerListAttributeOptionsRequest() # EntitymanagerListAttributeOptionsRequest | 

    try:
        api_response = api_instance.product_list_attribute_options(body)
        print("The response of ProductApi->product_list_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListAttributeOptionsRequest**](EntitymanagerListAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerListAttributeOptionsResponse**](EntitymanagerListAttributeOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_entities**
> EntitymanagerListEntitiesResponse product_list_entities(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerListEntitiesRequest() # EntitymanagerListEntitiesRequest | 

    try:
        api_response = api_instance.product_list_entities(body)
        print("The response of ProductApi->product_list_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListEntitiesRequest**](EntitymanagerListEntitiesRequest.md)|  | 

### Return type

[**EntitymanagerListEntitiesResponse**](EntitymanagerListEntitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_options_lists**
> EntitymanagerListOptionsListsResponse product_list_options_lists(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerListOptionsListsRequest() # EntitymanagerListOptionsListsRequest | 

    try:
        api_response = api_instance.product_list_options_lists(body)
        print("The response of ProductApi->product_list_options_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_options_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerListOptionsListsRequest**](EntitymanagerListOptionsListsRequest.md)|  | 

### Return type

[**EntitymanagerListOptionsListsResponse**](EntitymanagerListOptionsListsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_products**
> ProductListProductsResponse product_list_products(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductListProductsRequest() # ProductListProductsRequest | 

    try:
        api_response = api_instance.product_list_products(body)
        print("The response of ProductApi->product_list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListProductsRequest**](ProductListProductsRequest.md)|  | 

### Return type

[**ProductListProductsResponse**](ProductListProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_products_by_ids**
> ProductListProductsByIdsResponse product_list_products_by_ids(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductListProductsByIdsRequest() # ProductListProductsByIdsRequest | 

    try:
        api_response = api_instance.product_list_products_by_ids(body)
        print("The response of ProductApi->product_list_products_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_products_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListProductsByIdsRequest**](ProductListProductsByIdsRequest.md)|  | 

### Return type

[**ProductListProductsByIdsResponse**](ProductListProductsByIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_products_by_sku**
> ProductListProductsBySkuResponse product_list_products_by_sku(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductListProductsBySkuRequest() # ProductListProductsBySkuRequest | 

    try:
        api_response = api_instance.product_list_products_by_sku(body)
        print("The response of ProductApi->product_list_products_by_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_products_by_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListProductsBySkuRequest**](ProductListProductsBySkuRequest.md)|  | 

### Return type

[**ProductListProductsBySkuResponse**](ProductListProductsBySkuResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_variants_by_sku**
> ProductListVariantsBySkuResponse product_list_variants_by_sku(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.ProductListVariantsBySkuRequest() # ProductListVariantsBySkuRequest | 

    try:
        api_response = api_instance.product_list_variants_by_sku(body)
        print("The response of ProductApi->product_list_variants_by_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_list_variants_by_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductListVariantsBySkuRequest**](ProductListVariantsBySkuRequest.md)|  | 

### Return type

[**ProductListVariantsBySkuResponse**](ProductListVariantsBySkuResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_remove_media_gallery_entry**
> object product_remove_media_gallery_entry(body)



### Example


```python
import time
import os
import product
from product.models.product_remove_media_gallery_entry_request import ProductRemoveMediaGalleryEntryRequest
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
    body = product.ProductRemoveMediaGalleryEntryRequest() # ProductRemoveMediaGalleryEntryRequest | 

    try:
        api_response = api_instance.product_remove_media_gallery_entry(body)
        print("The response of ProductApi->product_remove_media_gallery_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_remove_media_gallery_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductRemoveMediaGalleryEntryRequest**](ProductRemoveMediaGalleryEntryRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

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


```python
import time
import os
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

No authorization required

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


```python
import time
import os
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_attribute_options**
> EntitymanagerUpdateAttributeOptionsResponse product_update_attribute_options(body)

rpc GetAttributeOptionByCode (product.entitymanager.GetAttributeOptionByCodeRequest) returns (product.entitymanager.GetAttributeOptionByCodeResponse) {}

### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerUpdateAttributeOptionsRequest() # EntitymanagerUpdateAttributeOptionsRequest | 

    try:
        # rpc GetAttributeOptionByCode (product.entitymanager.GetAttributeOptionByCodeRequest) returns (product.entitymanager.GetAttributeOptionByCodeResponse) {}
        api_response = api_instance.product_update_attribute_options(body)
        print("The response of ProductApi->product_update_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerUpdateAttributeOptionsRequest**](EntitymanagerUpdateAttributeOptionsRequest.md)|  | 

### Return type

[**EntitymanagerUpdateAttributeOptionsResponse**](EntitymanagerUpdateAttributeOptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_media_gallery_entry**
> object product_update_media_gallery_entry(body)



### Example


```python
import time
import os
import product
from product.models.product_update_media_gallery_entry_request import ProductUpdateMediaGalleryEntryRequest
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
    body = product.ProductUpdateMediaGalleryEntryRequest() # ProductUpdateMediaGalleryEntryRequest | 

    try:
        api_response = api_instance.product_update_media_gallery_entry(body)
        print("The response of ProductApi->product_update_media_gallery_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_media_gallery_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateMediaGalleryEntryRequest**](ProductUpdateMediaGalleryEntryRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update_options_list**
> EntitymanagerUpdateOptionsListResponse product_update_options_list(body)



### Example


```python
import time
import os
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


# Enter a context with an instance of the API client
with product.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product.ProductApi(api_client)
    body = product.EntitymanagerUpdateOptionsListRequest() # EntitymanagerUpdateOptionsListRequest | 

    try:
        api_response = api_instance.product_update_options_list(body)
        print("The response of ProductApi->product_update_options_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->product_update_options_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitymanagerUpdateOptionsListRequest**](EntitymanagerUpdateOptionsListRequest.md)|  | 

### Return type

[**EntitymanagerUpdateOptionsListResponse**](EntitymanagerUpdateOptionsListResponse.md)

### Authorization

No authorization required

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


```python
import time
import os
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

No authorization required

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


```python
import time
import os
import product
from product.models.product_update_product_request_v2 import ProductUpdateProductRequestV2
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

