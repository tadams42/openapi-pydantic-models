from typing import Any

# The Schema Object allows the definition of input and output data types. These types
# can be objects, but also primitives and arrays.
#
# ...
#
# In addition to the JSON Schema properties comprising the OAS dialect, the Schema
# Object supports keywords from any other vocabularies, or entirely arbitrary
# properties.


SchemaObject = dict[str, Any]
