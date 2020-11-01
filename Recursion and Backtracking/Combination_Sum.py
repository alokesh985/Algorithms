def combinationSum(candidates, target):
        ans = []
        
        def helper_function(i, path):
            
            if(sum(path) == target):
                ans.append(path[:])
                return
            
            if(sum(path) > target):
                return
            
            for x in range(i, len(candidates)):
                path.append(candidates[x])
                
                helper_function(x, path)
                
                path.pop()
                
        helper_function(0 , [])
        return ans
