from utils.source import print_source


def test_source(list_with_dict):
    assert print_source(list_with_dict[0]['from']) == "Maestro 1308 79** **** 7170"
    assert print_source(list_with_dict[0]['to']) == "Счет **8612"