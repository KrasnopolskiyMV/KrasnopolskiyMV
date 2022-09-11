
seconds = int(input())
days = seconds // (3600 * 24)
hours = seconds // 3600
minutes = seconds // 60
print(str(days) + ':' + str(hours - days*24) + ':' + str(minutes - hours*60) + ':' + str(seconds - minutes*60))