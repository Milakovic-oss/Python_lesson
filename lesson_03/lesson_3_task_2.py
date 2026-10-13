from smartphone import Smartphone

catalog = [
    Smartphone("samsung", "Galaxy S25", "+79010036166"),
    Smartphone("Apple", "Iphone 17", "+79220520522"),
    Smartphone("Xiaomi", "Redmi Note 14 Pro", "+79028765674"),
    Smartphone("Huawei", "Huawei Pura 70 Ultra", "+79087775564"),
    Smartphone("Poco", "Poco F7 Pro", "+79067658798"),
]

for phone in catalog:
    print(phone.brand, "-", phone.model, ".", phone.number)
