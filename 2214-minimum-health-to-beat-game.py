class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # shouldn't you just use armor on the biggest damage item?
        # This is O(n) solution, follow up might be - how to do in one pass?

        # could manually get these too
        minHealth = sum(damage) + 1
        maxDamage = max(damage)

        # damage = 3, armor = 2, saved = 2
        # damage = 3, armor = 3, saved = 3
        # damage = 3, armor = 4, saved = 3
        healthSavedByArmor = min(armor, maxDamage)
        minHealth -= healthSavedByArmor

        return minHealth
