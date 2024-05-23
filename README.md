# Build
```bash
$ docker build . -t torizon_ble_test:0.1
```
# Run
```bash
$ docker run --privileged --name torizonble --rm  -v /var/run/dbus/:/var/run/dbus/:z torizon_ble_test:0.1 <ble device mac accress> <timeout>

# example run
$ docker run --privileged --name torizonble --rm  -v /var/run/dbus/:/var/run/dbus/:z torizon_ble_test:0.1 60:77:71:26:27:33 20
```
