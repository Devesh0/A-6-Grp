# To-do list

Week 4:
- Get the maps integrated into the game.
- Make the transitions between the zones (DONE)

Week 5: 
- Create inventory, command windows.
- Put all the objects into the map, use keyboard movement to collect them and ensure they are going into the inventory. Display the items in the inventory. 
- Phase out: keyboard movement, phase in: automation - specify to the robot to go to a particular coordinate of a zone and make sure it goes there.
- Continue to work on algorithm. 
- Create a class for the parts/batteries. Instantiate them into the map.
- Make InitiateGameplay() it's own class. 

Week 6:
- Implement algorithm to detect where objects are + where walls are:
    - Save coords of walls/objects into a tuple.
    - Path-find based on this. 
- Add mode to command center: specify to the robot the items you wish to find and the order + give the initial zone you wish for them to start searching in: robot goes to the zone first, executes the algorithm and starts searching.
- Add button to inventory: sort the objects in order of value. Highest > lowest, lowest > highest.
- Add mode to command center: specify a time to the robot. Collect items randomnly in that time period.

Week 7: 
- Work out what will be done with the settings window, remove it if it has no purpose. 
- Consult group requirements and check that they are all met.


Advanced features:
- Map randomization. 
- SQL save/load game mode if there's time.
- More advanced tiles + path-finding to deal with them. 
