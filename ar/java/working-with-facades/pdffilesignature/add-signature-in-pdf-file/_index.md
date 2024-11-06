---
title: إضافة توقيع في ملف PDF
type: docs
weight: 10
url: ar/java/add-signature-in-pdf/
description: يشرح هذا القسم كيفية العمل مع التوقيع في ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## إضافة توقيع رقمي في ملف PDF (واجهات)

تتيح لك فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) إضافة توقيع في ملف PDF. تحتاج إلى إنشاء كائن من فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) باستخدام ملفات PDF المدخلة والمخرجة. تحتاج أيضًا إلى إنشاء كائن مستطيل في المكان الذي تريد إضافة التوقيع فيه ومن أجل ضبط المظهر يمكنك تحديد صورة باستخدام خاصية setSignatureAppearance لكائن [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature).

كما يوفر Aspose.Pdf.Facades أنواعًا مختلفة من التوقيعات مثل PKCS#1، PKCS#7، وPKCS#7Detached.
 من أجل إنشاء توقيع من نوع معين، تحتاج إلى إنشاء كائن من الفئة المحددة مثل PKCS1 أو PKCS7 أو PKCS7Detached باستخدام ملف الشهادة وكلمة المرور.

بمجرد إنشاء كائن من نوع توقيع معين، يمكنك استخدام طريقة sign من فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) لتوقيع ملف PDF وتمرير كائن التوقيع المحدد لهذه الفئة. يمكنك أيضًا تحديد سمات أخرى لهذه الطريقة. أخيرًا، تحتاج إلى حفظ ملف PDF الموقع باستخدام طريقة save من فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). يوضح لك الجزء التالي من الشفرة كيفية إضافة توقيع في ملف PDF.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // إنشاء مستطيل لموقع التوقيع
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // تعيين مظهر التوقيع
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // إنشاء أي من الأنواع الثلاثة للتوقيع
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "أنا مؤلف الوثيقة", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect,
                signature);
        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

يوضح مثال الشيفرة التالي قدرتنا على توقيع مستند بتوقيعين. في مثالنا، نضع التوقيع الأول على الصفحة الأولى، والثاني على الصفحة الثانية. يمكنك تحديد الصفحات التي تحتاجها.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // التوقيع بالتوقيع الأول

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // إنشاء مستطيل لموقع التوقيع الأول
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // إنشاء كائن التوقيع الأول
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "أنا مؤلف المستند", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, أستراليا", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // التوقيع بالتوقيع الثاني

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // إنشاء مستطيل لموقع التوقيع الثاني
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // إنشاء كائن التوقيع الثاني
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "أنا مراجع المستند", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, أستراليا", true,
                rect2, signature2);

        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


For a document with forms or acroforms that needs to be signed, see the following example.  
أنت بحاجة إلى إنشاء كائن من فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) باستخدام ملفات PDF المدخلة والمخرجة. استخدم bindPdf للربط. قم بإنشاء توقيع مع القدرة على إضافة الخصائص المطلوبة. في مثالنا هم 'Reason' و 'CustomAppearance'.

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // إنشاء أي من أنواع التوقيعات الثلاثة
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("التوقيع كمؤلف");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


إذا كان مستندنا يحتوي على حقلين، فإن خوارزمية توقيعه مشابهة للمثال الأول.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // إنشاء أي من أنواع التوقيع الثلاثة
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("التوقيع كالمؤلف"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // إنشاء أي من أنواع التوقيع الثلاثة
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("التوقيع كمراجع"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```