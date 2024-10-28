---
title: دمج PDF باستخدام C++
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /cpp/merge-pdf-documents/
description: توضح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

دمج ملفات pdf ليس مهمة سهلة، ولكنه شائع جداً. يمكنك استخدام مكتبة Aspose.PDF for C++ لدمج ملفات PDF في مستند واحد بسرعة وسهولة.

## دمج ملفات PDF باستخدام C++

لدمج ملفين PDF:

1. قم بإنشاء كائنين [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)، يحتوي كل منهما على أحد ملفات PDF المدخلة.
1. ثم قم باستدعاء طريقة الإضافة لمجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) لكائن المستند الذي تريد إضافة ملف PDF الآخر إليه.
1. أضف [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) من المستند الثاني إلى الملف الأول.
1. أخيراً، احفظ ملف PDF الناتج باستخدام طريقة Save.

يوضح مقتطف الكود التالي كيفية دمج ملفات PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // فتح المستند
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // إضافة صفحات المستند الثاني إلى الأول
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // حفظ الملف المدمج
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## مثال حي

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل دمج العروض التقديمية.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)