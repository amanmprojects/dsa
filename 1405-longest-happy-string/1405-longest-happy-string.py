import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(counts)

        res = []
        
        while counts:
            h, hchar = heapq.heappop(counts)
            
            if h == 0:
                break
                
            if len(res) > 1 and res[-1] == res[-2] == hchar:
                if counts:
                    sh, shchar = heapq.heappop(counts)
                    if sh == 0:
                        break
                    res.append(shchar)
                    sh += 1
                    
                    if sh != 0:
                        heapq.heappush(counts, (sh, shchar))
                    
                    heapq.heappush(counts, (h, hchar))
                    continue
                else:
                    break
                    
            res.append(hchar)
            h += 1

            if h != 0:
                heapq.heappush(counts, (h, hchar))
        
        return ''.join(res)
