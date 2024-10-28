---
title: الحصول على خصائص الصفحة وتعيينها
type: docs
weight: 20
url: /cpp/get-and-set-page-properties/
description: يمكنك الحصول على خصائص الصفحة وتعيينها من ملف PDF الخاص بك باستخدام مكتبة C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** تتيح لك قراءة وتعيين خصائص الصفحات في ملف PDF في تطبيقات C++ الخاصة بك. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة، والحصول على صفحة معينة من ملف PDF وهكذا.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما ترغب في معرفة عدد الصفحات التي تحتوي عليها. مع Aspose.PDF لا يتطلب ذلك أكثر من سطرين من التعليمات البرمجية.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. ثم استخدم خاصية Count لمجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) (من كائن Document) للحصول على العدد الإجمالي للصفحات في المستند.

يوضح مقتطف الشيفرة التالي كيفية الحصول على عدد صفحات ملف PDF.

```cpp
void GetNumberOfPages() {
    // فتح المستند
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // الحصول على عدد الصفحات
    std::cout << "عدد الصفحات: " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### الحصول على عدد الصفحات دون حفظ المستند

أحيانًا نقوم بإنشاء ملفات PDF على الطاير وخلال إنشاء ملف PDF، قد نواجه الحاجة (إنشاء جدول محتويات إلخ.) للحصول على عدد الصفحات لملف PDF دون حفظ الملف على النظام أو التدفق. من أجل تلبية هذا المتطلب، تم تقديم طريقة [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) في فئة Document. يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات للحصول على عدد الصفحات دون حفظ المستند.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // إنشاء مثيل Document
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();
    // إنشاء مثيل للحلقة
    for (int i = 0; i < 300; i++)
        // إضافة TextFragment إلى مجموعة الفقرات في كائن الصفحة
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"اختبار عدد الصفحات"));
    // معالجة الفقرات في ملف PDF للحصول على عدد الصفحات بدقة
    document->ProcessParagraphs();
    // طباعة عدد الصفحات في المستند
    std::cout << "عدد الصفحات في المستند = " << document->get_Pages()->get_Count();
}
```

## Get Page Properties
### الوصول إلى خصائص الصفحة

توفر فئة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) جميع الخصائص المتعلقة بصفحة PDF معينة. يتم احتواء جميع صفحات ملفات PDF في مجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

من هناك، يمكن الوصول إلى كائنات الصفحة الفردية باستخدام فهرسها، أو التكرار عبر المجموعة باستخدام حلقة foreach للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة فردية، يمكننا الحصول على خصائصها. يوضح مقتطف الشيفرة التالي كيفية الحصول على خصائص الصفحة.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // احصل على صفحة معينة
    auto pdfPage = document->get_Pages()->idx_get(1);
    // احصل على خصائص الصفحة
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```