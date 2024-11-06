---
title: العمل مع العوامل باستخدام C++
linktitle: العمل مع العوامل
type: docs
weight: 170
url: ar/cpp/operators/
description: يشرح هذا الموضوع كيفية استخدام العوامل مع Aspose.PDF في C++. توفر فئات العوامل ميزات رائعة للتلاعب بملفات PDF.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة للعوامل في PDF واستخدامها

العامل هو كلمة مفتاحية في PDF تحدد بعض الإجراءات التي يجب تنفيذها، مثل رسم شكل بياني على الصفحة. يتم تمييز الكلمة المفتاحية للعامل عن الكائن المسمى بغياب الحرف الأمامي الصلب (2Fh). تكون العوامل ذات معنى فقط داخل تدفق المحتوى.

تدفق المحتوى هو كائن تدفق PDF يتكون بياناته من تعليمات تصف العناصر الرسومية التي سيتم رسمها على الصفحة. يمكن العثور على مزيد من التفاصيل حول عوامل PDF في [مواصفات PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### تفاصيل التنفيذ

يشرح هذا الموضوع كيفية استخدام العوامل مع Aspose.PDF. يضيف المثال المحدد صورة إلى ملف PDF لتوضيح المفهوم. لإضافة صورة في ملف PDF، هناك حاجة إلى مشغلين مختلفين. يستخدم هذا المثال [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save)، [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix)، [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do)، و[GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- يقوم مشغل **GSave** بحفظ الحالة الرسومية الحالية لملف PDF.
- يتم استخدام مشغل **ConcatenateMatrix** (مصفوفة السلسلة) لتعريف كيفية وضع الصورة على صفحة PDF.
- يقوم مشغل **Do** برسم الصورة على الصفحة.
- يقوم مشغل **GRestore** باستعادة الحالة الرسومية.

لإضافة صورة إلى ملف PDF:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) وفتح مستند PDF المدخل.
1. احصل على الصفحة المحددة التي سيتم إضافة الصورة إليها.
1. أضف الصورة إلى مجموعة الموارد الخاصة بالصفحة.
1. استخدم المشغلين لوضع الصورة على الصفحة:
   - أولاً، استخدم المشغل GSave لحفظ الحالة الرسومية الحالية.
   - ثم استخدم المشغل ConcatenateMatrix لتحديد مكان وضع الصورة.
   - استخدم المشغل Do لرسم الصورة على الصفحة.
1. أخيرًا، استخدم المشغل GRestore لحفظ الحالة الرسومية المحدثة.

لقطة الكود التالية توضح كيفية استخدام مشغلي PDF.

```cpp
void ExampleUsingOperators()
{
    // افتح المستند
    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // تعيين الإحداثيات
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // احصل على الصفحة التي تحتاج إلى إضافة الصورة
    auto page = document->get_Pages()->idx_get(1);

    // تحميل الصورة إلى تدفق
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // إضافة الصورة إلى مجموعة الصور في موارد الصفحة
    page->get_Resources()->get_Images()->Add(imageStream);

    // استخدام المشغل GSave: هذا المشغل يحفظ الحالة الرسومية الحالية
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // إنشاء كائنات المستطيل والمصفوفة
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // استخدام المشغل ConcatenateMatrix (ضم المصفوفة): يحدد كيفية وضع الصورة
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // استخدام المشغل Do: هذا المشغل يرسم الصورة
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // استخدام المشغل GRestore: هذا المشغل يعيد الحالة الرسومية
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // حفظ المستند المحدث
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## رسم XForm على الصفحة باستخدام المشغلين

يشرح هذا الموضوع كيفية استخدام مشغلي GSave/GRestore، ومشغل ConcatenateMatrix لتحديد موضع xForm ومشغل Do لرسم xForm على الصفحة.

يقوم الكود أدناه بتغليف المحتويات الموجودة لملف PDF بزوج المشغلين GSave/GRestore. تساعد هذه الطريقة في الحصول على حالة الرسوميات الأولية في نهاية المحتويات الموجودة. بدون هذه الطريقة، قد تبقى التحويلات غير المرغوب فيها في نهاية سلسلة المشغلين الحالية.

```cpp
void DrawXFormOnPageUsingOperators() {
    // فتح المستند
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // يوضح المثال
    // استخدام مشغلي GSave/GRestore
    // استخدام مشغل ConcatenateMatrix لتحديد موضع xForm
    // استخدام مشغل Do لرسم xForm على الصفحة

    // تغليف المحتويات الحالية بزوج المشغلات GSave/GRestore
    // للحصول على حالة الرسوميات الأولية في نهاية المحتويات الحالية
    // وإلا قد تبقى بعض التحويلات غير المرغوب فيها في نهاية سلسلة المشغلين الحالية
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // إضافة مشغل حفظ حالة الرسوميات لتنظيف حالة الرسوميات بشكل صحيح بعد الأوامر الجديدة
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // إنشاء xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // تحديد عرض وارتفاع الصورة
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // تحميل الصورة إلى دفق
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // إضافة الصورة إلى مجموعة الصور في موارد XForm
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // استخدام مشغل Do: هذا المشغل يرسم الصورة
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // وضع النموذج عند الإحداثيات x=100 y=500
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // رسم النموذج باستخدام مشغل Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // وضع النموذج عند الإحداثيات x=100 y=300
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // رسم النموذج باستخدام مشغل Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // استعادة حالة الرسوميات مع GRestore بعد GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## إزالة الكائنات الرسومية باستخدام فئات المشغل

توفر فئات المشغل ميزات رائعة لمعالجة ملفات PDF. عندما يحتوي ملف PDF على رسومات لا يمكن إزالتها باستخدام طريقة [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) لفئة [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor)، يمكن استخدام فئات المشغل لإزالتها بدلاً من ذلك.

يوضح مقتطف الكود التالي كيفية إزالة الرسومات. يرجى ملاحظة أنه إذا كان ملف PDF يحتوي على تسميات نصية للرسومات، فقد تستمر في ملف PDF باستخدام هذا النهج. لذلك، ابحث عن مشغلات الرسومات للحصول على طريقة بديلة لحذف مثل هذه الصور.

```cpp
void RemoveGraphicsObjects() {
    // فتح المستند
    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // المشغلون المستخدمون للرسم بالمسار
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```