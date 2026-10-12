class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_max = max(nums[0:k])
        output_array = [curr_max]
        left_edge = 0
        for i in range(k, len(nums)):
            right_edge = nums[i]
            if right_edge > curr_max:
                # max is updated, don't need to recompute. Increment both edges and move on
                output_array.append(right_edge)
                curr_max = right_edge
                left_edge += 1
                continue
            if nums[left_edge] == curr_max:
                # recompute curr_max
                curr_max = max(nums[left_edge + 1: i + 1])
                output_array.append(curr_max)
                left_edge += 1
                continue
            output_array.append(curr_max)
            left_edge += 1
        return output_array
