from locust import HttpLocust, TaskSet, task


class UserTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/")

    @task
    def prod1(self):
        self.client.get("/product/66VCHSJNUP")

    @task
    def prod2(self):
        self.client.get("/product/0PUK6V6EV0")

    @task
    def prod3(self):
        self.client.get("/product/L9ECAV7KIM")

    @task
    def prod4(self):
        self.client.get("/product/OLJCESPC7Z")

    @task
    def prod5(self):
        self.client.get("/product/9SIQT8TOJO")

    @task
    def prod6(self):
        self.client.get("/product/LS4PSXUNUM")

    @task
    def create_post1(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.client.post("/cart",data="product_id=LS4PSXUNUM&quantity=4",headers=headers, name="cart-post-product-LS4")

    @task
    def create_post2(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.client.post("/cart",data="product_id=9SIQT8TOJO&quantity=4",headers=headers, name="cart-post-product-9SI")

    @task
    def create_post3(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.client.post("/cart",data="product_id=OLJCESPC7Z&quantity=4",headers=headers, name="cart-post-product-OLJ")

    @task
    def create_post4(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.client.post("/cart",data="product_id=L9ECAV7KIM&quantity=4",headers=headers, name="cart-post-product-L9E")

class WebsiteUser(HttpLocust):
    task_set = UserTasks
