#here we will create all functions for the project

#creating the function to convert a number from decimal to binary

#a function to reverse a string

from audioop import reverse


def reverse_string(sentence):

    if not isinstance(sentence,str):
        raise TypeError('please this function only takes string as parameters')

    array_string = list(sentence)
    array_string_reverse = array_string[::-1] #here we reverse the table

    return "".join(array_string_reverse) #then we convert the list back to string

#function to check if an ip is valid
def is_valid_ip(ip):

    if not isinstance(ip,str):
        raise TypeError('please this function only takes string as parameters')

    for i in ip.split('.'):
        try:
            num = int(i) # check if the item can be converted to number
        except ValueError:
            return False

    return len(ip.split('.')) == 4


#function to check if a mask is valid

def is_valid_mask(mask):

    with open("mask.txt", "r") as mask_list:

        for i in mask_list:
            
            if mask == i.strip():
                return True
            
        return False




def decimal_to_binary(number,format=False):

    binary_number = ""
    #checking if the number is an integer
    if not isinstance(number,int):
        raise TypeError("please provide an integer")

    
    while number > 0:
        binary_number += str(number%2)
        number=number//2

    #we will now try to always return the binary number with 8 digits

    binary_number = reverse_string(binary_number) #we reverse the result 

    if format :
        if len(binary_number) <= 8:
            zero_to_add = 8-len(binary_number) #the number of zero to add to the binary number for it to be 8 digits
            binary_number=("0"*zero_to_add)+binary_number
        else:
            raise ValueError("please we cannot format numbers greater than 255")
    
    return binary_number




def ip_to_binary(ip):

    if not isinstance(ip,str):
        raise TypeError('please this function only takes string as parameters')

    if not is_valid_ip(ip):
        raise ValueError('invalid IP address')
    """ 
        in this function we are trying to convert a decimal ip address to binary ip
    """
    permanent_list = ip.split('.') #convert the ip to a list of numbers
    permanent_list = [decimal_to_binary(int(i),True) for i in permanent_list] #convert each number in the list to binary

    return ".".join(permanent_list) #finally we join the 
    





#the function to convert a binary number to decimal

def binary_to_decimal(number):

    if not isinstance(number,str):
        raise ValueError('please this function only takes string as parameter')

    decimal_number = 0

    for index,value in enumerate(reverse_string(number)): 
        decimal_number += int(value) * (2**index) # we multiply each value by 2 power his index

    return str(decimal_number)



def ip_to_decimal(ip):
    if not isinstance(ip,str):
        raise TypeError('please this function only takes string as parameters')

    permanent_list = ip.split('.') #convert the ip to a list of numbers
    permanent_list = [binary_to_decimal(i) for i in permanent_list] #convert each number in the list to binary

    return ".".join(permanent_list) #finally we join the 


#fonction qui sort la configuration d'une adresse ip

def format(value):
    return value[:8]+"."+value[8:16]+"."+value[16:24]+"."+value[24:32]


def network_caracteristics(ip,mask):

    if not is_valid_ip or not is_valid_mask :
        raise ValueError('please give us a valid ip or mask address')

    divider = ip_to_binary(mask).count('1') #getting th number of zero inside the mask
    machine_address_part = "".join(list(ip_to_binary(ip).replace('.',''))[:divider]) #removing all dots and separing the machine address from the network_address
    network_address_part = "0"*(32-divider)
    broadcast_adress_part = "1"*(32-divider)
    final_address = format(machine_address_part+network_address_part) #assembling the first address 
    first_host = (machine_address_part+network_address_part)[:-1]+"1"
    broadcast_adress = format(machine_address_part + broadcast_adress_part) #assembling the broadcast domain
    last_host = (machine_address_part+broadcast_adress_part)[:-1]+"0"

    #we put the content of each variable in a dictionnary containing all network informations
    configuration = {'network':ip_to_decimal(final_address),'broadcast':ip_to_decimal(broadcast_adress),'available_hosts':(2**(32-divider)-2),'first_host':ip_to_decimal(format(first_host)),'last_host':ip_to_decimal(format(last_host))}
    
    return configuration


test_plage = {"network":"192.168.0.0","mask":"255.255.0.0"}

#function to adjust the plage

def give_plage(number):
    number_bit = 0
    while 2**number_bit < number:
        number_bit+=1
    
    return number_bit

def split_network(network,subnet_list):

    network_address = network.get('network')
    mask_address = network.get('mask')
    available_hosts = network_caracteristics(network_address,mask_address)['available_hosts']

    if not is_valid_ip(network_address) or not is_valid_mask(mask_address):
        raise ValueError("Invalid network address or mask address")
    
    subnet_list.sort(reverse=True)

    binary_mask = ip_to_binary(mask_address).replace('.','')
    range = binary_mask.count('1')


    for i in subnet_list:
        if not isinstance(i,int):
            raise TypeError('we cannot split a network with non int value')

    total_host_needed = sum(subnet_list)

    if total_host_needed > available_hosts :
        raise TypeError("the number of host needed cannot satisfy the range")


    # for index,subnet in enumerate(subnet_list):
    #     if index==0:
    #         print(format(mask_address))
    #         print(network_caracteristics(network_address,ip_to_decimal(format(mask_address))))
    #     else:
    #         binary_plage = "1"*(range+give_plage(subnet))+binary_mask[range+give_plage(subnet):]
    #         print(format(binary_plage))
    #         print(network_caracteristics(network_address,ip_to_decimal(format(binary_plage))))



#writing a function which lists all the hosts of a given domain

def format_ip(value):
    return value[:3]+"."+value[3:6]+"."+value[6:9]

    
    

def is_greater_ip(ip_one,ip_two):

    """
        this function allows to compare to ip addresses and return True if the first ip is greater than the order
    """    
    if not is_valid_ip(ip_one) or not is_valid_ip(ip_two):
        raise ValueError('a non valid ip was provided')

    list_one = ip_one.split('.') #converting ip's to list
    list_two = ip_two.split('.') #converting ip's to list

    first_comparison =None if list_one[0] == list_two[0] else list_one[0] > list_two[0]
    second_comparison = None if list_one[1] == list_two[1] else list_one[1] > list_two[1]
    third_comparison = None if list_one[2] == list_two[2] else list_one[2] > list_two[2]
    fourth_comparison = None if list_one[3] == list_two[3] else list_one[3] > list_two[3]
    
    """here we are stocking differents comparison inside variables to make our if/else conditions more readable"""

    if first_comparison is None:
        if second_comparison is None:
            if third_comparison is None:
                if fourth_comparison is None:
                    raise ValueError("the two ips are same")
                else:
                    return fourth_comparison
            else:
                return third_comparison
        else:
            return second_comparison
    else:
        return first_comparison


def is_within_mask(ip,mask,original_ip):

    network_config = network_caracteristics(original_ip,mask)
    first_host = network_config["first_host"]
    last_host = network_config["last_host"]
    
    return not is_greater_ip(first_host,ip) and is_greater_ip(last_host,ip)




print(is_within_mask("192.168.0.252","255.255.255.0","192.168.0.0"))
