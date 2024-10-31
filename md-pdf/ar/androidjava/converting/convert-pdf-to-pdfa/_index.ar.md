---
title: تحويل ملف PDF إلى PDF/A
linktitle: تحويل ملف PDF إلى PDF/A
type: docs
weight: 180
url: /androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF for Java لتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يسمح لك Aspose.PDF بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A. قبل القيام بذلك، يجب التحقق من صحة الملف. يوضح هذا المقال كيفية القيام بذلك.

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من توافق PDF/A. جميع الأدوات في السوق لديها "تمثيلها" الخاص لتوافق PDF/A. يرجى مراجعة هذا المقال حول [أدوات التحقق من PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) للمرجعية. اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF للملفات لأن Adobe هي في مركز كل ما يتعلق بـ PDF.

قبل تحويل PDF إلى ملف متوافق مع PDF/A، تحقق من صحة PDF باستخدام طريقة التحقق.
 تم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة إلى طريقة التحويل. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام التعداد [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## تحويل PDF إلى PDF/A_1b

يوضح الجزء التالي من الشفرة كيفية تحويل ملفات PDF إلى PDF متوافق مع PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // افتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم إجراء التحقق أيضًا
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // احفظ المستند الناتج
        document.save(pdfaFileName.toString());
    }
```

للقيام بالتحقق فقط، استخدم السطر التالي من الكود:

```java
public void ValidatePDF_A_1B() {
        // فتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // التحقق من المستند المتوافق مع PDF/A

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("المستند صالح");
        }
        else {
            resultMessage.setText("المستند غير صالح");
        }
    }
```

## تحويل PDF إلى PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // فتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحويل إلى مستند متوافق مع PDF/A
        // يتم إجراء التحقق أيضًا أثناء عملية التحويل
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // حفظ المستند الناتج
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## تحويل PDF إلى PDF/A_3a

```java
public void convertPDFtoPDFa3a() {
        // افتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم أيضًا إجراء التحقق
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // حفظ المستند الناتج
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## تحويل PDF إلى PDF/A_2a

```java
public void convertPDFtoPDFa2a() {
        // افتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم أيضًا إجراء التحقق
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // حفظ المستند الناتج
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## تحويل PDF إلى PDF/A_3U

```java
 public void convertPDFtoPDFa3u() {
        // فتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم أيضًا إجراء التحقق
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // حفظ المستند الناتج
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## إنشاء PDF/A-3 وإرفاق ملف XML

يوفر Aspose.PDF لنظام Android عبر Java ميزة تحويل ملفات PDF إلى تنسيق PDF/A ويدعم أيضًا إمكانيات إضافة الملفات كمرفقات إلى مستند PDF.
 في حال كان لديك متطلب لربط الملفات بتنسيق الامتثال PDF/A، نوصي باستخدام القيمة PDF_A_3A من تعداد com.aspose.pdf.PdfFormat، حيث أن PDF/A_3a هو التنسيق الذي يوفر ميزة إرفاق أي تنسيق ملف كملف مرفق لملف متوافق مع PDF/A. ومع ذلك، بمجرد إرفاق الملف، يجب تحويله إلى تنسيق Pdf-3a مرة أخرى، من أجل إصلاح البيانات الوصفية. يرجى الاطلاع على مقتطف الشيفرة التالي.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // فتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم أيضًا التحقق من الصلاحية
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // حفظ مستند الإخراج
        try {
            // تحميل ملف XML
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // إضافة المرفق إلى مجموعة المرفقات للمستند
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```