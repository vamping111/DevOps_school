#!/usr/bin/env python3
#!/usr/bin/env python3
import ipaddress
class Router:
    count = 0

    """Чтобы добавить новое устройство, используйте команду сеть = Router().
    Например: google = Router()"""
    def __init__(self):
        self.table_ip = []
        self.table_route = []
        self.table_gate = []
        self.table_int = []
    """"Чтобы добавить новый IP-адресс используйте команду сеть.add_ipaddress('ip-адресс','интерфейс').
    Например: google.add_ipaddress('192.0.2.0/28','eth1')"""

    def add_ipaddress(self,ip_address,interface):
        try:
            self.ip_address = self.table_ip.append(ip_address)
            self.interface = self.table_int.append(interface)
            route = ipaddress.ip_network(ip_address)[0]
            add_r = self.table_route.append(route)
            print("Добавляем IP-адрес {} на интерфейсе {}".format(self.table_ip[self.count],self.table_int[self.count]))
            self.count += 1
        except ValueError:
            print('Добавляем IP-адрес {} на интерфейсе {}'.format(self.table_ip[self.count],self.table_int[self.count]))
            self.count += 1

    """Чтобы просмотреть IP-адреса используйте команду сеть.show_ipaddress().
    Например: google.show_ipaddress"""
    def show_ipaddress(self):
        print("IP-адрес {}".format(self.table_ip))

    """Чтобы удалить IP-адрес из таблицы используйте команду сеть.del_ipaddress(ip-address).
    Например: google.del_ipaddress(192.0.2.0/28)"""
    def del_ipaddress(self,ip_address):
        self.table_ip.remove(ip_address)
        print('IP-адресс {} был удален из таблицы'.format(ip_address))

    """Чтобы добавить новый маршрут используйте команду сеть.add_route('маршрут','гейтвей').
    Например: google.add_route('127.0.0.1','192.0.2.0')"""
    def add_route(self,ip_route,gateway):
        if ipaddress.IPv4Address(gateway) in self.table_route:
            self.ip_route = self.table_route.append(ip_route)
            print('Маршрут {} добавлен через gateway {}.'.format(self.table_route[self.count],gateway))
        else:
            print('Невозможно добавить маршрут {} через gateway {}.'.format(self.table_route[self.count],gateway))

    """Чтобы просмотреть все доступные маршруты используйте команду сеть.show_route().
    Например: google.show_route()"""
    def show_route(self):
        print("Маршруты {}".format(self.table_route))

    """Чтобы удалить маршрут из таблицы используйте команду сеть.del_route(route).
        Например: google.del_route('127.0.0.1')"""
    def del_route(self,route):
        self.table_route.remove(route)
        print('Маршрут {} был удален из таблицы'.format(route))
