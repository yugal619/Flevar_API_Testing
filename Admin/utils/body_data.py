
class body_data:

    def get_save_coupon(self):
        save_coupon = {
            "coupon_name": "Diwali special",
            "coupon_code": self.fake.bothify(text='Coupon: ????-########', letters='ABCDE'),
            "coupon_type": 1,
            "coupon_value": 10,
            "min_cart_value": "100",
            "max_discount": "100",
            "start_date": "2020-02-04",
            "end_date": "2022-02-05",
            "location_id": 2
            }
        return save_coupon

    def get_register_user_data(self):
        register_user_data = {
            "name": self.fake.bothify(text='flevar: ????-########', letters='ABCDE'),
            "email": self.fake.email(),
            "password": self.fake.password(),
        }
        return register_user_data

    def get_save_product(self):
        save_product = {
            "name": self.fake.bothify(text='Product: ????-########'),
            "description": "Product1",
            "model": "Model",
            "rate": 5,
            "category_id": 1,
            "sub_category_id": 1,
            "cpt": 100,
            "mrp": 110,
            "short_description": "THis is short_description",
            "meta_title": "THis is meta_title",
            "meta_description": "",
            "meta_keyword": "",
            "is_best_seller": 1,
            "product_images": [{
                "id": "",
                "file": ""
            }],
            "location_ids": [1, 2, 3]
        }
        return save_product

    def get_user_update_data(self):
        update_user_data = {
                            "first_name":"Ayuhs",
                            "middle_name":"Kumar",
                            "last_name":"Agrawal",
                            "email": self.fake.email(),
                            "mobile":7828689898,
                            "password":"flevar@123",
                            "is_active":1,
                            "organization_location_id":1,
                            "designation_id":1,
                            "address":"XYZ",
                            "country_id":1,
                            "state_id":1,
                            "district_id":1,
                            "city_id":1,
                            "postal":1
                        }
        return update_user_data

    def get_save_product_category(self):
        save_product_category = {
            "name": self.fake.bothify(text='Category: ????-########', letters='ABCDE'),
            "description": "Category"
        }
        return save_product_category

    def get_save_sub_category_product(self):
        save_sub_category_product = {
            "name": self.fake.bothify(text='Sub Category: ????-########', letters='ABCDE'),
            "description": "new Sub Category",
            "category_id": 2
        }
        return save_sub_category_product

    def get_update_sub_category_product(self):
        update_sub_category_product = {
            "name": self.fake.bothify(text='New Sub Category: ????-########', letters='ABCDE'),
            "description":"new Sub Category",
            "category_id":2
        }
        return update_sub_category_product

    body = {
        "email": "flevar@gmail.com",
        "password": "flevar@123"
    }

    update_body = {
        "name":"flevar111",
        "email":"flevar111@gmail.com",
        "password":"flevar@123"
    }

    def get_update_product(self):
        update_product = {
            "name":self.fake.bothify(text='Product: ????-########', letters='ABCDE'),
            "description":"Product3",
            "model": "Modelq",
            "rate": 5,
            "category_id":1,
            "sub_category_id":1,
            "cpt":100,
            "mrp":110,
            "short_description":"THis is short_description",
            "meta_title":"THis is meta_title",
            "meta_description":"",
            "meta_keyword":"",
            "is_best_seller":1,
            "product_images":[{
                "id":"",
                "file":""
            }],
            "location_ids":[2]
        }
        return update_product