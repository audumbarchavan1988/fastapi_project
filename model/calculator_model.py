import multiprocessing
import logging

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
    lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    num_processes = multiprocessing.cpu_count()
  
    pool = multiprocessing.Pool(processes=num_processes)

    try:       
        results = pool.map(add_list, lists)
        logger.info("Results: %s", results)
    except Exception as e:
        logger.error("An error occurred: %s", e)
    finally:
       
        pool.close()
        
        pool.join()

if __name__ == "__main__":
    main()
