"""
Data provider base
"""

class DataProviderBase:
    """
    Data provider base
    """
    result = None
    def get_data(self) -> list:
        """ Get data from data provider"""
        return self.result

    def get_length(self) -> list:
        """ Get length"""
        return self.result.length
