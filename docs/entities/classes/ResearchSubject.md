
# Class: ResearchSubject


A research subject is the entity of interest in a research study, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.

URI: [ccdh:ResearchSubject](https://example.org/ccdh/ResearchSubject)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Patient]<associated_patient%200..1-%20[ResearchSubject&#124;id(pk):string],[CodeableConcept]<primary_disease_site%200..1-++[ResearchSubject],[CodeableConcept]<primary_disease_type%200..1-++[ResearchSubject],[Project]<associated_project%200..*-%20[ResearchSubject],[Identifier]<identifier%200..*-++[ResearchSubject],[Entity]^-[ResearchSubject],[Project],[Patient],[Identifier],[Entity],[CodeableConcept])

## Parents

 *  is_a: [Entity](../classes/Entity.md) - Any resource that has its own identifier

## Referenced by class


## Attributes


### Own

 * [ResearchSubject➞id](../slots/ResearchSubject_id.md)  <sub>REQ</sub>
     * Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
     * range: [String](../types/String.md)
 * [➞associated_patient](../slots/researchSubject__associated_patient.md)  <sub>OPT</sub>
     * Description: A reference to the Patient that is this ResearchSubject
     * range: [Patient](../classes/Patient.md)
 * [➞associated_project](../slots/researchSubject__associated_project.md)  <sub>0..*</sub>
     * Description: A reference to the Project(s) of which this ResearchSubject is a member
     * range: [Project](../classes/Project.md)
 * [➞identifier](../slots/researchSubject__identifier.md)  <sub>0..*</sub>
     * Description: A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier. 
     * range: [Identifier](../classes/Identifier.md)
 * [➞primary_disease_site](../slots/researchSubject__primary_disease_site.md)  <sub>OPT</sub>
     * Description: The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general categories.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞primary_disease_type](../slots/researchSubject__primary_disease_type.md)  <sub>OPT</sub>
     * Description: The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). 
     * range: [CodeableConcept](../classes/CodeableConcept.md)
