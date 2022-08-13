import logging
from datetime import datetime

import allure
from allure_commons.types import AttachmentType


def log_message(message, level='info'):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.warning(message)


def attach_screenshot(driver, file_name):
    allure.attach(driver.get_screenshot_as_png(), name=f'{file_name}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'
                  .replace(" ", "_").replace("/", "_").replace("::", "__"), attachment_type=AttachmentType.PNG)
