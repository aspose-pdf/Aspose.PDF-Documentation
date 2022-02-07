---
title: Adding Attachment to PDF document
linktitle: Adding Attachment to PDF document 
type: docs
weight: 10
url: /cpp/add-attachment-to-pdf-document/
description: This page describes how to add an attachment to a PDF file with Aspose.PDF for C++ library
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Attachments can contain a wide variety of information and can be of a variety of file types. This article explains how to add an attachment to a PDF file.

1. Create a new C++ project.
1. Add a reference to Aspose.PDF DLL.
1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Create a [FileSpecification](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) object with the file you are adding, and file description.
1. Add the [FileSpecification](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) object to the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object’s [EmbeddedFiles](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) collection, with the collection’s Add method.

The [EmbeddedFiles](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) collection contains all the attachments in the PDF file. The following code snippet shows you how to add an attachment in a PDF document.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{
	String _dataDir("C:\\Samples\\");

	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");

	// Setup new file to be added as attachment
	auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"Sample text file");

	// Add attachment to document's attachment collection
	pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);

	// Save new output
	pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```
