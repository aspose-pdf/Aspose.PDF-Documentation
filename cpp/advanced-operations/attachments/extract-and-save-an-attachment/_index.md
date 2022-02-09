---
title: Extract and Save an Attachment 
linktitle: Extract and Save an Attachment
type: docs
weight: 20
url: /cpp/extract-and-save-an-attachment/
description: Aspose.PDF for C++ allows you to get all attachments from a PDF document. Also, you can get an individual attachment from your document.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get All Attachments

With Aspose.PDF, it is possible to get all attachments from a PDF document. This is useful either when you want to save the documents separately from the PDF, or if you need to strip a PDF of attachments.

To get all attachments from a PDF file:

1. Loop through the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object’s [EmbeddedFiles](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) collection. The [EmbeddedFiles](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) collection contains all attachments. Each element of this collection represents a [FileSpecification](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) object. Each iteration of the foreach loop through the [EmbeddedFiles](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) collection returns a [FileSpecification](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) object.
1. Once the object is available, retrieve either all the attached file’s properties or the file itself.

The following code snippets show how to get all the attachments from a PDF document.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // Open document
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // Get embedded files collection
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // Get count of the embedded files
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // Loop through the collection to get all the attachments
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // Check if parameter object contains the parameters
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // Get the attachment and write to file or stream
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```

## Get Individual Attachment

In order to get an individual attachment, we can specify the index of attachment in `EmbeddedFiles` object of Document instance. Please try using following code snippet.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // Get particular embedded file
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // Get the file properties
    Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

    // Check if parameter object contains the parameters
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Creation Date: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Modification Date: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Size: {0}",
        fileSpecification->get_Params()->get_Size());
    }


    // Get the attachment and write to file or stream
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```
