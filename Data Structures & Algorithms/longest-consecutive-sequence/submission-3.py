class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 

        min_value = min(nums)
        attention_array = [' '] * (max(nums) + 1)
        negative_attention_array = [' '] * (abs(min(nums)) + 1) if min_value < 0 else [' ']

        for n in nums:
            if n < 0: 
                negative_attention_array[n] = '.'
            else:
                attention_array[n] = '.'
        
        attention_str = ''.join(negative_attention_array + attention_array)
        attention_span = [len(a) for a in attention_str.split()]

        return (max(attention_span))
        