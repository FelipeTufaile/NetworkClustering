# Importing libraries
import time
import sys


## Defining functions

def check_connection(clusterA, clusterB):
  """
  This functions receives two lists of elements and returns a boolean (True or False) indicating wether or not the two lists have at leat one element in common.
  The function also return a list of unique elements contained in the union of two lists.

  Args:
      clusterA (list): A list of elements.
      clusterB (list): A list of elements.

  Returns:
      tuple: A tuple holding the a boolean (True or False) indicating wether or not the clusters are connected.
  """
  # Connecting clusters
  connection = clusterA + clusterB

  # Removing duplicates in the 'connection'
  net_connection = list(set(connection))

  # Return True if clusterA and clusterB have one element in common and False otherwise
  connected_clusters = len(net_connection) < len(connection)

  # Return the 'connected_clusters' boolean and the net_connection
  return (connected_clusters, net_connection)


def find_connections(cluster, network):
  """
  This function receives a cluster (list of elements) and a network (list of lists of elements - sub-clusters) and check if there a connection between the
  reference cluster and all sub-clusters in the network. The functin then return an updated version of the reference cluster and network along with a boolean
  indicating whether or not the network was updated. In the case the network was not updated the boolean will be set to False and the updated versions of the
  cluster and network will equal to the original version of these lists.

  Args:
      cluster (list): A list of elements.
      network (list): A list of lists.

  Returns:
      tuple: A tuple holding the updated reference cluster, the updated network and a boolean (True or False) indicating wether or not there was an update in the network.
  """
  # Defining a list to hold the new work... after removing all sub-clusters connected to the reference cluster
  updated_network = []

  # Defining a list to hold the updated reference cluster
  updated_cluster = cluster.copy()

  # Iterating through all network of sub-clusters
  for sub_cluster in network:

    # Checking connection between the updated_cluster and the sub_cluster
    connection, net_cluster = check_connection(clusterA=updated_cluster, clusterB=sub_cluster)

    # Updating the 'updated_cluster' in case a connection is verified
    if(connection):
      updated_cluster = net_cluster

    # Returning the sub_cluster instance to the updated_network in case no connection was verified
    else:
      updated_network.append(sub_cluster)

  # Flagging wether or not the network was updated
  updated = len(updated_network) < len(network)

  # Return the 'updated_cluster', the 'updated_network' and a boolean indicating wether or not the network was updated
  return (updated_cluster, updated_network, updated)


def print_progress(current_time, start_time, n_clusters, n_subclusters, n_network):
  """
  This function receives the current time, the start time (when the network clustering process actually started), the number of clusters found in the network,
  as for the current time, the number of remaining sub-clusters in the network and the original size of the network. The function then prints a log of the
  status of the clustering process.

  Args:
      current_time (datetime): A datetime object informing the current date and time.
      start_time (datetime): A datetime object informing the date and time when the clustering process actually started.
      n_clusters (int): An integer indicating the number of clusters formed as for the current_time.
      n_subclusters (int): An integer indicating the number of sub-clusters remaining in the network as for the current_time.
      n_subclusters (int): An integer indicating the number of sub-clusters remaining in the network as for the current_time.

  Returns:
      The function prints a log of the status of the clustering process.
  """
  # Calculating the total run time as for the current_time
  run_time = current_time - start_time

  # Calculating the minutes part of the run_time
  run_time_m = int(run_time // 60)

  # Calculating the seconds part of the run_time
  run_time_s = int(run_time - run_time_m)

  # Calculating remaining time
  rem_time = run_time*n_subclusters / (n_network - n_subclusters)

  # Calculating the minutes part of the rem_time
  rem_time_m = int(rem_time // 60)

  # Calculating the seconds part of the rem_time
  rem_time_s = int(rem_time - rem_time_m)

  # Creating response string
  response = "Run time: {} min {} s | Remaining time: {} min {} s | Clusters found: {} | Remaining sub-clusters: {} | Total sub-clusters: {}"

  # Plot status
  sys.stdout.write('\r')
  sys.stdout.write(response.format(run_time_m, run_time_s, rem_time_m, rem_time_s, n_clusters, n_subclusters, n_network))
  sys.stdout.flush()


class NetworkClustering:
  """
  This class receives a network of sub-cluster and regroup these cluster based on commun elements (relationships) between clusters.
  Ex.:
    input_network = [['Person 1', 'Person 2'], ['Person 3', 'Person 4'], ['Person 1', 'Person 5', 'Person 6']]
    output_network = [['Person 1', 'Person 2', 'Person 5', 'Person 6'], ['Person 3', 'Person 4']]

  Args:
      input_network (list): A list of clusters (lists) representing the orginal un-clustered network.

  Returns:
      output_network (list): A list of clusters (lists) representing the clustered network.
  """

  def __init__(self, network):
    """
    Initializes the NetworkClustering class by attaching a network to the class.

    Args:
        input_network (list): A list of clusters (lists) representing the orginal un-clustered network.

    """
    # Defining a mutable network variable
    self.input_network = network

    # Initializing clusters list
    self.output_network = []


  def run_clustering(self, ):
    """
    Runs the clustering process and returns an updated (clustered) version of the input_ntework.

    Returns:
        output_network (list):  A list of clusters (lists) representing the clustered network.

    """
    # Creating an alias variable network from the given network
    # This alias will change along the clustering process as new groups are formed
    network = self.input_network.copy()

    # Setting start time
    start_time = time.time()

    # Run until there is a valid link in network
    while(len(network) > 1):

      # Initializing update and group variables
      updated, cluster = True, network[0]

      # Run while there is no update or it is the first run
      while (updated):

        # Clustering sub-clusters
        cluster, network, updated = find_connections(cluster=cluster, network=network)

      # Add the new cluster to the clusters list
      self.output_network.append(cluster)

      # Printing progress
      print_progress(current_time=time.time(), start_time=start_time, n_clusters=len(self.output_network), n_subclusters=len(network), n_network=len(self.input_network))

    # Add any remaining sub-cluster in the network as an individual cluster of clusters
    if(len(network) == 1):

      # Add the new cluster to the clusters list
      self.output_network.append(network[0])

      # Updating the network alias
      network = []

      # Printing progress
      print_progress(current_time=time.time(), start_time=start_time, n_clusters=len(self.output_network), n_subclusters=len(network), n_network=len(self.input_network))

    else:
      pass

    # Return the object
    return self
