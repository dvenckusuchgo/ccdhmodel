
# Class: Specimen


Any material taken as a sample from a biological entity (living or dead), or from a physical object or the environment. Specimens are usually collected as an example of their kind, often for use in some investigation.

URI: [ccdh:Specimen](https://example.org/ccdh/Specimen)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CodeableConcept]<qualification_status_flag%200..1-++[Specimen&#124;id(pk):string],[CodeableConcept]<matched_normal_flag%200..*-++[Specimen],[CodeableConcept]<analyte_concentration_method%200..1-++[Specimen],[Quantity]<analyte_concentration%200..1-++[Specimen],[Quantity]<current_volume%200..*-++[Specimen],[Quantity]<current_weight%200..*-++[Specimen],[CodeableConcept]<specific_tissue_morphology%200..1-++[Specimen],[CodeableConcept]<general_tissue_morphology%200..1-++[Specimen],[CodeableConcept]<cellular_composition%200..1-++[Specimen],[CodeableConcept]<source_material_type%200..1-++[Specimen],[Patient]<derived_from_subject%200..1-%20[Specimen],[Specimen]<derived_from_specimen%200..*-%20[Specimen],[CodeableConcept]<analyte_type%200..1-++[Specimen],[CodeableConcept]<specimen_type%200..1-++[Specimen],[Project]<associated_project%200..1-%20[Specimen],[Identifier]<identifier%200..*-++[Specimen],[Entity]^-[Specimen],[Quantity],[Project],[Patient],[Identifier],[Entity],[CodeableConcept])

## Parents

 *  is_a: [Entity](../classes/Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **None** *[➞derived_from_specimen](../slots/specimen__derived_from_specimen.md)*  <sub>0..*</sub>  **[Specimen](../classes/Specimen.md)**

## Attributes


### Own

 * [Specimen➞id](../slots/Specimen_id.md)  <sub>REQ</sub>
     * Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
     * range: [String](../types/String.md)
 * [➞analyte_concentration](../slots/specimen__analyte_concentration.md)  <sub>OPT</sub>
     * Description: The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'analyte', or an 'aliquot' derived from an analyte). e.g. the concentration of DNA in a specimen created through extracting DNA from a blood sample.
     * range: [Quantity](../classes/Quantity.md)
 * [➞analyte_concentration_method](../slots/specimen__analyte_concentration_method.md)  <sub>OPT</sub>
     * Description: The method used to determine the concentration of purified analyte  within a solution.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞analyte_type](../slots/specimen__analyte_type.md)  <sub>OPT</sub>
     * Description: When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞associated_project](../slots/specimen__associated_project.md)  <sub>OPT</sub>
     * Description: The Project associated with the specimen.
     * range: [Project](../classes/Project.md)
 * [➞cellular_composition](../slots/specimen__cellular_composition.md)  <sub>OPT</sub>
     * Description: The cellular composition of the sample
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞current_volume](../slots/specimen__current_volume.md)  <sub>0..*</sub>
     * Description: The current total volume of the specimen, at the time of recording.
     * range: [Quantity](../classes/Quantity.md)
 * [➞current_weight](../slots/specimen__current_weight.md)  <sub>0..*</sub>
     * Description: The current weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).
     * range: [Quantity](../classes/Quantity.md)
 * [➞derived_from_specimen](../slots/specimen__derived_from_specimen.md)  <sub>0..*</sub>
     * Description: A source/parent specimen from which this one was directly derived.
     * range: [Specimen](../classes/Specimen.md)
 * [➞derived_from_subject](../slots/specimen__derived_from_subject.md)  <sub>OPT</sub>
     * Description: The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.
     * range: [Patient](../classes/Patient.md)
 * [➞general_tissue_morphology](../slots/specimen__general_tissue_morphology.md)  <sub>OPT</sub>
     * Description: A term describing at a high-level the kind of tissue collected in a specimen, with respect to disease status or proximity to tumor tissue (e.g. is it normal, abnormal, tumor, tumor-adjacent). 

     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞identifier](../slots/specimen__identifier.md)  <sub>0..*</sub>
     * Description: A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). 
     * range: [Identifier](../classes/Identifier.md)
 * [➞matched_normal_flag](../slots/specimen__matched_normal_flag.md)  <sub>0..*</sub>
     * Description: A flag indicating that there is no matched normal aliquot for this case that can be used for variant calling purposes.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞qualification_status_flag](../slots/specimen__qualification_status_flag.md)  <sub>OPT</sub>
     * Description: A flag indicating whether the specimen is qualified or disqualified for data analysis in a study.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞source_material_type](../slots/specimen__source_material_type.md)  <sub>OPT</sub>
     * Description: The general kind of material from which the specimen was derived, indicating the physical nature of the source material. 
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞specific_tissue_morphology](../slots/specimen__specific_tissue_morphology.md)  <sub>OPT</sub>
     * Description: A term describing the specific pathology exhibited by the tissue in a specimen.
     * range: [CodeableConcept](../classes/CodeableConcept.md)
 * [➞specimen_type](../slots/specimen__specimen_type.md)  <sub>OPT</sub>
     * Description: The high-level type of the specimen, based on its how it has been derived from the original extracted sample. 

     * range: [CodeableConcept](../classes/CodeableConcept.md)
