from time import sleep, perf_counter

def task():
    print('starting a task...')
    sleep(1)
    print('done')

def main():
    start_time = perf_counter()
    task()
    task()
    end_time = perf_counter()

    delta = end_time - start_time
    
    print(f'It took {delta} seconds to complete')
main()