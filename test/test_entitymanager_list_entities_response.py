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

from product.models.entitymanager_list_entities_response import EntitymanagerListEntitiesResponse

class TestEntitymanagerListEntitiesResponse(unittest.TestCase):
    """EntitymanagerListEntitiesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitymanagerListEntitiesResponse:
        """Test EntitymanagerListEntitiesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitymanagerListEntitiesResponse`
        """
        model = EntitymanagerListEntitiesResponse()
        if include_optional:
            return EntitymanagerListEntitiesResponse(
                entities = [
                    product.models.entitymanager_entity.entitymanagerEntity(
                        tenant_id = '', 
                        id = '', 
                        type = '', 
                        code = '', 
                        parent_code = '', 
                        label = '', 
                        relationships = [
                            ''
                            ], 
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
                            ], )
                    ],
                next_page = 56
            )
        else:
            return EntitymanagerListEntitiesResponse(
        )
        """

    def testEntitymanagerListEntitiesResponse(self):
        """Test EntitymanagerListEntitiesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
