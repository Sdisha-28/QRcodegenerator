# QRcodegenerator
To run this script, you need to have Python installed on your system. You can install the required libraries using pip:
pip install qrcode[pil]
Clone the repository to your local machine:
git clone https://github.com/Sdisha-28/qr-code-generator.git
Navigate to the project directory:
cd qr-code-generator
Modify the script generate_qr_code.py to customize the QR code generation as per your requirements.
Run the script:
python generate_qr_code.py
This will generate a QR code and save it as an image file named GOOGLE.png in the current directory.
Customization
You can customize the QR code by modifying the following parameters in the generate_qr_code.py script:
Customization:
version: QR code version.
box_size: Size of each box (pixel) in the QR code.
border: Width of the border around the QR code (in box units).
error_correction: Error correction level.
fill_color: Foreground color of the QR code.
back_color: Background color of the QR code.
