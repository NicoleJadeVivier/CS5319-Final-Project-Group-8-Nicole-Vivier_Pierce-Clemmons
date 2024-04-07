## Galaga Remake
### Running the project
To run either architecture navigate to either the selected or unselected folders and execute main with python.

#### Install Python  
https://www.python.org/downloads/
#### Install Pygame
`pip install pygame`

For more information visit the following links:
- https://pypi.org/project/pygame/
- https://www.pygame.org/wiki/GettingStarted


Note: Pygame is a nessecary dependency, and python 3.10 or later may be required to use


## Architectures
We used two architectures for this application: Model-View-Controller and Event-Based. The primary different between the two architectures is the that the game state is controlled by the model in MVC. The event-based architecture contains an event controller that distributes events to all of the components. Each component is independent of each other and only connects to the event controller. On the other hand, the model view controller architecture has more interdependence and rather separates concerns. The model contains the game state, the view constains the graphical display, and the controller handles user input. Many of the components in the MVC architecture can be resused but repurposed in the event-based controller. We can still have a model, view, and controller class however they do not interact with eachother and can only interact with the event controller. The event controller controls everything. 

### Selected Architecture: MVC
We selected MVC as our primary architecture for many reasons including the separation of concerns, finish later


