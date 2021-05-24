# Quiz description URL:
# https://leetcode.com/problems/trapping-rain-water/

# result
# 	Time Limit Exceeded!!!!!!!!!!!!!!!!!!!!!!!



class Solution:
    def trap(self, height: List[int]) -> int:

        def count_water(new_height):

            wall_list = list()
            for i, el in enumerate(new_height):
                if el >= 1:
                    wall_list.append(i)

            n = len(wall_list)

            if n <= 1:
                return 0

            water_count = 0
            for j in range(n - 1):
                found_water_count = wall_list[j + 1] - wall_list[j] - 1
                if found_water_count >= 1:
                    water_count += found_water_count

            return water_count

        if len(height) <= 1:
            return 0

        layer_cnt = max(height)
        cur_height = 0
        water_count = 0

        for i in range(0, layer_cnt):
            flatted_height = [h - cur_height for h in height]
            water_count += count_water(flatted_height)
            cur_height += 1

        return water_count

