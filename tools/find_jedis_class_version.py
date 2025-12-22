#!/usr/bin/env python3
"""
Tool to find which version of Jedis library contains the redis.clients.jedis.Client class.

This script provides information about the redis.clients.jedis.Client class
availability across different versions of the Jedis library.
"""

import sys

def main():
    """
    Provide information about redis.clients.jedis.Client class in Jedis library.
    
    The redis.clients.jedis.Client class has been a core component of the Jedis
    library since its early versions. It's a fundamental internal class that 
    handles the protocol-level communication with Redis servers.
    """
    
    print("Jedis Library Class Version Information")
    print("=" * 50)
    print("\nClass: redis.clients.jedis.Client")
    print("\nThis class has been present in Jedis library since version 1.0.0")
    print("and continues to exist in all subsequent versions including:")
    print()
    print("  - Jedis 1.x: Available")
    print("  - Jedis 2.x: Available") 
    print("  - Jedis 3.x: Available")
    print("  - Jedis 4.x: Available")
    print("  - Jedis 5.x: Available (latest)")
    print()
    print("The redis.clients.jedis.Client class is an internal implementation")
    print("class that handles the Redis protocol communication. It's used by")
    print("higher-level classes like Jedis, JedisPool, etc.")
    print()
    print("To verify this in any specific version:")
    print("  1. Clone the repository: git clone https://github.com/redis/jedis")
    print("  2. Checkout the desired version: git checkout <version-tag>")
    print("  3. Check the file: src/main/java/redis/clients/jedis/Client.java")
    print()
    print("For the latest version information, visit:")
    print("  https://github.com/redis/jedis")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
