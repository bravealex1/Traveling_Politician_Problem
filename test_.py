#This code provides a solution for the most effificent route a politician to visit all fifty state capitals, starting in Iowa and ending in DC.
import matplotlib.pyplot as plt #import matplotlib to create scatter plot
from sklearn.cluster import KMeans #import sklearn to location on scatter plot into cluster (you may have to import as scikit to get it to install correcting.
import folium #import folium to create interactive map of the USA to act as a visual aid for ease of development
import itertools # import itertools to help create permutation of different possible routes
from geopy.distance import geodesic #import geopy to calculate distances between different longitudes and latitudes
import unittest # Import this to test code
import pandas as pd # import pandas to read and manipulate csv file
import shapely.geometry # To test longitude and latitude
class TestCapitals(unittest.TestCase):#Test to Validate Longitudes and Latitude

    def setUp(self):
        # Read the CSV file and store it in a DataFrame
        self.capitals = pd.read_csv(r"C:\Users\lmhmo\PycharmProjects\Traveling_Politcian\.venv\us-state-capitals.csv")
        # Create a scatter plot using the longitude and latitude data
        plt.scatter(self.capitals['longitude'], self.capitals['latitude'])
        # Create a KMeans instance with the desired number of clusters and n_init
        self.kmeans = KMeans(n_clusters=14, n_init=5, random_state=42)
        # Fit the model to the longitude and latitude data
        self.kmeans.fit(self.capitals[['longitude', 'latitude']])
        # Predict the cluster for each data point
        self.capitals['cluster'] = self.kmeans.predict(self.capitals[['longitude', 'latitude']])
        # Calculate the cluster centers
        self.centers = self.kmeans.cluster_centers_
        # Loop through the cluster centers
        for i, center in enumerate(self.centers):
            # Annotate the plot with the cluster numbers at the cluster centers
            plt.annotate(i, (center[0], center[1]), fontsize=12, color='red')
        # Get the labels from the annotations
        self.labels = [annotation.get_text() for annotation in plt.gca().texts]
        # Create a dictionary of all the different clusters
        self.clusters = {}
        # Loop over the rows in the DataFrame
        for _, row in self.capitals.iterrows():
            # If the cluster is not in the dictionary, add it
            if row['cluster'] not in self.clusters:
                self.clusters[row['cluster']] = []
            # Add the name and description of the location to the cluster
            self.clusters[row['cluster']].append(
                {'name': row['name'], "latitude": row['latitude'], 'longitude': row['longitude']})
        self.clusters = {}
        # Loop over the rows in the DataFrame
        for _, row in self.capitals.iterrows():
            # If the cluster is not in the dictionary, add it
            if row['cluster'] not in self.clusters:
                self.clusters[row['cluster']] = []
            # Add the name and description of the location to the cluster
            self.clusters[row['cluster']].append(
                {'name': row['name'], "latitude": row['latitude'], 'longitude': row['longitude']})
        # Assign the list of dictionaries representing locations in cluster 7 to a variable
        self.cluster_7 = self.clusters[7]
        # Define the name of the starting location
        self.start_location_name = 'Iowa'
        # Find the dictionary that matches the name of the starting location in cluster 7
        # If no match is found, assign None to start_location
        self.start_location = next((d for d in self.cluster_7 if d["name"] == self.start_location_name), None)
        # Check if start_location is None
        if self.start_location is None:
            # If yes, print a message indicating that the name is not found in cluster 7
            print(f"No location named {self.start_location_name} found in cluster_7")
        else:
            # If no, remove the dictionary of the starting location from cluster 7
            self.cluster_7 = [d for d in self.cluster_7 if d["name"] != self.start_location_name]
            # Generate all possible permutations of the remaining locations in cluster 7
            self.routes = list(itertools.permutations(self.cluster_7))
            # Add the starting location to the beginning of each permutation
            self.routes = [(self.start_location,) + route for route in self.routes]
            # Initialize an empty list to store the distances of each route
            self.distances = []
            # Loop through each route in routes
            for route in self.routes:
                # Initialize a variable to store the total distance of the current route
                total_distance = 0
                # Loop through each pair of consecutive locations in the route
                for i in range(len(route) - 1):
                    # Assign the first location to location1
                    location1 = route[i]
                    # Assign the second location to location2
                    location2 = route[i + 1]
                    # Calculate the distance between location1 and location2 using geodesic function
                    # The function takes the latitude and longitude of each location as arguments
                    # The function returns the distance in miles
                    distance = geodesic((location1['latitude'], location1['longitude']),
                                        (location2['latitude'], location2['longitude'])).miles
                    # Add the distance to the total distance of the current route
                    total_distance += distance
                # Append the total distance of the current route to the distances list
                self.distances.append(total_distance)
            # Find the minimum distance in the distances list
            self.min_distance7 = min(self.distances)
            # Find the route that corresponds to the minimum distance
            self.min_route7 = self.routes[self.distances.index(self.min_distance7)]
            self.distances = []
            # Loop through each route in routes
            for route in self.routes:
                # Initialize a variable to store the total distance of the current route
                total_distance = 0
                # Loop through each pair of consecutive locations in the route
                for i in range(len(route) - 1):
                    # Assign the first location to location1
                    location1 = route[i]
                    # Assign the second location to location2
                    location2 = route[i + 1]
                    # Calculate the distance between location1 and location2 using geodesic function
                    # The function takes the latitude and longitude of each location as arguments
                    # The function returns the distance in miles
                    distance = geodesic((location1['latitude'], location1['longitude']),
                                        (location2['latitude'], location2['longitude'])).miles
                    # Add the distance to the total distance of the current route
                    total_distance += distance
                # Append the total distance of the current route to the distances list
                self.distances.append(total_distance)

    def test_lonlat(self): #Validate Longitudes and Latitudes provides in CSV file
        # Iterate over each row of the DataFrame
        for index, row in self.capitals.iterrows():
            # Get the longitude and latitude values
            lon = row['longitude']
            lat = row['latitude']
            # Check if they are within the valid ranges
            self.assertGreaterEqual(lon, -180)
            self.assertLessEqual(lon, 180)
            self.assertGreaterEqual(lat, -90)
            self.assertLessEqual(lat, 90)
    def test_number_of_points(self): #Validates that 51 locations are plotted on scatter plot
        # Get the number of points on the scatter plot
        num_points = len(plt.gca().collections[0].get_offsets())
        # Check if the number of points is equal to 51 using the assert statement
        self.assertEqual(num_points, 51)
    def test_number_of_clusters(self): #Validates that 14 clusters were created
        # Get the number of unique values in the cluster column
        num_clusters = self.capitals['cluster'].nunique()
        # Check if the number of clusters is equal to 14 using the assert statement
        self.assertEqual(num_clusters, 14)
    def test_labels_are_numbers(self): #Validates that each cluster was assigned a number
        # Loop through the labels
        for label in self.labels:
            # Check if the label is an instance of the int type using the assert statement
            self.assertIsInstance(int(label), int)
    def test_clusters(self):#makes sure that each location in cluster has a name, longitude, and latitude
        # Loop over the cluster numbers in sorted order
        for cluster in sorted(self.clusters.keys()):
            # Get the locations in the cluster
            locations = self.clusters[cluster]
            # Loop over the locations in the cluster
            for location in locations:
                # Get the name, latitude and longitude of the location
                name = location['name']
                lat = location['latitude']
                lon = location['longitude']
                # Check if the name is in the capitals DataFrame using the assert statement
                self.assertIn(name, self.capitals['name'].values)
                # Get the row in the capitals DataFrame that matches the name
                row = self.capitals[self.capitals['name'] == name].iloc[0]
                # Check if the latitude and longitude are equal to the values in the DataFrame using the assert statement
                self.assertEqual(lat, row['latitude'])
                self.assertEqual(lon, row['longitude'])
     # Create test that ensure that the route of first cluster begins with Iowa
    def test_route_starts_with_iowa(self):#Makes sure that the first cluster's route begins in Iowa
        # Check if the first element of the shortest route is the dictionary of Iowa using the assert statement
        self.assertEqual(self.min_route7[0], self.start_location)
    def test_lonlat_validity(self): #validates longitude and latitude used in distance
        # Loop over each route in routes
        for route in self.routes:
            # Loop over each location in the route
            for location in route:
                # Get the longitude and latitude values
                lon = location['longitude']
                lat = location['latitude']
                # Check if they are within the valid ranges using the assert statements
                self.assertGreaterEqual(lon, -180)
                self.assertLessEqual(lon, 180)
                self.assertGreaterEqual(lat, -90)
                self.assertLessEqual(lat, 90)
# Run the tests
if __name__ == '__main__':
    unittest.main()

