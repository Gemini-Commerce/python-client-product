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

from product.models.product_create_product_request import ProductCreateProductRequest

class TestProductCreateProductRequest(unittest.TestCase):
    """ProductCreateProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductCreateProductRequest:
        """Test ProductCreateProductRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductCreateProductRequest`
        """
        model = ProductCreateProductRequest()
        if include_optional:
            return ProductCreateProductRequest(
                tenant_id = '',
                entity_type = '',
                entity_code = '',
                code = '',
                is_configurable = True,
                variant_attributes = [
                    ''
                    ],
                is_virtual = True,
                is_giftcard = True,
                has_configurator = True,
                url_key = product.models.product_localized_text.productLocalizedText(
                    value = {
                        'key' : ''
                        }, ),
                max_saleable_quantity = 56,
                media_variant_attributes = [
                    ''
                    ],
                attributes = {
                    'key' : {
                        'key' : None
                        }
                    },
                variants = {
                    'key' : product.models.product_product_variant.productProductVariant(
                        id = '', 
                        grn = '', 
                        max_saleable_quantity = 56, 
                        attributes = {
                            'key' : {
                                'key' : None
                                }
                            }, )
                    }
            )
        else:
            return ProductCreateProductRequest(
        )
        """

    def testProductCreateProductRequest(self):
        """Test ProductCreateProductRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()