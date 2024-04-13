import unittest

from src.core_prule.Files import Files


class FilesTest(unittest.TestCase):
    files = Files(
        'https://raw.githubusercontent.com/prule/data-processing-experiment-python/main/src/',
        './tmp/'
    )

    def test_copy(self):
        """
        Description goes here
        """

        self.files.copy_url('core_prule/Configuration.py')


if __name__ == '__main__':
    unittest.main()
