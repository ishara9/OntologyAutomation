from OntologyAutomation import *

# Intoduce clases in list
mainClasses = ['disease', 'cure', 'cause', 'prevention', 'symptom', 'treatment','nn'] #[Class, Class, ..]
# Intoduce subclases in list
subClasses = [['cancer','disease'],['inflammation','disease']]  # [Subclass, ParentClass]
# Introduce properties in list with domain and range
mainProperties = [['caused_by', 'cancer', 'inflammation']]  # [Predicate, Subject's Class, Object's Class]
# Introduce word concepts(instances) with classifications
classifiedWords = [['hepatitis', 'inflammation'],['cirrhosis', 'cancer']] # [individual, Class]
# semantic template
relationshipSet = [['cirrhosis', 'caused_by', 'hepatitis']]  # [Subject, Predicate, Object]

# CALLING FORMAT
owl = OntologyMaker()
owl.ClassDefiner(mainClasses)
owl.SubClassDefiner(subClasses)
owl.updateClassifications(classifiedWords)
owl.PropertyDefiner(mainProperties)
owl.relationshipBuilder(relationshipSet)
print(owl.onto.properties)
owl.saveOnto()
