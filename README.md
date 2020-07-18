This is a project titled "Image Encryption Using Rubik's Cube Based Algorithm". It is the process to transform the image securely so that no unauthorized user can be able to decrypt the image. Image encryption have applications in many fields including the internet communication, transmission, medical imaging etc.
First, in order to scramble the pixels of gray-scale original image, the principle of Rubik’s cube is deployed which only changes the position of the pixels. Using two random secret keys, the bitwise XOR is applied into the rows and columns. These steps can be repeated until the number of iterations is not reached. Numerical simulation has been performed to test the validity and the security of the proposed encryption algorithm.

During encryption, the two keys that will be required for decryption and the number of iterations will be sent to the Email provided by the user.
The keys will be required for decryption.

To encrypt, run encUI.py
To decrypt, run decUI.py

The data will be stored in database which can also be deleted later.

The encrypted images will be saved on enc_result folder
The decrypted images will be saved on dec_result folder
