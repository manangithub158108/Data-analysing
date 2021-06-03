import csv, statistics;

data = [60,61,65,63,98,99,90,95,91,96];

standard_deviation = statistics.stdev(data);
mean = statistics.mean(data);
median = statistics.median(data)
mode = statistics.mode(data)
print('Standard deviation >> ' + str(standard_deviation));
print('Median >> ' + str(median));
print('Mode >> ' + str(mode));
print('Mean >> ' + str(mean));