#!/usr/bin/env python3

'''
a unit tester for checking the different modules of butils package
'''

import unittest

import generators as gen
class TestGenerators (unittest.TestCase):
    
    # test when input is an iterator
    def test_reverse_enum_iter (self):
        iterator = range(4)
        old_way_iter = list(reversed(list(enumerate(iterator))))
        new_way_iter = list(gen.reverse_enum(iterator))
        self.assertEqual(old_way_iter, new_way_iter)
        
    # test when input is a sequence
    def test_reverse_enum_seq (self):
        sequence = list(range(4))
        old_way_seq = list(reversed(list(enumerate(sequence))))
        new_way_seq = list(gen.reverse_enum(sequence))
        self.assertEqual(old_way_seq, new_way_seq)
    
    def test_window_iter (self):
        # given input of [0,1,2,3,4] and window size of 3
        desired_output = [(0,1,2),
                          (1,2,3),
                          (2,3,4)]
        generated_output = list(gen.window(range(5), 3))
        self.assertEqual(desired_output, generated_output)

    def test_window_seq (self):
        # given input of [0,1,2,3,4] and window size of 3
        desired_output = [(0,1,2),
                          (1,2,3),
                          (2,3,4)]
        generated_output = list(gen.window(list(range(5)), 3))
        self.assertEqual(desired_output, generated_output)
    
import Servers

class TestServer (unittest.TestCase):
    def setUp (self):
        self.server = Servers.JobsServer("", 29786);
        
    # test if server recieves request for a new job
    def test_server_request_handling (self):
        pass
    
    # test if server reci
    def test_server_sending_job (self):
        pass
    
if __name__ == "__main__":
    unittest.main()
