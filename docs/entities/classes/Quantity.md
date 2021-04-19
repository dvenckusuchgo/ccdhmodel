
# Class: Quantity


A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including a value and unit.

URI: [ccdh:Quantity](https://example.org/ccdh/Quantity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Coding]<comparator%200..1-++[Quantity&#124;value:decimal%20%3F],[Coding]<unit%200..1-++[Quantity],[Specimen]++-%20analyte_concentration%200..1>[Quantity],[Specimen]++-%20current_volume%200..*>[Quantity],[Specimen]++-%20current_weight%200..*>[Quantity],[Specimen],[Coding])

## Referenced by class

 *  **None** *[➞analyte_concentration](../slots/specimen__analyte_concentration.md)*  <sub>OPT</sub>  **[Quantity](../classes/Quantity.md)**
 *  **None** *[➞current_volume](../slots/specimen__current_volume.md)*  <sub>0..*</sub>  **[Quantity](../classes/Quantity.md)**
 *  **None** *[➞current_weight](../slots/specimen__current_weight.md)*  <sub>0..*</sub>  **[Quantity](../classes/Quantity.md)**

## Attributes


### Own

 * [➞comparator](../slots/quantity__comparator.md)  <sub>OPT</sub>
     * Description: How to understand the value  . . .   < | <= | >= | >
     * range: [Coding](../classes/Coding.md)
 * [➞unit](../slots/quantity__unit.md)  <sub>OPT</sub>
     * Description: Unit representation (e.g. mg, mL)
     * range: [Coding](../classes/Coding.md)
 * [➞value](../slots/quantity__value.md)  <sub>OPT</sub>
     * Description: Numerical value (with implicit precision)
     * range: [Decimal](../types/Decimal.md)
