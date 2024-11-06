---
title: إضافة التعليقات التوضيحية إلى ملف PDF موجود
type: docs
weight: 80
url: ar/java/adding-annotations-to-existing-pdf-file/
description: يوضح هذا القسم كيفية إضافة التعليقات التوضيحية إلى ملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة تعليق نصي حر في ملف PDF موجود (واجهات)

يعرض التعليق النصي الحر النص مباشرة على الصفحة. يتيح لك [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) إضافة تعليقات توضيحية من أنواع مختلفة في ملف PDF موجود. يمكنك استخدام الطريقة المناسبة لإضافة تعليق معين. على سبيل المثال، في مقتطف الشيفرة التالي، استخدمنا طريقة [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) لإضافة تعليق من نوع النص الحر.

يمكن إضافة أي نوع من التعليقات التوضيحية إلى ملف PDF بنفس الطريقة.
 أولاً، تحتاج إلى إنشاء كائن من نوع [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) وربط ملف PDF المدخل باستخدام طريقة bindPdf. ثانياً، عليك إنشاء كائن مستطيل لتحديد منطقة التعليق التوضيحي. بعد ذلك، يمكنك استدعاء طريقة [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) لإضافة تعليق توضيحي للنص الحر، وتحديد رقم الصفحة التي يقع فيها التعليق التوضيحي، ثم استخدام طريقة الحفظ لحفظ ملف PDF المحدث.

يظهر لك مقطع الشيفرة التالي كيفية إضافة تعليق توضيحي للنص الحر في ملف PDF.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // المتغير الأخير هو رقم الصفحة
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## إضافة تعليق نصي في ملف PDF موجود (واجهات)

في هذا المثال أيضًا، تحتاج إلى إنشاء كائن من نوع [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) وربط ملف PDF المدخل باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-). ثانيًا، يجب عليك إنشاء كائن مستطيل لتحديد منطقة التعليق. بعد ذلك، يمكنك استدعاء طريقة [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) لإضافة تعليق نصي حر، وإنشاء عنوان لتعليقاتك، ورقم الصفحة التي يوجد بها التعليق.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## إضافة تعليق خط في ملف PDF موجود (الواجهات)

نحن أيضًا نحدد المستطيل، إحداثيات بداية ونهاية الخط، رقم الصفحة، السمك، النمط ولون إطار التعليق، نوع خط الفاصل، نوع بداية ونهاية الخط.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // إنشاء تعليق خط
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```