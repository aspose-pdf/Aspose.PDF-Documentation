---
title: تقسيم PDF برمجياً
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/cpp/split-pdf-document/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية باستخدام C++.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني على الإنترنت يسمح لك بالتحقيق في كيفية عمل وظيفة تقسيم العروض التقديمية.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يشرح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات C++ الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة باستخدام C++، يمكن اتباع الخطوات التالية:

1. قم بالتنقل عبر صفحات مستند PDF من خلال مجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. لكل تكرار، قم بإنشاء كائن Document جديد ونسخ كائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) الفردي إلى المستند الفارغ
1. احفظ ملف PDF الجديد باستخدام طريقة الحفظ

يوضح لك مقتطف الشفرة C++ التالي كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```cpp
void SplittingDocuments() {
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String documentFileName("sample.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // التكرار خلال كل الصفحات
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```