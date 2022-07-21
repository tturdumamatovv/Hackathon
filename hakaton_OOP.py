import json
class Car:
    FILE = 'j_file.json'
    id = 0 
    def __init__(self, brand, model, year_of_release, engine_capacity, color, type_, mileage, price):
        self.brand = brand
        self.model = model
        self.year_of_release = year_of_release
        self.engine_capacity = engine_capacity
        self.color = color
        self.type_ = type_
        self.mileage = mileage
        self.price = price
        self.send_car_to_json()

    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)

    @staticmethod
    def get_one_car(data, id):
        car =  list(filter(lambda x: x['id'] == id, data))
        if not car: 
            return 'Нет такой машины'
        return car[0]
    
    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)
    
    def send_car_to_json(self):
        data = Car.get_data()
        car = {
            'id': Car.get_id(),
            'brand': self.brand ,
            'model': self.model ,
            'year_of_release': self.year_of_release ,
            'engine_capacity': self.engine_capacity ,
            'color': self.color ,
            'type': self.type_ ,
            'mileage':self.mileage ,
            'price' :self.price 
        }
        data.append(car)

        with open(Car.FILE, 'w') as file:
            json.dump(data, file)

        return {'status': '201', 'msg': car}

    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        car = cls.get_one_car(data, id)
        return car

    @classmethod
    def update_data(cls, id, **kwargs):
        data = cls.get_data()
        car = cls.get_one_car(data, id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status': '200', 'msg': 'Updated'}

    @classmethod
    def delete_car(cls, id):
        data = cls.get_data()
        car = cls.get_one_car(data, id)
        if type(car) != dict:
            return car
        index = data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status': '204', 'msg': 'deleted'}


with open(Car.FILE, 'w') as file:
    json.dump([], file)


car = Car('BMW', 'E38', 1994, 2.8, 'Black', 'sedan', 5000, 9999.9)
car2 = Car('BMW', 'E39', 1999, 2.8, 'White', 'sedan', 5000, 1234.5)

print('Все машины:\n', Car.get_data())
print(Car.retrieve_data(1))
print(Car.update_data(1, model='E34'))
print(Car.delete_car(1))
print('Все машины:\n', Car.get_data())

        