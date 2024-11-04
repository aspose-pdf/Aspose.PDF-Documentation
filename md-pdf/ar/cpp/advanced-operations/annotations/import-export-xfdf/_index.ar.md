---
title: استيراد وتصدير التعليقات إلى تنسيق XFDF باستخدام Aspose.PDF لـ C++
linktitle: استيراد وتصدير التعليقات إلى تنسيق XFDF
type: docs
weight: 40
url: /cpp/import-export-xfdf/
description: يمكنك استيراد وتصدير التعليقات باستخدام تنسيق XFDF مع C++ ومكتبة Aspose.PDF لـ C++.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF هو تنسيق ملفات متوافق مع قارئات PDF. تستخدم ملفات XFDF تنسيق XML لتخزين البيانات مثل ترميز النماذج والتعليقات، والتي يمكن حفظها واستيرادها/تصديرها إلى PDF وعرضها.

يمكن استخدام XFDF لمهام مختلفة كثيرة، ولكن في حالتنا، يمكن استخدامه إما لإرسال أو استقبال بيانات النماذج أو التعليقات إلى أجهزة كمبيوتر أو خوادم أخرى، إلخ، أو يمكن استخدامه لأرشفة بيانات النماذج أو التعليقات.

{{% /alert %}}

**Aspose.PDF لـ C++** هو مكون غني بالميزات عندما يتعلق الأمر بتحرير مستندات PDF. كما نعلم، XFDF هو جانب مهم في معالجة نماذج PDF، وقد اهتمت Aspose.Pdf.Facades namespace في Aspose.PDF for C++ بهذا الأمر جيدًا، وقدمت طرقًا لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF.

تحتوي فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) طريقة توفر وظيفة تصدير التعليقات التوضيحية من مستند PDF إلى ملف XFDF، بينما [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) طريقة تسمح لك باستيراد التعليقات التوضيحية من ملف XFDF موجود. من أجل استيراد أو تصدير التعليقات التوضيحية نحتاج إلى تحديد أنواع التعليقات التوضيحية. يمكننا تحديد هذه الأنواع في شكل تعداد ثم تمرير هذا التعداد كمعامل لأي من هذه الطرق.

يظهر مقطع الشيفرة التالي كيفية تصدير التعليقات التوضيحية إلى ملف XFDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Create PdfAnnotationEditor object
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Bind PDF document to the Annotation Editor
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Export annotations
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
النص التالي يصف كيفية استيراد التعليقات إلى ملف XFDF:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // إنشاء كائن PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // إنشاء مستند PDF جديد
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // استيراد التعليقات
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // حفظ ملف PDF الناتج
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## طريقة أخرى لتصدير/استيراد التعليقات دفعة واحدة

في الكود أدناه، تتيح طريقة ImportAnnotations استيراد التعليقات مباشرة من مستند PDF آخر.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // إنشاء كائن PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // إنشاء مستند PDF جديد
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // يتيح محرر التعليقات استيراد التعليقات من عدة مستندات PDF،
    // ولكن في هذا المثال نستخدم واحدًا فقط.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // حفظ ملف PDF الناتج
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```