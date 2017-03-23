# decrypt airconsole firmware images
You might know the [airconsole](https://www.get-console.com) - some sort of
wifi enabled device that runs a minimal linux distribution similar to
openwrt which can be used as a serial to ethernet gateway.
They distribute firmware updates but unfortunately they are encrypted.

## Usage
```./decrypt [fwimage.bin]``` decrypts the firmware image into a file named
fwimage.bin.decrypted. Currently that's the only thing this tool can do.

## Where do I get a firmware file?
You can download the latest firmware (currently airconsole-2.80-web.bin)
[here](http://support.get-console.com/support/solutions/articles/5000656473-airconsole-firmware-2-80-build-for-airconsole-2-0-only-)
