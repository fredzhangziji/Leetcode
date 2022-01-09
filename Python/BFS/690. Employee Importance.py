
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # edge case
        if not employees:
            return 0
        
        dictionary = {} # id: Employee object
        size = len(employees)
        for i in range(size):
            if employees[i].id not in dictionary:
                dictionary[employees[i].id] = employees[i]
            
            if employees[i].id == id:
                employeeIndex = i
        
        tImportance = 0
        
        employee = employees[employeeIndex]
        queue = [employee]
        
        while queue:
            cEmployee = queue.pop(0)
            tImportance += cEmployee.importance
            for subordinate in cEmployee.subordinates:
                queue.append(dictionary[subordinate])
        
        return tImportance