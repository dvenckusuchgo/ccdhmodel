
# Class: Project




URI: [ccdh:Project](https://example.org/ccdh/Project)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ResearchSubject]-%20associated_project%200..*>[Project&#124;id(pk):string],[Specimen]-%20associated_project%200..1>[Project],[Entity]^-[Project],[Specimen],[ResearchSubject],[Entity])

## Parents

 *  is_a: [Entity](../classes/Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **None** *[➞associated_project](../slots/researchSubject__associated_project.md)*  <sub>0..*</sub>  **[Project](../classes/Project.md)**
 *  **None** *[➞associated_project](../slots/specimen__associated_project.md)*  <sub>OPT</sub>  **[Project](../classes/Project.md)**

## Attributes


### Own

 * [Project➞id](../slots/Project_id.md)  <sub>REQ</sub>
     * range: [String](../types/String.md)
