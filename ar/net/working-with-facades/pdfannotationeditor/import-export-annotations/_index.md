---
title: استيراد وتصدير التعليقات التوضيحية إلى XFDF
type: docs
weight: 20
url: /ar/net/import-export-annotations/
description: يوضح هذا القسم كيفية استيراد وتصدير التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF يشير إلى تنسيق بيانات نماذج XML. إنه تنسيق ملف يستند إلى XML. يُستخدم هذا التنسيق لتمثيل بيانات النماذج أو التعليقات التوضيحية الموجودة في نموذج PDF. يمكن استخدام XFDF لأغراض متعددة، ولكن في حالتنا، يمكن استخدامه إما لإرسال أو استقبال بيانات النماذج أو التعليقات التوضيحية إلى أجهزة كمبيوتر أو خوادم أخرى إلخ، أو يمكن استخدامه لأرشفة بيانات النماذج أو التعليقات التوضيحية. في هذه المقالة، سنرى كيف أخذ Aspose.Pdf.Facades هذا المفهوم بعين الاعتبار وكيف يمكننا استيراد وتصدير بيانات التعليقات التوضيحية إلى ملف XFDF.

## استيراد وتصدير التعليقات التوضيحية إلى XFDF

[Aspose.PDF for .NET](/pdf/ar/net/) هو مكون غني بالميزات عندما يتعلق الأمر بتحرير مستندات PDF. 
كما نعلم، XFDF هو جانب مهم من معالجة نماذج PDF، [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/ar/net/) قد أخذ هذا في الاعتبار جيدًا، وقدم طرقًا لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF.

تحتوي فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF.
``` [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) توفر الطريقة وظيفة تصدير التعليقات التوضيحية من مستند PDF إلى ملف XFDF، بينما [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) تتيح لك الطريقة استيراد التعليقات التوضيحية من ملف XFDF موجود. من أجل استيراد أو تصدير التعليقات التوضيحية، نحتاج إلى تحديد أنواع التعليقات التوضيحية. يمكننا تحديد هذه الأنواع في شكل تعداد ثم تمرير هذا التعداد كمعامل إلى أي من هذه الطرق. بهذه الطريقة، سيتم استيراد أو تصدير التعليقات التوضيحية للأنواع المحددة فقط إلى ملف XFDF.

يعرض لك مقتطف الشيفرة التالي كيفية استيراد التعليقات التوضيحية إلى ملف XFDF:

```csharp
public static void ImportAnnotation()
        {
            var sources = new string[] { _dataDir + "sample_cats_dogs.pdf" };
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample.pdf");
            annotationEditor.ImportAnnotations(sources);
            annotationEditor.Save(_dataDir + "sample_demo.pdf");
        }
```
النص البرمجي التالي يصف كيفية استيراد/تصدير التعليقات التوضيحية إلى ملف XFDF:

```csharp
public static void ImportExportXFDF01()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.Close();
            var document = new Document();
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```

بهذه الطريقة، سيتم فقط استيراد أو تصدير التعليقات التوضيحية من الأنواع المحددة إلى ملف XFDF.

```csharp
   public static void ImportExportXFDF02()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.Close();

            var document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```