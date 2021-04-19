
# Class: Patient




URI: [ccdh:Patient](https://example.org/ccdh/Patient)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CodeableConcept]<taxon%200..1-++[Patient&#124;id(pk):string],[Identifier]<identifier%200..*-++[Patient],[ResearchSubject]-%20associated_patient%200..1>[Patient],[Specimen]-%20derived_from_subject%200..1>[Patient],[Entity]^-[Patient],[Specimen],[ResearchSubject],[Identifier],[Entity],[CodeableConcept])

## Parents

 *  is_a: [Entity](../classes/Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **None** *[➞associated_patient](../slots/researchSubject__associated_patient.md)*  <sub>OPT</sub>  **[Patient](../classes/Patient.md)**
 *  **None** *[➞derived_from_subject](../slots/specimen__derived_from_subject.md)*  <sub>OPT</sub>  **[Patient](../classes/Patient.md)**

## Attributes


### Own

 * [Patient➞id](../slots/Patient_id.md)  <sub>REQ</sub>
     * Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
     * range: [String](../types/String.md)
 * [➞identifier](../slots/patient__identifier.md)  <sub>0..*</sub>
     * Description: A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems. 
     * range: [Identifier](../classes/Identifier.md)
 * [➞taxon](../slots/patient__taxon.md)  <sub>OPT</sub>
     * Description: The taxonomic group (e.g. species) of the patient.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
