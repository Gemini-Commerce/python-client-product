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

from product.models.product_media_gallery_entry_metadata import ProductMediaGalleryEntryMetadata

class TestProductMediaGalleryEntryMetadata(unittest.TestCase):
    """ProductMediaGalleryEntryMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductMediaGalleryEntryMetadata:
        """Test ProductMediaGalleryEntryMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductMediaGalleryEntryMetadata`
        """
        model = ProductMediaGalleryEntryMetadata()
        if include_optional:
            return ProductMediaGalleryEntryMetadata(
                roles = [
                    ''
                    ],
                alt = product.models.product_localized_text.productLocalizedText(
                    value = {
                        'key' : ''
                        }, )
            )
        else:
            return ProductMediaGalleryEntryMetadata(
        )
        """

    def testProductMediaGalleryEntryMetadata(self):
        """Test ProductMediaGalleryEntryMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
