#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spin.py
#  
#  Copyright 2013 Gemma Davenport
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
import os

def main():
	
	x = 0

	print("Starting Loop")
	while x == 0:
                with open('read', 'r') as f:
                        for line in f:
                                y = 1
                        f.close()
                        time.sleep(3.5)
	
	return 0

if __name__ == '__main__':
	main()

