from OntologyAutomation import *

# Intoduce clases in list
mainClasses = ['information_systems', 'computer_methodology', 'social_and_behavioral_sciences'] #[Class, Class, ..]
# Intoduce subclases in list
subClasses = [['information_search_and_retrieval','information_systems'],
              ['distributed_systems','computer_methodology'],
              ['distributed_artificial_intelligence_and_multi_agent_systems','computer_methodology']]  # [Subclass, ParentClass]
# Introduce properties in list with domain and range
mainProperties = [['has_keyword', 'Thing', '']]  # [Predicate, Subject's Class, Object's Class]
# Introduce word concepts(instances) with classifications
classifiedWords = [['agent', 'distributed_artificial_intelligence_and_multi_agent_systems'],
                   ['agent_id', 'information_search_and_retrieval'],
                   ['agent_number', 'information_search_and_retrieval']] # [individual, Class]
# semantic template
relationshipSet = [['agent', 'has_keyword', 'agent_id'],['agent', 'has_keyword', 'agent_number']]  # [Subject, Predicate, Object]

# CALLING FORMAT
owl = OntologyMaker()
owl.ClassDefiner(mainClasses)
owl.SubClassDefiner(subClasses)
owl.updateClassifications(classifiedWords)
owl.PropertyDefiner(mainProperties)
owl.relationshipBuilder(relationshipSet)
print(owl.onto.properties)
owl.saveOnto()
