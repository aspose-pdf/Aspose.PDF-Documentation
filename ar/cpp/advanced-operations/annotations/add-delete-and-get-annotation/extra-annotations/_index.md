---
title: إضافات توضيحية إضافية باستخدام C++
linktitle: إضافات توضيحية إضافية
type: docs
weight: 60
url: ar/cpp/extra-annotations/
description: يصف هذا القسم كيفية إضافة، الحصول على، وحذف أنواع إضافية من الإضافات التوضيحية من مستند PDF الخاص بك.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية إضافة توضيح Caret في ملف PDF موجود

توضيح Caret هو رمز يشير إلى تحرير النص. توضيح Caret هو أيضًا توضيح تمييز، لذا فإن فئة Caret تشتق من فئة Markup وتوفر أيضًا وظائف للحصول أو تعيين خصائص توضيح Caret وإعادة تعيين تدفق مظهر توضيح Caret.

الخطوات التي ننشئ بها توضيح Caret:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. إنشاء [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) جديد وتعيين معلمات Caret (مستطيل جديد، عنوان، موضوع، أعلام، لون، عرض، أسلوب البداية وأسلوب النهاية). يُستخدم هذا التعليق التوضيحي للإشارة إلى إدراج النص.
1. إنشاء [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) جديد وتعيين معلمات Caret (مستطيل جديد، عنوان، موضوع، أعلام، لون، عرض، أسلوب البداية وأسلوب النهاية). يُستخدم هذا التعليق التوضيحي للإشارة إلى استبدال النص.
1. إنشاء [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) جديد وتعيين المعلمات (مستطيل جديد، عنوان، لون، نقاط رباعية جديدة ونقاط جديدة، موضوع، في الرد على، نوع الرد).
1. بعد ذلك يمكننا إضافة التعليقات التوضيحية إلى الصفحة.

يظهر مقطع الشيفرة التالي كيفية إضافة Caret Annotation إلى ملف PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // يُستخدم هذا التعليق التوضيحي للإشارة إلى إدراج النص
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"مستخدم Aspose");
    caretAnnotation1->set_Subject(u"تم إدراج النص 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // يُستخدم هذا التعليق التوضيحي للإشارة إلى استبدال النص
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"مستخدم Aspose");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"تم إدراج النص 2");
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

    strikeOutAnnotation->set_Subject(u"شطب");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### احصل على تعليق توضيحي للمؤشر

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق توضيحي للمؤشر في مستند PDF

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // طباعة النتائج
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### حذف تعليق توضيحي للمؤشر

يوضح مقتطف الشيفرة التالي كيفية حذف تعليق توضيحي للمؤشر من ملف PDF.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // حذف التعليق التوضيحي
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## كيفية إضافة تعليق توضيحي للرابط

[تعليق توضيحي للرابط](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) هو رابط نصي فائق يؤدي إلى وجهة في مكان آخر في المستند أو إلى إجراء يتم تنفيذه.

الرابط هو منطقة مستطيلة يمكن وضعها في أي مكان على الصفحة. كل رابط له إجراء PDF مطابق مرتبط به. يتم تنفيذ هذا الإجراء عندما ينقر المستخدم في منطقة هذا الرابط.

يظهر مقتطف الكود التالي كيفية إضافة تعليق توضيحي للرابط إلى ملف PDF باستخدام مثال رقم هاتف:

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

### الحصول على تعليق الرابط

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق LinkAnnotation من مستند PDF.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // تصفية التعليقات باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // طباعة النتائج
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // طباعة عنوان URL لكل تعليق رابط
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // طباعة النص المرتبط بالرابط
        Console::WriteLine(extractedText);
    }
}
```

### حذف شرح الرابط

يوضح مقتطف الشيفرة التالي كيفية حذف شرح الرابط من ملف PDF. لهذا نحتاج إلى العثور على وحذف جميع شروحات الروابط في الصفحة الأولى. بعد ذلك سنحفظ المستند بعد إزالة الشرح.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // تصفية الشروحات باستخدام AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // طباعة النتائج
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // حفظ المستند بعد إزالة الشرح
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## إخفاء منطقة معينة من الصفحة باستخدام تعليق الإخفاء باستخدام Aspose.PDF لـ C++

يدعم Aspose.PDF لـ C++ ميزة إضافة وتعديل التعليقات التوضيحية في ملف PDF موجود. في الآونة الأخيرة، طلب بعض عملائنا إخفاء (إزالة النص، أو الصورة، أو العناصر الأخرى من) منطقة معينة من مستند PDF. لتلبية هذا الطلب، تم توفير فئة تسمى RedactionAnnotation، والتي يمكن استخدامها لإخفاء مناطق معينة من الصفحة أو يمكن استخدامها للتعامل مع RedactionAnnotations الموجودة وإخفائها (أي تسطيح التعليق وإزالة النص تحته).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // إنشاء مثيل RedactionAnnotation لمنطقة صفحة محددة
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // النص المراد طباعته على تعليق الإخفاء
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // تكرار النص المطبوع على تعليق الإخفاء
    annot->set_Repeat(true);

    // إضافة التعليق إلى مجموعة التعليقات التوضيحية للصفحة الأولى
    page->get_Annotations()->Add(annot);

    // تسطيح التعليق وإخفاء محتويات الصفحة (أي إزالة النص والصورة
    // تحت التعليق المخفي)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## نهج الواجهات

تدعم Apose.PDF.Facades فئة [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) التي توفر ميزة التلاعب بالتعليقات التوضيحية الموجودة داخل ملف PDF.

تحتوي هذه الفئة على طريقة تسمى [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) التي توفر القدرة على إزالة مناطق معينة من الصفحة.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // تنقيح منطقة معينة من الصفحة
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```