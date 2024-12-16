---
title: استخراج التعليقات التوضيحية (الواجهات)
type: docs
weight: 30
url: /ar/java/extract-annotation/
description: يشرح هذا القسم كيفية استخراج التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) تتيح لك طريقة استخراج التعليقات التوضيحية من ملف PDF. لاستخراج التعليقات التوضيحية، تحتاج إلى إنشاء كائن [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-). بعد ذلك، تحتاج إلى إنشاء تعداد لأنواع التعليقات التوضيحية التي تريد استخراجها من ملف PDF. وأخيرًا، احفظ ملف PDF المحدث باستخدام طريقة Save لكائن PdfAnnotationEditor. يوضح لك مقطع الشيفرة التالي كيفية استخراج التعليقات التوضيحية من ملف PDF.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // استخراج التعليقات التوضيحية
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```