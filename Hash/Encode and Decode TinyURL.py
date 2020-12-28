'''
https://leetcode.com/problems/encode-and-decode-tinyurl/
'''
class Codec:
    
    def __init__(self):
        
        self.alphabet = [str(i) for i in range(10)]+list(string.ascii_lowercase)
        self.hash = {}
        self.decode_hash = {}
        self.digit = 3

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.decode_hash.keys(): 
            random_hash = ''.join([random.choice(self.alphabet) for i in range(self.digit)])
            while random_hash in self.hash.keys():
                random_hash = ''.join([random.choice(self.alphabet) for i in range(self.digit)])
            self.hash[random_hash]=longUrl
            self.decode_hash[longUrl]=random_hash
        return self.decode_hash[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.hash.keys():
            return self.hash[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))