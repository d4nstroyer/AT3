# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:48:14 2024

@author: Danny
"""

import unittest
from unittest.mock import patch
from whatsupp_client import filter_words

class TestClient(unittest.TestCase):

    @patch('socket.socket')
    def test_start_client(self, mock_socket):
        mock_socket.return_value.recv.return_value = b'Test response'
        client_socket = mock_socket.return_value

        # Connect to the server
        client_socket.connect(('localhost', 65432))
        
        # Simulate sending a message to the server
        message_to_send = "Hello, I am stupid"
        client_socket.sendall(filter_words(message_to_send).encode('utf-8'))

        # Check that sendall was called
        self.assertTrue(client_socket.sendall.called)

        # Check response handling
        response = client_socket.recv(1024)
        self.assertEqual(response, b'Test response')

    def test_filter_words_functionality(self):
        self.assertEqual(filter_words("You are stupid"), "You are *****")
        self.assertEqual(filter_words("This is damn good."), "This is **** good.")
        self.assertEqual(filter_words("Don't be an idiot."), "Don't be an *****.")
        self.assertEqual(filter_words("I am happy *smile*"), "I am happy (^_^)")
        self.assertEqual(filter_words("I am feeling *sad*"), "I am feeling (T_T)")

if __name__ == '__main__':
    unittest.main()