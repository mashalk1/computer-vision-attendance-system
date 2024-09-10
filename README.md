This system designed in python, is aimed to use a camera and process that image to match it with an already known student's/persons' ID. 
It uses an encoding generator library. Each image present in its library has an encoded matrix, whenever an image is captured, an encoding 
matrix is generated for this new image and is compared to all those previously saved i.e the known people to the system.
If it matches more that 80% with that of known persons matrix, the database is updated and the persons presence will be marked.
