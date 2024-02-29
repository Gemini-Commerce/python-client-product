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

from product.models.entitymanager_update_options_list_request import EntitymanagerUpdateOptionsListRequest

class TestEntitymanagerUpdateOptionsListRequest(unittest.TestCase):
    """EntitymanagerUpdateOptionsListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitymanagerUpdateOptionsListRequest:
        """Test EntitymanagerUpdateOptionsListRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitymanagerUpdateOptionsListRequest`
        """
        model = EntitymanagerUpdateOptionsListRequest()
        if include_optional:
            return EntitymanagerUpdateOptionsListRequest(
                tenant_id = '',
                option_list = product.models.entitymanager_options_list.entitymanagerOptionsList(
                    code = '', 
                    name = '', )
            )
        else:
            return EntitymanagerUpdateOptionsListRequest(
        )
        """

    def testEntitymanagerUpdateOptionsListRequest(self):
        """Test EntitymanagerUpdateOptionsListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
