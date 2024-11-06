---
title: إنشاء مستند PDF باستخدام C++
linktitle: إنشاء
type: docs
weight: 10
url: ar/cpp/create-document/
description: المهمة الأكثر شيوعًا وأساسًا في العمل مع ملف PDF هي إنشاء مستند من البداية. استخدم مكتبة Aspose.PDF for C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** API تمكن مطوري تطبيقات C++ من تضمين وظائف معالجة مستندات PDF في تطبيقاتهم. يمكن استخدامها لإنشاء وقراءة ملفات PDF دون الحاجة إلى أي برامج أخرى مثبتة على الجهاز الأساسي. يمكن استخدام Aspose.PDF for C++ في مجموعة متنوعة من أنواع تطبيقات C++ مثل QT وMFC وتطبيقات الكونسول.

## كيفية إنشاء ملف PDF باستخدام C++

لإنشاء ملف PDF باستخدام C++، يمكن استخدام الخطوات التالية.

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. إضافة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) إلى كائن المستند
1.  إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)
1. إضافة [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) في الصفحة
1. حفظ مستند PDF الناتج

```cpp
void CreatePDF() {
    // سلسلة لمسار الاسم.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String filename("sample-new.pdf");

    // تهيئة كائن المستند
    auto document = MakeObject<Document>();
    // إضافة صفحة
    auto page = document->get_Pages()->Add();

    // إضافة نص إلى الصفحة الجديدة
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // حفظ ملف PDF المحدث
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```