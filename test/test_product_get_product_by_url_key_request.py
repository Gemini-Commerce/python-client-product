# coding: utf-8

"""
    Product Service

    API for managing products

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from product.models.product_get_product_by_url_key_request import ProductGetProductByUrlKeyRequest

class TestProductGetProductByUrlKeyRequest(unittest.TestCase):
    """ProductGetProductByUrlKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductGetProductByUrlKeyRequest:
        """Test ProductGetProductByUrlKeyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductGetProductByUrlKeyRequest`
        """
        model = ProductGetProductByUrlKeyRequest()
        if include_optional:
            return ProductGetProductByUrlKeyRequest(
                tenant_id = '',
                url_key = '',
                locale = ''
            )
        else:
            return ProductGetProductByUrlKeyRequest(
        )
        """

    def testProductGetProductByUrlKeyRequest(self):
        """Test ProductGetProductByUrlKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
