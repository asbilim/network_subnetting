from config import Network,NetworkingIp
from functions import binary_to_decimal,decimal_to_binary,ip_to_decimal,ip_to_binary

#if you want to convert a number to binary , use this function

number =8 #replace_by_the_number_you_want_to_convert
binary_number = decimal_to_binary(number) #you can add a second argument a boolean if you want the result to be 8 digits
# print(binary_number)



#if you want to convert a binary number use this function

binary_number = "1010" #replace_by_the_number_you_want_to_convert
decimal_number = binary_to_decimal(binary_number) 
# print(decimal_number)

"""
    you can continue with the same process for all the others functions
"""

#to make an ip address usable you can use the NetworkingIp class

my_machine_ip = NetworkingIp() #we inititize the class
my_machine_ip.add_ip('192.168.100.63') #replace the parameter in the parentesis with your ip
# print(my_machine_ip.to_binary()) #you can convert your ip address directly in binary

############# this is the part for the subnetting ###############
################################################################


ub_network = Network("192.168.0.0","255.255.255.0") #initializing the network with an ip address and a subnet mask
# print(ub_network.split_network()) #calling a method to split a network 

"""
    there is more other methods that you can use such as:
    get_first_host
    get_last_host
    etc..........
"""


###############################################################
###############################################################

def main():

    print(
        """this script has been created by kirikode a student in college of technology , university of buea
        you will found here two differents class , both for dealing with tcp/ip adresses v4
        dont hesitate to read the course before using this script
        """
    )

if __name__ == '__main__':
    main()
