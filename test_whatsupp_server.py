# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:54:09 2024

@author: Danny
"""

import unittest
from unittest.mock import patch, MagicMock
from whatsupp_server import filter_words

class TestServer(unittest.TestCase):

    @patch('socket.socket')
    def test_start_server(self, mock_socket):
        # Create a mock socket and setup the accept method
        mock_server_socket = mock_socket.return_value
        mock_server_socket.accept.return_value = (MagicMock(), ('127.0.0.1', 65432))

        # Simulate binding and listening
        mock_server_socket.bind(('localhost', 65432))
        mock_server_socket.listen(1)

        # Check that bind and listen were called
        self.assertTrue(mock_server_socket.bind.called)
        self.assertTrue(mock_server_socket.listen.called)

    def test_filter_words_functionality(self):
        self.assertEqual(filter_words("You are stupid"), "You are *****")
        self.assertEqual(filter_words("This is damn good."), "This is **** good.")
        self.assertEqual(filter_words("Don't be an idiot."), "Don't be an *****.")
        self.assertEqual(filter_words("I am happy *smile*"), "I am happy (^_^)")
        self.assertEqual(filter_words("I am feeling *sad*"), "I am feeling (T_T)")

if __name__ == '__main__':
    unittest.main()
