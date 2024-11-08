---
title: استخراج صفحات PDF
type: docs
weight: 40
url: /ar/net/extract-pdf-pages/
description: يوضح هذا القسم كيفية استخراج صفحات PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## استخراج صفحات PDF بين رقمين باستخدام مسارات الملفات

تتيح لك طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) لفئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) استخراج نطاق محدد من الصفحات من ملف PDF. يتيح لك هذا التحميل الزائد استخراج الصفحات أثناء معالجة ملفات PDF من القرص. يتطلب هذا التحميل الزائد المعلمات التالية: مسار ملف الإدخال، الصفحة البداية، الصفحة النهاية، ومسار ملف الإخراج. سيتم استخراج الصفحات من الصفحة البداية إلى الصفحة النهاية وسيتم حفظ الإخراج على القرص. يُظهر لك مقطع الشيفرة التالي كيفية استخراج صفحات PDF بين رقمين باستخدام مسارات الملفات.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // إنشاء كائن PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // استخراج الصفحات
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## استخراج مصفوفة من صفحات PDF باستخدام مسارات الملفات

إذا كنت لا ترغب في استخراج نطاق من الصفحات، بل مجموعة من الصفحات المحددة، فإن طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) تتيح لك القيام بذلك أيضًا. تحتاج أولاً إلى إنشاء مصفوفة أعداد صحيحة تحتوي على جميع أرقام الصفحات التي تحتاج إلى استخراجها. تأخذ هذه الحمولة الزائدة من طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) المعلمات التالية: ملف PDF الإدخال، مصفوفة أعداد صحيحة للصفحات المراد استخراجها، وملف PDF الإخراج. يوضح لك مقتطف الشيفرة التالي كيفية استخراج صفحات PDF باستخدام مسارات الملفات.

```csharp
public static void Extract_PDFPages_Streams()
{
    // إنشاء كائن PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // إنشاء تدفقات
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // استخراج الصفحات
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## استخراج صفحات PDF بين رقمين باستخدام التدفقات

تسمح لك طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) في فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) باستخراج مجموعة من الصفحات باستخدام التدفقات. تحتاج إلى تمرير المعلمات التالية إلى هذا التحميل الزائد: دفق الإدخال، الصفحة البدء، الصفحة الانتهاء، ودفق الإخراج. سيتم استخراج الصفحات المحددة بالنطاق بين صفحة البدء وصفحة الانتهاء من دفق الإدخال وحفظها في دفق الإخراج. يوضح لك مقتطف الشيفرة التالي كيفية استخراج صفحات PDF بين رقمين باستخدام التدفقات.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // إنشاء كائن PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // استخراج الصفحات
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## استخراج مجموعة من صفحات PDF باستخدام التدفقات


يمكن استخراج مجموعة من الصفحات من تدفق PDF وحفظها في تدفق الإخراج باستخدام التحميل الزائد المناسب لطريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). إذا كنت لا ترغب في استخراج نطاق من الصفحات، بل مجموعة معينة من الصفحات، فإن طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) تتيح لك القيام بذلك أيضًا. تحتاج أولاً إلى إنشاء مصفوفة أعداد صحيحة تحتوي على جميع أرقام الصفحات التي تحتاج إلى استخراجها. هذا التحميل الزائد لطريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) يأخذ المعلمات التالية: تدفق الإدخال، مصفوفة صحيحة للصفحات المراد استخراجها وتدفق الإخراج.
يظهر لك مقتطف الكود التالي كيفية استخراج صفحات PDF باستخدام التدفقات.

```csharp
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
```