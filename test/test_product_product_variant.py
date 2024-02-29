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

from product.models.product_product_variant import ProductProductVariant

class TestProductProductVariant(unittest.TestCase):
    """ProductProductVariant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductProductVariant:
        """Test ProductProductVariant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductProductVariant`
        """
        model = ProductProductVariant()
        if include_optional:
            return ProductProductVariant(
                id = '',
                grn = '',
                max_saleable_quantity = 56,
                attributes = {
                    'key' : {
                        'key' : None
                        }
                    }
            )
        else:
            return ProductProductVariant(
        )
        """

    def testProductProductVariant(self):
        """Test ProductProductVariant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
