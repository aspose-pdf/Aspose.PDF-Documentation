---
title: استخراج التعليقات التوضيحية من PDF 
type: docs
weight: 30
url: /net/extract-annotation/
description: توضح هذه القسم كيفية استخراج التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) تتيح لك الطريقة استخراج التعليقات التوضيحية من ملف PDF. من أجل استخراج التعليقات التوضيحية، تحتاج إلى إنشاء كائن [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، تحتاج إلى إنشاء تعداد لأنواع التعليقات التوضيحية التي تريد استخراجها من ملف PDF.

ثم يمكنك استخدام طريقة [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) لاستخراج التعليقات التوضيحية إلى ArrayList. بعد ذلك، يمكنك الدوران عبر هذه القائمة والحصول على التعليقات الفردية. وأخيرا، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor). يوضح لك مقطع الشيفرة التالي كيفية استخراج التعليقات من ملف PDF.

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Extract annotations
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```