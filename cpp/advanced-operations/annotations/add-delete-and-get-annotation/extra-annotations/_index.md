---
title: Extra Annotations using C++
linktitle: Extra Annotations
type: docs
weight: 60
url: /cpp/extra-annotations/
description: This section describes how to add, get, and delete extra kinds of annotations from your PDF document.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## How to add Link Annotation

A [Link Annotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) is a hypertext link that leads to a destination elsewhere in the document or to an action to be performed.

A Link is a rectangular area that can be placed anywhere on the page. Each link has a corresponding PDF action associated with it. This action is performed when the user clicks in the area of this link.

The following code snippet shows how to add Link Annotation to a PDF file using a phone number example:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    
    auto page = document->get_Pages()->idx_get(1);

    // Create TextFragmentAbsorber object to find a phone number
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // Accept the absorber for the 1st page only
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // Create Link Annotation and set the action to call a phone number
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // Add annotation to page
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");    
}
```

### Get Link Annotation

Please try using the following code snippet to Get LinkAnnotation from PDF document.

```cpp
void GetLinkAnnotations() {
    
    String _dataDir("C:\\Samples\\");
    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filter annotations using AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // print results
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // Print the URL of each Link Annotation
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // Print the text associated with hyperlink
        Console::WriteLine(extractedText);
    }
}
```

### Delete Link Annotation

The following code snippet shows how to Delete Link Annotation from PDF file. For this we need to find and and remove all link annotations on the 1st page. After this we will save document with removed annotation.

```cpp
void DeleteLinkAnnotations() 
{
    String _dataDir("C:\\Samples\\");
    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filter annotations using AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // print results
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // Save document with removed annotation
    document->Save(_dataDir + u"SimpleResume_del.pdf");        
}
```

