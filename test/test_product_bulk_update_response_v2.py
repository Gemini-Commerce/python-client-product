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

from product.models.product_bulk_update_response_v2 import ProductBulkUpdateResponseV2

class TestProductBulkUpdateResponseV2(unittest.TestCase):
    """ProductBulkUpdateResponseV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductBulkUpdateResponseV2:
        """Test ProductBulkUpdateResponseV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductBulkUpdateResponseV2`
        """
        model = ProductBulkUpdateResponseV2()
        if include_optional:
            return ProductBulkUpdateResponseV2(
                product_response = [
                    product.models.product_bulk_update_response_v2_response.productBulkUpdateResponseV2Response(
                        product_id = '', 
                        attributes = {
                            'key' : {
                                'key' : None
                                }
                            }, )
                    ]
            )
        else:
            return ProductBulkUpdateResponseV2(
        )
        """

    def testProductBulkUpdateResponseV2(self):
        """Test ProductBulkUpdateResponseV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
