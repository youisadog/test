from sklearn import datasets
import matplotlib.pyplot as plt # 画图工具
data,target=datasets.make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0,n_repeated=0, n_classes=2, n_clusters_per_class=1)
print(data.shape)
print(target.shape)
plt.scatter(data[:,0],data[:,1],c=target)
plt.show()