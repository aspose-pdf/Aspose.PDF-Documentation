---
title: العمل مع التوقيع في ملف PDF
type: docs
weight: 40
url: ar/java/working-with-signature-in-a-pdf-file/
description: يشرح هذا القسم كيفية العمل مع التوقيع في ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## كيفية استخراج معلومات التوقيع

يدعم Aspose.PDF for Java ميزة التوقيع الرقمي لملفات PDF باستخدام فئة PdfFileSignature. حاليًا، من الممكن أيضًا تحديد صلاحية الشهادة ولكن لا يمكننا استخراج الشهادة كاملة. المعلومات التي يمكن استخراجها هي المفتاح العام، البصمة، والجهة المصدرة، إلخ.

لاستخراج معلومات التوقيع، قمنا بتقديم الطريقة extractCertificate(..) إلى فئة PdfFileSignature. يرجى إلقاء نظرة على الكود التالي الذي يوضح الخطوات لاستخراج الشهادة من كائن PdfFileSignature:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## استخراج الصورة من حقل التوقيع (PdfFileSignature)

تدعم Aspose.PDF for Java ميزة التوقيع الرقمي لملفات PDF باستخدام فئة PdfFileSignature، وأثناء توقيع المستند يمكنك أيضًا تعيين صورة لمظهر التوقيع. الآن توفر هذه الواجهة البرمجية أيضًا القدرة على استخراج معلومات التوقيع وكذلك الصورة المرتبطة بحقل التوقيع.

من أجل استخراج معلومات التوقيع، قمنا بإضافة طريقة [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) إلى فئة PdfFileSignature. يرجى إلقاء نظرة على مقطع الشيفرة التالي الذي يوضح الخطوات لاستخراج الصورة من كائن PdfFileSignature:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## قمع الموقع والسبب

تتيح وظيفة Aspose.PDF تكوينًا مرنًا لحالة التوقيع الرقمي. توفر فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) القدرة على توقيع ملف PDF. يسمح تنفيذ طريقة التوقيع بتوقيع PDF وتمرير كائن التوقيع المحدد إلى هذه الفئة. تحتوي طريقة التوقيع على مجموعة من السمات لتخصيص توقيع رقمي الناتج. في حالة الحاجة إلى قمع بعض سمات النص من توقيع الناتج، يمكنك تركها فارغة. يوضح جزء الشيفرة التالي كيفية قمع صفين الموقع والسبب من كتلة التوقيع:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // إنشاء مستطيل لموقع التوقيع
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // تعيين مظهر التوقيع
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // إنشاء أي نوع من الأنواع الثلاثة للتوقيع
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## ميزات التخصيص للتوقيع الرقمي

تتيح Aspose.PDF لـ Java ميزات تخصيص للتوقيع الرقمي. يتم تنفيذ طريقة Sign لفئة SignatureCustomAppearance مع 6 تحمّلات لراحتك في الاستخدام. على سبيل المثال، يمكنك تكوين نتيجة التوقيع فقط بواسطة مثيل فئة SignatureCustomAppearance وقيم خصائصها. يوضح المقتطف البرمجي التالي كيفية إخفاء "موقع رقميًا بواسطة" التسمية التوضيحية من توقيعك الرقمي في الـ PDF.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // إنشاء مستطيل لموقع التوقيع
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // إنشاء أي من الأنواع الثلاثة للتوقيعات
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("مُوقَّع بواسطة:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // حفظ ملف PDF الناتج
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## تغيير اللغة في النص الرقمي للتوقيع

باستخدام Aspose.PDF لواجهة برمجة تطبيقات Java، يمكنك توقيع ملف PDF باستخدام أي من الأنواع الثلاثة التالية من التوقيعات:

- PKCS#1
- PKCS#7
- PKCS#7

كل من التوقيعات المقدمة تحتوي على مجموعة من خصائص الإعدادات المطبقة لراحتك (التوطين، تنسيق التاريخ والوقت، عائلة الخط إلخ). يوفر الصف SignatureCustomAppearance الوظائف المقابلة. يوضح مقتطف الكود التالي كيفية تغيير اللغة في النص الرقمي للتوقيع:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // إنشاء مستطيل لموقع التوقيع
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // إنشاء أي من الأنواع الثلاثة للتوقيع
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // توقيع ملف PDF
        pdfSign.sign(1, true, rect, pkcs);
        // حفظ ملف PDF الناتج
        pdfSign.save(outFile);
    }
```