---
title: استخراج الصور باستخدام PdfExtractor
type: docs
weight: 20
url: /net/extract-images/
description: يشرح هذا القسم كيفية استخراج الصور باستخدام Aspose.PDF Facades باستخدام فئة PdfExtractor.
lastmod: "2021-07-15"
---

## استخراج الصور من ملف PDF بالكامل إلى ملفات (واجهات)

تسمح لك فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) باستخراج الصور من ملف PDF. 
أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` بعد ذلك، قم باستدعاء طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طرق [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى استخدام حلقة while للتنقل عبر جميع الصور المستخرجة. من أجل حفظ الصور على القرص، يمكنك استدعاء التحميل الزائد لطريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) التي تأخذ مسار الملف كوسيطة. يظهر لك مقطع الشيفرة التالي كيفية استخراج الصور من ملف PDF بالكامل إلى ملفات.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // فتح ملف PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // استخراج جميع الصور
            pdfExtractor.ExtractImage();

            // الحصول على جميع الصور المستخرجة
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## استخراج الصور من ملف PDF بالكامل إلى تدفقات (واجهات)

فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) تتيح لك استخراج الصور من ملف PDF إلى تدفقات. 
أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` بعد ذلك، قم باستدعاء [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور في الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى تكرار جميع الصور المستخرجة باستخدام حلقة while. من أجل حفظ الصور إلى الذاكرة، يمكنك استدعاء الحمل الزائد لطريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) التي تأخذ Stream كحجة. يوضح لك مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF بالكامل إلى الذاكرات.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // افتح ملف PDF المدخل
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // استخراج الصور
            pdfExtractor.ExtractImage();
            // احصل على جميع الصور المستخرجة
            while (pdfExtractor.HasNextImage())
            {
                // اقرأ الصورة في ذاكرة مؤقتة
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // اكتبها إلى القرص، إذا أردت، أو استخدمها بطريقة أخرى.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## استخراج الصور من صفحة معينة من ملف PDF (واجهات)

يمكنك استخراج الصور من صفحة معينة من ملف PDF. ```
In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) الخصائص إلى الصفحة المحددة التي تريد استخراج الصور منها.
``` 
أولاً وقبل كل شيء، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * و[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) الخصائص. بعد ذلك، قم باستدعاء [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة الطرق [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. يمكنك إما حفظ الصور إلى القرص أو البث. تحتاج فقط إلى استدعاء التحميل المناسب من طريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). يوضح لك مقتطف الشفرة التالي كيفية استخراج الصور من صفحة معينة من PDF إلى تدفقات.

```csharp
public static void ExtractImagesParticularPage()
{
    // افتح ملف PDF المدخل
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // تعيين خصائص StartPage و EndPage إلى رقم الصفحة التي
    // تريد استخراج الصور منها
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // استخراج الصور
    pdfExtractor.ExtractImage();
    // الحصول على الصور المستخرجة
    while (pdfExtractor.HasNextImage())
    {
        // قراءة الصورة في تدفق الذاكرة
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // الكتابة إلى القرص، إذا أحببت، أو استخدامها بطريقة أخرى.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## استخراج الصور من نطاق صفحات ملف PDF (واجهات)

يمكنك استخراج الصور من نطاق صفحات ملف PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) خصائص لتحديد نطاق الصفحات التي تريد استخراج الصور منها. 
أولاً وقبل كل شيء، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) و[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) الخصائص. بعد ذلك، قم باستدعاء [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة الطريقتين [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار عبر جميع الصور المستخرجة باستخدام حلقة while. يمكنك إما حفظ الصور على القرص أو تدفقها. تحتاج فقط إلى استدعاء التحميل المناسب لطريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). يوضح لك المقتطف البرمجي التالي كيفية استخراج الصور من نطاق صفحات PDF إلى تدفقات.

```csharp
public static void ExtractImagesRangePages()
{
    // افتح ملف PDF المدخل
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // تعيين خصائص StartPage و EndPage إلى رقم الصفحة التي
    // تريد استخراج الصور منها
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // استخراج الصور
    pdfExtractor.ExtractImage();
    // الحصول على الصور المستخرجة
    while (pdfExtractor.HasNextImage())
    {
        // قراءة الصورة في تدفق الذاكرة
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // الكتابة إلى القرص، إذا أردت، أو استخدامها بغير ذلك.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## استخراج الصور باستخدام وضع استخراج الصور (الواجهات)

فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) تتيح لك استخراج الصور من ملف PDF. Aspose.PDF يدعم وضعين لاستخراج الصور؛ الأول هو ActuallyUsedImage الذي يستخرج الصور المستخدمة فعلياً في مستند PDF. Second mode is [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) والذي يقوم باستخراج الصور المعرفة في موارد مستند PDF (وهو وضع الاستخراج الافتراضي). First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، حدد وضع استخراج الصورة باستخدام خاصية [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). ثم قم باستدعاء طريقة [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) لاستخراج جميع الصور إلى الذاكرة حسب الوضع الذي حددته. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة الطرق [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) و[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). تحتاج إلى التكرار من خلال جميع الصور المستخرجة باستخدام حلقة while. من أجل حفظ الصور على القرص، يمكنك استدعاء التحميل الزائد لطريقة [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) التي تأخذ مسار الملف كحجة.

يوضح لك مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF باستخدام خيار ExtractImageMode.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // افتح ملف PDF الإدخال
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // حدد وضع استخراج الصور
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // استخراج الصور بناءً على وضع استخراج الصور
    extractor.ExtractImage();

    // احصل على جميع الصور المستخرجة
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

للتحقق مما إذا كان ملف PDF يحتوي على نص أو صور، استخدم مقتطف الشفرة التالي:

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // إنشاء كائن memoryStream لاحتواء النص المستخرج من المستند
            MemoryStream ms = new MemoryStream();
            // إنشاء كائن PdfExtractor
            PdfExtractor extractor = new PdfExtractor();

            // ربط مستند PDF الإدخال إلى المستخرج
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // استخراج النص من مستند PDF الإدخال
            extractor.ExtractText();
            // حفظ النص المستخرج إلى ملف نصي
            extractor.GetText(ms);
            // التحقق مما إذا كان طول MemoryStream أكبر من أو يساوي 1

            bool containsText = ms.Length >= 1;

            // استخراج الصور من مستند PDF الإدخال
            extractor.ExtractImage();

            // استدعاء طريقة HasNextImage في حلقة while. عندما تنتهي الصور، ستخرج الحلقة
            bool containsImage = extractor.HasNextImage();

            // الآن اكتشف ما إذا كان هذا PDF يحتوي فقط على نص أو فقط على صورة

            if (containsText && !containsImage)
                Console.WriteLine("PDF يحتوي فقط على نص");
            else if (!containsText && containsImage)
                Console.WriteLine("PDF يحتوي فقط على صورة");
            else if (containsText && containsImage)
                Console.WriteLine("PDF يحتوي على نص وصورة");
            else if (!containsText && !containsImage)
                Console.WriteLine("PDF لا يحتوي على نص ولا صورة");
        }

    }
```