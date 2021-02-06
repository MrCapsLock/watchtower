# watchtower
telegram bot to check status of specified ip or domain

### Requirements
[python3](https://python.org)
[python-wheel](https://github.com/pypa/wheel)
[python-apscheduler](https://github.com/agronholm/apscheduler)
[pyrogram](https://github.com/pyrogram/pyrogram)
[tgcrypto](https://github.com/pyrogram/tgcrypto)
[python-motor](https://github.com/mongodb/motor/)
[python-redis](https://github.com/andymccurdy/redis-py)
[python-uvloop](https://github.com/MagicStack/uvloop)

### Installion using docker
requires docker-compose

```
$ docker-compose up -d
```

this will install all of required dependices inside a docker container

### Configuration
copy example configuration into config.ini and edit it if needed.

```
$ cp config.ini.sample config.ini
```

## License
[GPL-3.0 and later](https://github.com/MrCapsLock/watchtower/blob/master/LICENSE)
