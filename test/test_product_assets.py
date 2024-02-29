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

from product.models.product_assets import ProductAssets

class TestProductAssets(unittest.TestCase):
    """ProductAssets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductAssets:
        """Test ProductAssets
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductAssets`
        """
        model = ProductAssets()
        if include_optional:
            return ProductAssets(
                entries = [
                    product.models.product_assets_entry.productAssetsEntry(
                        id = '', 
                        asset_grn = '', 
                        localized_asset_grn = product.models.product_localized_asset.productLocalizedAsset(
                            value = {
                                'key' : ''
                                }, ), 
                        locales = [
                            ''
                            ], 
                        position = 56, 
                        metadata = [
                            product.models.product_assets_entry_metadata.productAssetsEntryMetadata(
                                roles = [
                                    ''
                                    ], 
                                alt = product.models.product_localized_text.productLocalizedText(), )
                            ], )
                    ]
            )
        else:
            return ProductAssets(
        )
        """

    def testProductAssets(self):
        """Test ProductAssets"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
