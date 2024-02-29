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

from product.models.product_localized_asset import ProductLocalizedAsset

class TestProductLocalizedAsset(unittest.TestCase):
    """ProductLocalizedAsset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductLocalizedAsset:
        """Test ProductLocalizedAsset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductLocalizedAsset`
        """
        model = ProductLocalizedAsset()
        if include_optional:
            return ProductLocalizedAsset(
                value = {
                    'key' : ''
                    }
            )
        else:
            return ProductLocalizedAsset(
        )
        """

    def testProductLocalizedAsset(self):
        """Test ProductLocalizedAsset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
