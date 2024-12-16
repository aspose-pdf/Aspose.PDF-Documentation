---
title: إضافة ختم نص وصورة
type: docs
weight: 20
url: /ar/net/add-text-and-image-stamp/
description: يشرح هذا القسم كيفية إضافة ختم نص وصورة باستخدام Aspose.PDF Facades باستخدام فئة PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## إضافة ختم نص على جميع الصفحات في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) بإضافة ختم نص على جميع صفحات ملف PDF. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

من أجل إضافة ختم نصي، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). 
أنت أيضًا بحاجة إلى إنشاء ختم النص باستخدام طريقة [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك ضبط سمات أخرى مثل الأصل، الدوران، الخلفية إلخ باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، قم بحفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يُظهر لك مقطع الكود التالي كيفية إضافة ختم نص على جميع الصفحات في ملف PDF.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
```
## إضافة ختم نصي على صفحات معينة في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) بإضافة ختم نصي على صفحات معينة من ملف PDF. 
من أجل إضافة ختم نصي، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).
``` You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  
تحتاج أيضًا إلى إنشاء ختم النص باستخدام طريقة [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) لفئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك تعيين سمات أخرى مثل الأصل، الدوران، الخلفية، إلخ. 
باستخدام [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) كائن أيضًا.
``` كما تريد إضافة ختم نصي على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) لفئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تتطلب هذه الخاصية مصفوفة أعداد صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يُظهر لك مقتطف الشيفرة التالي كيفية إضافة ختم نصي على صفحات معينة في ملف PDF.

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء الختم
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // تعيين الصفحات المعينة
            stamp.Pages = new int[] { 2 };

            // إضافة الختم إلى ملف PDF
            fileStamp.AddStamp(stamp);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```
## إضافة ختم صورة على جميع صفحات ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) بإضافة ختم صورة على جميع صفحات ملف PDF. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

من أجل إضافة ختم صورة، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء ختم الصورة باستخدام [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) طريقة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) فئة. يمكنك تعيين سمات أخرى مثل الأصل، الدوران، الخلفية إلخ. باستخدام [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) كائن أيضًا. ثم يمكنك إضافة الختم في ملف PDF باستخدام [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) طريقة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) فئة. وأخيرًا، احفظ ملف PDF الناتج باستخدام [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) طريقة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) فئة. يوضح لك مقتطف الشيفرة التالي كيفية إضافة ختم صورة على جميع الصفحات في ملف PDF.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء الختم
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // تعيين صفحات معينة
            stamp.Pages = new int[] { 2 };

            // إضافة الختم إلى ملف PDF
            fileStamp.AddStamp(stamp);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```
### التحكم في جودة الصورة عند إضافتها كختم

عند إضافة صورة ككائن ختم، يمكنك أيضًا التحكم في جودة الصورة. لتحقيق هذا المتطلب، تمت إضافة خاصية الجودة لفئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). وتشير إلى جودة الصورة بالنسبة المئوية (القيم الصالحة هي 0..100).

## إضافة ختم صورة على صفحات معينة في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) بإضافة ختم صورة على صفحات معينة من ملف PDF. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

من أجل إضافة ختم صورة، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  
تحتاج أيضًا إلى إنشاء ختم الصورة باستخدام [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) طريقة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) فئة. You can set other attributes like origin, rotation, background etc.  
يمكنك تعيين سمات أخرى مثل الأصل، والدوران، والخلفية، إلخ. باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. كما تريد إضافة ختم صورة على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) لفئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تتطلب هذه الخاصية مصفوفة أعداد صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح لك مقتطف الشيفرة التالي كيفية إضافة ختم صورة على صفحات معينة في ملف PDF.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```