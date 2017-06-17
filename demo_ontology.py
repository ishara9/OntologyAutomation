from OntologyAutomation import *

# Intoduce clases in list
mainClasses = ['disease', 'cure', 'cause', 'prevention', 'symptom', 'treatment','nn']
# Intoduce subclases in list
subClasses = [['cancer','disease'],['inflammation','disease']]
# Introduce properties in list with domain and range
mainProperties = [['caused_by', 'cancer', 'inflammation']]
# Introduce word concepts(instances) with classifications
classifiedWords = [['hepatitis', 'inflammation'],['cirrhosis', 'cancer']]
# semantic template
relationshipSet = [['cirrhosis', 'caused_by', 'hepatitis']]

# CALLING FORMAT
owl = OntologyMaker()
owl.ClassDefiner(mainClasses)
owl.SubClassDefiner(subClasses)
owl.updateClassifications(classifiedWords)
owl.PropertyDefiner(mainProperties)
owl.relationshipBuilder(relationshipSet)
print(owl.onto.properties)
owl.saveOnto()
