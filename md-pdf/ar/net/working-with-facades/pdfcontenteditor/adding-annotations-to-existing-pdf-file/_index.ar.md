---
title: إضافة التعليقات التوضيحية إلى ملف PDF موجود
type: docs
weight: 80
url: /net/adding-annotations-to-existing-pdf-file/
description: تشرح هذه القسم كيفية إضافة التعليقات التوضيحية إلى ملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة تعليق توضيحي نصي مجاني في ملف PDF موجود (واجهات)

يسمح لك [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) بإضافة تعليقات توضيحية من أنواع مختلفة في ملف PDF موجود. يمكنك استخدام الطريقة المناسبة لإضافة تعليق توضيحي معين. على سبيل المثال، في مقطع الكود التالي، قمنا باستخدام طريقة [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) لإضافة تعليق توضيحي من نوع [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

يمكن إضافة أي نوع من التعليقات التوضيحية إلى ملف PDF بنفس الطريقة.
``` 
أولاً، تحتاج إلى إنشاء كائن من نوع [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثانياً، يجب عليك إنشاء كائن Rectangle لتحديد منطقة التعليق.

بعد ذلك، يمكنك استدعاء طريقة [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) لإضافة تعليق [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)، ثم استخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لحفظ ملف PDF المحدث.

يعرض مقتطف الكود التالي كيفية إضافة تعليق نص حر في ملف PDF.

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
```
## إضافة تعليق نصي في ملف PDF موجود (الواجهات)

في هذا المثال أيضًا، تحتاج إلى إنشاء كائن من نوع [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثانيًا، يجب عليك إنشاء كائن Rectangle لتحديد منطقة التعليق. بعد ذلك، يمكنك استدعاء طريقة [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) لإضافة تعليق نصي حر، وإنشاء عنوان للتعليقات الخاصة بك، ورقم الصفحة التي يقع فيها التعليق.

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## إضافة تعليق خط في ملف PDF موجود (الواجهات)

نحدد أيضًا المستطيل، إحداثيات بداية ونهاية الخط، رقم الصفحة، السمك، النمط واللون لإطار التعليق، نوع خط الشرطة، نوع بداية ونهاية الخط.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Create Line Annotation
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```