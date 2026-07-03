class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        log_dict, digit_logs = self.create_dict(logs)
        print(log_dict, digit_logs)
        log_keys = sorted(list(log_dict.keys()))
        #log_keys = self.merge_sort(log_keys)
        return [log_dict[k] for k in log_keys] + digit_logs

    # def merge_sort(self, keys: Tuple[int, str, str]) -> List[str]:
    #     N = len(keys)
    #     if N < 2:
    #         return keys
    #     if N == 2:
    #         keys = [keys[0], keys[1]] if keys[0] <= keys[1] else [keys[1], keys[0]]
    #         return keys
        
    #     fst = self.merge_sort(keys[:N//2])
    #     lst = self.merge_sort(keys[N//2:])

    #     i = 0
    #     j = 0
    #     while j < len(lst):
    #         if i == len(fst):
    #             fst = fst + lst[j:]
    #             break
    #         else:
    #             #print(fst[i], lst[j])
    #             if fst[i] > lst[j]:
    #                 fst = fst[:i] + [lst[j]] + fst[i:]
    #                 j += 1
    #             i += 1
    #     return keys

    def create_dict(self, logs: List[str]) -> Dict[Tuple[int, str, str], str]:
        digits = set([str(i) for i in range(0, 10)])
        log_dict = {}
        digit_logs = []
        for log in logs:
            id_, message = log.split(" ", 1)
            if message[0] not in digits:
                log_dict[(0, message, id_)] = log
            else:
                digit_logs.append(log)

        return log_dict, digit_logs

        