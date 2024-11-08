---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: /ar/cpp/text-annotation/
description: Aspose.PDF for C++ يسمح لك بإضافة، الحصول على، وحذف تعليقات النص من مستند PDF الخاص بك.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## كيفية إضافة تعليق نصي إلى ملف PDF موجود

التعليق النصي هو تعليق مرتبط بموقع محدد في مستند PDF. عندما يكون مغلقًا، يتم عرض التعليق كأيقونة؛ وعند فتحه، يجب أن يعرض نافذة منبثقة تحتوي على نص الملاحظة بالخط والحجم الذي يختاره القارئ.

تكون التعليقات موجودة في مجموعة [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) لصفحة معينة. هذه المجموعة تحتوي على التعليقات لتلك الصفحة الفردية فقط؛ كل صفحة لديها مجموعة التعليقات الخاصة بها.

لإضافة تعليق إلى صفحة معينة، قم بإضافته إلى مجموعة التعليقات لتلك الصفحة باستخدام طريقة [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9).


1. أولاً، قم بإنشاء توضيح تريد إضافته إلى ملف PDF.
1. ثم افتح ملف PDF المدخل.
1. أضف التوضيح إلى مجموعة التوضيحات في كائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

يظهر لك مقطع الشيفرة التالي كيفية إضافة توضيح في صفحة PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Aspose User");
    textAnnotation->set_Subject(u"Sample Subject");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Sample contents for the annotation");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```
```

## الحصول على تعليق نصي

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق نصي في مستند PDF:

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // تصفية التعليقات باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // طباعة النتائج
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## حذف تعليق نصي من ملف PDF

يوضح مقتطف الشيفرة التالي كيفية حذف تعليق نصي من ملف PDF.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // تصفية التعليقات باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // حذف التعليقات
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## كيفية إضافة (أو إنشاء) تعليق نصي حر جديد

يظهر تعليق النص الحر النص مباشرة على الصفحة. في المقتطف التالي، نضيف تعليق نصي حر فوق أول ظهور للنص.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"عرض النص الحر");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## الحصول على التعليق النصي الحر

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على التعليق النصي في مستند PDF:

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // تصفية التعليقات باستخدام AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // طباعة النتائج
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### جعل التعليق النصي الحر غير مرئي

أحيانًا يكون من الضروري إنشاء علامة مائية غير مرئية في المستند عند عرضه ولكن يجب أن تكون مرئية عند طباعة المستند. استخدم علامات التعليق التوضيحي لهذا الغرض. يوضح مقطع الشيفرة التالي كيفية القيام بذلك.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // حفظ الملف الناتج
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## حذف تعليق النص الحر

يوضح مقطع الشيفرة التالي كيفية حذف تعليق النص الحر من ملف PDF.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // تصفية التعليقات باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // حذف التعليقات
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```