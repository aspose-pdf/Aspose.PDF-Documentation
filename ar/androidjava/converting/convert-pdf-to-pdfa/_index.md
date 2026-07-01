---
title: تحويل ملف PDF إلى PDF/A
linktitle: تحويل ملف PDF إلى PDF/A
type: docs
weight: 180
url: /ar/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-06-30"
description: يوضح لك هذا الموضوع كيف يتيح Aspose.PDF for Java تحويل ملف PDF إلى ملف PDF/A متوافق.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يتيح لك Aspose.PDF تحويل ملف PDF إلى ملف PDF متوافق مع PDF/A. قبل القيام بذلك، يجب التحقق من صحة الملف. توضح هذه المقالة كيفية ذلك.

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من توافق PDF/A. جميع الأدوات في السوق لديها \"representation\" الخاصة بها لتوافق PDF/A. يرجى التحقق من هذه المقالة على [أدوات التحقق من صحة PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) للتوثيق. اخترنا منتجات أدوبي للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن أدوبي هي في مركز كل ما يتعلق بـ PDF.

قبل تحويل ملف PDF إلى ملف متوافق مع PDF/A، قم بالتحقق من صحة ملف PDF باستخدام طريقة validate. يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة convert. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام [إجراء تحويل الخطأ](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) التعداد.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت من خلال هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## تحويل PDF إلى PDF/A_1b

يظهر المقتطف التالي من الكود كيفية تحويل ملفات PDF إلى PDF متوافق مع PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

لإجراء التحقق فقط، استخدم السطر التالي من الشيفرة:

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## تحويل PDF إلى PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
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
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
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
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
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
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
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

يقدم Aspose.PDF for Android عبر Java ميزة تحويل ملفات PDF إلى تنسيق PDF/A كما يدعم أيضًا إمكانية إضافة ملفات كمرفق إلى مستند PDF. إذا كان لديك حاجة لإرفاق ملفات إلى تنسيق الامتثال PDF/A، فإننا نوصي باستخدام القيمة PDF_A_3A من تعداد com.aspose.pdf.PdfFormat، حيث إن PDF/A_3a هو التنسيق الذي يتيح إمكانية إرفاق أي صيغة ملف كمرفق إلى ملف متوافق مع PDF/A. ومع ذلك، بمجرد إرفاق الملف، يجب عليك تحويله مرة أخرى إلى تنسيق Pdf-3a لإصلاح البيانات الوصفية. يرجى إلقاء نظرة على مقتطف الشيفرة التالي.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
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

