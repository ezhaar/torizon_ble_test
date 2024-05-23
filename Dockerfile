FROM python:3.11.8-alpine3.19
RUN apk add --no-cache bluez
RUN adduser -D aladmin
USER aladmin
COPY requirements.txt ./
RUN pip install -r ./requirements.txt
COPY Torizon_BLE_Test /app/BLE_Driver
WORKDIR /app/BLE_Driver
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENTRYPOINT [ "python", "-u", "main.py" ]  
