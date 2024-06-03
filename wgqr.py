import sys
import qrcode

wg = sys.stdin.read()
    
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

qr.add_data(wg)
qr.make(fit=True)
qr.print_ascii(tty=True)