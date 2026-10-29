class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if len(s1) > len(s2):
            return False
        
        # Build the target hash map for s1
        s1_count = Counter(s1)
        
        # Initialize the sliding window hash map for the first window of size len(s1)
        window_count = Counter(s2[:len(s1)])
        
        # Check if the initial window matches s1
        if s1_count == window_count:
            return True
            
        # Slide the window across s2
        for r in range(len(s1), len(s2)):
            # Add the new character entering the window
            char_in = s2[r]
            window_count[char_in] += 1
            
            # Remove the old character leaving the window
            char_out = s2[r - len(s1)]
            if window_count[char_out] == 1:
                del window_count[char_out]  # Remove key entirely to keep hash maps cleanly comparable
            else:
                window_count[char_out] -= 1
                
            # Direct hash map comparison in Python is highly optimized O(1) space since max keys = 26
            if s1_count == window_count:
                return True
                
        return False