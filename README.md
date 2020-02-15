# AirBnB clone - The console

![airbnb-img][]

## Description
### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

  The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

  This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

  The console will be a tool to validate this storage engine

  [ Foto console ]

### Files and Directories
- `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - attributes: `id`, `created_at` and `updated_at`
  - methods: `save()` and `to_json()`
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment you will have only one: `file_storage.py`.

## Repositor of test
[In construction]

## Requirements
- All your files will be interpreted/compiled on `Ubuntu 14.04 LTS` using `python3` (version 3.4.3)
- The first line of all your files should be exactly `#!/usr/bin/python3`


## Authors and Contributors
- Julian Castañeda
    - Twitter: [@Castaedajulian]
    - Github: [@juliancastaeda]
- Lina María Montaño Ramírez
    - Twitter: [@calypsobronte]
    - Github: [@calypsobronte]

## License
[MIT]


<!-- links -->
[airbnb-img]: https://live.staticflickr.com/65535/49537006097_086e766504_k.jpg
[@Castaedajulian]: https://twitter.com/Castaedajulian
[@calypsobronte]: https://twitter.com/calypsobronte
[@juliancastaeda]: https://github.com/juliancastaeda
[@calypsobronte]: https://github.com/calypsobronte
[MIT]: https://github.com/calypsobronte/AirBnB_clone/blob/master/LICENSE
