# Agglomerative-clustering

Hierarchical clustering, also known as hierarchical cluster​ analysis, is an algorithm that groups similar objects into groups called clusters.

There are two types of Hierarchical clustering :
Agglomerative Clustering
Divisive Clustering

Since, we will be working with only Agglomerative clustering, we will introduce this algorithm here.
In an agglomerative hierarchical clustering algorithm each individual element is supposed to be a cluster. These clusters are merged iteratively until all the elements belong to one cluster.These algorithms will be used in calculating distance matrix in our agglomerative clustering algorithm.

There are several type of linkages :
Single Linking : We take the closest clusters and link those clusters and then recompute
the distance between the newly created cluster and the remaining clusters. Also, the clusters that form the new clusters are removed from the distance matrix.For distance between two clusters that contain more than one element, the minimum distance between the points in the cluster is chosen.
  
Complete Linkage : ​ For two clusters R and S, the single linkage returns the maximum distance between two points i and j such that i belongs to R and j belongs to S.

Average Linkage : For two clusters R and S, first for the distance between any data-point i in R and any data-point j in S and then the arithmetic mean of these distances are calculated. Average Linkage returns this value of the arithmetic mean.

Ward : This approach uses a minimised sum of squared differences between two clusters.

--XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX--

In this algorithm, we first take the number of points the user wants to enter. Next, we consider each of these points itself to be an individual cluster and calculate the distance between each of these clusters and store it in a matrix called “Distance”. The algorithms we use to calculate distance are commonly referred to as linkages which are available for merging these clusters.

We will be implementing the single linkage approach in our algorithm. As soon as we compute our initial distance matrix we move on the recursive algorithm. Firstly, we choose two clusters which are nearest to each other, and merge them. Secondly, we update our distance matrix, using the single linkage approach. The above two steps are repeated until we are left with only one cluster. At the end we graph this cluster, which is commonly referred to as a dendrogram.

--XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX--

 
 
