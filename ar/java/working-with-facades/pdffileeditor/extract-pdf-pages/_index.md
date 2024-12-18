---
title: استخراج صفحات PDF
type: docs
weight: 20
url: /ar/java/extract-pdf-pages/
description: يوضح هذا القسم كيفية استخراج صفحات PDF باستخدام com.aspose.pdf.facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## استخراج صفحات PDF بين رقمين باستخدام مسارات الملفات

تسمح لك طريقة [استخراج](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) باستخراج نطاق محدد من الصفحات من ملف PDF. يتيح لك هذا التحميل الزائد استخراج الصفحات أثناء معالجة ملفات PDF من القرص. يتطلب هذا التحميل الزائد المعلمات التالية: مسار ملف الإدخال، صفحة البداية، صفحة النهاية، ومسار ملف الإخراج. سيتم استخراج الصفحات من صفحة البداية إلى صفحة النهاية وسيتم حفظ الإخراج على القرص. يوضح لك مقتطف الشيفرة البرمجية التالي كيفية استخراج صفحات PDF بين رقمين باستخدام مسارات الملفات.

```java
  public static void Extract_PDFPages_FilePaths() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // استخراج الصفحات
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## استخراج مجموعة من صفحات PDF باستخدام مسارات الملفات

إذا كنت لا ترغب في استخراج نطاق من الصفحات، بل مجموعة معينة من الصفحات، فإن طريقة [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) تتيح لك القيام بذلك أيضًا. تحتاج أولاً إلى إنشاء مصفوفة صحيحة تحتوي على جميع أرقام الصفحات التي تحتاج إلى استخراجها. يأخذ هذا التحميل الزائد من طريقة [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) المعلمات التالية: ملف PDF المدخل، مصفوفة صحيحة للصفحات المراد استخراجها، وملف PDF المخرج. يوضح لك مقطع الكود التالي كيفية استخراج صفحات PDF باستخدام مسارات الملفات.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // استخراج الصفحات
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## استخراج صفحات PDF بين رقمين باستخدام التدفقات

تسمح لك طريقة [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) باستخراج مجموعة من الصفحات باستخدام التدفقات. تحتاج إلى تمرير المعلمات التالية لهذا التحميل الزائد: تدفق الإدخال، الصفحة البداية، الصفحة النهاية، وتدفق الإخراج. سيتم استخراج الصفحات المحددة بالنطاق بين صفحة البداية وصفحة النهاية من تدفق الإدخال وحفظها في تدفق الإخراج. يوضح لك مقتطف الشيفرة التالي كيفية استخراج صفحات PDF بين رقمين باستخدام التدفقات.

```java
public static void Extract_PDFPages_Streams()
    {
         // إنشاء كائن PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
         // إنشاء التدفقات
         using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
         using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
         // استخراج الصفحات
         pdfEditor.Extract(inputStream, 1, 3, outputStream);

    }
```


## استخراج مصفوفة من صفحات PDF باستخدام التدفقات

يمكن استخراج مصفوفة من الصفحات من تدفق PDF وحفظها في تدفق الإخراج باستخدام التحميل المناسب لطريقة [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-). إذا كنت لا ترغب في استخراج نطاق من الصفحات، بل مجموعة من الصفحات المعينة، فإن طريقة [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) تتيح لك القيام بذلك أيضًا. تحتاج أولاً إلى إنشاء مصفوفة أعداد صحيحة تحتوي على جميع أرقام الصفحات التي تحتاج إلى استخراجها. يتطلب هذا التحميل الزائد لطريقة [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) المعلمات التالية: تدفق الإدخال، مصفوفة أعداد صحيحة للصفحات التي سيتم استخراجها، وتدفق الإخراج. يوضح لك مقتطف الكود التالي كيفية استخراج صفحات PDF باستخدام التدفقات.

```java
public static void Extract_ArrayPDFPages_Streams()
        {
            // إنشاء كائن PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
            // إنشاء التدفقات
            using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
            using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
            {
                int[] pagesToExtract = new int[] { 1, 2 };
                // استخراج الصفحات
                pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
            }
        }
```