---
title: تحويل PDF إلى تنسيقات PDF/A
linktitle: تحويل PDF إلى تنسيقات PDF/A
type: docs
weight: 100
url: ar/java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: يوضح لك هذا الموضوع كيفية استخدام Aspose.PDF لتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java** يسمح لك بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A. قبل القيام بذلك، يجب التحقق من صحة الملف. يوضح هذا المقال كيفية القيام بذلك.

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من مطابقة PDF/A. كل الأدوات في السوق لديها "تمثيل" خاص بها لمطابقة PDF/A. يرجى مراجعة هذا المقال حول [أدوات التحقق من PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) للمراجعة. اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe تقع في مركز كل ما يتصل بـ PDF.

قبل تحويل PDF إلى ملف متوافق مع PDF/A، تحقق من صحة PDF باستخدام طريقة التحقق.
 يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة التحويل. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام التعداد [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## تحويل PDF إلى PDF/A_1b

يظهر المقتطف التالي من الشيفرة كيفية تحويل ملفات PDF إلى ملفات متوافقة مع PDF/A-1b.

```java
// فتح المستند
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// التحويل إلى مستند متوافق مع PDF/A
// أثناء عملية التحويل، يتم أيضًا إجراء التحقق
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// حفظ المستند الناتج
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

لإجراء التحقق فقط، استخدم السطر التالي من الشيفرة:

```java
// فتح المستند
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// التحقق من PDF لـ PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("صالح");
} else {
    System.out.println("غير صالح");
}
document.close();
```

## تحويل PDF إلى PDF/A_3b

من [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java)، تدعم واجهة برمجة التطبيقات أيضًا تحويل ملفات PDF إلى تنسيق PDF/A_3b.

```java
// فتح المستند
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// التحويل إلى مستند متوافق مع PDF/A
// أثناء عملية التحويل، يتم أيضًا إجراء التحقق
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// حفظ المستند الناتج
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## تحويل PDF إلى PDF/A_3a

من [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java)، تدعم واجهة برمجة التطبيقات أيضًا تحويل ملفات PDF إلى تنسيق PDF/A_3a.

```java
// فتح المستند
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// التحويل إلى مستند متوافق مع PDF/A
// أثناء عملية التحويل، يتم أيضًا إجراء التحقق
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// حفظ المستند الناتج
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## تحويل PDF إلى PDF/A_2a

بدءًا من إصدار [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java)، توفر واجهة برمجة التطبيقات ميزة تحويل ملفات PDF إلى تنسيق PDF/A3.

```java
    public static void ConvertPDFtoPDFa2a() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم التحقق أيضًا
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // حفظ المستند الناتج
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## تحويل PDF إلى PDF/A_3U

بدءًا من إصدار Aspose.PDF for Java 17.2.0، توفر واجهة برمجة التطبيقات ميزة تحويل ملفات PDF إلى تنسيق PDF/A_3U.

```java
    public static void ConvertPDFtoPDFa3u() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // تحويل إلى مستند متوافق مع PDF/A
        // أثناء عملية التحويل، يتم التحقق أيضًا
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // حفظ المستند الناتج
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## إنشاء PDF/A-3 وإرفاق ملف XML

يوفر Aspose.PDF for Java ميزة تحويل ملفات PDF إلى تنسيق PDF/A ويدعم أيضًا قدرات إضافة الملفات كمرفقات إلى مستند PDF. في حال كنت بحاجة إلى إرفاق ملفات بتنسيق PDF/A الامتثالي، فنحن نوصي باستخدام قيمة PDF_A_3A من تعداد com.aspose.pdf.PdfFormat، حيث أن PDF/A_3a هو التنسيق الذي يوفر ميزة إرفاق أي تنسيق ملف كمرفق إلى ملف متوافق مع PDF/A. ومع ذلك، بمجرد إرفاق الملف، يجب تحويله إلى تنسيق Pdf-3a مرة أخرى، من أجل إصلاح البيانات الوصفية. يرجى إلقاء نظرة على مقتطف الكود التالي.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // إضافة صفحة إلى ملف PDF
        doc.getPages().add();
        // تحميل ملف XML
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "ملف xml نموذجي");
        // إضافة المرفق إلى مجموعة مرفقات المستند
        doc.getEmbeddedFiles().add(fileSpecification);
        // تنفيذ تحويل PDF/A_3a
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* أو PDF_A_3B */, ConvertErrorAction.Delete);
        // حفظ ملف PDF النهائي
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PDF/A باستخدام تطبيق مجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}