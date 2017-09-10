
from pyspark import SparkContext
from pyspark.rdd import RDD

def read_to_geometry_rdd(sc, input_path):
	jrdd = sc._jvm.org.datasyslab.geospark.formatMapper.shapefileParser.ShapefileReader.normalrdd(sc._jsc)
	return RDD(jrdd, sc)


