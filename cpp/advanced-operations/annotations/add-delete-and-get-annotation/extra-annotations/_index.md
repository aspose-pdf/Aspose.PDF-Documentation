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

## How to add Caret Annotation into existing PDF file

Caret Annotation is a symbol that indicates text editing. Caret Annotation is also markup annotation, so the Caret class derives from the Markup class and also provides functions to get or set properties of the Caret Annotation and reset the flow of the Caret Annotation appearance.

Steps with which we create Caret annotation:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Create new [Caret Annotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the insertion of text.
1. Create new [Caret Annotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the replacement of text.
1. Create new [StrikeOutAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) and set parameters (new Rectangle, title, color, new QuadPoints and new points, Subject, InReplyTo,ReplyType).
1. After we can Add annotations to the page.

The following code snippet shows how to add Caret Annotation to a PDF file:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // This annotation is used to indicate the insertion of text
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1), 
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Aspose User");
    caretAnnotation1->set_Subject(u"Inserted text 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // This annotation is used to indicate the replacement of text
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1), 
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Aspose User");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Inserted text 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1), 
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416), 
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Cross-out");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```

### Get Caret Annotation

Please try using the following code snippet to Get Caret Annotation in PDF document

```cpp
void MarkupAnnotations::GetCaretAnnotation() {
    
    String _dataDir("C:\\Samples\\");
    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filter annotations using AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // print results
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Delete Caret Annotation

The following code snippet shows how Delete Caret Annotation from a PDF file.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {
    
    String _dataDir("C:\\Samples\\");
    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filter annotations using AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // delete annotation
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

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

## Redact certain page region with Redaction Annotation using Aspose.PDF for C++

Aspose.PDF for C++ supports the feature to add as well as manipulate Annotations in an existing PDF file. Recently some of our customers posted a required to redact (remove text, image, etc elements from) a certain page region of PDF document. In order to fulfill this requirement, a class named RedactionAnnotation is provided, which can be used to redact certain page regions or it can be used to manipulate existing RedactionAnnotations and redact them (i.e. flatten annotation and remove the text under it).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Create RedactionAnnotation instance for specific page region
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // Text to be printed on redact annotation
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // Repat Overlay text over redact Annotation
    annot->set_Repeat(true);

    // Add annotation to annotations collection of first page
    page->get_Annotations()->Add(annot);

    // Flattens annotation and redacts page contents (i.e. removes text and image
    // Under redacted annotation)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Facades approach 

Aspose.PDF.Facades nsupports [PdfAnnotationEditor](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) class, which provides the feature to manipulate existing Annotations inside PDF file. 

This class contains a method named [RedactArea(..)](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) which provides the capability to remove certain page regions.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // Redact certain page region
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```

