class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # current direction
        facing = 0
        
        # origin
        x = y = 0
        
        for i in instructions:
            if i == 'G':
                x += directions[facing][0]
                y += directions[facing][1]
                
            if i == 'L':
                # facing = (facing - 1) % 4
                facing = (facing + 3) % 4
            if i == 'R':
                facing = (facing + 1) % 4
            
        
        # after one cycle:
        # robot returns into initial postion: true
        # robot doesn't face north: true
        
        # if x == 0 and y == 0 or facing != 0:
        #     return True
        # else:
        #     return False
        
        return (x == 0 and y == 0) or facing != 0