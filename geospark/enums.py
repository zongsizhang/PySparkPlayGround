from enum import Enum

class FileDataSplitter(Enum):
	# the csv.
	CSV = 0,

	# the tsv.
	TSV = 1,

	# the geojson.
	GEOJSON = 2,

	# the wkt.
	WKT = 3

	"""
	return relevant java FileDataSplitter object according to python object
	"""
	@staticmethod
	def getj_file_data_splitter(sc, psplitter):
		return {
		    FileDataSplitter.CSV : sc._jvm.org.datasyslab.geospark.enums.FileDataSplitter.CSV,
		    FileDataSplitter.TSV : sc._jvm.org.datasyslab.geospark.enums.FileDataSplitter.TSV,
		    FileDataSplitter.GEOJSON : sc._jvm.org.datasyslab.geospark.enums.FileDataSplitter.GEOJSON,
		    FileDataSplitter.WKT : sc._jvm.org.datasyslab.geospark.enums.FileDataSplitter.WKT
		}[psplitter]

class GridType(Enum):
	# The equalgrid.
	EQUALGRID = 0,

	# The hilbert.
	HILBERT = 1,

	# The rtree.
	RTREE = 2,

	# The voronoi.
	VORONOI = 3,

	# The voronoi.
	QUADTREE = 4

	@staticmethod
	def getj_grid_type(sc, pgridtype):
		return {
			GridType.EQUALGRID : sc._jvm.org.datasyslab.geospark.enums.GridType.EQUALGRID,
			GridType.HILBERT : sc._jvm.org.datasyslab.geospark.enums.GridType.HILBERT,
			GridType.RTREE : sc._jvm.org.datasyslab.geospark.enums.GridType.RTREE,
			GridType.VORONOI : sc._jvm.org.datasyslab.geospark.enums.GridType.VORONOI,
			GridType.QUADTREE : sc._jvm.org.datasyslab.geospark.enums.GridType.QUADTREE
		}[pgridtype]

class IndexType(Enum):

	# The quadtree.
	QUADTREE = 0,
	
	# The rtree.
	RTREE = 1

	@staticmethod
	def getj_index_type(sc, pindextype):
		return {
		    IndexType.QUADTREE : sc._jvm.org.datasyslab.geospark.enums.IndexType.QUADTREE,
		    IndexType.RTREE : sc._jvm.org.datasyslab.geospark.enums.IndexType.RTREE
		}[pindextype]




