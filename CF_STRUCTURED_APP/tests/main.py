import unittest
import tests

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(tests.TestApp)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)