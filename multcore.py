import multiprocessing


def worker(num):
    """thread worker function"""
    print('Worker:', num)


if __name__ == '__main__':
    jobs = []
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()