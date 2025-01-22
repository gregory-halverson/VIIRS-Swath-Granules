import datetime

EXAMPLE_GRANULE_ID = "VNP21IMG_NRT.A2025021.1018.002.2025021155440"
EXAMPLE_PRODUCT_NAME = "VNP21IMG_NRT"
EXAMPLE_DATE = datetime.date(2025, 1, 21)
EXAMPLE_SWATH = "1018"
EXAMPLE_BUILD = 2

def test_parse_VIIRS_product():
    from VIIRS_swath_granules.granule_ID import parse_VIIRS_product
    assert parse_VIIRS_product(EXAMPLE_GRANULE_ID) == EXAMPLE_PRODUCT_NAME

def test_parse_VIIRS_date():
    from VIIRS_swath_granules.granule_ID import parse_VIIRS_date
    assert parse_VIIRS_date(EXAMPLE_GRANULE_ID) == EXAMPLE_DATE

def test_parse_VIIRS_swath():
    from VIIRS_swath_granules.granule_ID import parse_VIIRS_swath
    assert parse_VIIRS_swath(EXAMPLE_GRANULE_ID) == EXAMPLE_SWATH

def test_parse_VIIRS_build():
    from VIIRS_swath_granules.granule_ID import parse_VIIRS_build
    assert parse_VIIRS_build(EXAMPLE_GRANULE_ID) == EXAMPLE_BUILD
