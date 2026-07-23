class Solution {
    
    public void helper(Node root, ArrayList<Integer> preOrder){
        if(root == null){
            return;
        }
        
        preOrder.add(root.data);
        helper(root.left, preOrder);
        helper(root.right, preOrder);
    }
    
    public ArrayList<Integer> preOrder(Node root) {
        ArrayList<Integer> ans = new ArrayList<>();
        helper(root, ans);
        return ans;
    }
}