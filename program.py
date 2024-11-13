from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

endpoint = "https://**************************************************.cognitiveservices.azure.com/"
key =  "**************************************************"
ducumentURL = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"


document_analysis_document = DocumentAnalysisClient(
                            endpoint= endpoint,
                            credential= AzureKeyCredential(key))


pollar = document_analysis_document.begin_analyze_document_from_url("prebuilt-read", ducumentURL)

result = pollar.result()

#Extracting page, line and word the analysis using Python 

for page in result.pages:
    print(f"Document page {page.page_number} has {len(page.lines)} lines and {len(page.words)} words.") 
    
    for i, line in enumerate(page.lines):
            print("Line {} : {}".format(i+1, line.content))

    for word in page.words:
          print("word '{}' has a confidence of {}".format(word.content, word.confidence))

print("-------------")

#Extracting paragraph analysis using Python 

for paragraph in result.paragraphs:
      print(f"{paragraph.role} : {paragraph.content}")
