from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        table = {}
        
        for string in cpdomains:
            tmp = string.split(" ")
            count = int(tmp[0])
            website = tmp[1]
            
            domains = []
            domains.append(website)
            while "." in website:
                websiteTmp = website.split(".",1)
                website = website[len(websiteTmp[0])+1:]
                domains.append(websiteTmp[1])
            
            for domain in domains:
                if domain in table:
                    table[domain] += count
                if domain not in table:
                    table[domain] = count
            
        for domain, count in table.items():
            tmpRes = str(count) + " " + domain
            res.append(tmpRes)
            
        return res