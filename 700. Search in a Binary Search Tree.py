class Solution(object):
    def searchBST(self, root, val):
        
        temp = root 

        while temp is not None :

            if temp.val == val :
                return temp

            elif val < temp.val :
                temp = temp.left

            else:
                temp = temp.right
                
        return None                
        
