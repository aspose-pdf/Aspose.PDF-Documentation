---
title: تعليق التمييز في ملفات PDF باستخدام C++
linktitle: تعليق التمييز
type: docs
weight: 20
url: /ar/cpp/highlights-annotation/
description: يتم عرض تعليقات التوصيف في النص كتمييزات أو خطوط تحتية أو خطوط مشطوبة أو خطوط متعرجة في نص المستند.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يجب عرض تعليقات التوصيف النصية في نص المستند كتمييز أو خط تحت أو شطب أو خط متعرج. عند فتحها، يجب أن تعرض نافذة منبثقة تحتوي على نص الملاحظة المقابلة.

يمكنك تحرير خصائص تعليقات التوصيف النصية في ملف PDF باستخدام نافذة الخصائص المتوفرة في وحدة التحكم في عارض PDF. يمكنك تغيير اللون والشفافية والمؤلف والموضوع لتعليقات التوصيف النصية.

يمكنك الحصول على إعدادات تعليق التمييز أو تعيينها باستخدام خاصية highlightSettings. The highlightSettings property is used to set the color, opacity, author, theme, modifiedDate, and isLocked properties for highlight annotations.

يتم استخدام خاصية highlightSettings لتعيين اللون، الشفافية، المؤلف، السمة، تاريخ التعديل، وخصائص isLocked للتعليقات التوضيحية بالتمييز.

It is also possible to get or set strikethrough annotation settings using the strikethroughSettings property. The strikethroughSettings property is used to set the color, opacity, author, theme, modifiedDate, and isLocked properties of strikethrough annotations.

من الممكن أيضًا الحصول على أو تعيين إعدادات التعليقات التوضيحية للشطب باستخدام خاصية strikethroughSettings. يتم استخدام خاصية strikethroughSettings لتعيين اللون، الشفافية، المؤلف، السمة، تاريخ التعديل، وخصائص isLocked للتعليقات التوضيحية للشطب.

The next feature is the ability to get or set the settings for underline annotations using the underlineSettings property. The underlineSettings property is used to set the color, opacity, author, theme, modifiedDate, and isLocked properties for underline annotations.

الميزة التالية هي القدرة على الحصول على أو تعيين الإعدادات للتعليقات التوضيحية للتسطير باستخدام خاصية underlineSettings. يتم استخدام خاصية underlineSettings لتعيين اللون، الشفافية، المؤلف، السمة، تاريخ التعديل، وخصائص isLocked للتعليقات التوضيحية للتسطير.

## Add Text Markup Annotation

## إضافة تعليق توضيحي لنص

In order to add an Text Markup Annotation to the PDF document, we need to perform the following actions:

لإضافة تعليق توضيحي لنص إلى مستند PDF، نحتاج إلى القيام بالإجراءات التالية:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.

1. تحميل ملف PDF - كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) جديد.

1. Create annotations:

1. إنشاء تعليقات توضيحية:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.highlight_annotation) and set parameters (title, color).

    - [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.highlight_annotation) وتعيين المعلمات (العنوان، اللون).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation) وتعيين المعلمات (العنوان، اللون).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.squiggly_annotation) وتعيين المعلمات (العنوان، اللون).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.underline_annotation) وتعيين المعلمات (العنوان، اللون).
1. بعد ذلك يجب علينا إضافة جميع التعليقات التوضيحية إلى الصفحة.

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
```

إذا كنت تريد تمييز جزء متعدد الأسطر، يجب عليك استخدام المثال المتقدم:

```cpp
/// <summary>
/// مثال متقدم إذا كنت تريد تمييز جزء متعدد الأسطر
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
/// كيفية الحصول على نص مميز
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

## الحصول على تعليق توضيحي لنص

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق توضيحي لنص من وثيقة PDF.

```cpp
void TextMarkupAnnotations::GetTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
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

## حذف تعليق توضيحي لنص

يوضح مقتطف الشيفرة التالي كيفية حذف تعليق توضيحي لنص من ملف PDF.

```cpp
void TextMarkupAnnotations::DeleteTextMarkupAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
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