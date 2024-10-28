---
title: كيفية التوقيع الإلكتروني على PDF
linktitle: التوقيع الإلكتروني على PDF
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: التوقيع الإلكتروني على مستندات PDF باستخدام Java. التحقق من صحة التوقيعات الإلكترونية على ملفات PDF باستخدام تطبيق Java مع مكتبة PDF. يمكنك توثيق ملف PDF بشهادة PKCS1.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

عند توقيع مستند PDF باستخدام توقيع، فإنك تؤكد في الأساس أن محتوياته يجب أن تبقى "كما هي". وبالتالي، فإن أي تغييرات تُجرى بعد ذلك تُبطل التوقيع، وبذلك تعرف ما إذا تم تعديل المستند. يتيح لك توثيق المستند أولاً تحديد التغييرات التي يمكن للمستخدم إجراؤها على المستند دون إبطال التوثيق.

بمعنى آخر، سيظل المستند يُعتبر محافظًا على سلامته ويمكن للمستلم أن يثق في المستند. لمزيد من التفاصيل، يرجى زيارة توثيق وتوقيع PDF.

لتنفيذ المتطلبات المذكورة أعلاه، تم إجراء التغييرات التالية على واجهة برمجة التطبيقات العامة.

تمت إضافة طريقة isCertified(…) إلى فئة PdfFileSignature.

## توقيع PDF بالتوقيعات الرقمية

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // استخدام كائنات PKCS7/PKCS7Detached
                                                                                             
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // حفظ ملف PDF الناتج
        signature.save(outFile);
    }
```

## إضافة طابع زمني إلى التوقيع الرقمي

يدعم Aspose.PDF for Java توقيع ملفات PDF رقميًا باستخدام خادم طوابع زمنية أو خدمة ويب.

من أجل تحقيق هذا المتطلب، تم إضافة فئة [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) إلى مساحة الأسماء Aspose.PDF. يرجى إلقاء نظرة على المقتطف البرمجي التالي الذي يحصل على الطابع الزمني ويضيفه إلى مستند PDF:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // يمكن تجاهل اسم المستخدم/كلمة المرور
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // إنشاء أي نوع من أنواع التوقيعات الثلاثة
        signature.sign(1, "سبب التوقيع", "الاتصال", "الموقع", true, rect, pkcs);
        // حفظ ملف PDF الناتج
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```