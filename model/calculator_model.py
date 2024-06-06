import multiprocessing
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def add_list(list):
    """
    Function to add a list of integers.
    """
    result = sum(list)
    logger.debug(f"Sum of {list} is {result}")
    return result

def main():
    # Sample input lists
    lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Number of processes to use
    num_processes = multiprocessing.cpu_count()

    # Initialize multiprocessing pool
    pool = multiprocessing.Pool(processes=num_processes)

    try:
        # Perform addition on input lists using multiprocessing pool
        results = pool.map(add_list, lists)
        logger.info("Results: %s", results)
    except Exception as e:
        logger.error("An error occurred: %s", e)
    finally:
        # Close the pool
        pool.close()
        # Wait for all processes to complete
        pool.join()

if __name__ == "__main__":
    main()
