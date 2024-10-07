---
title: تعديل التعليقات التوضيحية في ملف PDF الخاص بك
type: docs
weight: 50
url: /net/modify-annotations/
description: يوضح هذا القسم كيفية تعديل التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تتيح لك طريقة [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) تغيير السمات الأساسية للتعليق التوضيحي مثل الموضوع، وتاريخ التعديل، والمؤلف، ولون التعليق التوضيحي، وعلم الفتح. يمكنك أيضًا تعيين المؤلف مباشرة باستخدام طريقة ModifyAnnotations. توفر هذه الفئة أيضًا طريقتين محملتين لحذف التعليقات التوضيحية. الطريقة الأولى المسماة DeleteAnnotations تحذف جميع التعليقات التوضيحية من ملف PDF.

على سبيل المثال، في الشيفرة التالية، فكر في تغيير المؤلف في تعليقنا التوضيحي باستخدام [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

الطريقة الثانية تتيح لك حذف جميع التعليقات التوضيحية من نوع محدد.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // إنشاء كائن جديد من النوع Annotation لتعديل خصائص التعليقات التوضيحية
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // تعيين خصائص جديدة للتعليقات التوضيحية
                Title = "Aspose.PDF Demo User",
                Subject = "Technical Article"
            };
            // تعديل التعليقات التوضيحية في ملف PDF
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## انظر أيضًا

حاول المقارنة وإيجاد طريقة للعمل مع التعليقات التوضيحية التي تناسبك. لنتعلم قسم [التعليقات التوضيحية على PDF](/pdf/net/annotations/).