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

from product.models.product_create_product_response_v2 import ProductCreateProductResponseV2

class TestProductCreateProductResponseV2(unittest.TestCase):
    """ProductCreateProductResponseV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductCreateProductResponseV2:
        """Test ProductCreateProductResponseV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductCreateProductResponseV2`
        """
        model = ProductCreateProductResponseV2()
        if include_optional:
            return ProductCreateProductResponseV2(
                id = ''
            )
        else:
            return ProductCreateProductResponseV2(
        )
        """

    def testProductCreateProductResponseV2(self):
        """Test ProductCreateProductResponseV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
