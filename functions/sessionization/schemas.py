from pyspark.sql.types import DateType, StringType, StructType, StructField, DoubleType, IntegerType, TimestampType, BooleanType, LongType, ArrayType

session_schema = StructType([
        StructField("fullVisitorId", StringType(), True),
        StructField("visitId", StringType(), True),
        StructField("userId", StringType(), True),
        StructField("visitNumber", IntegerType(), True), 
        StructField("visitStartTime", LongType(), True), 
        StructField("date", IntegerType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("trafficSource_campaign", StringType(), True),
        StructField("trafficSource_source", StringType(), True), 
        StructField("trafficSource_medium", StringType(), True),
        StructField("trafficSource_keyword", StringType(), True),
        StructField("trafficSource_ad_content", StringType(), True),
        StructField("geoNetwork_continent", StringType(), True),
        StructField("geoNetwork_subContinent", StringType(), True),
        StructField("geoNetwork_country", StringType(), True),
        StructField("geoNetwork_region", StringType(), True),
        StructField("geoNetwork_metro", StringType(), True),
        StructField("geoNetwork_city", StringType(), True),
        StructField("geoNetwork_cityId", IntegerType(), True),
        StructField("geoNetwork_networkDomain", StringType(), True),
        StructField("geoNetwork_latitude", DoubleType(), True),
        StructField("geoNetwork_longitude", DoubleType(), True),
        StructField("geoNetwork_networkLocation", StringType(), True),
        StructField("device_browser", StringType(), True),
        StructField("device_browserVersion", DoubleType(), True),
        StructField("device_browserSize", StringType(), True),
        StructField("device_operatingSystem", StringType(), True),
        StructField("device_operatingSystemVersion", StringType(), True),
        StructField("device_isMobile", BooleanType(), True),
        StructField("device_mobileDeviceBranding", StringType(), True),
        StructField("device_mobileDeviceModel", StringType(), True), 
        StructField("device_mobileInputSelector", StringType(), True),
        StructField("device_mobileDeviceInfo", StringType(), True),
        StructField("device_mobileDeviceMarketingName", StringType(), True),
        StructField("device_flashVersion", IntegerType(), True),
        StructField("device_javaEnabled", StringType(), True),
        StructField("device_language", StringType(), True),
        StructField("device_screenColors", StringType(), True),
        StructField("device_screenResolution", StringType(), True),
        StructField("device_deviceCategory", StringType(), True),
        StructField("totals_transactionRevenue", StringType(), True),
        StructField("landingPage", StringType(), True),
        StructField("hits_type", StringType(), True),
        StructField("touchpoints", ArrayType(StringType()), True),
        StructField("touchpoints_wo_direct", ArrayType(StringType()), True),
        StructField("first_touchpoint", StringType(), True),
        StructField("last_touchpoint", StringType(), True)
        ])

batch_schema = StructType([
        StructField("timestamp", TimestampType(), True),
        StructField("status", StringType(), True)
        ])