#!/usr/bin/env python

from client.runner import Client

def main(args=None):
  client = Client()
  client.run()

if __name__ == '__main__':
  main()
