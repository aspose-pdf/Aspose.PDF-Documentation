---
title: PDF File Metadata 
type: docs
weight: 120
url: /net/pdf-file-metadata/
---

## Get PDF File Information

In order to get file specific information of a PDF file, you first need to get the [DocumentInfo](https://apireference.aspose.com/pdf/net/aspose.pdf/documentinfo) object using [Info](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/info) property of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object. Once the [DocumentInfo](https://apireference.aspose.com/pdf/net/aspose.pdf/documentinfo) object is retrieved, you can get the values of the individual properties. The following code snippet shows you how to get PDF file information.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Get document information
DocumentInfo docInfo = pdfDocument.Info;
// Show document information
Console.WriteLine("Author: {0}", docInfo.Author);
Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
Console.WriteLine("Keywords: {0}", docInfo.Keywords);
Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
Console.WriteLine("Subject: {0}", docInfo.Subject);
Console.WriteLine("Title: {0}", docInfo.Title);
```
## Set PDF File Information

Aspose.PDF for .NET allows you to set file-specific information for a PDF, information like author, creation date, subject, and title. To set this information:

1. Create a [DocumentInfo](https://apireference.aspose.com/pdf/net/aspose.pdf/documentinfo) object.
1. Set the values of the properties.
1. Save the updated document using the Document class’ Save method.

{{% alert color="primary" %}}

Please note that you cannot set values against the *Application* and *Producer* fields, because Aspose Ltd. and Aspose.PDF for .NET x.x.x will be displayed against these fields.

{{% /alert %}}

The following code snippet shows you how to set PDF file information.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Specify document information
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "PDF Information";
docInfo.Title = "Setting PDF Document Information";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Save output document
pdfDocument.Save(dataDir);
```
## Get XMP Metadata from PDF File

Aspose.PDF allows you to access a PDF file’s XMP metadata. To get a PDF file’s metadata:

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object and open the input PDF file.
1. Get the file’s metadata using the [Metadata](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) property.

The following code snippet shows you how to get metadata from the PDF file.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Get properties
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```
## Set XMP Metadata in a PDF File

Aspose.PDF allows you to set metadata in a PDF file. To set metadata:

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Set metadata values using the [Metadata](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) property.
1. Save the updated document using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.

The following code snippet shows you how to set metadata in a PDF file.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Set properties
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Save document
pdfDocument.Save(dataDir);
```
## Insert Metadata with Prefix

Some developers need to create a new metadata namespace with a prefix. The following code snippet shows how to insert metadata with prefix.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Xmlns prefix was removed
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Save document
pdfDocument.Save(dataDir);
```
