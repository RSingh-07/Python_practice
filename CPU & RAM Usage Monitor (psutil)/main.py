import time 
import psutil

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = ''
    mem_usage = (mem_usage / 100.0)