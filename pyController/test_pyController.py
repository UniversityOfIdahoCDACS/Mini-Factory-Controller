
"""This module tests the runability of pyController.py"""

import logging
from job_queue import JobQueue
from job_data import JobData
from inventory import Inventory
from factory.factory_sim2 import FactorySim2    # Simulated factory
from pyController import Orchastrator
from pyController.webapp import webadmin

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG) # sets default logging level for this module

def main():
    """Main Function"""
    logger.info("test pyController started")

    logger.debug("Creating Job and orchastrator")

    # Setup Job Queue and Inventory objects
    job_queue = JobQueue()
    inventory = Inventory()
    inventory.preset_inventory()

    # Setup factory sim object
    factory = FactorySim2()

    # Setup orchastrator object
    orchastrator = Orchastrator(mqtt=None, queue=job_queue, inventory=inventory, factory=factory)

    # Setup webadmin object
    #webadmin.start_webapp()
    #webadmin.callbacks.add_order_cb(orchastrator.add_job_callback)


    if True:
        logger.info("Running Tests")
        add_job = JobData(job_id=123, order_id=100, color='red', cook_time=12, sliced=True)
        orchastrator.add_job_callback(add_job)
        add_job = JobData(job_id=124, order_id=100, color='red', cook_time=12, sliced=True)
        orchastrator.add_job_callback(add_job)
        add_job = JobData(job_id=125, order_id=201, color='red', cook_time=12, sliced=True)
        orchastrator.add_job_callback(add_job)
        add_job = JobData(job_id=126, order_id=201, color='red', cook_time=12, sliced=True)
        orchastrator.add_job_callback(add_job)
        add_job = JobData(job_id=127, order_id=201, color='red', cook_time=12, sliced=True)
        orchastrator.add_job_callback(add_job)


        orchastrator.cancel_job_id_callback(124)
        orchastrator.cancel_job_id_callback(1256)
        orchastrator.cancel_job_order_callback(201)
        orchastrator.cancel_job_order_callback(201201)


if __name__ == '__main__':
    main()
