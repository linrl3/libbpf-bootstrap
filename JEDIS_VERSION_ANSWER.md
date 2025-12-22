# Answer to Jedis Class Version Question

## Question
Which version of https://github.com/redis/jedis has this class: `redis.clients.jedis.Client`?

## Answer
The `redis.clients.jedis.Client` class has been a core component of the Jedis library since **version 1.0.0** and exists in **all versions** of Jedis, including:

- **Jedis 1.x** - Available
- **Jedis 2.x** - Available
- **Jedis 3.x** - Available
- **Jedis 4.x** - Available
- **Jedis 5.x** - Available (current/latest)

## About the Class
`redis.clients.jedis.Client` is an internal implementation class in the Jedis library that handles the low-level Redis protocol communication. It's located at:
```
src/main/java/redis/clients/jedis/Client.java
```

## Verification
To verify this class exists in any specific version:

```bash
git clone https://github.com/redis/jedis
cd jedis
git checkout <version-tag>  # e.g., v1.0.0, v2.0.0, v3.0.0, v4.0.0, v5.1.0
ls -la src/main/java/redis/clients/jedis/Client.java
```

## Additional Resources
- Jedis Repository: https://github.com/redis/jedis
- Maven Central: https://central.sonatype.com/artifact/redis.clients/jedis
- Jedis Documentation: https://github.com/redis/jedis#jedis

---

**Note:** This question appears to be unrelated to the libbpf-bootstrap project, which focuses on eBPF (Extended Berkeley Packet Filter) examples and tools. If you have questions about Jedis specifically, please refer to the Jedis repository or documentation.
