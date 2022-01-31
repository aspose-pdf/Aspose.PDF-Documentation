---
title: Update Links in PDF 
linktitle: Update Links
type: docs
weight: 20
url: /cpp/update-links/
description: Update links in PDF programmatically with Aspose.PDF for C++. This guide is about how to update links in PDF file. 
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Update Links in PDF File

As discussed in Add Hyperlink in a PDF File, the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) class makes it possible to add links in a PDF file. There’s also a similar class used to get existing links from inside PDF files. Use this if you need to update an existing link. To update an existing link:

1. Load a PDF file.
1. Go to a specific page in the PDF file.
1. Specify the link destination using the [GoToAction](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action) object’s Destination property.
1. The destination page is specified using the [XYZExplicitDestination](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination) constructor.

### Set Link Target to a Page in the Same Document

The following code snippet shows you how to update a link in a PDF file and set its target to the second page of the document.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modification link: change link destination
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // Specify the destination for link object
    // Represents explicit destination that displays the page with the coordinates (left, top) positioned at the upper-left corner of 
    // the window and the contents of the page magnified by the factor zoom.
    // The 1st parameter is destination page number. 
    // The 2nd is left coordinate
    // The 3nd is top coordinate
    // The 4th argument is zoom factor when displaying the respective page. Using 2 means page will be displayed in 200% zoom
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // Save the document with updated link
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Set Link Destination to a Web Address

To update the hyperlink so that it points to a web address, instantiate the [GoToURIAction](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) object and pass it to the LinkAnnotation’s Action property. The following code snippet shows how to update a link in a PDF file and set its target to a web address.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // Load the PDF file
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modification link: change link action and set target as web address
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // Save the document with updated link
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Set Link Target to Another PDF File

The following code snippet shows how to update a link in a PDF file and set its target to another PDF file.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // Load the PDF file
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modification link: change link action and set target as web address
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // Next line update destination, do not update file
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // Next line update file
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // Save the document with updated link
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Update LinkAnnotation Text Color

The link annotation does not contain text. Instead, the text is placed in the contents of the page under the annotation. Therefore, to change the color of the text, replace the color of the page text instead of trying change color of the annotation. The following code snippet shows how to update the color of link annotation in a PDF file.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // Load the PDF file
    String _dataDir("C:\\Samples\\");

    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // Search the text under the annotation
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // Change color of the text.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // Save the document with updated link
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```

