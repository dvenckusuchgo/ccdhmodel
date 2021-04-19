# Auto generated from entities.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-18 20:33
# Schema: CCDH-MVP
#
# id: https://example.org/ccdh/model/MVPv0
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from linkml.utils.metamodelcore import Bool, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CCDH = CurieNamespace('ccdh', 'https://example.org/ccdh/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
TYPES = CurieNamespace('types', 'https://example.org/ccdh/datatypes/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CCDH


# Types
class Url(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "url"
    type_model_uri = CCDH.Url


class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = CCDH.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = CCDH.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = CCDH.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = CCDH.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = CCDH.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = CCDH.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = CCDH.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = CCDH.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = CCDH.Datetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = CCDH.Uriorcurie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = CCDH.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = CCDH.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = CCDH.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = CCDH.Nodeidentifier


# Class references
class EntityId(extended_str):
    pass


class SpecimenId(EntityId):
    pass


class PatientId(EntityId):
    pass


class ResearchSubjectId(EntityId):
    pass


class ProjectId(EntityId):
    pass


@dataclass
class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Entity
    class_class_curie: ClassVar[str] = "ccdh:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CCDH.Entity

    id: Union[str, EntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Specimen(Entity):
    """
    Any material taken as a sample from a biological entity (living or dead), or from a physical object or the
    environment. Specimens are usually collected as an example of their kind, often for use in some investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Specimen
    class_class_curie: ClassVar[str] = "ccdh:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = CCDH.Specimen

    id: Union[str, SpecimenId] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    associated_project: Optional[Union[str, ProjectId]] = None
    specimen_type: Optional[Union[dict, "CodeableConcept"]] = None
    analyte_type: Optional[Union[dict, "CodeableConcept"]] = None
    derived_from_specimen: Optional[Union[Union[str, SpecimenId], List[Union[str, SpecimenId]]]] = empty_list()
    derived_from_subject: Optional[Union[str, PatientId]] = None
    source_material_type: Optional[Union[dict, "CodeableConcept"]] = None
    cellular_composition: Optional[Union[dict, "CodeableConcept"]] = None
    general_tissue_morphology: Optional[Union[dict, "CodeableConcept"]] = None
    specific_tissue_morphology: Optional[Union[dict, "CodeableConcept"]] = None
    current_weight: Optional[Union[Union[dict, "Quantity"], List[Union[dict, "Quantity"]]]] = empty_list()
    current_volume: Optional[Union[Union[dict, "Quantity"], List[Union[dict, "Quantity"]]]] = empty_list()
    analyte_concentration: Optional[Union[dict, "Quantity"]] = None
    analyte_concentration_method: Optional[Union[dict, "CodeableConcept"]] = None
    matched_normal_flag: Optional[Union[Union[dict, "CodeableConcept"], List[Union[dict, "CodeableConcept"]]]] = empty_list()
    qualification_status_flag: Optional[Union[dict, "CodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SpecimenId):
            self.id = SpecimenId(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, Identifier) else Identifier(**v) for v in self.identifier]

        if self.associated_project is not None and not isinstance(self.associated_project, ProjectId):
            self.associated_project = ProjectId(self.associated_project)

        if self.specimen_type is not None and not isinstance(self.specimen_type, CodeableConcept):
            self.specimen_type = CodeableConcept(**self.specimen_type)

        if self.analyte_type is not None and not isinstance(self.analyte_type, CodeableConcept):
            self.analyte_type = CodeableConcept(**self.analyte_type)

        if self.derived_from_specimen is None:
            self.derived_from_specimen = []
        if not isinstance(self.derived_from_specimen, list):
            self.derived_from_specimen = [self.derived_from_specimen]
        self.derived_from_specimen = [v if isinstance(v, SpecimenId) else SpecimenId(v) for v in self.derived_from_specimen]

        if self.derived_from_subject is not None and not isinstance(self.derived_from_subject, PatientId):
            self.derived_from_subject = PatientId(self.derived_from_subject)

        if self.source_material_type is not None and not isinstance(self.source_material_type, CodeableConcept):
            self.source_material_type = CodeableConcept(**self.source_material_type)

        if self.cellular_composition is not None and not isinstance(self.cellular_composition, CodeableConcept):
            self.cellular_composition = CodeableConcept(**self.cellular_composition)

        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, CodeableConcept):
            self.general_tissue_morphology = CodeableConcept(**self.general_tissue_morphology)

        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, CodeableConcept):
            self.specific_tissue_morphology = CodeableConcept(**self.specific_tissue_morphology)

        if self.current_weight is None:
            self.current_weight = []
        if not isinstance(self.current_weight, list):
            self.current_weight = [self.current_weight]
        self.current_weight = [v if isinstance(v, Quantity) else Quantity(**v) for v in self.current_weight]

        if self.current_volume is None:
            self.current_volume = []
        if not isinstance(self.current_volume, list):
            self.current_volume = [self.current_volume]
        self.current_volume = [v if isinstance(v, Quantity) else Quantity(**v) for v in self.current_volume]

        if self.analyte_concentration is not None and not isinstance(self.analyte_concentration, Quantity):
            self.analyte_concentration = Quantity(**self.analyte_concentration)

        if self.analyte_concentration_method is not None and not isinstance(self.analyte_concentration_method, CodeableConcept):
            self.analyte_concentration_method = CodeableConcept(**self.analyte_concentration_method)

        if self.matched_normal_flag is None:
            self.matched_normal_flag = []
        if not isinstance(self.matched_normal_flag, list):
            self.matched_normal_flag = [self.matched_normal_flag]
        self.matched_normal_flag = [v if isinstance(v, CodeableConcept) else CodeableConcept(**v) for v in self.matched_normal_flag]

        if self.qualification_status_flag is not None and not isinstance(self.qualification_status_flag, CodeableConcept):
            self.qualification_status_flag = CodeableConcept(**self.qualification_status_flag)

        super().__post_init__(**kwargs)


@dataclass
class Patient(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Patient
    class_class_curie: ClassVar[str] = "ccdh:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = CCDH.Patient

    id: Union[str, PatientId] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    taxon: Optional[Union[dict, "CodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PatientId):
            self.id = PatientId(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, Identifier) else Identifier(**v) for v in self.identifier]

        if self.taxon is not None and not isinstance(self.taxon, CodeableConcept):
            self.taxon = CodeableConcept(**self.taxon)

        super().__post_init__(**kwargs)


@dataclass
class ResearchSubject(Entity):
    """
    A research subject is the entity of interest in a research study, typically a human being or an animal, but can
    also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not
    traceable to a particular person to protect the subject’s privacy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.ResearchSubject
    class_class_curie: ClassVar[str] = "ccdh:ResearchSubject"
    class_name: ClassVar[str] = "ResearchSubject"
    class_model_uri: ClassVar[URIRef] = CCDH.ResearchSubject

    id: Union[str, ResearchSubjectId] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    associated_project: Optional[Union[Union[str, ProjectId], List[Union[str, ProjectId]]]] = empty_list()
    primary_disease_type: Optional[Union[dict, "CodeableConcept"]] = None
    primary_disease_site: Optional[Union[dict, "CodeableConcept"]] = None
    associated_patient: Optional[Union[str, PatientId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResearchSubjectId):
            self.id = ResearchSubjectId(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, Identifier) else Identifier(**v) for v in self.identifier]

        if self.associated_project is None:
            self.associated_project = []
        if not isinstance(self.associated_project, list):
            self.associated_project = [self.associated_project]
        self.associated_project = [v if isinstance(v, ProjectId) else ProjectId(v) for v in self.associated_project]

        if self.primary_disease_type is not None and not isinstance(self.primary_disease_type, CodeableConcept):
            self.primary_disease_type = CodeableConcept(**self.primary_disease_type)

        if self.primary_disease_site is not None and not isinstance(self.primary_disease_site, CodeableConcept):
            self.primary_disease_site = CodeableConcept(**self.primary_disease_site)

        if self.associated_patient is not None and not isinstance(self.associated_patient, PatientId):
            self.associated_patient = PatientId(self.associated_patient)

        super().__post_init__(**kwargs)


@dataclass
class Project(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Project
    class_class_curie: ClassVar[str] = "ccdh:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CCDH.Project

    id: Union[str, ProjectId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Identifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Identifier
    class_class_curie: ClassVar[str] = "types:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = CCDH.Identifier

    value: Optional[str] = None
    system: Optional[str] = None
    type: Optional[Union[dict, "CodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.system is not None and not isinstance(self.system, str):
            self.system = str(self.system)

        if self.type is not None and not isinstance(self.type, CodeableConcept):
            self.type = CodeableConcept(**self.type)

        super().__post_init__(**kwargs)


@dataclass
class Coding(YAMLRoot):
    """
    A structured representation of a coded/enumerated data value, that includes additional metadata about the code and
    code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Coding
    class_class_curie: ClassVar[str] = "types:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = CCDH.Coding

    code: Optional[str] = None
    display: Optional[str] = None
    system: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        if self.system is not None and not isinstance(self.system, str):
            self.system = str(self.system)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class Quantity(YAMLRoot):
    """
    A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including
    a value and unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Quantity
    class_class_curie: ClassVar[str] = "types:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = CCDH.Quantity

    value: Optional[Decimal] = None
    unit: Optional[Union[dict, Coding]] = None
    comparator: Optional[Union[dict, Coding]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, Decimal):
            self.value = Decimal(self.value)

        if self.unit is not None and not isinstance(self.unit, Coding):
            self.unit = Coding(**self.unit)

        if self.comparator is not None and not isinstance(self.comparator, Coding):
            self.comparator = Coding(**self.comparator)

        super().__post_init__(**kwargs)


@dataclass
class CodeableConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.CodeableConcept
    class_class_curie: ClassVar[str] = "types:CodeableConcept"
    class_name: ClassVar[str] = "CodeableConcept"
    class_model_uri: ClassVar[URIRef] = CCDH.CodeableConcept

    coding: Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]] = empty_list()
    text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.coding is None:
            self.coding = []
        if not isinstance(self.coding, list):
            self.coding = [self.coding]
        self.coding = [v if isinstance(v, Coding) else Coding(**v) for v in self.coding]

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=CCDH.id, name="id", curie=CCDH.curie('id'),
                   model_uri=CCDH.id, domain=None, range=URIRef)

slots.specimen__identifier = Slot(uri=CCDH.identifier, name="specimen__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.specimen__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.specimen__associated_project = Slot(uri=CCDH.associated_project, name="specimen__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH.specimen__associated_project, domain=None, range=Optional[Union[str, ProjectId]])

slots.specimen__specimen_type = Slot(uri=CCDH.specimen_type, name="specimen__specimen_type", curie=CCDH.curie('specimen_type'),
                   model_uri=CCDH.specimen__specimen_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__analyte_type = Slot(uri=CCDH.analyte_type, name="specimen__analyte_type", curie=CCDH.curie('analyte_type'),
                   model_uri=CCDH.specimen__analyte_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__derived_from_specimen = Slot(uri=CCDH.derived_from_specimen, name="specimen__derived_from_specimen", curie=CCDH.curie('derived_from_specimen'),
                   model_uri=CCDH.specimen__derived_from_specimen, domain=None, range=Optional[Union[Union[str, SpecimenId], List[Union[str, SpecimenId]]]])

slots.specimen__derived_from_subject = Slot(uri=CCDH.derived_from_subject, name="specimen__derived_from_subject", curie=CCDH.curie('derived_from_subject'),
                   model_uri=CCDH.specimen__derived_from_subject, domain=None, range=Optional[Union[str, PatientId]])

slots.specimen__source_material_type = Slot(uri=CCDH.source_material_type, name="specimen__source_material_type", curie=CCDH.curie('source_material_type'),
                   model_uri=CCDH.specimen__source_material_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__cellular_composition = Slot(uri=CCDH.cellular_composition, name="specimen__cellular_composition", curie=CCDH.curie('cellular_composition'),
                   model_uri=CCDH.specimen__cellular_composition, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="specimen__general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                   model_uri=CCDH.specimen__general_tissue_morphology, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="specimen__specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                   model_uri=CCDH.specimen__specific_tissue_morphology, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__current_weight = Slot(uri=CCDH.current_weight, name="specimen__current_weight", curie=CCDH.curie('current_weight'),
                   model_uri=CCDH.specimen__current_weight, domain=None, range=Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]])

slots.specimen__current_volume = Slot(uri=CCDH.current_volume, name="specimen__current_volume", curie=CCDH.curie('current_volume'),
                   model_uri=CCDH.specimen__current_volume, domain=None, range=Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]])

slots.specimen__analyte_concentration = Slot(uri=CCDH.analyte_concentration, name="specimen__analyte_concentration", curie=CCDH.curie('analyte_concentration'),
                   model_uri=CCDH.specimen__analyte_concentration, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimen__analyte_concentration_method = Slot(uri=CCDH.analyte_concentration_method, name="specimen__analyte_concentration_method", curie=CCDH.curie('analyte_concentration_method'),
                   model_uri=CCDH.specimen__analyte_concentration_method, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__matched_normal_flag = Slot(uri=CCDH.matched_normal_flag, name="specimen__matched_normal_flag", curie=CCDH.curie('matched_normal_flag'),
                   model_uri=CCDH.specimen__matched_normal_flag, domain=None, range=Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]])

slots.specimen__qualification_status_flag = Slot(uri=CCDH.qualification_status_flag, name="specimen__qualification_status_flag", curie=CCDH.curie('qualification_status_flag'),
                   model_uri=CCDH.specimen__qualification_status_flag, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.patient__identifier = Slot(uri=CCDH.identifier, name="patient__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.patient__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.patient__taxon = Slot(uri=CCDH.taxon, name="patient__taxon", curie=CCDH.curie('taxon'),
                   model_uri=CCDH.patient__taxon, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.researchSubject__identifier = Slot(uri=CCDH.identifier, name="researchSubject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.researchSubject__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.researchSubject__associated_project = Slot(uri=CCDH.associated_project, name="researchSubject__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH.researchSubject__associated_project, domain=None, range=Optional[Union[Union[str, ProjectId], List[Union[str, ProjectId]]]])

slots.researchSubject__primary_disease_type = Slot(uri=CCDH.primary_disease_type, name="researchSubject__primary_disease_type", curie=CCDH.curie('primary_disease_type'),
                   model_uri=CCDH.researchSubject__primary_disease_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.researchSubject__primary_disease_site = Slot(uri=CCDH.primary_disease_site, name="researchSubject__primary_disease_site", curie=CCDH.curie('primary_disease_site'),
                   model_uri=CCDH.researchSubject__primary_disease_site, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.researchSubject__associated_patient = Slot(uri=CCDH.associated_patient, name="researchSubject__associated_patient", curie=CCDH.curie('associated_patient'),
                   model_uri=CCDH.researchSubject__associated_patient, domain=None, range=Optional[Union[str, PatientId]])

slots.identifier__value = Slot(uri=CCDH.value, name="identifier__value", curie=CCDH.curie('value'),
                   model_uri=CCDH.identifier__value, domain=None, range=Optional[str])

slots.identifier__system = Slot(uri=CCDH.system, name="identifier__system", curie=CCDH.curie('system'),
                   model_uri=CCDH.identifier__system, domain=None, range=Optional[str])

slots.identifier__type = Slot(uri=CCDH.type, name="identifier__type", curie=CCDH.curie('type'),
                   model_uri=CCDH.identifier__type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.coding__code = Slot(uri=CCDH.code, name="coding__code", curie=CCDH.curie('code'),
                   model_uri=CCDH.coding__code, domain=None, range=Optional[str])

slots.coding__display = Slot(uri=CCDH.display, name="coding__display", curie=CCDH.curie('display'),
                   model_uri=CCDH.coding__display, domain=None, range=Optional[str])

slots.coding__system = Slot(uri=CCDH.system, name="coding__system", curie=CCDH.curie('system'),
                   model_uri=CCDH.coding__system, domain=None, range=Optional[str])

slots.coding__version = Slot(uri=CCDH.version, name="coding__version", curie=CCDH.curie('version'),
                   model_uri=CCDH.coding__version, domain=None, range=Optional[str])

slots.quantity__value = Slot(uri=CCDH.value, name="quantity__value", curie=CCDH.curie('value'),
                   model_uri=CCDH.quantity__value, domain=None, range=Optional[Decimal])

slots.quantity__unit = Slot(uri=CCDH.unit, name="quantity__unit", curie=CCDH.curie('unit'),
                   model_uri=CCDH.quantity__unit, domain=None, range=Optional[Union[dict, Coding]])

slots.quantity__comparator = Slot(uri=CCDH.comparator, name="quantity__comparator", curie=CCDH.curie('comparator'),
                   model_uri=CCDH.quantity__comparator, domain=None, range=Optional[Union[dict, Coding]])

slots.codeableConcept__coding = Slot(uri=CCDH.coding, name="codeableConcept__coding", curie=CCDH.curie('coding'),
                   model_uri=CCDH.codeableConcept__coding, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.codeableConcept__text = Slot(uri=CCDH.text, name="codeableConcept__text", curie=CCDH.curie('text'),
                   model_uri=CCDH.codeableConcept__text, domain=None, range=Optional[str])

slots.Specimen_id = Slot(uri=CCDH.id, name="Specimen_id", curie=CCDH.curie('id'),
                   model_uri=CCDH.Specimen_id, domain=Specimen, range=Union[str, SpecimenId])

slots.Patient_id = Slot(uri=CCDH.id, name="Patient_id", curie=CCDH.curie('id'),
                   model_uri=CCDH.Patient_id, domain=Patient, range=Union[str, PatientId])

slots.ResearchSubject_id = Slot(uri=CCDH.id, name="ResearchSubject_id", curie=CCDH.curie('id'),
                   model_uri=CCDH.ResearchSubject_id, domain=ResearchSubject, range=Union[str, ResearchSubjectId])

slots.Project_id = Slot(uri=CCDH.id, name="Project_id", curie=CCDH.curie('id'),
                   model_uri=CCDH.Project_id, domain=Project, range=Union[str, ProjectId])
