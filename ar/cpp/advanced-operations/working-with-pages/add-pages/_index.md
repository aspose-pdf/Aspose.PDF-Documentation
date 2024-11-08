---
title: إضافة صفحات في PDF باستخدام C++
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/cpp/add-pages/
description: تُعلِّم هذه المقالة كيفية إدراج (إضافة) صفحة في الموقع المطلوب في ملف PDF. تعرف على كيفية نقل وحذف (إزالة) الصفحات من ملف PDF باستخدام C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

توضح هذه القسم كيفية إضافة صفحات إلى ملف PDF باستخدام مكتبة **Aspose.PDF for C++**.

يوفر Aspose.PDF for C++ API المرونة الكاملة للعمل مع الصفحات في مستند PDF باستخدام C++.

يحافظ على جميع صفحات مستند PDF في [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) التي يمكن استخدامها للعمل مع صفحات PDF.
يتيح لك Aspose.PDF for C++ إدراج صفحة في مستند PDF في أي موقع في الملف وكذلك إضافة صفحات إلى نهاية ملف PDF.

## إضافة أو إدراج صفحة في ملف PDF

يتيح لك Aspose.PDF for C++ إدراج صفحة في مستند PDF في أي موقع في الملف وكذلك إضافة صفحات إلى نهاية ملف PDF.

### إدراج صفحة فارغة في ملف PDF في الموقع المطلوب
```

The following code sample explains you on how to add page in a PDF document.

يوضح نموذج التعليمات البرمجية التالي كيفية إضافة صفحة في مستند PDF.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class object with the input PDF file.
1. أنشئ كائن فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ملف PDF المُدخل.
2. Call the [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) method with specified index.
2. استدعِ طريقة [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) لمجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) بالفهرس المحدد.
3. Save the output PDF
3. احفظ ملف PDF الناتج

The following code snippet shows you how to insert a page in a PDF file.

يوضح الجزء التالي من الكود كيفية إدراج صفحة في ملف PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // Open document
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insert a empty page in a PDF
    document->get_Pages()->Insert(2);

    // Save output file
    document->Save(_dataDir + outputFileName);
}
```

في مثال الكود التالي، يمكنك إدراج صفحة فارغة في الموقع المطلوب عن طريق نسخ معلمات الصفحة المحددة:

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // فتح المستند
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // إدراج صفحة فارغة في PDF
    auto pageNew = document->get_Pages()->Insert(2);

    //نسخ معلمات الصفحة من الصفحة 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // حفظ الملف الناتج
    document->Save(_dataDir + outputFileName);
}
```

### إضافة صفحة فارغة في نهاية ملف PDF

أحيانًا، تريد التأكد من أن المستند ينتهي بصفحة فارغة. هذا الموضوع يشرح كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. قم بإنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ملف PDF المدخل.
2. استدع طريقة [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) لمجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)، بدون أي معلمات.
3. احفظ ملف PDF الناتج باستخدام طريقة Save.

يظهر لك مقطع الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```cpp
void AddEmptyPageEnd() {
    // فتح المستند
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // إدراج صفحة فارغة في نهاية ملف PDF
    document->get_Pages()->Add();

    // حفظ الملف الناتج
    document->Save(_dataDir + outputFileName);
}
```