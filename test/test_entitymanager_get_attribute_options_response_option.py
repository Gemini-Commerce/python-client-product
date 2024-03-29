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

from product.models.entitymanager_get_attribute_options_response_option import EntitymanagerGetAttributeOptionsResponseOption

class TestEntitymanagerGetAttributeOptionsResponseOption(unittest.TestCase):
    """EntitymanagerGetAttributeOptionsResponseOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitymanagerGetAttributeOptionsResponseOption:
        """Test EntitymanagerGetAttributeOptionsResponseOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitymanagerGetAttributeOptionsResponseOption`
        """
        model = EntitymanagerGetAttributeOptionsResponseOption()
        if include_optional:
            return EntitymanagerGetAttributeOptionsResponseOption(
                list_code = '',
                option = product.models.entitymanager_attribute_option.entitymanagerAttributeOption(
                    sort = 56, 
                    id = '', 
                    code = '', 
                    value = product.models.productentitymanager_localized_text.productentitymanagerLocalizedText(), 
                    swatches = [
                        product.models.entitymanager_attribute_option_swatch.entitymanagerAttributeOptionSwatch(
                            grn = '', 
                            hex = '', )
                        ], )
            )
        else:
            return EntitymanagerGetAttributeOptionsResponseOption(
        )
        """

    def testEntitymanagerGetAttributeOptionsResponseOption(self):
        """Test EntitymanagerGetAttributeOptionsResponseOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
