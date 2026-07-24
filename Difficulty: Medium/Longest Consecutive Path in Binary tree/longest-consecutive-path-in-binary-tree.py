class Solution:
    def longestConsecutive(self, root):
        maxi=-float("inf")
        queue=[[root,1]]
        while queue:
            a=queue.pop(0)
            node=a[0]
            length=a[1]
            maxi=max(maxi,length)
            if node.left:
                if node.data==node.left.data-1:
                    queue.append([node.left,length+1])
                else:
                    queue.append([node.left,1])
            if node.right:
                if node.data==node.right.data-1:
                    queue.append([node.right,length+1])
                else:
                    queue.append([node.right,1])
        return maxi if maxi!=1 else -1