
# Class: Coding


A structured representation of a coded/enumerated data value, that includes additional metadata about the code and code system.

URI: [ccdh:Coding](https://example.org/ccdh/Coding)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CodeableConcept]++-%20coding%200..*>[Coding&#124;code:string%20%3F;display:string%20%3F;system:string%20%3F;version:string%20%3F],[Quantity]++-%20comparator%200..1>[Coding],[Quantity]++-%20unit%200..1>[Coding],[Quantity],[CodeableConcept])

## Referenced by class

 *  **None** *[➞coding](../slots/codeableConcept__coding.md)*  <sub>0..*</sub>  **[Coding](../classes/Coding.md)**
 *  **None** *[➞comparator](../slots/quantity__comparator.md)*  <sub>OPT</sub>  **[Coding](../classes/Coding.md)**
 *  **None** *[➞unit](../slots/quantity__unit.md)*  <sub>OPT</sub>  **[Coding](../classes/Coding.md)**

## Attributes


### Own

 * [➞code](../slots/coding__code.md)  <sub>OPT</sub>
     * Description: The value of the code itself.
     * range: [String](../types/String.md)
 * [➞display](../slots/coding__display.md)  <sub>OPT</sub>
     * Description: A human-readable name for the code.
     * range: [String](../types/String.md)
 * [➞system](../slots/coding__system.md)  <sub>OPT</sub>
     * Description: The code system where the code is defined.
     * range: [String](../types/String.md)
 * [➞version](../slots/coding__version.md)  <sub>OPT</sub>
     * Description: The version of the code system.
     * range: [String](../types/String.md)
