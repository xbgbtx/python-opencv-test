#!/usr/bin/env python3

from contextlib import contextmanager
import cv2
import time
import numpy as np
import random


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


def process_frame(frame):

    frame[:, :] = [17, 17, 17]

    return frame


def process_loop(vid):
    t0 = t1 = 0
    while (True):
        ret, frame = vid.read()

        frame = process_frame(frame)

        t1 = time.time()
        fps = 1 / (t1 - t0)
        t0 = t1

        fps_str = str(int(fps))
        cv2.putText(frame, fps_str, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3,
                    (100, 255, 0), 3, cv2.LINE_AA)

        cv2.imshow('OpenCV out', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    print("Open CV test")

    list_ports()

    with VideoCapture(0) as vid:
        process_loop(vid)


if __name__ == "__main__":
    main()
