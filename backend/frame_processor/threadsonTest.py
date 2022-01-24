import threading
import time
from random import randrange
from threading import Thread


class DoAnalysis(Thread):
    start_time = int

    def __init__(self, max_time_limit=20):
        super(DoAnalysis, self).__init__()
        self.start_time = time.time()
        self.max_time_limit = max_time_limit
        print(f"{self.getName()} is started")
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def run(self):
        while True:
            if (time.time() - self.start_time) > self.max_time_limit:
                print(f"{self.getName()} is dead")
                break


def main():
    all_threads = [DoAnalysis(randrange(1, 2)) for _ in range(20)]
    for thread in all_threads:
        thread.start()
    total_threads_active = threading.active_count()
    while True:
        if total_threads_active != threading.active_count():
            for thread_index in range(len(all_threads)):
                if not all_threads[thread_index].is_alive():
                    all_threads[thread_index].stop()
                    all_threads[thread_index] = DoAnalysis(randrange(10, 20))
                    all_threads[thread_index].start()


if __name__ == "__main__":
    main()