from smartphone import Smartphone 
catalog = [
        Smartphone("Siemens", "S4", "+79533456776"),
        Smartphone("Iphone", "16", "+7963345353376"),
        Smartphone("Xiaomi", "L15", "+79745633566"),
        Smartphone("Samsung", "A25", "+79833456457"),
        Smartphone("Huawei", "P69 PRO", "+79993456722")]
    
for Smartphone in catalog:
    print(f" {Smartphone.markphone} - {Smartphone.modelphone}. {Smartphone.number}")