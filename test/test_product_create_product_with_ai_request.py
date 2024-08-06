# coding: utf-8

"""
    Product Service

    Introducing our revolutionary Product Management Service! Designed to streamline your product inventory and elevate customer experiences, our cutting-edge protobuf service is a game-changer in the world of efficient product management.  With our service, you can effortlessly create new products, allowing you to quickly bring your ideas to life and expand your catalog. Retrieve product information in a snap, providing accurate and personalized details to your customers based on their specific needs and preferences.  Stay ahead of the competition by easily updating product information, ensuring your catalog is always up-to-date and optimized. Seamlessly remove products from your inventory when needed, maintaining a clean and relevant product selection.  Enhance the visual appeal of your products with our advanced media gallery functionalities. Effortlessly add and update captivating images and videos to showcase your products in the best possible light, engaging your customers and driving conversions.  Personalization is key in today's market, and our service enables you to offer unique options to your customers. Easily create and manage lists of customizable options for your products, providing flexibility and tailoring to individual preferences.  Attributes play a vital role in defining products, and our service empowers you to effectively manage them. From bulk attribute creation to listing and retrieving attribute options, our service ensures your product information is rich and comprehensive.  Our service extends its capabilities to entity management, allowing you to effortlessly handle different entities and create customized options lists associated with them. This provides further flexibility and customization options for your product offerings.  When it comes to bulk updates, our service has you covered. Effortlessly update multiple products simultaneously, saving you time and streamlining your operations.  Finding specific products and variants is a breeze with our service. Quickly locate products based on their unique stock keeping unit (SKU) values, ensuring efficient inventory management and smooth order fulfillment.  Experience a new level of efficiency and productivity with our Product Management Service. Unlock the full potential of streamlined product management and empower your business to thrive in today's competitive market. Try our service today and elevate your product management to new heights!

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from product.models.product_create_product_with_ai_request import ProductCreateProductWithAIRequest

class TestProductCreateProductWithAIRequest(unittest.TestCase):
    """ProductCreateProductWithAIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductCreateProductWithAIRequest:
        """Test ProductCreateProductWithAIRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductCreateProductWithAIRequest`
        """
        model = ProductCreateProductWithAIRequest()
        if include_optional:
            return ProductCreateProductWithAIRequest(
                tenant_id = '',
                product = product.models.product_create_product_request_v2.productCreateProductRequestV2(
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
                    attributes = {
                        'key' : {
                            'key' : None
                            }
                        }, 
                    variants = {
                        'key' : product.models.product_product_variant.productProductVariant(
                            id = '', 
                            grn = '', 
                            max_saleable_quantity = 56, )
                        }, 
                    media_variant_attributes = [
                        ''
                        ], ),
                locale = '',
                product_brand = '',
                product_code = '',
                product_name = '',
                skip_review = True,
                attributes_to_enrich = [
                    product.models.product_attribute_to_enrich.productAttributeToEnrich(
                        code = '', 
                        type = 'ATTRIBUTE_TO_ENRICH_TYPE_UNKNOWN', 
                        can_create_value = True, )
                    ]
            )
        else:
            return ProductCreateProductWithAIRequest(
        )
        """

    def testProductCreateProductWithAIRequest(self):
        """Test ProductCreateProductWithAIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
