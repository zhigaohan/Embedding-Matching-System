

from annoy import AnnoyIndex
import numpy as np
import logging
import pickle

VECTOR_LENGTH = 512


class MatchingUtil:

  def __init__(self, index_file):
    logging.info('Initialising matching utility...')
    self.index = AnnoyIndex(VECTOR_LENGTH)
    self.index.load(index_file, prefault=True)
    logging.info('Annoy index {} is loaded'.format(index_file))
    with open(index_file + '.mapping', 'rb') as handle:
      self.mapping = pickle.load(handle)
    logging.info('Mapping file {} is loaded'.format(index_file + '.mapping'))
    logging.info('Matching utility initialised.')

  def find_similar_items(self, vector, num_matches):
    item_ids = self.index.get_nns_by_vector(
      vector, num_matches, search_k=-1, include_distances=False)
    identifiers = [self.mapping[item_id]
                   for item_id in item_ids]
    return identifiers

  def find_similar_vectors(self, vector, num_matches):
    items = self.find_similar_items(vector, num_matches)
    vectors = [np.array(self.index.get_item_vector(item))
               for item in items]
    return vectors


