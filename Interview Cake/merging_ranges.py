'''
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when *everyone* is available.

To do this, you’ll need to know when *any* team is having a meeting. In HiCal, a meeting is stored as a tuple of integers *(start_time, end_time).

These integers represent the number of 30-minute blocks past 9:00am. For example:

(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
For example, given:
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:
[(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order.** The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges.
Here we've simplified our times down to the number of 30-minute slots past 9:00 am. But we want the function to work even 
for very large numbers, like Unix timestamps. In any case, the spirit of the challenge is to merge meetings where start_time 
and end_time don't have an upper bound.
'''
import unittest

def merge_ranges(meetings):

    # Merge meeting ranges
    
    #It's more simple to do merge slots of time 
    meetings.sort()
    
    #declare new list, for the merged meetings 
    merged_meetings = []
    #inicialize the merged meenting, with the firts meeting
    merged_meetings = [meetings[0]]
    
    #iterating throw meeting starting from the second meeting
    for start_curr,end_curr in meetings[1:]:
        
        #merged_meetings[-1] acess the last tuple inside de list 
        last_merged_start, last_merged_end = merged_meetings[-1]
        
        if (last_merged_end >= start_curr):
            
            merged_meetings[-1] = (last_merged_start, max(end_curr, last_merged_end))

        else: 
            merged_meetings.append((start_curr,end_curr))
        
    return merged_meetings


#Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)