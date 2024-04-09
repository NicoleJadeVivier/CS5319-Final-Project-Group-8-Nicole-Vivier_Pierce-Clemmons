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
We used two architectures for this application: Model-View-Controller and Event-Based. The primary different between the two architectures is the that the game state is controlled by the model in MVC. The event-based architecture contains an event controller that distributes events to all of the components. In other words, the event controller is a centralized event router. Each component is independent of each other and only connects to the event controller. On the other hand, the model view controller architecture has more interdependence and separates concerns. The model contains the game state, the view constains the graphical display, and the controller handles user input. Many of the components in the MVC architecture can be resused but repurposed in the event-based controller. We can still have a model, view, and controller class however they do not interact with eachother and can only interact with the event controller. The event controller controls everything. 

### Selected Architecture: MVC
We selected MVC as our primary architecture for many reasons including the separation of concerns, scalability, and improved testability. By separating the game logic, view, and user interface, we have a very clean and readable codebase. Additionally, Pygame has built in functions for each aspect of the game so each file contains the similar function calls. The modular design results in a very scalable application because the process for adding features is the same and it is very clear where any additions need to go. Scaling the event-based architecture is more complicated and poses more risks like event overhead due to passing large amounts of data back and forth. Lastly, we decided to select the MVC architecture because of how easy it is to test and debug. We can independently test the model, view, and controller to find any bugs. Event-based is much more difficult to debug because there is so much data being passed around. Overall, the MVC architecture fits developing a game perfectly because at its core a game can be broken down into game logic, game graphical display, and user input. 


