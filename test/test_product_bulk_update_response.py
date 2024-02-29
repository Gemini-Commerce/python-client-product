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

from product.models.product_bulk_update_response import ProductBulkUpdateResponse

class TestProductBulkUpdateResponse(unittest.TestCase):
    """ProductBulkUpdateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductBulkUpdateResponse:
        """Test ProductBulkUpdateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductBulkUpdateResponse`
        """
        model = ProductBulkUpdateResponse()
        if include_optional:
            return ProductBulkUpdateResponse(
                product_response = [
                    product.models.product_bulk_update_response_response.productBulkUpdateResponseResponse(
                        product_id = '', 
                        success = True, 
                        attributes = {
                            'key' : {
                                'key' : None
                                }
                            }, )
                    ]
            )
        else:
            return ProductBulkUpdateResponse(
        )
        """

    def testProductBulkUpdateResponse(self):
        """Test ProductBulkUpdateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
