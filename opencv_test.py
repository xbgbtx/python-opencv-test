#!/usr/bin/env python3

from contextlib import contextmanager
import cv2
import time
import numpy as np
import random
from img_gen.img_gen_numpy import ImgGenNumpy as ImgGen


@contextmanager
def VideoCapture(*args, **kwargs):
    cap = cv2.VideoCapture(*args, **kwargs)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    try:
        yield cap
    finally:
        cap.release()


def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    for dev_port in range(10):
        with VideoCapture(dev_port) as camera:
            is_reading, img = camera.read()
            w = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
            h = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            if is_reading:
                print("Port %s is working and reads images (%d x %d)" %
                      (dev_port, w, h))


def process_loop(vid, img_gen):
    title = "Open CV"
    while (True):
        ret, frame = vid.read()

        img_gen.add_frame(frame)

        frame = img_gen.get_frame()

        cv2.imshow(title, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    print("Open CV test")

    list_ports()

    with VideoCapture(0) as vid:
        vid_shape = (720, 1280, 3)
        img_gen = ImgGen(vid_shape)
        process_loop(vid, img_gen)


if __name__ == "__main__":
    main()
