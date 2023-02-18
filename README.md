# Viber secret chat bruteforce and change

## Files

- `pins_rest_full_sorted.txt` and `pins_reset_fuill.txt` bruteforce pin code and change it to `0000` value. "sorted" file contains PIN numbers with selected numbers in front of list, i.e. if you know that PIN contains `7` than change `MAJOR_NUMS` value in `generator.py`.
- generator.py
  - Generates Badusb files for Flipper to bruteforce viber secret chat pin code.

## How to use this

1. Copy files `pins_reset_full_sorted.txt` or/and `pins_reset_full.txt` to the Flipper internal memory or SD card.
2. On Android phone open Viber -> Settings -> Privacy -> Hidden Chats -> Change PIN.
3. Connect Flipper to the phone and Run `BadUsb` script.
4. Once pin found it will be changed to `0000` and you will see "Confirm PIN" pop ups instead of "Enter your current 4-digit PIN".
5. Use pin `0000` to open secret chats.

NOTE. It did not tested on iPhone devices.
