import asyncio
import sys
from bleak import BleakScanner, BleakClient


async def main(ble_address: str, timeout: int):
    try:
        while True:
            device = await BleakScanner.find_device_by_address(ble_address, timeout=timeout)
            if not device:
                print("not found")
                sys.exit(f"BLE device: {ble_address} could not be found...")
            print(f"Found device: {ble_address}")
            async with BleakClient(device, timeout=timeout) as client:
                print(f"Connected to BLE device: {ble_address}")
                print(f"Disconnected from: {ble_address}")
            print(f"waiting for 5 seconds before starting over...")
            await asyncio.sleep(5)
    except TimeoutError as e:
        print("Something went wrong while trying to connect...")
        print("Please increase the timeout and try again!")
        print(e)
    except Exception as e:
        print("Unknow error happened...")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit("Please provide a Mac Address and timeout (secs)")
    ble_address = args[0]
    timeout = int(args[1])
    asyncio.run(main(ble_address, timeout))

