class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.directions =  [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)] # ['East', 'North', 'West', 'South']
        self.boundarys = [width - 1, height - 1, 0, 0] # [max_x, max_y, min_x, min_y]
        self.direction_index = 0

    def step(self, num: int) -> None:
        num %= (2 * (self.width + self.height - 2))
        if num == 0 and (self.x, self.y) == (0, 0):
            self.direction_index = 3
        while num > 0:
            # east 
            if self.direction_index == 0 and self.x == self.boundarys[0]:
                self.direction_index = (self.direction_index + 1) % 4
            # north
            elif self.direction_index == 1 and self.y == self.boundarys[1]:
                self.direction_index = (self.direction_index + 1) % 4
            # west
            elif self.direction_index == 2 and self.x == self.boundarys[2]:
                self.direction_index = (self.direction_index + 1) % 4
            # south
            elif self.direction_index == 3 and self.y == self.boundarys[3]:
                self.direction_index = (self.direction_index + 1) % 4
            
            dx , dy = self.directions[self.direction_index][0] , self.directions[self.direction_index][1]
            # print( num , self.direction_index , "x , y" ,  self.x , self.y )

            steps_x = min(self.width - self.x - 1 , num) * dx if self.directions[self.direction_index][0] >= 0 else min(self.x  , num ) * dx 
            steps_y = min(self.height - self.y - 1, num) * dy if self.directions[self.direction_index][1] >= 0 else min(self.y , num ) * dy
            # print(steps_x , steps_y)
            self.x += steps_x 
            self.y += steps_y
            # print(num)
        

            num -= max(abs(steps_x) , abs(steps_y))
        
        


    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        directions = ['East', 'North', 'West', 'South']
        return directions[self.direction_index]