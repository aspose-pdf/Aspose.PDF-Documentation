---
title: Working with Attachments
type: docs
weight: 30
url: /cpp/working-with-attachments/
keywords: Cpp PDF API,add pdf attachment using cpp,get pdf attachment info using cpp,remove pdf attachment using cpp
description: Use C++ PDF API to access, add and remove attachments in PDF files using C++ from within your applications. Complete guide with C++ code samples.
lastmod: "2021-06-05"
---

## <ins>**Add Attachment to PDF**
Attachments can contain a wide variety of information, and can be of a variety of file types. This article explains how to add an attachment to a PDF file.

To add an attachment to a PDF document:

1. Create a SharedPtr ```<FileSpecification>``` object with the file you are adding, and a file description.
1. Add the SharedPtr ```<FileSpecification>```  object to the Document object's EmbeddedFiles collection, with the collection’s Add method.

The EmbeddedFiles collection contains all the attachments in the PDF file. The following code snippet shows you how to add attachment in a PDF document.



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Attachments-AddAttachments-AddAttachments.cpp" >}}
