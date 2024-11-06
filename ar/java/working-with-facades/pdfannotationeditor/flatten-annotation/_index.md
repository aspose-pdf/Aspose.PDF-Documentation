---
title: Flatten Annotation from PDF File to XFDF (facades)
type: docs
weight: 40
url: ar/java/flatten-annotation/
description: يوضح هذا القسم كيفية تصدير التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تعني عملية التسطيح عندما تتم إزالة التعليق التوضيحي من مستند، يتم الاحتفاظ بتمثيله المرئي كما هو. يظل التعليق التوضيحي المسطح مرئيًا ولكنه لم يعد قابلاً للتحرير من قبل المستخدمين أو تطبيقك. يمكن استخدام هذا، على سبيل المثال، لتطبيق التعليقات التوضيحية بشكل دائم على مستندك أو لجعل التعليقات التوضيحية مرئية للمشاهدين الذين لا يمكنهم عرض التعليقات التوضيحية بطريقة أخرى. إذا لم يتم تحديد ذلك، سيحتفظ التصدير بجميع التعليقات التوضيحية كما هي.

عند تحديد هذا الخيار، سيتم تضمين تعليقاتك التوضيحية في ملف PDF المصدر الخاص بك كتعليقات توضيحية معيارية لـ PDF.

تحقق من كيفية استخدام طريقة [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) في مقتطف الشفرة التالي.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        // ربط ملف PDF
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        // تطبيق التصحيحات
        flattenSettings.setApplyRedactions(true);
        // استدعاء الأحداث
        flattenSettings.setCallEvents(false);
        // إخفاء الأزرار
        flattenSettings.setHideButtons(true);
        // تحديث المظاهر
        flattenSettings.setUpdateAppearances(true);
        // تسطيح التعليقات التوضيحية
        annotationEditor.flatteningAnnotations(flattenSettings);
        // حفظ الملف
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```