import psutil
import time
from datetime import datetime

# first we get cpu using psutil
def get_cpu():
    print('\n'+'='*50)
    print('CPU monitring')
    print(f'time :{datetime.now().strftime('%H,%M,%S')}')
    print('='*50)
    # cpu precentage
    get_cpp = psutil.cpu_percent(interval=1)
    print(get_cpp)

    # cores of cpu
    per_core = psutil.cpu_percent(interval=1,percpu=True)
    for i,usege in enumerate(per_core):
        print(f'core :{i} & usegs {usege}')

    # pysical or logical cores
    pysical_cores = psutil.cpu_percent(interval=1,percpu=True)
    logical_cores = psutil.cpu_percent(interval=1,percpu=False)
    print(f'print pysical_cores :{pysical_cores}')
    print(f'print logical cores :{logical_cores}')
    # freequncy
    freq = psutil.cpu_freq()
    if freq:
        print(f'Current Freq of CPU :{freq.current}.0f:MHz')
        print(f'MIN freq of CPU     :{freq.min}.0f:MHz')
        print(f'MAX freq of CPU     :{freq.max}.0f:MHz')
    
    # states of cpu
    states = psutil.cpu_stats()
    print(f'no. of interrupts :{states.interrupts}')
    print(f'no. of Switches   :{states.ctx_switches}')
# get_cpu()
# ram 
def get_ram():
    print('='*50)
    print('Ram Monitering')
    print(f'{datetime.now().strftime('%H.%M.%S')}')
    print('='*50)
    ram = psutil.virtual_memory()
    # available ram
    free = ram.available
    print(f'Available Ram in GB :{free / 1024**3} GB')
    # used ram
    used_ram = ram.used
    print(f'Used Ram in GB      :{used_ram / 1024**3} GB')
    # total ram
    total_ram = ram.total
    print(f'Total Ram in GB     :{total_ram / 1024**3} GB')
    # precent
    percent = ram.percent
    print(f'Percent of Ram {percent} %')

    try:
        swap = psutil.swap_memory()
        print('swap %',swap.percent)
    except Exception as e:
        print('Swap Data not available :',e)
# get_ram()
# get disk data
def get_disk():
    print('='*50)
    print('DISK Monitering')
    print(f'{datetime.now().strftime('%H.%M.%S')}')
    print('='*50)
    disk = psutil.disk_usage('/')
    # used free total 
    total = disk.total
    used = disk.used
    free = disk.free
    precent = disk.percent
    print(f'Total Disk      :{total / 1024**3} GB')
    print(f'USed Disk       :{used /1024**3} GB')
    print(f'Available Disk  :{free /1024**3} GB')
    print(f'Precent of Disk :{precent}')

    io = psutil.disk_io_counters()
    print(io.read_bytes,io.read_count,io.write_bytes,io.write_count)

    partetion = psutil.disk_partitions()
    for i in partetion:
        try:
            usage = psutil.disk_usage(i.mountpoint)
            print(usage.percent)
        except PermissionError:
            print(f'{i.device} - access nhi mila')
            continue
# get_disk()
# gettemp 

def get_all_data():
    try:
        while True:
            get_cpu()
            get_disk()
            get_ram()
            time.sleep(5)
    except KeyboardInterrupt:
        print('monitrinnt band kr di gayi hai ')
get_all_data()