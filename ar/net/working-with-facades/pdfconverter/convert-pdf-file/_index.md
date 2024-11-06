---
title: تحويل ملف PDF
type: docs
weight: 30
url: ar/net/convert-pdf-file/
description: يشرح هذا القسم كيفية تحويل ملف PDF باستخدام واجهات Aspose.PDF باستخدام فئة PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## تحويل صفحات PDF إلى صيغ صور مختلفة (واجهات)

من أجل تحويل صفحات PDF إلى صيغ صور مختلفة، تحتاج إلى إنشاء كائن [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) وفتح ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، تحتاج إلى استدعاء طريقة [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) لمهام التهيئة. ثم، يمكنك التكرار عبر جميع الصفحات باستخدام طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) و[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). تتيح لك طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) إنشاء صورة لصفحة معينة. تحتاج أيضًا إلى تمرير ImageFormat إلى هذه الطريقة من أجل إنشاء صورة من نوع محدد مثل JPEG، GIF أو PNG وما إلى ذلك. أخيرًا، استدعاء طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) من فئة [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). يوضح لك مقتطف الكود التالي كيفية تحويل صفحات PDF إلى صور.

```csharp
public static void ConvertPdfPagesToImages01()
{
    // Create PdfConverter object
    PdfConverter converter = new PdfConverter();

    // Bind input pdf file
    converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
        converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

    // Close the PdfConverter object
    converter.Close();
}
```
في مقتطف الشيفرة التالي، سنوضح كيف يمكنك تغيير بعض المعلمات. باستخدام [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) نضبط الإطار 'CropBox'. كما يمكننا تغيير [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) بتحديد عدد النقاط في البوصة. التالي هو [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - وضع عرض النموذج. ثم نشير إلى [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) الذي يتم من خلاله تحديد رقم الصفحة لبداية التحويل. يمكننا أيضًا تحديد الصفحة الأخيرة عن طريق تحديد نطاق.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // إنشاء كائن PdfConverter
            PdfConverter converter = new PdfConverter();

            // ربط ملف pdf المدخل
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // تهيئة عملية التحويل
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // تحقق من وجود الصفحات ثم قم بتحويلها إلى صورة واحدة تلو الأخرى
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // إغلاق كائن PdfConverter
            converter.Close();
        }
```

## انظر أيضا

Aspose.PDF for .NET يسمح بتحويل مستندات PDF إلى صيغ مختلفة وأيضًا التحويل من صيغ أخرى إلى PDF. كما يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت باستخدام تطبيق Aspose.PDF converter. تعرف على قسم [التحويل](/pdf/net/converting/) لحل مهامك.