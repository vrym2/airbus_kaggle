from src.utils import airbus_meta

def test_meta():
    airbus = airbus_meta()
    df = airbus.read_annotations()
    assert df is not None