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

from product.models.product_attribute_response_error import ProductAttributeResponseError

class TestProductAttributeResponseError(unittest.TestCase):
    """ProductAttributeResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductAttributeResponseError:
        """Test ProductAttributeResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductAttributeResponseError`
        """
        model = ProductAttributeResponseError()
        if include_optional:
            return ProductAttributeResponseError(
                code = '',
                message = '',
                attribute_code = ''
            )
        else:
            return ProductAttributeResponseError(
        )
        """

    def testProductAttributeResponseError(self):
        """Test ProductAttributeResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()