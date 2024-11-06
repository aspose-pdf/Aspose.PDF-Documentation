---
title: Import and Export Annotations to XFDF format using com.aspose.pdf.facades
type: docs
weight: 20
url: ar/java/import-export-annotations/
description: يوضح هذا القسم كيفية تصدير واستيراد التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF تعني تنسيق بيانات النماذج XML. إنه تنسيق ملف يعتمد على XML. يُستخدم تنسيق الملف هذا لتمثيل بيانات النموذج أو التعليقات التوضيحية الموجودة في نموذج PDF. يمكن استخدام XFDF لأغراض عديدة مختلفة، ولكن في حالتنا، يمكن استخدامه إما لإرسال أو استقبال بيانات النموذج أو التعليقات التوضيحية إلى أجهزة كمبيوتر أو خوادم أخرى، أو يمكن استخدامه لأرشفة بيانات النموذج أو التعليقات التوضيحية. في هذه المقالة، سنرى كيف أخذ Aspose.Pdf.Facades هذا المفهوم بعين الاعتبار وكيف يمكننا استيراد وتصدير بيانات التعليقات التوضيحية إلى ملف XFDF.

تحتوي فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) توفر طريقة تصدير التعليقات التوضيحية من مستند PDF إلى ملف XFDF، بينما [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) تسمح لك باستيراد التعليقات التوضيحية من ملف XFDF موجود. من أجل استيراد أو تصدير التعليقات التوضيحية نحتاج إلى تحديد أنواع التعليقات التوضيحية. يمكننا تحديد هذه الأنواع في شكل تعداد ثم تمرير هذا التعداد كوسيطة إلى أي من هذه الطرق.

يظهر لك مقتطف الكود التالي كيفية استيراد التعليقات التوضيحية إلى ملف XFDF:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

مقطع الشيفرة التالي يصف كيفية استيراد/تصدير التعليقات التوضيحية إلى ملف XFDF:

```java
    public static void ImportExportXFDF01() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;
        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            annotationEditor.exportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Document document = new Document();
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```

بهذه الطريقة، سيتم فقط استيراد أو تصدير التعليقات التوضيحية من الأنواع المحددة إلى ملف XFDF.

```java
    public static void ImportExportXFDF02() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;

        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            int[] annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.exportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.close();
        } catch (IOException e) {            
            e.printStackTrace();
        }

        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```