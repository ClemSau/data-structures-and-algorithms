# 1108. Defanging an IP Adrress

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
