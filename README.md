# decrypt airconsole firmware images
You might know the [airconsole](https://www.get-console.com) - some sort of
wifi enabled device that runs a minimal linux distribution similar to
openwrt which can be used as a serial to ethernet gateway.
They distribute firmware updates but unfortunately they are encrypted.

## Usage
`./fw_tool [fwimage.bin]` decrypts the firmware image into a file named
fwimage.bin.decrypted and encrypts the firmware into a new file named
fwimage.bin.encrypted.

### Example
Let's assume, that you've got a file named `airconsole-2.80-web.bin` with
the following hash values:
```
SHA256: 8863e9d926b7c96330813d35df1451dda12889f8802c3d100cdd54c8adf99f9b airconsole-2.80-web.bin
SHA512: e72a3085d6db86c88a5d2b1668c3c9566910f3f22542e05e995d8a24f93003a3d244a94a06e4679debacedfb68d9b9830d06bad49e1115797649ee6e09fa61bb airconsole-2.80-web.bin
```

This is how the decryption of the file would look like:
```
feuerrot@lynx % ./fw_tool airconsole-2.80-web.bin
File length:
From header: 3489792 byte
 Calculated: 3489792 byte
Header CRC32:
From header: 0x7ac49366
 Calculated: 0x7ac49366
Data CRC32:
From header: 0x49132a26
 Calculated: 0x49132a26
Timestamp: 2016-10-07 01:58:14
XTEA key: 0x7AC49366 0x57F6E516 0x00353FC0 0x49132A26
```

## Where do I get a firmware file?
You can download the latest firmware (currently airconsole-2.80-web.bin)
[here](http://support.get-console.com/support/solutions/articles/5000656473-airconsole-firmware-2-80-build-for-airconsole-2-0-only-)
