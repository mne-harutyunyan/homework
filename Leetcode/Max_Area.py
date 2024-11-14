def maxArea(self, height: list[int]) -> int:
        distance = len(height) - 1 
        left = 0
        right = len(height) - 1
        max_element = 0
        min_element = 0
        for _ in height:
            if height[left] < height[right]:
                min_element = height[left]
                left+=1
            else:
                min_element = height[right]
                right-=1
            if max_element < distance * min_element:
                max_element = distance * min_element
            distance -=1
        return max_element