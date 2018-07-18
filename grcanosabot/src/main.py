#!/usr/bin/env python
# -*- coding: utf-8 -*-


from grcanosabot.grcanosabot import GrcanosaBot

def main():
    n = GrcanosaBot("/mnt/shared","/data")
    n.start()
    n.idle()

if __name__ == '__main__':
    main()