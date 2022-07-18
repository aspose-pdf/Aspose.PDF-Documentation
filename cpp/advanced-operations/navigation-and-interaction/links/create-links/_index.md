---
title: Create Links in PDF file with C++
linktitle: Create Links
type: docs
weight: 10
url: /cpp/create-links/
description: This section explains how to create links in your PDF document with C++. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Create Links

By adding a link to an application into a document, it is possible to link to applications from a document. This is useful when you want readers to take a certain action at a specific point in a tutorial, for example, or to create a feature-rich document. To create an application link:

1. [Create a Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Get the [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) you want to add link to.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) object using the Page and [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) object.
1. Also, set the to [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/) object’s Action property.
1. When creating the [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/) object, specify the application you want to launch.
1. Add the link to the Page object’s [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) property.
1. Finally, save the updated PDF using the Document object’s Save method.

The following code snippet shows how to create a link to an application in a PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```

### Create PDF Document Link in a PDF File

Aspose.PDF for C++ allows you to add a link to an external PDF file so that you can link several documents together. To create a PDF document link:

1. First, create a [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Then, get the particular [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) you want to add the link to.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) object using the Page and [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) object.
1. Set the Action property to the [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/) object.
1. While creating the GoToRemoteAction object, specify the PDF file that should launch, as well as the page number it should open on.
1. Add the link to the Page object’s Annotations collection.
1. Save the updated PDF using the Document object’s Save method.

The following code snippet shows how to create PDF document link in a PDF file.

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```