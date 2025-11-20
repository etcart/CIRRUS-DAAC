import logging
import boto3
from run_cumulus_task import run_cumulus_task

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def _list_it():
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket="ob-cumulus-sit-data-products-staging")
    logging.warning(response)
def _nop():
    """
    Implements the No Operation function. It does nothing!
    """
    logger.info("NOP called. Doing nothing!")


def _cma_output(result):
    """
    Returns a dict with the NOP result.
    """
    return {"NOP": result}


def process_event(event, context):
    """Processes the Cumulus event and creates a Cumulus-compatible
    output.
    """
    result = _nop()
    _list_it()
    return _cma_output(result)


def lambda_handler(event, context):
    """AWS Lambda Function entrypoint

    Parameters
    ----------
    event: dict, required
        Lambda trigger event
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc:
          https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    """
    return run_cumulus_task(process_event, event, context)
