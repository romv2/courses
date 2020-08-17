t1_hours, t1_minutes, t1_seconds = int(input()), int(input()), int(input())
t2_hours, t2_minutes, t2_seconds = int(input()), int(input()), int(input())
print((t2_hours - t1_hours) * 3600 + (t2_minutes - t1_minutes) * 60 + (t2_seconds - t1_seconds))
