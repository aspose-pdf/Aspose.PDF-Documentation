---
title: PdfFileMend Class
type: docs
weight: 20
url: /java/pdffilemend-class/
description: يشرح هذا القسم كيفية العمل مع Aspose.PDF Facades باستخدام فئة PdfFileMend.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

قد يبدو أن إدراج [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) في مستند PDF ليس مهمة صعبة، بشرط أن يكون لديك النسخة الأصلية القابلة للتحرير من هذا المستند. لنفترض أنك أنشأت مستندًا، ثم تذكرت أنك بحاجة إلى إضافة سطر آخر أو نتحدث عن حجم أكبر من المستندات، في كلتا الحالتين سيساعدك Aspose.PDF Facades. لننظر في إمكانية إضافة نص في ملف PDF موجود باستخدام فئة [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend).

## إضافة نص في ملف PDF موجود (facades)

يمكننا إضافة النص بطرق عدة.
 اعتبر الأول. نأخذ [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) ونضيفه إلى الصفحة. بعد ذلك، نحدد إحداثيات الزاوية السفلية اليسرى، ثم نضيف نصنا إلى الصفحة.

```java
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

![إضافة نص](/pdf/net/images/add_text.png)

الطريقة الثانية لإضافة [FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext). بالإضافة إلى ذلك، نحدد مستطيل يجب أن يناسب نصنا داخله.

```java
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

المثال الثالث يوفر القدرة على إضافة نص إلى صفحات محددة. في مثالنا، دعونا نضيف تعليقاً توضيحياً على الصفحات 1 و 3 من المستند.

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("مرحبًا بكم في Aspose!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // احفظ ملف الإخراج
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## إضافة صورة في ملف PDF موجود (الواجهات)

هل سبق لك أن حاولت إضافة صورة إلى ملف PDF موجود؟
 نحن متأكدون أنك تعلم أن هذه ليست مهمة سهلة. ربما تقوم بملء نموذج عبر الإنترنت وتحتاج إلى إرفاق صورة للتعريف أو إرفاق صورتك بسيرة ذاتية موجودة. في السابق، كانت تُحل هذه المهمة عن طريق إنشاء صورة، إرفاقها بوثيقة، ثم مسحها ضوئيًا وإرسالها. كانت هذه العملية تستغرق الكثير من الوقت وتُسبب الكثير من المتاعب.

إضافة الصور والنصوص في ملف PDF موجود هو مطلب شائع وnamespace com.aspose.pdf.facades يلبي هذا المطلب بشكل جيد جدًا. إنه يوفر فئة [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) والتي تتيح لك إضافة الصور في ملف PDF.

تُظهر لك هذه المقالة كيفية إدراج صورة في PDF باستخدام com.aspose.pdf.facades. هناك أيضًا عدة خيارات لإضافة الصور إلى PDF.

إدراج صورة في وثيقة PDF عن طريق تعيين معايير المستطيل.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // تحميل الصورة في التدفق
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // حفظ الملف الناتج
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![إضافة صورة](/pdf/net/images/add_image1.png)

لننظر في الشيفرة الثانية. باستخدام تغييرات في معلمات فئة [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters)، يمكننا الحصول على تأثيرات تصميم مختلفة. لقد جربنا واحدة منها.

```java
 public static void AddImage02()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // تحميل الصورة في التدفق
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // حفظ الملف الناتج
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![إضافة صورة](/pdf/net/images/add_image2.png)

في مقتطف الشيفرة التالي نستخدم [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType). يشير ImageFilterType إلى نوع ترميز الدفق الذي سيتم استخدامه للترميز، افتراضيًا Jpeg. إذا قمت بتحميل صورة بتنسيق PNG، فسيتم حفظها في المستند كـ JPEG (أو بتنسيق آخر قمت بتحديده).

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // تحميل الصورة في الدفق
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // حفظ الملف الناتج
        mender.Save(_dataDir + "PdfFileMend06_output.pdf");
    }
```


في مقتطف الشيفرة التالي يمكنك ملاحظة استخدام الطريقة [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--).

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) هو علم يشير إلى ما إذا كان يجب تطبيق قناع على الصورة لتحقيق شفافية الصورة الأصلية

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // تحميل الصورة في الدفق
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // حفظ ملف الإخراج
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```