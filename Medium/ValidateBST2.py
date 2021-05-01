"""
----- NAME: Validate BST -----
----- Category: Arrays -----
----- Level :  -----
------ BRIEF ------
# has recursive solution


------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)