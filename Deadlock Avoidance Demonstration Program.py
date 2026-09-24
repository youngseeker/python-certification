# The following Python program demonstrates a Lock Ordering / Lock Hierarchy Strategy to prevent circular wait deadlocks when multiple worker threads share resources concurrently:

import threading
import time

class ResourceLockManager:
    """
    Guarantees deadlock prevention by enforcing a global strict hierarchy
    on lock acquisition orders, eliminating the Circular Wait condition.
    """
    @staticmethod
    def acquire_locks_safely(*locks):
        # Sort locks by their unique memory address / system ID
        sorted_locks = sorted(locks, key=lambda l: id(l))
        for lock in sorted_locks:
            lock.acquire()
        return sorted_locks

    @staticmethod
    def release_locks_safely(sorted_locks):
        # Release in reverse order of acquisition
        for lock in reversed(sorted_locks):
            lock.release()

# Shared Resources (e.g., Database Connection and File Handle)
resource_A = threading.Lock()
resource_B = threading.Lock()

def worker_task_1():
    print("[Worker 1] Requesting Resource A and Resource B...")
    # Acquire locks using global ordering
    acquired = ResourceLockManager.acquire_locks_safely(resource_A, resource_B)
    try:
        print("[Worker 1] Acquired both resources! Executing critical task...")
        time.sleep(0.5)
    finally:
        ResourceLockManager.release_locks_safely(acquired)
        print("[Worker 1] Released all resources successfully.")

def worker_task_2():
    print("[Worker 2] Requesting Resource B and Resource A (Reverse Order)...")
    # Even though requested in reverse order, ResourceLockManager enforces global acquisition order
    acquired = ResourceLockManager.acquire_locks_safely(resource_B, resource_A)
    try:
        print("[Worker 2] Acquired both resources! Executing critical task...")
        time.sleep(0.5)
    finally:
        ResourceLockManager.release_locks_safely(acquired)
        print("[Worker 2] Released all resources successfully.")

if __name__ == "__main__":
    t1 = threading.Thread(target=worker_task_1)
    t2 = threading.Thread(target=worker_task_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("\n[System] All concurrent tasks completed without deadlock!")