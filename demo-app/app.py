# This app intentionally eats memory and crashes
data = []

while True:
    data.append("A" * 10_000_000)  # 10MB chunks
