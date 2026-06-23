class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)

        return True






    # אם הגעתי לאינדקס שלא ניתן להגיע אליו
    # תחזיר False

    # עדכן farthest

# אם סיימתי את הלולאה
# תחזיר True
        