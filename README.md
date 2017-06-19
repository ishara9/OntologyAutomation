## OntologyAutomation

Based on OwlReady library this is an extention to automatically generate an entire ontology with using some simple semantic templates

To use OntologyAutomation class

## Create instance of it and use definitions inside that class.

`owl = OntologyMaker()

owl.ClassDefiner(mainClasses) #defines all classes
owl.SubClassDefiner(subClasses) #defines all subClasses
owl.updateClassifications(classifiedWords) #defines all induviduals within those classes
owl.PropertyDefiner(mainProperties) #defines all main properties
owl.relationshipBuilder(relationshipSet)  #defines relationships between each objects (individuals)
owl.saveOnto()`
