# WireguardQR

A simple Python script to generate a QR code from an existing Wireguard configuration file using the `qrcode` Python library.

## Prerequisites

Install the `qrcode` Python library using pip:

```bash
pip install qrcode
```

## Usage

Pipe your Wireguard configuration file to the Python script `wgqr.py` using `cat`:

```bash
cat wg.conf | python ./wgqr.py
```

The QR code will be displayed in the terminal using ASCII characters. You can use this QR code to quickly import the tunnel into the Wireguard mobile app.

## Example

You can use the provided `example.conf` file in this repository to test the import:

```bash
cat example.conf | python ./wgqr.py
```

This is only a sample file and does not serve any other purpose.