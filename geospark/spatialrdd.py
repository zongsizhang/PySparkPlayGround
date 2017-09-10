from enums import FileDataSplitter

class PointRDD(object):
	def __init__(self, jpointrdd):
		self._jpointrdd = jpointrdd

	def __init__(self, sc, input_location, offset, splitter, carry_input_data, partitions):
		self._jpointrdd = sc._jvm.org.datasyslab.geospark.spatialRDD.PointRDD(sc._jsc, input_location, offset, FileDataSplitter.getj_file_data_splitter(sc, splitter) , carry_input_data, partitions)
	