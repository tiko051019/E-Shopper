from django.test import TestCase
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class MainTestCase(TestCase):
    def setUp(self):
        self.main = MainInfo.objects.create(
            name = 'tiko',
            phone = '+37444927999',
            email = 'abrahamyantiko65@gmail.com',
            facebook = 'https://www.youtube.com/',
            twitter = 'https://www.youtube.com/',
            linkedin = 'https://www.youtube.com/',
            dribbble = 'https://www.youtube.com/',
            googleplus = 'https://www.youtube.com/',
            img = SimpleUploadedFile(
                'myimg',content=b'\x01\x02\x03',content_type='image/jpeg'
            ),
            info = 'sacvhjadsvcb',
            owner = 'dcbdsj',
            add = SimpleUploadedFile(
                'myimg',content=b'\x01\x02\x03',content_type='image/jpeg'
            ),
            map_img = SimpleUploadedFile(
                'myimg',content=b'\x01\x02\x03',content_type='image/jpeg'
            ),
            adress = 'jsacbhsck12111'
            ) 

    def test_main_info_creation(self):
        self.assertEqual(self.main.name, 'tiko')
        self.assertEqual(self.main.phone, '+37444927999')
        self.assertEqual(self.main.email, 'abrahamyantiko65@gmail.com')
        self.assertEqual(self.main.facebook, 'https://www.youtube.com/')
        self.assertEqual(self.main.twitter, 'https://www.youtube.com/')
        self.assertEqual(self.main.linkedin, 'https://www.youtube.com/')
        self.assertEqual(self.main.dribbble, 'https://www.youtube.com/')
        self.assertEqual(self.main.googleplus, 'https://www.youtube.com/')
        self.assertEqual(self.main.info, 'sacvhjadsvcb')
        self.assertEqual(self.main.owner, 'dcbdsj')
        self.assertEqual(self.main.adress, 'jsacbhsck12111')
        self.assertIsNotNone(self.main.img)
        self.assertIsNotNone(self.main.add)
        self.assertIsNotNone(self.main.map_img)



class CarouselTestCase(TestCase):

    def setUp(self):
        self.carousel = Carousel.objects.create(
            text1='This is the first text.',
            text2='This is the second text.',
            img=SimpleUploadedFile(
                'girls_image.jpg', content=b'\x01\x02\x03', content_type='image/jpeg'
            ),
            disc_img=SimpleUploadedFile(
                'discount_image.jpg', content=b'\x01\x02\x03', content_type='image/jpeg'
            )
        )

    def test_carousel_creation(self):
        # Checking if the fields are set correctly
        self.assertEqual(self.carousel.text1, 'This is the first text.')
        self.assertEqual(self.carousel.text2, 'This is the second text.')

        # Checking if the images are uploaded correctly
        self.assertIsNotNone(self.carousel.img)
        self.assertIsNotNone(self.carousel.disc_img)


class CategoryTestCase(TestCase):

    def setUp(self):
        # Create Category objects with different values for sub_bool
        self.category1 = Category.objects.create(
            name='Technology',
            sub_bool=True
        )
        self.category2 = Category.objects.create(
            name='Health',
            sub_bool=False
        )
        # Create SubCategory objects linked to Category
        self.subcat_test_model = SubCategory.objects.create(
            key=self.category1,
            subname='Electronics'
        )
        # Create ItemsName objects
        self.itemsname_test_model = ItemsName.objects.create(
            name='Laptop'
        )

    def test_category_creation(self):
        # Check if Category objects are created with correct values
        self.assertEqual(self.category1.name, 'Technology')
        self.assertEqual(self.category1.sub_bool, True)
        self.assertEqual(self.category2.name, 'Health')
        self.assertEqual(self.category2.sub_bool, False)

    def test_subcategory_creation(self):
        # Check if SubCategory is correctly linked to Category
        self.assertEqual(self.subcat_test_model.key, self.category1)
        self.assertEqual(self.subcat_test_model.subname, 'Electronics')

    def test_itemsname_creation(self):
        # Check if ItemsName is correctly created
        self.assertEqual(self.itemsname_test_model.name, 'Laptop')

    def test_subcategory_category_relationship(self):
        # Ensure that the SubCategory is linked to the correct Category
        self.assertEqual(self.subcat_test_model.key.name, 'Technology')
        self.assertEqual(self.subcat_test_model.key.sub_bool, True)

    def test_itemsname_subcategory_relationship(self):
        # Ensure that ItemsName is correctly created and related
        self.assertEqual(self.itemsname_test_model.name, 'Laptop')

class ProductsTestCase(TestCase):

    def setUp(self):
        # Create an image file to use for the test
        self.image_file = SimpleUploadedFile(
            'test_image.jpg', content=b'\x01\x02\x03', content_type='image/jpeg'
        )
        # Create the Products instance
        self.product = Products.objects.create(
            add=self.image_file
        )

class ItemsDetailsTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Technology', sub_bool=True)
        self.subcategory = SubCategory.objects.create(key=self.category, subname='Electronics')
        self.itemsname = ItemsName.objects.create(name='Laptop')

        # Create Items instance for foreign key in ItemsDetails
        self.item = Items.objects.create(
            key1=self.category,
            key2=self.subcategory,
            key3=self.itemsname,
            price=1000,
            info='High quality laptop',
            brand='Dell',
            reccomend_bool=True,
            discount=10,
            disc_icon=SimpleUploadedFile(
            'test_image.jpg', content=b'\x01\x02\x03', content_type='image/jpeg'
        )
        )
        # Create ItemsDetails instance
        self.items_details = ItemsDetails.objects.create(
            key=self.item,
            moreinfo='This is a high-performance laptop suitable for all tasks.',
            availability=True,
            condition=True,
        )

    def test_items_details_creation(self):
        # Test if ItemsDetails object is created with correct values
        self.assertEqual(self.items_details.moreinfo, 'This is a high-performance laptop suitable for all tasks.')
        self.assertEqual(self.items_details.availability, True)
        self.assertEqual(self.items_details.condition, True)

    def test_items_details_key_relationship(self):
        # Test if the foreign key (key) points to the correct Items object
        self.assertEqual(self.items_details.key, self.item)

    def test_items_details_availability(self):
        # Test if the availability field is correctly set
        self.assertTrue(self.items_details.availability)

    def test_items_details_condition(self):
        # Test if the condition field is correctly set
        self.assertTrue(self.items_details.condition)

class ItemsImagesTestCase(TestCase):

    def setUp(self):
        # Create Category, SubCategory, and ItemsName instances for foreign key relationships
        self.category = Category.objects.create(name='Technology', sub_bool=True)
        self.subcategory = SubCategory.objects.create(key=self.category, subname='Electronics')
        self.itemsname = ItemsName.objects.create(name='Laptop')

        # Create Items instance for foreign key in ItemsImages
        self.item = Items.objects.create(
            key1=self.category,
            key2=self.subcategory,
            key3=self.itemsname,
            price=1000,
            info='High quality laptop',
            brand='Dell',
            reccomend_bool=True,
            discount=10,
            disc_icon=None
        )

        # Create an image for the img field
        self.image_file = SimpleUploadedFile(
            'carousel_image.jpg', content=b'\x01\x02\x03', content_type='image/jpeg'
        )

        # Create ItemsImages instance
        self.items_image = ItemsImages.objects.create(
            key=self.item,
        )

    def test_items_images_creation(self):
        # Test if ItemsImages object is created with the correct image
        self.assertEqual(self.items_image.key, self.item)


class GalleryTestCase(TestCase):

    def setUp(self):
        # Create an image file for testing the img field
        self.image_file = SimpleUploadedFile(
            'gallery_image.jpg', content=b'\x01\x02\x03', content_type='image/jpeg'
        )
        # Create a Gallery instance
        self.gallery_item = Gallery.objects.create(
            img=self.image_file,
            desc='This is a sample gallery image.',
            date=(2025,1,1)
        )

    def test_gallery_creation(self):
        # Test if Gallery object is created correctly with the given fields
        self.assertEqual(self.gallery_item.desc, 'This is a sample gallery image.')
        self.assertEqual(self.gallery_item.date, (2025,1,1))


class ContactMessageTestCase(TestCase):

    def setUp(self):
        # Create a ContactMessage instance
        self.contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            subject='Inquiry about product',
            message='I am interested in learning more about your product.'
        )

    def test_contact_message_creation(self):
        # Test if ContactMessage object is created with correct values
        self.assertEqual(self.contact_message.name, 'John Doe')
        self.assertEqual(self.contact_message.email, 'johndoe@example.com')
        self.assertEqual(self.contact_message.subject, 'Inquiry about product')
        self.assertEqual(self.contact_message.message, 'I am interested in learning more about your product.')


class ReviewMessageTestCase(TestCase):

    def setUp(self):
        # Create Category, SubCategory, and ItemsName instances for foreign key relationships
        self.category = Category.objects.create(name='Technology', sub_bool=True)
        self.subcategory = SubCategory.objects.create(key=self.category, subname='Electronics')
        self.itemsname = ItemsName.objects.create(name='Laptop')

        # Create Items instance for foreign key in ReviewMessage
        self.item = Items.objects.create(
            key1=self.category,
            key2=self.subcategory,
            key3=self.itemsname,
            price=1000,
            info='High quality laptop',
            brand='Dell',
            reccomend_bool=True,
            discount=10,
        )

        # Create ReviewMessage instance
        self.review_message = ReviewMessage.objects.create(
            key=self.item,
            name='John Doe',
            email='johndoe@example.com',
            message='Great product, highly recommend!',
            rating=5,
            review_date=(2025,1,1),
        )

    def test_review_message_creation(self):
        # Test if ReviewMessage object is created correctly with the provided values
        self.assertEqual(self.review_message.name, 'John Doe')
        self.assertEqual(self.review_message.email, 'johndoe@example.com')
        self.assertEqual(self.review_message.message, 'Great product, highly recommend!')
        self.assertEqual(self.review_message.rating, 5)

    def test_review_message_key_relationship(self):
        # Test if the foreign key (key) correctly points to the related Items object
        self.assertEqual(self.review_message.key, self.item)

    def test_review_message_rating_choices(self):
        # Test if the rating is set correctly within the defined choices
        self.assertIn(self.review_message.rating, [1, 2, 3, 4, 5])


class UserForTestCase(TestCase):

    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(
            username='johndoe', 
            password='password123'
        )
        
        # Create UserFor instance with a verification code
        self.user_for = UserFor.objects.create(
            key=self.user,
            ver_code=123456
        )

    def test_user_for_creation(self):
        # Test if UserFor object is created with correct values
        self.assertEqual(self.user_for.key, self.user)
        self.assertEqual(self.user_for.ver_code, 123456)

class TotalPaymentTestCase(TestCase):

    def setUp(self):
        # Create a Total_payment instance with sample values for Eco_Tax and Shipping_Cost
        self.total_payment = Total_payment.objects.create(
            Eco_Tax=50,
            Shipping_Cost=30
        )

    def test_total_payment_creation(self):
        # Test if Total_payment object is created with correct values
        self.assertEqual(self.total_payment.Eco_Tax, 50)
        self.assertEqual(self.total_payment.Shipping_Cost, 30)
