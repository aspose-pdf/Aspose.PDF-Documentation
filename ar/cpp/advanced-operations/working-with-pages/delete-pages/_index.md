---
title: حذف صفحات PDF برمجيًا
linktitle: حذف صفحات PDF
type: docs
weight: 30
url: ar/cpp/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF باستخدام مكتبة C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكنك حذف الصفحات من ملف PDF باستخدام Aspose.PDF لـ C++. لحذف صفحة معينة من مجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).

## حذف صفحة من ملف PDF

1. قم باستدعاء الطريقة [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) وحدد مؤشر الصفحة
2. قم باستدعاء طريقة Save لحفظ ملف PDF المحدث
يوضح مقطع الشيفرة التالي كيفية حذف صفحة معينة من ملف PDF باستخدام C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // احذف صفحة معينة
    document->get_Pages()->Delete(2);

    // احفظ ملف PDF المحدث
    document->Save(_dataDir + inputFileName);
}
```