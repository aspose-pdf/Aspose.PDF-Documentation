---
title: Flatten Annotation from PDF to XFDF 
type: docs
weight: 40
url: /net/flatten-annotation/
description: يشرح هذا القسم كيفية تصدير التعليقات التوضيحية من ملف PDF إلى XFDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تعني عملية التسوية أنه عندما تتم إزالة تعليق توضيحي من مستند، يتم الاحتفاظ بالتمثيل المرئي كما هو. يبقى التعليق التوضيحي المسطح مرئيًا ولكنه لم يعد قابلًا للتحرير من قبل المستخدمين أو التطبيق. يمكن استخدام هذا، على سبيل المثال، لتطبيق التعليقات التوضيحية بشكل دائم على المستند أو لجعل التعليقات التوضيحية مرئية للمشاهدين الذين لا يمكنهم عرض التعليقات التوضيحية. إذا لم يتم تحديد ذلك، فسيحتفظ التصدير بجميع التعليقات التوضيحية كما هي.

عند تحديد هذا الخيار، سيتم تضمين التعليقات التوضيحية في ملف PDF الذي تم تصديره كتعليقات توضيحية قياسية في PDF.

تحقق من كيفية استخدام طريقة [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) في مقتطف الشيفرة التالي.

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```