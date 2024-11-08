---
title: إدارة الرأس والتذييل
type: docs
weight: 40
url: /ar/net/manage-header-and-footer/
description: يوضح هذا القسم كيفية إدارة الرأس والتذييل باستخدام واجهات Aspose.PDF باستخدام فئة PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## إضافة رأس في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) بإضافة رأس في ملف PDF. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.  
من أجل إضافة رأس، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تنسيق نص العنوان باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). بمجرد أن تكون جاهزًا لإضافة العنوان في الملف، تحتاج إلى استدعاء طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). تحتاج أيضًا إلى تحديد الهامش العلوي على الأقل في طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). يوضح لك مقطع الشيفرة التالي كيفية إضافة عنوان في ملف PDF.

```csharp
 public static void AddHeader()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء نص منسق لرقم الصفحة
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // إضافة العنوان
            fileStamp.AddHeader(formattedText, 10);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```
## إضافة تذييل في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) بإضافة تذييل في ملف PDF. 
من أجل إضافة التذييل، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main).
``` يمكنك تنسيق نص التذييل باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). بمجرد أن تكون جاهزًا لإضافة تذييل في الملف، تحتاج إلى استدعاء طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). تحتاج أيضًا إلى تحديد الهامش السفلي على الأقل في طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يوضح لك مقتطف الشيفرة التالي كيفية إضافة تذييل في ملف PDF.

```csharp
 public static void AddFooter()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء نص منسق لرقم الصفحة
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // إضافة تذييل
            fileStamp.AddFooter(formattedText, 10);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```
## إضافة صورة في رأس ملف PDF موجود

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) بإضافة صورة في رأس ملف PDF. 
من أجل إضافة صورة في الرأس، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). بعد ذلك، تحتاج إلى استدعاء طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تمرير الصورة إلى طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يظهر لك مقطع الشيفرة التالي كيفية إضافة صورة في رأس ملف PDF.

```csharp
public static void AddImageHeader()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // إضافة الرأس
                fileStamp.AddHeader(fs, 10);

                // حفظ ملف PDF المحدث
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // إغلاق fileStamp
                fileStamp.Close();
            }
        }
```
```
## إضافة صورة في تذييل ملف PDF موجود

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) بإضافة صورة في تذييل ملف PDF. من أجل إضافة صورة في التذييل، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). بعد ذلك، تحتاج إلى استدعاء طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تمرير الصورة إلى طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يوضح لك مقتطف الشيفرة التالي كيفية إضافة صورة في تذييل ملف PDF.

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```