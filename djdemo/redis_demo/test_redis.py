from redis import Redis

if __name__ == '__main__':
    redis = Redis.from_url(url="redis://:zft@192.168.1.103:6379/0")
    print(redis)
    redis.set("name", "xiaoming1")
    ret = redis.get("name")
    print(ret, ret.decode())