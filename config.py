"""in this file i will declare all classes"""
from functions import is_valid_ip,ip_to_binary,network_caracteristics,split_network

class NetworkingIp:
    """this is a class for an ip address it provides many methods 
        for example convert an ip to decimal , vice versa
    """
    def __init__(self):
        self.ip = "0.0.0.0"
        self.is_binary = False
    def add_ip(self,ip):
        
        if not is_valid_ip(ip):
            raise ValueError("this ip address is not valid")
        self.ip = ip

    def to_binary(self):
        if self.is_binary:
            raise ValueError("the ip is already in binary format")
        self.ip = ip_to_binary(self.ip)
        self.is_binary = True
        return self.ip


class Network:

    def __init__(self,ip_address,subnet_mask):

        self.subnet_mask = subnet_mask
        self.ip_address = ip_address
        self.caracteristics = network_caracteristics(self.ip_address,self.subnet_mask)
        self.number_hosts = self.caracteristics['available_hosts']
        self.first_host = self.caracteristics['first_host']
        self.last_host = self.caracteristics['last_host']
        self.network_address = self.caracteristics['network']
        self.broadcast = self.caracteristics['broadcast']
        self.people = []
        self.people_names = []
    
    def get_number_hosts(self):
        return self.number_hosts

    def get_network_address(self):
        return self.network_address

    def get_first_host(self):
        return  self.first_host

    def get_last_host(self):
        return self.last_host

    def get_broadcast_address(self):
        return self.broadcast

    def add_people(self,people):
        if not isinstance(people,list):
            raise TypeError("this methods take a list of person")

        if sum(people) >= self.number_hosts:
            raise ValueError("The number of hosts available on this range cannot satisfy all the people provided")

        self.people = people

    def add_people_names(self,names):
        if not isinstance(names,list):
            raise TypeError("this methods take a list of person")
        self.people_names = names

    def split_network(self):
        answer = 0

        if not len(self.people) :
            print("you did not provide a list of people, do you want to enter it manually?")
            answer = int(input("if yes type 1:"))

            if answer == 1:
                print(f"the number of hosts available is {self.number_hosts} , so please enter a number of people \n less than this number or the program may crash")
                number_networks = int(input("type the number of networks :"))

                if not number_networks > 1 :
                    raise ValueError("please enter a number greater than 0 or 1")

                self.people_names = []
                print('make sure you start by the greatest the number please , or the script may returns error')

                for i in range(number_networks):
        
                    single_people = int(input("how many people for this network? :"))
                    single_people_name = input("enter a name title for this network :")
                    print("great!\n")
                    self.people.append(single_people)
                    self.people_names.append(single_people_name)

        network_conf = {"network":self.ip_address,"mask":self.subnet_mask}

        if not len(self.people_names):
            return split_network(network_conf,self.people,format=True)

        return split_network(network_conf,self.people,format=True,names=self.people_names)


    def __str__(self) :
        """the class is made to send different configuration for a given network"""
        return self.caracteristics
