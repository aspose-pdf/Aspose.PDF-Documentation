---
title: PDF Hightlights Annotation using C++
linktitle: Hightlights Annotation
type: docs
weight: 20
url: /cpp/hightlights-annotation/
description: The Markup annotations are presented in the text as highlights, underlines, strikeouts, or jagged underlines in the text of a document.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Text Markup Annotations should be displayed in the text of the document as a highlight, underline, strikethrough, or squiggly underline. When opened, they should display a pop-up window containing the text of the corresponding note.

You can edit the properties of Text Markup Annotations in a PDF by using the Properties window provided in the PDF Viewer control. You can change the color, opacity, author, and theme of the Text Markup Annotations.

You can get or set the highlight annotation settings by using the highlightSettings property. The highlightSettings property is used to set the color, opacity, author, theme, modifiedDate, and isLocked properties for highlight annotations.

It is also possible to get or set strikethrough annotation settings using the strikethroughSettings property. The strikethroughSettings property is used to set the color, opacity, author, theme, modifiedDate, and isLocked properties of strikethrough annotations.

The next feature is the ability to get or set the settings for underline annotations using the underlineSettings property. The underlineSettings property is used to set the color, opacity, author, theme, modifiedDate, and isLocked properties for underline annotations.

## Add Text Markup Annotation

In order to add an Text Markup Annotation to the PDF document, we need to perform the following actions:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Create annotations:
    - [HighlightAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.highlight_annotation) and set parameters (title, color).
    - [StrikeOutAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation) and set parameters (title, color).
    - [SquigglyAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.squiggly_annotation) and set parameters (title, color).
    - [UnderlineAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.underline_annotation) and set parameters (title, color).
1. After we should add all annotations to the page.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextMarkupAnnotations::AddTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    try
    {
        // Load the PDF file
        auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
        auto tfa = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>(u"PDF");
        tfa->Visit(document->get_Pages()->idx_get(1));

        //Create annotations
        auto highlightAnnotation = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(1)->get_Rectangle());
        highlightAnnotation->set_Title(u"Aspose User");
        highlightAnnotation->set_Color(Color::get_LightGreen());

        auto strikeOutAnnotation = MakeObject<Aspose::Pdf::Annotations::StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(2)->get_Rectangle());
        strikeOutAnnotation->set_Title(u"Aspose User");
        strikeOutAnnotation->set_Color(Color::get_Blue());

        auto squigglyAnnotation = MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(3)->get_Rectangle());
        squigglyAnnotation->set_Title(u"Aspose User");
        squigglyAnnotation->set_Color(Color::get_Blue());

        auto underlineAnnotation = MakeObject<Aspose::Pdf::Annotations::UnderlineAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(4)->get_Rectangle());
        underlineAnnotation->set_Title(u"Aspose User");
        underlineAnnotation->set_Color(Color::get_Blue());

        // Add annotation to the page
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(highlightAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(squigglyAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
        document->Save(_dataDir + u"sample_mod.pdf");
    }
    catch (Exception ex)
    {
        Console::WriteLine(ex->get_Message());
    }
}
```

If you want to highlight a multi-line fragment you should use advanced example:

```cpp
/// <summary>
/// Advanced example for you want to highlight a multi-line fragment
/// </summary>

System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color);

void TextMarkupAnnotations::AddHighlightAnnotationAdvanced()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>(
        u"Adobe\\W+Acrobat\\W+Reader",
        MakeObject<Aspose::Pdf::Text::TextSearchOptions>(true));

    tfa->Visit(page);

    for (auto textFragment : tfa->get_TextFragments())
    {
        auto highlightAnnotation = HighLightTextFragment(page, textFragment, Color::get_Yellow());
        page->get_Annotations()->Add(highlightAnnotation);
    }
    document->Save(_dataDir + u"sample_mod.pdf");
}


System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color)
{
    if (textFragment->get_Segments()->get_Count() == 1)
    {
        auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
        ha->set_Title(u"Aspose User");
        ha->set_Color(color);

        ha->set_Modified(DateTime::get_Now());

        auto quadPoints = MakeArray<System::SharedPtr<Point>>(4);

        quadPoints[0] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[1] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[2] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        quadPoints[3] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        ha->set_QuadPoints(quadPoints);
        return ha;
    }

    auto offset = 0;
    auto quadPoints = MakeArray<System::SharedPtr<Point>>(textFragment->get_Segments()->get_Count() * 4);

    for (auto segment : textFragment->get_Segments())
    {
        quadPoints[offset + 0] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 1] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 2] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_LLY());
        quadPoints[offset + 3] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_LLY());
        offset += 4;
    }

    double llx = quadPoints[0]->get_X();
    double lly = quadPoints[0]->get_Y();
    double urx = quadPoints[0]->get_X();
    double ury = quadPoints[0]->get_Y();
    for (auto &pt : quadPoints) {
        if (llx > pt->get_X())
        llx = pt->get_X();
        if (lly > pt->get_Y())
        lly = pt->get_Y();
        if (urx < pt->get_X())
        urx = pt->get_X();
        if (ury < pt->get_Y())
        ury = pt->get_Y();
    }

    auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
    ha->set_Title(u"Aspose User");
    ha->set_Color(color);

    ha->set_Modified(DateTime::get_Now());

    ha->set_QuadPoints(quadPoints);
    return ha;
}


/// <summary>
/// How to get a Highlighted Text
/// </summary>
void TextMarkupAnnotations::GetHighlightedText()
{
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        auto ha = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(ta);
        Console::WriteLine(ha->GetMarkedText());
    }
}
```

## Get Text Markup Annotation

Please try using the following code snippet to Get Text Markup Annotation from PDF document.

```cpp
void TextMarkupAnnotations::GetTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        Console::WriteLine(u"{0} {1}", ta->get_AnnotationType(), ta->get_Rect());
    }
}
```

## Delete Text Markup Annotation

The following code snippet shows how to Delete Text Markup Annotation from PDF file.

```cpp
void TextMarkupAnnotations::DeleteTextMarkupAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector1 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector1);
    auto annotationSelector2 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector2);

    for (auto ta : annotationSelector1->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    for (auto ta : annotationSelector2->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    document->Save(_dataDir + u"sample_del.pdf");
}
```
