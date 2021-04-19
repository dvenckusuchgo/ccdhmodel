
# Class: Identifier




URI: [types:Identifier](https://example.org/ccdh/datatypes/Identifier)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CodeableConcept]<type%200..1-++[Identifier&#124;value:string%20%3F;system:string%20%3F],[CodeableConcept])

## Attributes


### Own

 * [➞system](../slots/identifier__system.md)  <sub>OPT</sub>
     * Description: The system or namespace that defines the identifier.
     * range: [String](../types/String.md)
 * [➞type](../slots/identifier__type.md)  <sub>OPT</sub>
     * Description: A code that defines the type of the identifier.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞value](../slots/identifier__value.md)  <sub>OPT</sub>
     * Description: The value of the identifier, as defined by the system.
     * range: [String](../types/String.md)
