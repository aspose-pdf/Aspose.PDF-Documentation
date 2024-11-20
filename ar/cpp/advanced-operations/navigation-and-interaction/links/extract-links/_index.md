---
title: استخراج الروابط من ملف PDF
linktitle: استخراج الروابط
type: docs
weight: 30
url: /ar/cpp/extract-links/
description: استخراج الروابط من PDF باستخدام C#. يشرح هذا الموضوع كيفية استخراج الروابط باستخدام فئة AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الروابط من ملف PDF

يتم تمثيل الروابط كتعليقات توضيحية في ملف PDF، لذا لاستخراج الروابط، قم باستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. احصل على [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) التي تريد استخراج الروابط منها.
``` استخدم فئة [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) لاستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) من الصفحة المحددة.
1. مرر كائن [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) إلى طريقة Accept الخاصة بكائن Page.
1. احصل على جميع تعليقات الروابط المحددة في كائن IList باستخدام خاصية Selected الخاصة بكائن [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

يظهر لك مقطع الكود التالي كيفية استخراج الروابط من ملف PDF.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // تحميل ملف PDF
    String _dataDir("C:\\Samples\\");

    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"تم تحديد التعليق: {0}", annot->get_Rect());
    }
}
```