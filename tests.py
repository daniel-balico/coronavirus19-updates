from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# Ensure that flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure that main page was set up correctly
	def test_main_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertTrue(b'COVID-19 UPDATES' in response.data)
		self.assertTrue(b'Currently in:' in response.data)
		self.assertTrue(b'#StayAtHome' in response.data)
		

	# Ensure that table view page was set up correctly
	def test_tableview_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/tableview', content_type='html/text')
		self.assertTrue(b'COVID-19 UPDATES' in response.data)
		self.assertTrue(b'No.' in response.data)
		self.assertTrue(b'Country' in response.data)
	


if __name__ == '__main__':
	unittest.main()