```
---
title: إضافة الصور والنصوص
type: docs
weight: 10
url: ar/net/adding-images-and-text-using-pdffilemend-class/
description: يشرح هذا القسم كيفية إضافة الصور والنصوص باستخدام فئة PdfFileMend.
lastmod: "2021-06-05"
draft: false
---

يمكن لفئة [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) مساعدتك في إضافة الصور والنصوص في مستند PDF موجود، في موقع محدد.
``` 
إنه يوفر طريقتين بأسماء [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) و[AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index).
``` 
[AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) تتيح لك إضافة صور من نوع JPG، GIF، PNG، وBMP. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) تأخذ وسيطًا من نوع [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) وتضيفه في ملف PDF الحالي. يمكن إضافة الصور والنصوص في منطقة مستطيلة محددة بإحداثيات النقاط السفلية اليسرى والعلوية اليمنى. عند إضافة الصور يمكنك تحديد إما مسار ملف الصورة أو دفق لملف الصورة. من أجل تحديد رقم الصفحة التي يجب إضافة الصورة أو النص عليها، توفر كلا الطريقتين وسيطًا لرقم الصفحة. لذلك، يمكنك ليس فقط إضافة الصور والنصوص في الموقع المحدد بل أيضًا في صفحة معينة.

الصور جزء مهم من محتويات مستند PDF.
``` 
التلاعب بالصور في ملف PDF موجود هو مطلب شائع للأشخاص الذين يعملون مع ملفات PDF. في هذه المقالة، سنستكشف كيفية التلاعب بالصور في ملف PDF موجود بمساعدة [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) لـ [Aspose.PDF for .NET](/pdf/net/). تم دمج جميع العمليات المتعلقة بالصور لـ [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في هذه المقالة.

## تفاصيل التنفيذ

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) يسمح لك بإضافة صور جديدة في ملف PDF موجود.
``` يمكنك أيضًا استبدال أو إزالة صورة موجودة. يمكن أيضًا تحويل ملف PDF إلى صور. يمكنك إما تحويل كل صفحة فردية إلى صورة واحدة أو تحويل ملف PDF كامل إلى صورة واحدة. يتيح لك التنسيق بصيغ مثل JPEG، BMP، PNG وTIFF إلخ. يمكنك أيضًا استخراج الصور من ملف PDF. يمكنك استخدام أربع فئات من [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) لتنفيذ هذه العمليات مثل [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)، [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)، [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) و [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## عمليات الصورة

في هذا القسم، سنلقي نظرة مفصلة على هذه العمليات الخاصة بالصور. نحن سنرى أيضًا أجزاء الكود لإظهار استخدام الفئات والأساليب ذات الصلة. أولاً، دعونا نلقي نظرة على إضافة صورة في ملف PDF موجود. يمكننا استخدام طريقة [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) من فئة [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) لإضافة صورة جديدة. باستخدام هذه الطريقة، يمكنك ليس فقط تحديد رقم الصفحة التي تريد إضافة الصورة عليها، ولكن أيضًا يمكن تحديد موقع الصورة.

## إضافة صورة في ملف PDF موجود (Facades)

يمكنك استخدام طريقة [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) من فئة [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). The [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) يتطلب الأسلوب إضافة الصورة، رقم الصفحة التي تحتاج إلى إضافة الصورة فيها، ومعلومات الإحداثيات. بعد ذلك، احفظ ملف PDF المحدث باستخدام أسلوب [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

في المثال التالي، نضيف صورة إلى الصفحة باستخدام imageStream:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image1.png)

بمساعدة [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)، يمكننا تركيب صورة واحدة فوق أخرى:
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // تحميل الصورة في دفق
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // حفظ ملف الإخراج
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![إضافة صورة](/pdf/net/images/add_image2.png)

هناك عدة طرق لتخزين صورة في ملف PDF. سنوضح واحدة منها في المثال التالي:

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // تحميل الصورة في دفق
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // حفظ ملف الإخراج
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## إضافة نص إلى ملف PDF موجود (واجهات)

يمكننا إضافة نص بعدة طرق. النظر في الأول. نحن نأخذ [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) ونضيفه إلى الصفحة. بعد ذلك، نحدد إحداثيات الزاوية السفلى اليسرى، ثم نضيف النص الخاص بنا إلى الصفحة.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // حفظ ملف الإخراج
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

تحقق كيف يبدو:

![Add Text](/pdf/net/images/add_text.png)

الطريقة الثانية لإضافة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). بالإضافة إلى ذلك، نشير إلى مستطيل يجب أن يتناسب النص الخاص بنا داخله.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // حفظ ملف الإخراج
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
المثال الثالث يوفر القدرة على إضافة نص إلى صفحات محددة. في مثالنا، دعونا نضيف تعليقًا على الصفحات 1 و 3 من المستند.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```