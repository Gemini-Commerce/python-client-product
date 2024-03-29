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

from product.api.product_api import ProductApi


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductApi()

    def tearDown(self) -> None:
        pass

    def test_product_add_media_gallery_entry(self) -> None:
        """Test case for product_add_media_gallery_entry

        """
        pass

    def test_product_bulk_add_assets_entries(self) -> None:
        """Test case for product_bulk_add_assets_entries

        Assets endpoints
        """
        pass

    def test_product_bulk_create_attribute(self) -> None:
        """Test case for product_bulk_create_attribute

        """
        pass

    def test_product_bulk_delete_products(self) -> None:
        """Test case for product_bulk_delete_products

        """
        pass

    def test_product_bulk_remove_assets_entries(self) -> None:
        """Test case for product_bulk_remove_assets_entries

        """
        pass

    def test_product_bulk_update(self) -> None:
        """Test case for product_bulk_update

        """
        pass

    def test_product_bulk_update_assets_entries(self) -> None:
        """Test case for product_bulk_update_assets_entries

        """
        pass

    def test_product_bulk_update_v2(self) -> None:
        """Test case for product_bulk_update_v2

        """
        pass

    def test_product_create_attribute_group(self) -> None:
        """Test case for product_create_attribute_group

        """
        pass

    def test_product_create_attribute_options(self) -> None:
        """Test case for product_create_attribute_options

        """
        pass

    def test_product_create_entity(self) -> None:
        """Test case for product_create_entity

        """
        pass

    def test_product_create_options_list(self) -> None:
        """Test case for product_create_options_list

        """
        pass

    def test_product_create_product(self) -> None:
        """Test case for product_create_product

        """
        pass

    def test_product_create_product_v2(self) -> None:
        """Test case for product_create_product_v2

        """
        pass

    def test_product_delete(self) -> None:
        """Test case for product_delete

        """
        pass

    def test_product_delete_attribute(self) -> None:
        """Test case for product_delete_attribute

        """
        pass

    def test_product_delete_product(self) -> None:
        """Test case for product_delete_product

        """
        pass

    def test_product_get_attribute_group(self) -> None:
        """Test case for product_get_attribute_group

        """
        pass

    def test_product_get_attribute_option(self) -> None:
        """Test case for product_get_attribute_option

        """
        pass

    def test_product_get_attribute_options(self) -> None:
        """Test case for product_get_attribute_options

        """
        pass

    def test_product_get_entity(self) -> None:
        """Test case for product_get_entity

        """
        pass

    def test_product_get_options_list(self) -> None:
        """Test case for product_get_options_list

        """
        pass

    def test_product_get_product(self) -> None:
        """Test case for product_get_product

        """
        pass

    def test_product_get_product_by_code(self) -> None:
        """Test case for product_get_product_by_code

        """
        pass

    def test_product_get_product_by_url_key(self) -> None:
        """Test case for product_get_product_by_url_key

        """
        pass

    def test_product_list_attribute_groups(self) -> None:
        """Test case for product_list_attribute_groups

        Attribute Groups endpoints
        """
        pass

    def test_product_list_attribute_options(self) -> None:
        """Test case for product_list_attribute_options

        """
        pass

    def test_product_list_entities(self) -> None:
        """Test case for product_list_entities

        """
        pass

    def test_product_list_options_lists(self) -> None:
        """Test case for product_list_options_lists

        """
        pass

    def test_product_list_products(self) -> None:
        """Test case for product_list_products

        """
        pass

    def test_product_list_products_by_ids(self) -> None:
        """Test case for product_list_products_by_ids

        """
        pass

    def test_product_list_products_by_sku(self) -> None:
        """Test case for product_list_products_by_sku

        """
        pass

    def test_product_list_variants_by_sku(self) -> None:
        """Test case for product_list_variants_by_sku

        """
        pass

    def test_product_remove_media_gallery_entry(self) -> None:
        """Test case for product_remove_media_gallery_entry

        """
        pass

    def test_product_update_attribute(self) -> None:
        """Test case for product_update_attribute

        """
        pass

    def test_product_update_attribute_group(self) -> None:
        """Test case for product_update_attribute_group

        """
        pass

    def test_product_update_attribute_options(self) -> None:
        """Test case for product_update_attribute_options

        rpc GetAttributeOptionByCode (product.entitymanager.GetAttributeOptionByCodeRequest) returns (product.entitymanager.GetAttributeOptionByCodeResponse) {}
        """
        pass

    def test_product_update_media_gallery_entry(self) -> None:
        """Test case for product_update_media_gallery_entry

        """
        pass

    def test_product_update_options_list(self) -> None:
        """Test case for product_update_options_list

        """
        pass

    def test_product_update_product(self) -> None:
        """Test case for product_update_product

        """
        pass

    def test_product_update_product_v2(self) -> None:
        """Test case for product_update_product_v2

        """
        pass


if __name__ == '__main__':
    unittest.main()
