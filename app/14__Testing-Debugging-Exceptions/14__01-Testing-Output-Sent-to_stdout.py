# PROBLEM:  Like to test with proper input; proper output will be sent to stdout (display)
# SOLUTION: Use unittest.mock module's patch() function

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import mymodule

class TestURLPrint(TestCase):
  def test_url_gets_to_stdout(self):
    protocol = 'http'
    host = 'www'
    domain = 'example.com'
    expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

    # patch() is a context manager that replaces mymodules print stdout with StringIO
    #   when with exists normal operation returns
    with patch('sys.stdout', new=StringIO()) as fake_out:
      mymodule.urlprint(protocol, host, domain)
      self.assertEqual(fake_out.getvalue(), expected_url)

t = TestURLPrint()
t.test_url_gets_to_stdout
