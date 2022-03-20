import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4_pat = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
        if re.match(ipv4_pat, queryIP):
            m_obj = re.findall(ipv4_pat, queryIP)
            flag = True
            for obj in m_obj[0]:
                if obj.startswith('0') and obj != '0':
                    flag = False
                if int(obj) > 255:
                    flag = False
            if flag:
                return "IPv4"
        
        ipv6_pat = re.compile(r'^([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})\:([\dABCDEFabcdef]{1,4})$')
        if re.match(ipv6_pat, queryIP):
            return "IPv6"
        
        return "Neither"