
# Class: CodeableConcept




URI: [types:CodeableConcept](https://example.org/ccdh/datatypes/CodeableConcept)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Coding],[Coding]<coding%200..*-++[CodeableConcept&#124;text:string%20%3F],[Identifier]++-%20type%200..1>[CodeableConcept],[Identifier])

## Referenced by class

 *  **None** *[➞type](../slots/identifier__type.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**

## Attributes


### Own

 * [➞coding](../slots/codeableConcept__coding.md)  <sub>0..*</sub>
     * Description: A reference to a code defined by a terminology system
     * range: [Coding](../classes/Coding.md)
 * [➞text](../slots/codeableConcept__text.md)  <sub>OPT</sub>
     * Description: A human language representation of the concept represented by the Coding
     * range: [String](../types/String.md)
