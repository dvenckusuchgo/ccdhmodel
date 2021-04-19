
# Class: CodeableConcept




URI: [ccdh:CodeableConcept](https://example.org/ccdh/CodeableConcept)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Coding],[Coding]<coding%200..*-++[CodeableConcept&#124;text:string%20%3F],[Identifier]++-%20type%200..1>[CodeableConcept],[Patient]++-%20taxon%200..1>[CodeableConcept],[ResearchSubject]++-%20primary_disease_site%200..1>[CodeableConcept],[ResearchSubject]++-%20primary_disease_type%200..1>[CodeableConcept],[Specimen]++-%20analyte_concentration_method%200..1>[CodeableConcept],[Specimen]++-%20analyte_type%200..1>[CodeableConcept],[Specimen]++-%20cellular_composition%200..1>[CodeableConcept],[Specimen]++-%20general_tissue_morphology%200..1>[CodeableConcept],[Specimen]++-%20matched_normal_flag%200..*>[CodeableConcept],[Specimen]++-%20qualification_status_flag%200..1>[CodeableConcept],[Specimen]++-%20source_material_type%200..1>[CodeableConcept],[Specimen]++-%20specific_tissue_morphology%200..1>[CodeableConcept],[Specimen]++-%20specimen_type%200..1>[CodeableConcept],[Specimen],[ResearchSubject],[Patient],[Identifier])

## Referenced by class

 *  **None** *[➞type](../slots/identifier__type.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞taxon](../slots/patient__taxon.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞primary_disease_site](../slots/researchSubject__primary_disease_site.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞primary_disease_type](../slots/researchSubject__primary_disease_type.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞analyte_concentration_method](../slots/specimen__analyte_concentration_method.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞analyte_type](../slots/specimen__analyte_type.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞cellular_composition](../slots/specimen__cellular_composition.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞general_tissue_morphology](../slots/specimen__general_tissue_morphology.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞matched_normal_flag](../slots/specimen__matched_normal_flag.md)*  <sub>0..*</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞qualification_status_flag](../slots/specimen__qualification_status_flag.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞source_material_type](../slots/specimen__source_material_type.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞specific_tissue_morphology](../slots/specimen__specific_tissue_morphology.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**
 *  **None** *[➞specimen_type](../slots/specimen__specimen_type.md)*  <sub>OPT</sub>  **[CodeableConcept](../classes/CodeableConcept.md)**

## Attributes


### Own

 * [➞coding](../slots/codeableConcept__coding.md)  <sub>0..*</sub>
     * Description: A reference to a code defined by a terminology system
     * range: [Coding](../classes/Coding.md)
 * [➞text](../slots/codeableConcept__text.md)  <sub>OPT</sub>
     * Description: A human language representation of the concept represented by the Coding
     * range: [String](../types/String.md)
