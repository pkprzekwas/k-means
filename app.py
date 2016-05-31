from pylab import plot,show
from numpy import array
from scipy.cluster.vq import kmeans,vq

file_path = '199607.tar\\199607\\199607daily.txt'

with open(file_path) as f:
    all_data = f.read().split('\n')
    all_data = [data.split(',') for data in all_data]
    temp_min = []
    i = 0
    for ids, record in enumerate(all_data):
        try:
            temp_min.append((ids, float(record[3])))
        except (IndexError, ValueError):
            i += 1

data = array(temp_min)
centroids, _ = kmeans(data, 3)
idx, _ = vq(data, centroids)

# Plotting
plot(data[idx == 0, 0], data[idx == 0, 1], 'ob',
     data[idx == 1, 0], data[idx == 1, 1], 'or',
     data[idx == 2, 0], data[idx == 2, 1], 'og')
plot(centroids[:, 0], centroids[:, 1], 'sg', markersize=8)
show()
