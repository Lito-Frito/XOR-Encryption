# XOR Encryption Demo
![XOR](https://user-images.githubusercontent.com/56422761/165651711-3a9c08c4-0959-4607-9cea-805b10c4e8f3.png)
## [![Run on Repl.it](https://repl.it/badge/github/crc8109/XOR-Encryption)](https://repl.it/github/crc8109/XOR-Encryption)

This is a simple CLI app I made that showcases how XOR is implemented in encryption. I made this because we learned about how encryption works in my grad class and I wanted a tool to help people visualize how one of the basic techniques in encryption works.

If you've ever wondered how encryption works, XOR is used in many different types of encryption algorithms at some point.

## What This Includes
* `main.py`: The example script to showcase XOR encryption; run this to see the XOR encryption demo.
* `encrypt.py` & `decrypt.py`: Supplementary files that feed into `main.py` (no need to touch these).

# Getting Started

## Requirements
* Python3
* a CLI (if you're on Windows, this is the Command Prompt; for Linux and Mac, this is your terminal)
* Docker (only if you choose to run the container version of this app)

## Quick Start
You can go to [repl.it](https://repl.it/@crc8109/XOR-Encryption#.replit) where I'm hosting the app in a personal repl. When you click the link, just hit the button up top that says `Run` with the forward arrow and the app will start up.

## Starting from Scratch
Download the file `main.py` and then open the CLI from the folder that has the `main.py` file. Run the file by typing `python3 main.py`.

If this doesn't work, feel free to reach out!

## Running Via Docker
This script is available as a container (if you needed it as one for whatever reason) over at [Docker Hub](https://hub.docker.com/r/crc8109/xor_program). You can download the image via `docker pull crc8109/xor_program`.

Run the container via `docker run -i xor_program`. Don't forget the `-i` flag. You need to be able to pass along STDIN to the container, otherwise the application won't run properly.
