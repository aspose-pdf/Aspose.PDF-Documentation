---
title: تعديل التعليقات التوضيحية في ملف PDF الخاص بك (واجهات)
type: docs
weight: 50
url: ar/java/modify-annotations/
description: يوضح هذا القسم كيفية تعديل التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تتيح لك طريقة [modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) تغيير السمات الأساسية للتعليق التوضيحي مثل الموضوع وتاريخ التعديل والمؤلف ولون التعليق التوضيحي وعلم الفتح. يمكنك أيضًا تعيين المؤلف مباشرة باستخدام طريقة ModifyAnnotations. توفر هذه الفئة أيضًا طريقتين محملتين لحذف التعليقات التوضيحية. الطريقة الأولى المسماة DeleteAnnotations تحذف جميع التعليقات التوضيحية من ملف PDF.

على سبيل المثال، في الكود التالي، فكر في تغيير المؤلف في تعليقنا التوضيحي باستخدام [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

تتيح لك الطريقة الثانية حذف جميع التعليقات التوضيحية لنوع محدد.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // إنشاء كائن جديد من النوع Annotation لتعديل خصائص التعليق التوضيحي
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Aspose.PDF Demo User");
        annotation.setSubject("Technical Article");

        // تعديل التعليقات التوضيحية في ملف PDF
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## انظر أيضًا

حاول المقارنة وإيجاد طريقة للعمل مع التعليقات التوضيحية التي تناسبك. دعنا نتعلم قسم [التعليقات التوضيحية على PDF](/pdf/java/annotations/).