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

from product.models.entitymanager_bulk_create_attribute_request import EntitymanagerBulkCreateAttributeRequest

class TestEntitymanagerBulkCreateAttributeRequest(unittest.TestCase):
    """EntitymanagerBulkCreateAttributeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitymanagerBulkCreateAttributeRequest:
        """Test EntitymanagerBulkCreateAttributeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitymanagerBulkCreateAttributeRequest`
        """
        model = EntitymanagerBulkCreateAttributeRequest()
        if include_optional:
            return EntitymanagerBulkCreateAttributeRequest(
                tenant_id = '',
                entity_data = product.models.entitymanager_entity_identifier.entitymanagerEntityIdentifier(
                    type = '', 
                    code = '', ),
                entity_id = '',
                attributes = [
                    product.models.entitymanager_attribute.entitymanagerAttribute(
                        entity_id = '', 
                        code = '', 
                        label = '', 
                        type = 'TEXT', 
                        option_list = '', 
                        entity = '', 
                        default = '', 
                        is_required = True, 
                        is_system = True, 
                        is_repeated = True, 
                        sort = 56, 
                        group_code = '', 
                        title = {
                            'key' : ''
                            }, 
                        render_as = 'DEFAULT', )
                    ]
            )
        else:
            return EntitymanagerBulkCreateAttributeRequest(
        )
        """

    def testEntitymanagerBulkCreateAttributeRequest(self):
        """Test EntitymanagerBulkCreateAttributeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()