'''
1108. Defanging an IP Address
by Laith Kamal
'''

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")
