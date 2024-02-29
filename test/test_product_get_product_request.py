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

from product.models.product_get_product_request import ProductGetProductRequest

class TestProductGetProductRequest(unittest.TestCase):
    """ProductGetProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductGetProductRequest:
        """Test ProductGetProductRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductGetProductRequest`
        """
        model = ProductGetProductRequest()
        if include_optional:
            return ProductGetProductRequest(
                tenant_id = '',
                id = ''
            )
        else:
            return ProductGetProductRequest(
        )
        """

    def testProductGetProductRequest(self):
        """Test ProductGetProductRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
