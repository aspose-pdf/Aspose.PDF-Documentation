---
title: PDF File Metadata
type: docs
weight: 20
url: /cpp/pdf-file-metadata/
---

## Get/Set PDF File Information

In order to get file specific information of a PDF file, you first need to call the **get_Info()** of Document class. Once the DocumentInfo object is retrieved, you can get the values of the individual properties. Furthermore, you can also set the properties by using respective methods of DocumentInfo class. Following code snippet demonstrate, how to get/set PDF File information using Aspose.PDF for C++:

{{% alert color="primary" %}}

Please note that you cannot set values against the **Application** and **Producer** fields, because Aspose Ltd. and Aspose.PDF for C++ x.x.x will be displayed against these fields.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // Get document information
    auto docInfo = pdfDocument->get_Info();
    // Show document information
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // Specify document information
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"PDF Information");
    docInfo->set_Title (u"Setting PDF Document Information");

    // Save output document
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## Get/Set XMP Metadata from PDF File

Aspose.PDF for C++ allows you to access a PDF file's XMP metadata as well as set it. To get/set a PDF file's metadata:

1. Create a Document object and open the input PDF file.
1. Get/Set the file's metadata using respective methods.

The following code snippet shows you how to get/set metadata from the PDF file.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // Get properties
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // Set properties
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // Save document
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // xmlns prefix has been removed
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // Save document
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```
