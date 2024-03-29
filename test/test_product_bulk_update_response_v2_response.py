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

from product.models.product_bulk_update_response_v2_response import ProductBulkUpdateResponseV2Response

class TestProductBulkUpdateResponseV2Response(unittest.TestCase):
    """ProductBulkUpdateResponseV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductBulkUpdateResponseV2Response:
        """Test ProductBulkUpdateResponseV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductBulkUpdateResponseV2Response`
        """
        model = ProductBulkUpdateResponseV2Response()
        if include_optional:
            return ProductBulkUpdateResponseV2Response(
                product_id = '',
                attributes = {
                    'key' : {
                        'key' : None
                        }
                    }
            )
        else:
            return ProductBulkUpdateResponseV2Response(
        )
        """

    def testProductBulkUpdateResponseV2Response(self):
        """Test ProductBulkUpdateResponseV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
