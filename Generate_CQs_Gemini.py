import json
import os
import google.generativeai as genai
import pandas as pd
import re

# Replace with your Google API key.
os.environ["GOOGLE_API_KEY"] = "API_key"

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
 
# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Call the Gemini API.
def call_gemini_api(LLM_role, ontology, user_prompt):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')  # Gemini model being accessed.

        response = model.generate_content(
            [LLM_role + ' ' + ontology + ' ' + user_prompt],
            generation_config={
                "temperature": 1,
                "max_output_tokens": 2048,
                "top_p": 1
            }
        )
        return response.text

    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None


def add_column_to_excel(file_path, sheet_name, column_name, data):
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    
    # Remove any formatting.
    data = re.sub(r'^```json\s*|```$', '', data.strip(), flags=re.IGNORECASE)

    data = json.loads(data)

    df[column_name] = data['questions']

    df.to_excel(file_path, index=False)
    
    print(f"Column '{column_name}' added successfully!")


prompt_zero_shot = """
I am providing you with a set of knowledge graph classes and properties. Using only the provided information, generate 20 template-style competency questions that could be asked about this ontology.

A competency question in this context is defined as a natural language question that helps convey the scope and potential of a KG to users unfamiliar with its structure with the aim of supporting exploration.

Phrase questions in natural, user-friendly language, avoiding technical or ontology-specific terms e.g. use "was born" instead of "birth event".
    
Use template-style phrasing: general questions with placeholders like "a person", "a place" etc.

Focus on creating general, reusable question templates that can later be filled with specific instance data.

Only use the given classes, properties, and relationships; do not invent additional concepts.

You may combine classes and properties if it helps express a useful question.

Phrase each competency question naturally, as if it were intended for a user exploring the knowledge graph.

Return your output strictly in the following JSON format:
{ "questions" : ["Question 1", "Question 2", ..., "Question 20"] }

Do not include any additional text, explanations, headings, or formatting (such as "JSON" or backticks).
"""

prompt_zero_shot_relationships = """
I am providing you with a set of knowledge graph classes, properties, and relationships. Using only the provided information, generate 20 template-style competency questions that could be asked about this ontology.

A competency question in this context is defined as a natural language question that helps convey the scope and potential of a KG to users unfamiliar with its structure with the aim of supporting exploration.

Phrase questions in natural, user-friendly language, avoiding technical or ontology-specific terms e.g. use "was born" instead of "birth event".
    
Use template-style phrasing: general questions with placeholders like "a person", "a place" etc.

Focus on creating general, reusable question templates that can later be filled with specific instance data.

Only use the given classes, properties, and relationships; do not invent additional concepts.

You may combine classes and properties if it helps express a useful question.

Phrase each competency question naturally, as if it were intended for a user exploring the knowledge graph.

Return your output strictly in the following JSON format:
{ "questions" : ["Question 1", "Question 2", ..., "Question 20"] }

Do not include any additional text, explanations, headings, or formatting (such as "JSON" or backticks).
"""

prompt_few_shot = """
I am providing you with a set of knowledge graph classes and properties. Using only the provided information, generate 20 template-style competency questions that could be asked about this ontology.

A competency question in this context is defined as a natural language question that helps convey the scope and potential of a KG to users unfamiliar with its structure with the aim of supporting exploration.

Examples of the type of questions I am looking for are: "Where was a person born?", "When did a person die?", "What type of place is this?".

Phrase questions in natural, user-friendly language, avoiding technical or ontology-specific terms e.g. use "was born" instead of "birth event".
    
Use template-style phrasing: general questions with placeholders like "a person", "a place" etc.

Focus on creating general, reusable question templates that can later be filled with specific instance data.

Only use the given classes, properties, and relationships; do not invent additional concepts.

You may combine classes and properties if it helps express a useful question.

Phrase each competency question naturally, as if it were intended for a user exploring the knowledge graph.

Return your output strictly in the following JSON format:
{ "questions" : ["Question 1", "Question 2", ..., "Question 20"] }

Do not include any additional text, explanations, headings, or formatting (such as "JSON" or backticks).
"""

prompt_few_shot_relationships = """
I am providing you with a set of knowledge graph classes, properties, and relationships. Using only the provided information, generate 20 template-style competency questions that could be asked about this ontology.

A competency question in this context is defined as a natural language question that helps convey the scope and potential of a KG to users unfamiliar with its structure with the aim of supporting exploration.

Examples of the type of questions I am looking for are: "Where was a person born?", "When did a person die?", "What type of place is this?".

Phrase questions in natural, user-friendly language, avoiding technical or ontology-specific terms e.g. use "was born" instead of "birth event".
    
Use template-style phrasing: general questions with placeholders like "a person", "a place" etc.

Focus on creating general, reusable question templates that can later be filled with specific instance data.

Only use the given classes, properties, and relationships; do not invent additional concepts.

You may combine classes and properties if it helps express a useful question.

Phrase each competency question naturally, as if it were intended for a user exploring the knowledge graph.

Return your output strictly in the following JSON format:
{ "questions" : ["Question 1", "Question 2", ..., "Question 20"] }

Do not include any additional text, explanations, headings, or formatting (such as "JSON" or backticks).
"""

full_ontology = """
Classes:
Attribute Assignment
Person
Physical Human-Made_Thing
Conceptual Object
Authority_Document
Actor
Appellation
Place Appellation
Time-Span
Place
Dimension
Time Primitive
Birth
Death
Human-Made Thing
Group
Actor Appellation
Propositional Object
Feature
Geometry
QuadMap
QuadMapATable
QuadMapColumn
QuadMapFText
QuadMapFormat
QuadMapValue
QuadStorage
array-of-QuadMap
array-of-QuadMapATable
array-of-QuadMapColumn
array-of-QuadMapFormat
array-of-string
Property
rdf-schema#Class
AnnotationProperty
owl#Class
Ontology
OntologyProperty
sparql-service-description#Service
Q1093829
Q22746
Q23442
Q253019
Q2755753
Q3957
Q532
Q62049
Q6256

Properties:
easting  
northing  
square  
hectares  
has title  
has current or former member  
occurred in the presence of  
has alternative form  
assigned attribute to  
assigned  
approximates  
is identified by  
has type  
has dimension  
has preferred identifier  
has time-span  
is depicted by  
refers to  
is referred to by  
lists  
is listed in  
took place at  
end of the begin  
begin of the end  
begin of the begin  
end of the end  
falls within  
took out of existence  
brought into life  
osmIRI  
contributor  
created  
creator  
extent  
modified  
references  
url  
asWKT  
hasBoundingBox  
hasCentroid  
hasGeometry  
hasMetricArea  
ownerUser  
inheritFrom  
isGcResistantType  
isSpecialPredicate  
item  
loadAs  
noInherit  
qmGraphMap  
qmMatchingFlags  
qmObjectMap  
qmPredicateMap  
qmSubjectMap  
qmTableName  
qmf01blankOfShortTmpl  
qmf01uriOfShortTmpl  
qmfBoolOfShortTmpl  
qmfBoolTmpl  
qmfCmpFuncName  
qmfColumnCount  
qmfCustomString1  
qmfDatatypeOfShortTmpl  
qmfDatatypeTmpl  
qmfDtpOfNiceSqlval  
qmfExistingShortOfLongTmpl  
qmfExistingShortOfSqlvalTmpl  
qmfExistingShortOfTypedsqlvalTmpl  
qmfExistingShortOfUriTmpl  
qmfHasCheapSqlval  
qmfIidOfShortTmpl  
qmfIsBijection  
qmfIsStable  
qmfIsSubformatOfLong  
qmfIsSubformatOfLongWhenEqToSql  
qmfIsSubformatOfLongWhenRef  
qmfIsblankOfShortTmpl  
qmfIslitOfShortTmpl  
qmfIsnumericOfShortTmpl  
qmfIsrefOfShortTmpl  
qmfIsuriOfShortTmpl  
qmfLanguageOfShortTmpl  
qmfLanguageTmpl  
qmfLongOfShortTmpl  
qmfLongTmpl  
qmfMapsOnlyNullToNull  
qmfName  
qmfOkForAnySqlvalue  
qmfShortOfLongTmpl  
qmfShortOfNiceSqlvalTmpl  
qmfShortOfSqlvalTmpl  
qmfShortOfTypedsqlvalTmpl  
qmfShortOfUriTmpl  
qmfShortTmpl  
qmfSparqlEbvOfShortTmpl  
qmfSparqlEbvTmpl  
qmfSqlvalOfShortTmpl  
qmfSqlvalTmpl  
qmfStrsqlvalOfShortTmpl  
qmfSubFormatForRefs  
qmfSuperFormats  
qmfTypemaxTmpl  
qmfTypeminTmpl  
qmfUriIdOffset  
qmfUriOfShortTmpl  
qmfValRange-rvrDatatype  
qmfValRange-rvrLanguage  
qmfValRange-rvrRestrictions  
qmfWrapDistinct  
qmvATables  
qmvColumns  
qmvColumnsFormKey  
qmvFText  
qmvFormat  
qmvGeo  
qmvTableName  
qmvaAlias  
qmvaTableName  
qmvcAlias  
qmvcColumnName  
qmvftAlias  
qmvftColumnName  
qmvftConds  
qmvftTableName  
qmvftXmlIndex  
qsDefaultMap  
qsMatchingFlags  
qsUserMaps  
version  
1
2
3
4
5
first  
rest  
type  
comment  
domain  
is defined by  
label  
range  
see also  
sub class of  
sub property of  
complement of  
imports  
prior version  
same as  
union of  
version info  
endpoint  
feature  
result format  
supported language  
url  
P31  
P625  
depiction  
DIB ID  
area of interest  
ISBN  
Links  
OSM identifier  
OS identifier  
OSi identifier  
Osi Identifier  
Osm Identifier  
VRTI ERA  
VRTI REF ID  
Vrti Identifier  
composed of  
counsellee  
counselor  
geo identifier  
links  
object  
part of  
reports to  
represented by  
subject  
subjects  
townland Link  
vrti identifier  
DIB ID  
ISBN  
VRTI ERA  
VRTI REF ID  
century  
DIB ID  
ISBN  
OSM ID  
OS ID  
VRTI ERA  
VRTI KG ID  
VRTI REF ID  
century  
links  
"""

ontology_subset = """
Classes:
Attribute Assignment
Person
Physical Human-Made Thing
Conceptual Object
Authority_Document
Appellation
Place Appellation
Time-Span
Place
Dimension
Time Primitive
Birth
Death
Human-Made Thing
Group
Actor Appellation
Propositional Object
Feature
Geometry

Properties:
hectares  
has title  
has current or former member  
occurred in the presence of  
has alternative form  
assigned attribute to  
assigned  
approximates  
is identified by  
has type  
has dimension  
has preferred identifier  
has time-span  
is depicted by  
refers to  
is referred to by  
lists  
is listed in  
took place at  
falls within  
took out of existence  
brought into life  
DIB ID  
area of interest  
ISBN  
composed of  
counsellee  
counselor  
geo identifier  
part of  
reports to  
represented by  
subject  
townland Link  
vrti identifier   
"""

ontology_subset_relationships = """
Classes:
  - Attribute_Assignment
  - Person (subclass of Actor)
  - Group (subclass of Actor)
  - Appellation (subclass of Symbolic_Object)
  - Identifier (subclass of Appellation)
  - Type
  - Birth (subclass of Beginning_of_Existence)
  - Death (subclass of End_of_Existence)
  - feature
  - geometry

Properties:
  - carried_out_by: domain Attribute_Assignment, range Person
  - has_type: domain Attribute_Assignment, range Type
  - assigned: domain Attribute_Assignment, range Person | Actor | Group
  - assigned_value: domain Attribute_Assignment, range Type | Appellation | Group
  - assigned_attribute_type: domain Attribute_Assignment, range Type
  - identified_by: domain Person, range Appellation | Identifier
  - has_gender: domain Person, range Type
  - born: domain Person, range Birth
  - died: domain Person, range Death
  - had_role: domain Person, range Type
  - DIB_area_of_interest  
  - composed_of  
    - counsellee  
    - counselor  
    - geo_identifier  
    - links  
    - object  
    - part_of  
    - reports_to  
    - represented_by  
    - subject  
    - subjects  
    - townlandLink  
    - vrti_identifier  
    - DIB_ID  
    - ISBN  
    - century  
"""

LLM_role = """
You are a historical knowledge graph exploration assistant. Your task is to generate natural language, template-style competency questions that ordinary users might ask when exploring a historical knowledge graph.
"""

data = call_gemini_api("", full_ontology, prompt_zero_shot)
file_path = "Run1.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api("", ontology_subset, prompt_zero_shot)
file_path = "Run2.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api("", ontology_subset_relationships, prompt_zero_shot_relationships)
file_path = "Run3.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api("", full_ontology, prompt_few_shot)
file_path = "Run4.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api("", ontology_subset, prompt_few_shot)
file_path = "Run5.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api("", ontology_subset_relationships, prompt_few_shot_relationships)
file_path = "Run6.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api(LLM_role, full_ontology, prompt_zero_shot)
file_path = "Run7.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api(LLM_role, ontology_subset, prompt_zero_shot)
file_path = "Run8.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api(LLM_role, ontology_subset_relationships, prompt_zero_shot_relationships)
file_path = "Run9.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api(LLM_role, full_ontology, prompt_few_shot)
file_path = "Run10.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api(LLM_role, ontology_subset, prompt_few_shot)
file_path = "Run11.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)

data = call_gemini_api(LLM_role, ontology_subset_relationships, prompt_few_shot_relationships)
file_path = "Run12.xlsx"  # Path to your Excel file
sheet_name = "Tabelle1"  # Sheet where you want to add data
add_column_to_excel(file_path, sheet_name, 0, data)


