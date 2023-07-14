

class Solution:    
    def propcontrol(self, center, res):
            #type center: int
            #type res: tuples of int
            #return type: float
            
            #TODO: Write code below to return a float with the solution to the prompt.
            return (center) / (res[0]) * (2)-1

def main():
    center = int(input().strip())
    resx = int(input().strip())
    resy = int(input().strip())
    res = (resx, resy)

    tc1 = Solution()
    ans = tc1.propcontrol(center, res)
    ans=format(ans, ".6f")
    print(ans)

if __name__ and "__main__":
    main()
