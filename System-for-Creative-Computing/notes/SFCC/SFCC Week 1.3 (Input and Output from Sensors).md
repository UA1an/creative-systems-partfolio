Sensors are most using Python/JS libraries

Everything on *nix systems is a file

Usually in the **/dev** directory
- Read from the device file for input
-  Write to the device file for output

## /dev

####  /dev/tty
- Magic device
- The “terminal” for the current process
####  /dev/null
- The “bit-bucket”
- Anything written to /dev/null is silently discarded
- On read, returns EOF

# Complications
## Blocking I/O

- Normal situation
- On read, program will wait until input is complete (or return pressed)
- On write, will wait until output completed
- Not what you want for interactive systems, usually

## Non-blocking I/O

- (Output is often buffered so automatically non-blocking)
- Non-blocking input:
   - If input is ready, returns what it has
   - Otherwise, returns null
   - Try and avoid busy-waiting since it wastes processor cycles
   - Consider using events

## Character vs. block devices

- Most /dev devices are character-oriented
   *Read/write one character at a time*
- Some (e.g. disks, screen/keyboard) also have a block device
-  Read/write one block at a time
   *512 bytes logical, often 4096 bytes physical*
