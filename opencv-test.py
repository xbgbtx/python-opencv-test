#!/usr/bin/env python3

from contextlib import contextmanager
import cv2


@contextmanager
def VideoCapture(*args, **kwargs):
    cap = cv2.VideoCapture(*args, **kwargs)
    try:
        yield cap
    finally:
        cap.release()

def main():
    print("Open CV test")

    with VideoCapture(0) as vid:
        while(True):
            ret, frame = vid.read()

            cv2.imshow('frame', frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break



if __name__ == "__main__":
    main()
