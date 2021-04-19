
# Datatypes schema





### Classes

 * [CodeableConcept](classes/CodeableConcept.md)
 * [Coding](classes/Coding.md) - A structured representation of a coded/enumerated data value, that includes additional metadata about the code and code system.
 * [Identifier](classes/Identifier.md)
 * [Quantity](classes/Quantity.md) - A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including a value and unit.

### Mixins


### Slots

 * [➞coding](slots/codeableConcept__coding.md) - A reference to a code defined by a terminology system
 * [➞text](slots/codeableConcept__text.md) - A human language representation of the concept represented by the Coding
 * [➞code](slots/coding__code.md) - The value of the code itself.
 * [➞display](slots/coding__display.md) - A human-readable name for the code.
 * [➞system](slots/coding__system.md) - The code system where the code is defined.
 * [➞version](slots/coding__version.md) - The version of the code system.
 * [➞system](slots/identifier__system.md) - The system or namespace that defines the identifier.
 * [➞type](slots/identifier__type.md) - A code that defines the type of the identifier.
 * [➞value](slots/identifier__value.md) - The value of the identifier, as defined by the system.
 * [➞comparator](slots/quantity__comparator.md) - How to understand the value  . . .   < | <= | >= | >
 * [➞unit](slots/quantity__unit.md) - Unit representation (e.g. mg, mL)
 * [➞value](slots/quantity__value.md) - Numerical value (with implicit precision)

### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [Url](types/Url.md)  ([String](types/String.md)) 
