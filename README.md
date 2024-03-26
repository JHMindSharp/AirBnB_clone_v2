# HBNB - The Console

This repository is part of a collaborative project by Jonathan Huybrechts and Mickael Perret. It contains the initial stage of building a clone of the AirBnB website, focusing on a backend interface, or console, to manage program data. The console allows users to create, update, and destroy objects, as well as manage file storage through JSON serialization/deserialization, ensuring persistence between sessions.

## Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ----------- |
| 0: Authors/README File | [AUTHORS](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant |
| 2: Unit Testing | [/tests](https://github.com/JHMindSharp/AirBnB_clone/tree/dev/tests) | Unit tests for all class-defining modules |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/base_model.py) | Defines BaseModel for inheritance by all other classes |
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/base_model.py) | Enhances BaseModel to recreate instances from a dictionary |
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/engine/file_storage.py), [/models/__init__.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/__init__.py), [/models/base_model.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/base_model.py) | Manages a persistent file storage system |
| 6. Console 0.0.1 | [console.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/console.py) | Implements basic console functionalities |
| 7. Console 0.1 | [console.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/console.py) | Extends console functionalities to manage data storage |
| 8. Create User class | [console.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/console.py), [/models/engine/file_storage.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/engine/file_storage.py), [/models/user.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements User class |
| 9. More Classes | Various | Implements additional classes like Place, City, Amenity, State, and Review |
| 10. Console 1.0 | [console.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/console.py), [/models/engine/file_storage.py](https://github.com/JHMindSharp/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Updates console and storage for dynamic class management |

## General Use

1. Clone this repository.
2. Navigate to the repository directory and run the `console.py` file:
    ```
    /AirBnB_clone$ ./console.py
    ```
3. You should see the following prompt, indicating you are in the HBnB console:
    ```
    (hbnb)
    ```
4. Various commands are available within the console:

    - `create`: Creates an instance based on a given class.
    - `destroy`: Destroys an object based on class and UUID.
    - `show`: Shows an object based on class and UUID.
    - `all`: Displays all objects, or all objects of a given class.
    - `update`: Updates an object's attributes based on class name and UUID.
    - `quit`: Exits the program. EOF also exits.

### Alternative Syntax

The console supports an alternative syntax for some commands:

```
<class_name>.<command>([<id>][<attribute_name>="value"] | [<id>][kwargs])
```

Implemented for: `all`, `count`, `show`, `destroy`, `update`.

## Examples

### Primary Command Syntax

#### Example 0: Create an object
```
(hbnb) create BaseModel
```

#### Example 1: Show an object
```
(hbnb) show BaseModel <id>
```

#### Example 2: Destroy an object
```
(hbnb) destroy BaseModel <id>
```

#### Example 3: Update an object
```
(hbnb) update BaseModel <id> first_name "John"
```

### Alternative Syntax

#### Example 0: Show all User objects
```
(hbnb) User.all()
```

#### Example 1: Destroy a User
```
(hbnb) User.destroy("<id>")
```

#### Example 2: Update User (by attribute)
```
(hbnb) User.update("<id>", "name", "John Doe")
```

#### Example 3: Update User (by dictionary)
```
(hbnb) User.update("<id>", {"name": "John Doe", "age": 30})
```
