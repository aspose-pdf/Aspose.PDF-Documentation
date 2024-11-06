---
title: إضافة ختم صفحة PDF
type: docs
weight: 10
url: ar/net/add-pdf-page-stamp/
description: يشرح هذا القسم كيفية العمل مع واجهات Aspose.PDF باستخدام فئة PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## إضافة ختم صفحة PDF على جميع الصفحات في ملف PDF

فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) تسمح لك بإضافة ختم صفحة PDF على جميع صفحات ملف PDF. في سبيل إضافة ختم صفحة PDF، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تحتاج أيضًا إلى إنشاء ختم صفحة PDF باستخدام طريقة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). يمكنك تعيين سمات أخرى مثل الأصل، الدوران، الخلفية وغيرها باستخدام كائن [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) أيضًا. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). وأخيرًا، حفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح لك المقتطف التالي من الشيفرة كيفية إضافة ختم صفحة PDF على جميع الصفحات في ملف PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء الختم
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // إضافة الختم إلى ملف PDF
            fileStamp.AddStamp(stamp);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // إغلاق الملف
            fileStamp.Close();
        }
```
## إضافة ختم صفحة PDF على صفحات معينة في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) بإضافة ختم صفحة PDF على صفحات معينة من ملف PDF. في البداية لإضافة ختم صفحة PDF، تحتاج أولاً إلى إنشاء كائنات من [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the PDF page stamp using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  
أنت أيضًا بحاجة إلى إنشاء ختم صفحة PDF باستخدام [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) طريقة من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). ```
يمكنك تعيين سمات أخرى مثل الأصل، التدوير، الخلفية إلخ.
``` استخدام [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) الكائن أيضًا. As you want to add PDF page stamp on particular pages of the PDF file, you also need to set the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add PDF page stamp on particular pages in a PDF file.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }

        // Add PDF Page Numbers
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

كما تريد إضافة ختم صفحة PDF على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) من فئة [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). تتطلب هذه الخاصية مصفوفة عددية تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. يمكنك بعد ذلك إضافة الختم في ملف PDF باستخدام طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يظهر لك المقتطف البرمجي التالي كيفية إضافة ختم صفحة PDF على صفحات معينة في ملف PDF.
## إضافة رقم الصفحة في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) بإضافة أرقام الصفحات في ملف PDF. In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class.  
   
من أجل إضافة أرقام الصفحات، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

إذا كنت تريد عرض رقم الصفحة مثل "الصفحة X من N" حيث X هو رقم الصفحة الحالية و N هو العدد الإجمالي للصفحات في ملف PDF، فأنت بحاجة أولاً إلى الحصول على عدد الصفحات باستخدام خاصية [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) في فئة [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). من أجل الحصول على رقم الصفحة الحالي يمكنك استخدام علامة **#** في نصك في أي مكان ترغب فيه. يمكنك تنسيق نص رقم الصفحة باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). إذا كنت تريد بدء ترقيم الصفحات من رقم معين يمكنك تعيين خاصية [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). بمجرد أن تكون جاهزًا لإضافة رقم الصفحة في الملف، تحتاج إلى استدعاء طريقة [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). يوضح لك مقتطف الشيفرة البرمجية التالي كيفية إضافة رقم الصفحة في ملف PDF.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // الحصول على العدد الإجمالي للصفحات
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // إنشاء نص منسق لرقم الصفحة
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // تعيين الرقم الابتدائي للصفحة الأولى؛ قد ترغب في البدء من 2 أو أكثر
            fileStamp.StartingNumber = 1;

            // إضافة رقم الصفحة
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```
### أسلوب ترقيم مخصص

تقدم فئة PdfFileStamp ميزة إضافة معلومات رقم الصفحة ككائن ختم داخل مستند PDF. قبل هذا الإصدار، كانت الفئة تدعم فقط 1،2،3،4 كأسلوب ترقيم الصفحات. ومع ذلك، كان هناك طلب من بعض العملاء لاستخدام أسلوب ترقيم مخصص عند وضع ختم رقم الصفحة داخل مستند PDF. لتحقيق هذا الطلب، تم تقديم خاصية [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle)، والتي تقبل القيم من تعداد [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). موضحة أدناه هي القيم التي تقدم في هذا التعداد.

- أحرف صغيرة
- أحرف كبيرة
- أرقام عربية
- أرقام رومانية صغيرة
- أرقام رومانية كبيرة

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // الحصول على العدد الإجمالي للصفحات
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // إنشاء نص منسق لرقم الصفحة
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // تحديد أسلوب الترقيم كأرقام رومانية كبيرة
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // تعيين الرقم الابتدائي للصفحة الأولى؛ قد ترغب في البدء من 2 أو أكثر
            fileStamp.StartingNumber = 1;

            // إضافة رقم الصفحة
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```