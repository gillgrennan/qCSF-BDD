# -*- coding: utf-8 -*

import logging
import pathlib
from datetime import datetime


def startLog(sessionID=None, filepath='data'):
	'''Setup file logging to a file with the session ID and timestamp as the filename'''
	
	pathlib.Path(pathlib.Path(filepath)).mkdir(parents=True, exist_ok=True)
	if sessionID is None or sessionID == '':
		sessionID = 'NO-ID'

	timestamp = datetime.today().strftime('%Y-%m-%d %H-%M-%S')
	path = pathlib.Path(
		pathlib.Path(filepath),
		pathlib.Path(f'QuickCSF {sessionID} {timestamp}.log')
	)

	logger = logging.getLogger('QuickCSF')
	logger.setLevel(logging.DEBUG)
	
	fh = logging.FileHandler(path.resolve())

	fh.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)8s: %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)
	logger.addHandler(fh)
	logger.addHandler(ch)
