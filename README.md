<h1>Traveling Politican Solution</h1>
<h4> This program uses Python 3.12.0 to solve the Traveling Politician Problem, which requires someone to find the shortest possible route for a the policitian's campaign trail starting in Iowa, visiting every state capital, and ending in DC.
<h2> What does the program do?</h2
<h4> 1. Imports a CVS file that contains all the capital cities of the US and their longitudes and latitudes.<br>2. Creates a Scatter plot,groups State Capitals into small clusters, and assigns clusters to numbers.<br>
  4. Uses itertools to find permutations for every possible route.<br>5. Uses geopy to calculate distance between each coordinate.<br>5. Identifies the route with the shortest distance.<br>6. Repeats process through each cluster.<br>7. Adds total distance together and outputs the entire route that will be traveled.</h4>
<h2>How to Use</h2>
<h4>Download zip file or use command prompt below</h4>
<h4>git clone https://github.com/Lexi79Ha/Traveling_politician.git</h4>
<h2>What to Import?</h2>
<h4>- import matplotlib.pyplot as plt<br>
- import sklearn<br>
- import folium<br>
- import itertools<br>
- import geopy<br>
- import unittest(For test file only)<br>
- import geometry(For test file only)</h4>
<h2>Test Units</h2>
<h4>-Test_.py will validate # of locations, longitudes, latitudes, and dictionary items.<br>
-Test2_.py will validate that the politician's route begins in Iowa.<br>
-Solutions.pynb has a test located at the end of the file that will validate that the politician's route ends in DC.</h4>
<h3>Author</h3>
<h4>Alexis Harris</h4>
<h4>Email for Questions: Lmh.mo.6@gmail.com</h4>
<h3>Contributors</h3>
<h4>Feier</h4># Traveling_Politician_Problem
