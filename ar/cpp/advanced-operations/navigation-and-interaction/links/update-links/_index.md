---
title: تحديث الروابط في PDF 
linktitle: تحديث الروابط
type: docs
weight: 20
url: /ar/cpp/update-links/
description: تحديث الروابط في PDF برمجيًا باستخدام Aspose.PDF لـ C++. هذا الدليل يتحدث عن كيفية تحديث الروابط في ملف PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحديث الروابط في ملف PDF

كما تم مناقشته في إضافة رابط في ملف PDF، فإن فئة [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) تجعل من الممكن إضافة روابط في ملف PDF. هناك أيضًا فئة مشابهة تستخدم للحصول على الروابط الموجودة داخل ملفات PDF. استخدم هذا إذا كنت بحاجة إلى تحديث رابط موجود. لتحديث رابط موجود:

1. قم بتحميل ملف PDF.
1. اذهب إلى صفحة محددة في ملف PDF.
1. حدد وجهة الرابط باستخدام خاصية Destination لكائن [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action).
1. الصفحة الوجهة محددة باستخدام المنشئ [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination).

### ضبط هدف الرابط إلى صفحة في نفس المستند

يعرض لك مقتطف الشيفرة التالي كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى الصفحة الثانية من المستند.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // تعديل الرابط: تغيير وجهة الرابط
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // تحديد الوجهة لكائن الرابط
    // يمثل الوجهة الصريحة التي تعرض الصفحة بإحداثياتها (يسار، أعلى) موضوعة في الزاوية العلوية اليسرى من
    // النافذة ومحتوى الصفحة مكبر بعامل التكبير zoom.
    // المعامل الأول هو رقم صفحة الوجهة.
    // الثاني هو إحداثي اليسار
    // الثالث هو إحداثي الأعلى
    // المعامل الرابع هو عامل التكبير عند عرض الصفحة المعنية. استخدام 2 يعني أن الصفحة ستعرض بتكبير 200%
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // حفظ المستند مع الرابط المحدث
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### تعيين وجهة الرابط إلى عنوان ويب

لتحديث الارتباط التشعبي بحيث يشير إلى عنوان ويب، قم بإنشاء كائن [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) وتمريره إلى خاصية Action الخاصة بـ LinkAnnotation. يوضح مقتطف الشيفرة التالي كيفية تحديث رابط في ملف PDF وتعيين وجهته إلى عنوان ويب.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // تحميل ملف PDF
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // تعديل الرابط: تغيير إجراء الرابط وتعيين الهدف كعنوان ويب
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // حفظ الوثيقة بالرابط المحدث
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### تعيين هدف الرابط إلى ملف PDF آخر

يوضح مقتطف الشفرة التالي كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى ملف PDF آخر.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // تحميل ملف PDF
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للوثيقة
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // تعديل الرابط: تغيير إجراء الرابط وتعيين الهدف كعنوان ويب
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // السطر التالي يحدّث الوجهة، لا يُحدّث الملف
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // السطر التالي يحدّث الملف
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // حفظ الوثيقة بالرابط المحدث
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### تحديث لون نص التعليق التوضيحي للرابط

التعليق التوضيحي للرابط لا يحتوي على نص. بدلاً من ذلك، يتم وضع النص في محتويات الصفحة تحت التعليق التوضيحي. لذلك، لتغيير لون النص، قم باستبدال لون نص الصفحة بدلاً من محاولة تغيير لون التعليق التوضيحي. يوضح مقطع الشيفرة التالي كيفية تحديث لون التعليق التوضيحي للرابط في ملف PDF.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // تحميل ملف PDF
    String _dataDir("C:\\Samples\\");

    // إنشاء كائن المستند
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // إضافة صفحة إلى مجموعة صفحات ملف PDF
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // البحث عن النص تحت التعليق التوضيحي
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // تغيير لون النص.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // حفظ المستند مع تحديث الرابط
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```