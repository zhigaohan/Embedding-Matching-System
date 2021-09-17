

import logging
from google.cloud import datastore


class DatastoreUtil:

  def __init__(self, kind):
    logging.info('Initialising datastore lookup utility...')
    self.kind = kind
    self.client = datastore.Client()
    logging.info('Datastore lookup utility initialised.')

  def get_items(self, keys):

    keys = [self.client.key(self.kind, key)
            for key in keys]

    items = self.client.get_multi(keys)
    return items




