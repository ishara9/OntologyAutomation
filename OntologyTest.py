from owlready import *
import types

class OntologyMakerTest:

    def __init__(self):
        ontology_name = "test.owl"
        ont_url = "http://test.org/test.owl"
        local_path = "ontologies"
        # owlready_ontology = get_ontology("http://srilankasquash.com/projects/onto/beyond.owl").load()
        self.onto = Ontology(ont_url)
        onto_path.append(local_path)
        self.ontoName = str(self.onto.load())
        self.ontology_version = 0.0
        for annotation_property, annotation_value, annotation_lang in ANNOTATIONS[self.onto].items():
            self.ontology_version = float(annotation_value)
            # print(self.ontology_version)
        # print("Ontology Version: " + str(self.ontology_version + 1))
        ANNOTATIONS[self.onto].del_annotation("versionInfo", str(self.ontology_version))
        onto_value = float(self.ontology_version) + 1
        ANNOTATIONS[self.onto].add_annotation("versionInfo", str(onto_value))
        self.ontology_version = onto_value

        prob_not_found = True
        for annotation in self.onto.annotation_properties:
            if str(annotation) == "probabilityValue":
                prob_not_found = False
        if prob_not_found:
            NewClass = types.new_class("probabilityValue", (AnnotationProperty,), kwds={"ontology": self.onto})

        # TO instantiate classes at the class declaration use following
        # print(self.onto.annotation_properties)
        # InitialClasses = ['cause', 'disease', 'biology', 'nn', 'microorganism', 'symptom']
        # self.ClassDefiner(InitialClasses)
        # for inC in InitialClasses:
        #     NewClass = types.new_class(inC, (Thing,), kwds={"ontology": self.onto})

    # Add New Classification type
    def ClassDefiner(self,mainClasses):
        for eachclass in mainClasses:
            class_found = True
            for cc in set(self.onto.classes):
                if eachclass == str(cc):
                    class_found = False
            if class_found:
                NewClass = types.new_class(eachclass, (Thing,), kwds={"ontology": self.onto})

    # Add New SubClassDefiner type
    def SubClassDefiner(self, subClasses):
        for eachclass in subClasses:
            sub_class_not_found = True
            for cc in set(self.onto.classes):
                if eachclass[0]==str(cc):
                    sub_class_not_found = False
            for cc in set(self.onto.classes):
                if eachclass[1] == str(cc) and sub_class_not_found:
                    NewClass = types.new_class(eachclass[0], (cc,), kwds={"ontology": self.onto})


    # Add New Property
    def PropertyDefiner(self, mainProperties):
        for eachRelation in mainProperties:
            relation_found = True
            for cc in set(self.onto.properties):
                if eachRelation[0] == str(cc):
                    relation_found = False
            for instance_is in set(self.onto.classes):
                if eachRelation[0] == str(instance_is):
                    relation_found = False
                if eachRelation[1] == str(instance_is):
                    domain = instance_is
                if eachRelation[2] == str(instance_is):
                    range = instance_is
            if relation_found:
                Prop = types.new_class(eachRelation[0], (Property,), kwds={"ontology": self.onto})
                Prop.domain = [domain]
                Prop.range = [range]

    def InversePropertyDefiner(self, mainProperties):
        for eachRelation in mainProperties:
            relation_found = True
            for cc in set(self.onto.properties):
                if eachRelation[0] == str(cc):
                    relation_found = False
                if eachRelation[3] == str(cc):
                    inverse_property = cc
            for instance_is in set(self.onto.classes):
                if eachRelation[0] == str(instance_is):
                    relation_found = False
                if eachRelation[1] == str(instance_is):
                    domain = instance_is
                if eachRelation[2] == str(instance_is):
                    range = instance_is

            if relation_found:
                Prop = types.new_class(eachRelation[0], (Property,), kwds={"ontology": self.onto})
                Prop.domain = [range]
                Prop.range = [domain]
                Prop.inverse_property = inverse_property

    # Update new Tagged Classified sets
    def updateClassifications(self, classifiedWords):
        for eachWord in classifiedWords:
            individual_not_found = True
            for instance_is in set(self.onto.instances):
                if eachWord[0] == str(instance_is):
                    individual_not_found = False
            for instance_is in set(self.onto.classes):
                if eachWord[0] == str(instance_is):
                    individual_not_found = False
            if individual_not_found:
                for thisClass in self.onto.classes:
                    if eachWord[1] == str(thisClass):
                        random = thisClass(eachWord[0])


    # Use to build Relationships from Tripples
    def relationshipBuilder(self, relationshipSet):
        # try:
            for eachRelation in relationshipSet:
                for thisInstance in self.onto.instances:
                    if eachRelation[0] == str(thisInstance):
                        subject = thisInstance
                    else:
                        pass
                    if eachRelation[2] == str(thisInstance):
                        object = thisInstance
                for thisProperty in self.onto.properties:
                    if eachRelation[1] == str(thisProperty):
                        predicate = thisProperty

                method = str(predicate)

                relation_not_found = True
                for cc in set(getattr(subject, method)):
                    if str(object) == str(cc):
                        relation_not_found = False
                if relation_not_found:
                    getattr(subject, method).append(object)
                    # versionInfo use number of times relationship occurs
                    ANNOTATIONS[subject, predicate, object].add_annotation("versionInfo", "1.0")
                    # label use version_at_begining
                    ANNOTATIONS[subject, predicate, object].add_annotation("label", str(self.ontology_version))
                    # comment use probabilityValue
                    ANNOTATIONS[subject, predicate, object].add_annotation("probabilityValue", "1.0")
                    # priorVersion use priorVersion of ontology
                    ANNOTATIONS[subject, predicate, object].add_annotation("priorVersion", str(self.ontology_version))
                    # deprecated use to track adjustment
                    ANNOTATIONS[subject, predicate, object].add_annotation("deprecated", "0.0")
                    # print("---------------------------------------------------------------")
                else:
                    version_value = "0.0"
                    version_at_begining = "0.0"
                    probabilityValue_at_begining = "0.0"
                    previous_ontology_version = 0
                    adjusment = 0
                    for annotation_property, annotation_value, annotation_lang in ANNOTATIONS[
                        subject, predicate, object].items():
                        if str(annotation_property) == "versionInfo":
                            version_value = annotation_value
                        if str(annotation_property) == "label":
                            version_at_begining = annotation_value
                        if str(annotation_property) == "probabilityValue":
                            probabilityValue_at_begining = annotation_value
                        if str(annotation_property) == "priorVersion":
                            previous_ontology_version = float(annotation_value)
                        if str(annotation_property) == "deprecated":
                            adjusment = float(annotation_value)
                            ANNOTATIONS[subject, predicate, object].del_annotation("deprecated", str(adjusment))
                    ANNOTATIONS[subject, predicate, object].del_annotation("versionInfo", version_value)
                    value = float(version_value) + 1
                    ANNOTATIONS[subject, predicate, object].add_annotation("versionInfo", str(value))
                    if float(self.ontology_version) == previous_ontology_version:
                        adjusment += 1
                    else:
                        ANNOTATIONS[subject, predicate, object].del_annotation("priorVersion",
                                                                               str(previous_ontology_version))
                        ANNOTATIONS[subject, predicate, object].add_annotation("priorVersion",
                                                                               str(self.ontology_version))

                    ANNOTATIONS[subject, predicate, object].add_annotation("deprecated", str(adjusment))
                    # caculate probabilityValue
                    probabilityValue = (float(value)) / (float(self.ontology_version + adjusment) - (float(version_at_begining) - 1))
                    # print("adjustment: " + str(adjusment) + " previous_ontology_version: " + str(
                    #     previous_ontology_version) + " ontology version: " + str(self.ontology_version))
                    # print("value: " + str(value) + " probabilityValue " + str(probabilityValue))
                    ANNOTATIONS[subject, predicate, object].del_annotation("probabilityValue", probabilityValue_at_begining)
                    ANNOTATIONS[subject, predicate, object].add_annotation("probabilityValue", str(probabilityValue))

            # print()
        # except Exception as e:
        #     print("Error Saving to Ontology: " + str(relationshipSet))
        #     print(e)

    # def rel_builder(self,relationshipSet):
    #     add_relation(relationshipSet[0][0],relationshipSet[0][1],relationshipSet[0][2])

    #Ontology save
    def saveOnto(self):
        self.onto.save()

# Intoduce clases in list
mainClasses = ['Disease', 'Cure', 'Cause', 'Prevention', 'Symptom', 'Treatment']

# Introduce properties in list with domain and range
mainProperties = [['has_cause', 'Disease', 'Cause']]
inverseProperties = [['is_cause_by', 'Disease', 'Cause','has_cause']]

# Introduce word concepts(instances) with classifications
classifiedWords = [['influenza', 'Disease'], ['HIV', 'Disease'], ['arthritis', 'Disease'],
                   ['immune_system_dysfunction', 'Symptom'], ['injury', 'Cause']]

# semantic template
relationshipSet = [['arthritis', 'has_cause', 'injury']]



# CALLING FORMAT
owl = OntologyMakerTest()
owl.ClassDefiner(mainClasses)
owl.updateClassifications(classifiedWords)
owl.PropertyDefiner(mainProperties)
owl.InversePropertyDefiner(inverseProperties)
owl.relationshipBuilder(relationshipSet)
# owl.rel_builder(relationshipSet)



# class Drug(Thing):
#     ontology = owl.onto

# class Ingredient(Thing):
#     ontology = owl.onto


# class has_for_ingredient(Property):
#     ontology = owl.onto
#     domain   = [Drug]
#     range    = [Ingredient]

# class is_ingredient_of(Property):
#     ontology         = owl.onto
#     domain           = [Ingredient]
#     range            = [Drug]
#     inverse_property = has_for_ingredient

# Drug = types.new_class("Drug1", (Thing,), kwds={"ontology": owl.onto})
# Ingredient = types.new_class("Ingredient1", (Thing,), kwds={"ontology": owl.onto})
# has_for_ingredient = types.new_class("has_for_ingredient", (Property,), kwds={"ontology": owl.onto})
# has_for_ingredient.domain = [Drug]
# has_for_ingredient.range = [Ingredient]
#
# is_ingredient_of = types.new_class("is_ingredient_of", (Property,), kwds={"ontology": owl.onto})
# is_ingredient_of.domain = [Ingredient]
# is_ingredient_of.range = [Drug]
# is_ingredient_of.inverse_property = has_for_ingredient





owl.saveOnto()