import logging


def base_error_log_record_example():
    logging.basicConfig(filename='sample.log', level=logging.INFO)
    log = logging.getLogger('ex')

    try:
        raise RuntimeError
    except RuntimeError:
        log.exception('Error!')


def base_success_log_record_example():
    logging.basicConfig(filename='sample.log', level=logging.INFO)
    logging.info('Program started')
    result = 7 + 8
    logging.info('Done!')


base_error_log_record_example()
