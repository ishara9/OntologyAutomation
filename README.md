# OntologyAutomation

Based on OwlReady library this is an extention to automatically generate an entire ontology with using some simple semantic templates

To use OntologyAutomation class

## Create instance of it and use definitions inside that class.

`owl = OntologyMaker()`
 #defines all classes
`owl.ClassDefiner(mainClasses)`
#defines all subClasses
`owl.SubClassDefiner(subClasses)` 
#defines all induviduals within those classes
`owl.updateClassifications(classifiedWords) `
#defines all main properties
`owl.PropertyDefiner(mainProperties)`
#defines relationships between each objects (individuals)
`owl.relationshipBuilder(relationshipSet)`
#Saving
owl.saveOnto()`
