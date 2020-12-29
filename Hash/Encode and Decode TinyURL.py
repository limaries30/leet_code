"""
https://leetcode.com/problems/encode-and-decode-tinyurl/
"""


class Codec:
    def __init__(self):

        self.alphabet = [str(i) for i in range(10)] + list(string.ascii_lowercase)
        self.hash = {}
        self.decode_hash = {}
        self.digit = 3

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.decode_hash.keys():
            random_hash = "".join([random.choice(self.alphabet) for i in range(self.digit)])
            while random_hash in self.hash.keys():
                random_hash = "".join([random.choice(self.alphabet) for i in range(self.digit)])
            self.hash[random_hash] = longUrl
            self.decode_hash[longUrl] = random_hash
        return self.decode_hash[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        if shortUrl in self.hash.keys():
            return self.hash[shortUrl]


class Codec:
    """open addressing linear probing"""

    hashmap_size = 2048
    hashmap = [False] * hashmap_size

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        hash_idx = 0
        substring = re.sub("https?://", "", longUrl)
        for s in substring:
            hash_idx += ord(s)
        hash_idx %= self.hashmap_size
        while self.hashmap[hash_idx]:
            hash_idx += 1
        self.hashmap[hash_idx] = longUrl

        return "https://:tinyyrl.com/" + str(hash_idx)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""

        hash_idx = int(re.sub("https://:tinyyrl.com/", "", shortUrl))

        return self.hashmap[hash_idx]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))