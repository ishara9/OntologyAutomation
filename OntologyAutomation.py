from owlready import *
import types

class OntologyMaker:

    def __init__(self):
        ontology_name ="intel.owl"
        ont_url = "http://test.org/intel.owl"
        local_path = "ontologies"
        self.onto = Ontology(ont_url)
        onto_path.append(local_path)
        self.ontoName = str(self.onto.load())
        self.ontology_version =0.0
        for annotation_property, annotation_value, annotation_lang in ANNOTATIONS[self.onto].items():
                self.ontology_version = float(annotation_value)
                print(self.ontology_version)
        print("Ontology Version: "+str(self.ontology_version+1))
        ANNOTATIONS[self.onto].del_annotation("versionInfo", str(self.ontology_version))
        onto_value = float(self.ontology_version)+1
        ANNOTATIONS[self.onto].add_annotation("versionInfo", str(onto_value))
        self.ontology_version =onto_value
        InitialClasses = ['hardware', 'network', 'computer_methodology']
        self.ClassDefiner(InitialClasses)
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
                # print(cc)
                if eachclass[0]==str(cc):
                    sub_class_not_found = False

            for cc in set(self.onto.classes):
                if eachclass[1] == str(cc) and sub_class_not_found:

                    NewClass = types.new_class(eachclass[0], (cc,), kwds={"ontology": self.onto})



    # Update new Tagged Classified sets
    def updateClassifications(self, classifiedWords):
        for eachWord in classifiedWords:
            individual_found = True
            for instance_is in set(self.onto.instances):
                if eachWord[0] == str(instance_is):
                    individual_found = False
            for instance_is in set(self.onto.classes):
                if eachWord[0] == str(instance_is):
                    individual_found = False
            if individual_found:
                for thisClass in self.onto.classes:
                    if eachWord[1] == str(thisClass):
                        eachWord[0] = thisClass(eachWord[0])


    print()

    # Update new Tagged Classified sets
    def updateClassifications(self, classifiedWords):
        for eachWord in classifiedWords:
            eachWordName = str(self.ontoName + "." + str(eachWord[0]))
            individual_found = True
            for instance_is in set(self.onto.instances):
                # print("INSTANCE PRINTING : " +str(eachWord[0]) + " Matching: "+str(instance_is))
                # print(instance_is)
                # print("EACH WORD")
                # print(eachWord[0])
                if eachWord[0] == str(instance_is):
                    # print("WORKING")
                    individual_found = False
            for instance_is in set(self.onto.classes):
                # print("INSTANCE PRINTING : " +str(eachWord[0]) + " Matching: "+str(instance_is))
                # print(instance_is)
                # print("EACH WORD")
                # print(eachWord[0])
                if eachWord[0] == str(instance_is):
                    # print("WORKING")
                    individual_found = False

            if individual_found:
                # print("woriking new if: " + str(eachWord))
                # if eachWordName.lower() not in str(self.onto.instances).lower():
                for thisClass in self.onto.classes:
                    if eachWord[1] == str(thisClass):
                        eachWord[0] = thisClass(eachWord[0])
                        print('New Instance Created ' + str(eachWord[0]))
                        # print('updateClassifications')

    # Use to build Relationships from Tripples
    def relationshipBuilder(self, relationshipSet):
        try:
            #     subject=""
            #     object=""
            #     print("relationshipBuilder Executed")
            for eachRelation in relationshipSet:

                eachRelationName = str(self.ontoName + "." + str(eachRelation[0]))
                for thisInstance in self.onto.instances:
                    # print("thisInstance : " + str(thisInstance))
                    if eachRelation[0] == str(thisInstance):
                        # print("eachRelation 0 "+ str(eachRelation[0]))
                        subject = thisInstance
                    else:
                        # print(thisInstance)
                        pass
                    if eachRelation[2] == str(thisInstance):
                        # print("eachRelation 2 " + str(eachRelation[2]))
                        object = thisInstance
                for thisProperty in self.onto.properties:
                    if eachRelation[1] == str(thisProperty):
                        # print("eachRelation 1 " + str(eachRelation[1]))
                        predicate = thisProperty
                        # print(predicate)
                        # predicate.append(object)

                # pred =types.new_class(eachRelation[1], (property,), kwds={"ontology": self.onto})
                # sub = types.new_class(eachRelation[0], (pr,), kwds={"ontology": self.onto})
                # obj = types.new_class(eachRelation[2], (Annotations,), kwds={"ontology": self.onto})

                method = str(predicate)
                # print("Method : "+ method)
                # print("Inside ontology : "+str(getattr(subject, method)))

                ObjectName = str(self.ontoName + "." + str(object))

                relation_found = True
                for cc in set(getattr(subject, method)):
                    if str(object) == str(cc):
                        relation_found = False
                # if relationName.lower() not in str(self.onto.properties).lower():
                if relation_found:

                    # print("Object : " + str(ObjectName))
                    # print(str(self.onto.instances))
                    # if ObjectName not in str(getattr(subject, method)):
                    # print("Executed!!!")
                    # for annotation_property, annotation_value, annotation_lang in ANNOTATIONS[subject].items():
                    # sub_version_value = float(self.ontology_version) + 1
                    #     print(sub_version_value)
                    # ANNOTATIONS[subject].add_annotation("versionInfo", sub_version_value)

                    getattr(subject, method).append(object)
                    # versionInfo use number of times relationship occurs
                    ANNOTATIONS[subject, predicate, object].add_annotation("versionInfo", "1.0")
                    # label use version_at_begining
                    ANNOTATIONS[subject, predicate, object].add_annotation("label", str(self.ontology_version))
                    # comment use probability
                    ANNOTATIONS[subject, predicate, object].add_annotation("probability", "1.0")
                    # priorVersion use priorVersion of ontology
                    ANNOTATIONS[subject, predicate, object].add_annotation("priorVersion", str(self.ontology_version))
                    # deprecated use to track adjustment
                    ANNOTATIONS[subject, predicate, object].add_annotation("deprecated", "0.0")
                    print("---------------------------------------------------------------")
                else:
                    version_value = ""
                    version_at_begining = ""
                    probability_at_begining = ""
                    previous_ontology_version = 0
                    adjusment = 0
                    for annotation_property, annotation_value, annotation_lang in ANNOTATIONS[
                        subject, predicate, object].items():
                        if str(annotation_property) == "versionInfo":
                            version_value = annotation_value
                            # print(annotation_value)
                        if str(annotation_property) == "label":
                            version_at_begining = annotation_value
                            # print(annotation_value)
                        if str(annotation_property) == "probability":
                            probability_at_begining = annotation_value
                        if str(annotation_property) == "priorVersion":
                            previous_ontology_version = float(annotation_value)
                        if str(annotation_property) == "deprecated":
                            adjusment = float(annotation_value)
                            ANNOTATIONS[subject, predicate, object].del_annotation("deprecated", str(adjusment))
                            # print(annotation_value)
                            # print("Annotaion: "+str(annotation_property)+" "+ str(annotation_value)+" "+ str(annotation_lang))

                    # print("version_value: " + version_value)
                    ANNOTATIONS[subject, predicate, object].del_annotation("versionInfo", version_value)

                    value = float(version_value) + 1
                    ANNOTATIONS[subject, predicate, object].add_annotation("versionInfo", str(value))

                    # print("version_value: " + str(version_value) + " self.ontology_version: " + str(self.ontology_version) + " version_at_begining:")

                    if float(self.ontology_version) == previous_ontology_version:
                        adjusment += 1

                    else:
                        # adjusment=0
                        ANNOTATIONS[subject, predicate, object].del_annotation("priorVersion",
                                                                               str(previous_ontology_version))
                        ANNOTATIONS[subject, predicate, object].add_annotation("priorVersion",
                                                                               str(self.ontology_version))
                    ANNOTATIONS[subject, predicate, object].add_annotation("deprecated", str(adjusment))
                    # caculate probability
                    probability = (float(value)) / (
                    float(self.ontology_version + adjusment) - (float(version_at_begining) - 1))

                    print("adjustment: " + str(adjusment) + " previous_ontology_version: " + str(
                        previous_ontology_version) + " ontology version: " + str(self.ontology_version))
                    print("value: " + str(value) + " probability " + str(probability))
                    ANNOTATIONS[subject, predicate, object].del_annotation("probability", probability_at_begining)
                    ANNOTATIONS[subject, predicate, object].add_annotation("probability", str(probability))
                    pass
                    # subject.has_cause.append(object)

            # my_drug.has_for_ingredient.append(acetaminophen)
            print()
        except Exception as e:
            print("Error Saving to Ontology: " + str(relationshipSet))
            print(e)

    #Ontology save
    def saveOnto(self):
        self.onto.save()


# # Uncomment by one following code to test  ==>  #
# # Intoduce clases in list
# mainClasses = ['disease', 'cure', 'cause', 'prevention', 'symptom', 'treatment','nn']
# # Introduce word concepts(instances) with classifications
# classifiedWords = [['influenza', 'disease'], ['HIV', 'disease']]

# # CALLING FORMAT
mainClasses = ['hardware', 'network', 'computer_methodology']
subClasses = [['pic','hardware'],['microcontroller','hardware'],['network_algorithems','hardware'],
              ['ai','computer_methodology'],['distributed_systems','computer_methodology'],['agent','computer_methodology'],['machine_learning','computer_methodology']]
classifiedWords = [['intelligent_agent', 'ai'],['operational_symantics', 'ai']]
owl = OntologyMaker()
owl.ClassDefiner(mainClasses)
owl.SubClassDefiner(subClasses)
print(owl.onto.classes)
owl.updateClassifications(classifiedWords)
owl.saveOnto()
