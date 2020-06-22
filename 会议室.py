#Leetcode253
class Solution:
    def minMeetingRooms(self, intervals):
        rooms = []  # 记录各会议室的结束时间
        meetings = sorted(intervals)  # 按开始时间升序
        for meeting in meetings:
            find = False
            for index, end_time in enumerate(rooms):
                # 找到满足结束时间早于当前会议开始时间的会议室，并更新会议室的时间表
                if meeting[0] >= end_time:
                    rooms[index] = meeting[1]
                    find = True
                    break
            # 如果没找到，则新增会议室
            if not find:
                rooms.append(meeting[1])
        return len(rooms)

if __name__ == "__main__":
    test = [[0,30],[5,10],[15,20],[17,25],[19,24],[35,50],[49,61],[62,63]]
    print(sorted(test))
    solution = Solution()
    solution.minMeetingRooms(test)