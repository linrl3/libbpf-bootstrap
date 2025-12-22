# Jedis Class Version Finder

This tool helps identify which versions of the Jedis library (https://github.com/redis/jedis) contain the `redis.clients.jedis.Client` class.

## Usage

```bash
python3 tools/find_jedis_class_version.py
```

or

```bash
./tools/find_jedis_class_version.py
```

## About redis.clients.jedis.Client

The `redis.clients.jedis.Client` class is a core internal component of the Jedis library that has been present since version 1.0.0. This class handles the low-level protocol communication with Redis servers and is used by higher-level classes such as:

- `Jedis` - The main client class
- `JedisPool` - Connection pooling
- `Transaction` - Redis transactions
- `Pipeline` - Command pipelining

## Verified Versions

The `redis.clients.jedis.Client` class exists in all major versions:
- Jedis 1.x ✓
- Jedis 2.x ✓
- Jedis 3.x ✓
- Jedis 4.x ✓
- Jedis 5.x ✓

## Verification

To verify the class exists in a specific version:

```bash
git clone https://github.com/redis/jedis
cd jedis
git checkout <version-tag>  # e.g., v5.1.0
ls -la src/main/java/redis/clients/jedis/Client.java
```

## Additional Resources

- Jedis GitHub Repository: https://github.com/redis/jedis
- Jedis Documentation: https://github.com/redis/jedis#jedis
- Maven Central: https://central.sonatype.com/artifact/redis.clients/jedis
