class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")

        rebuiltPath = []
        for item in items:
            if item == '':
                continue
            if item == '.':
                continue
            if item == '..':
                if rebuiltPath:
                    rebuiltPath.pop()
                continue
            rebuiltPath.append(item)
        
        if not rebuiltPath:
            return "/"
            
        ret = "/"
        for rebuild in rebuiltPath:
            ret += (rebuild + "/")
        
        return ret[:-1]
