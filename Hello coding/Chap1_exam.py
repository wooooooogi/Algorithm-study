#   Coded by Sungwook Kim
#   Date: 2019-07-30
#   Python version: 3.6.5
#   IDE: Spyder 3

'''
1. 128개의 이름이 정렬되어 있는 리스트가 있습니다. 이진 탐색으로 이름을 찾을 때 필요한 최대의 추측 횟수는 얼마일까요?
2. 만약 리스트의 크기가 두 배가 된다면 최대 추측 횟수는 어떻게 될까요?

다음 각각의 실행 시간을 빅오 표기법으로 표시하세요.

3. 어떤 사람의 이름을 알고 있습니다. 전화번호부에서 이 사람의 전화번호를 찾고 싶습니다.
4. 전화번호가 있습니다. 전화번호부에서 이 전화번호를 가진 사람의 이름을 찾고 싶습니다. (힌트: 전화번호부를 모두 찾아야 할 수도 있습니다!)
5. 전화번호부에 있는 모든 사람의 전화번호를 알고 싶습니다.
6. 알파벳 A로 시작하는 사람들의 전화번호를 알고 싶습니다.
'''

'''
1. 128개의 이름이 정렬되어 있는 리스트가 있습니다. 이진 탐색으로 이름을 찾을 때 필요한 최대의 추측 횟수는 얼마일까요?
Binary search execution time: log_2_N
-> log_2_128 = 7
'''

'''
2. 만약 리스트의 크기가 두 배가 된다면 최대 추측 횟수는 어떻게 될까요?
Same as prob 1.
-> log_2_256 = 8
'''

'''
3. 어떤 사람의 이름을 알고 있습니다. 전화번호부에서 이 사람의 전화번호를 찾고 싶습니다.
Simple search: O(N), Number of people.
Binary search: O(log_2_N), only if phone book is sorted by alphabet. (NICE)
'''

'''
4. 전화번호가 있습니다. 전화번호부에서 이 전화번호를 가진 사람의 이름을 찾고 싶습니다. (힌트: 전화번호부를 모두 찾아야 할 수도 있습니다!)
Simple search: O(N), Number of phone number.
Binary search: O(log_2_N), only if phone book is sorted by number. (HAHA)
'''

'''
5. 전화번호부에 있는 모든 사람의 전화번호를 알고 싶습니다.
Only can do using simple search. O(N)
'''

'''
6. 알파벳 A로 시작하는 사람들의 전화번호를 알고 싶습니다. O(N)
Simple search: O(N), Number of people.
If phone book is sorted by alphabet: O(N/26), wrong! O(N). Ignore constant with N
'''