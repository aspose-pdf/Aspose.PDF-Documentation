---
title: تحسين أو ضغط أو تقليل حجم ملف PDF في C#
linktitle: تحسين PDF
type: docs
weight: 30
url: /ar/net/optimize-pdf/
description: تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إزالة التضمين للخطوط، إزالة العناصر غير المستخدمة باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تحسين PDF باستخدام C#",
    "alternativeHeadline": "كيفية تحسين PDF باستخدام .NET",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثائق PDF",
    "keywords": "pdf, c#, تحسين pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق توثيق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إزالة التضمين للخطوط، إزالة العناصر غير المستخدمة باستخدام C#."
}
</script>
قد يحتوي مستند PDF أحيانًا على بيانات إضافية. تقليل حجم ملف PDF سيساعدك على تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب، المشاركة على شبكات التواصل الاجتماعي، الإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام عدة تقنيات لتحسين PDF:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إلغاء تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة تسطيح حقول النماذج
- إزالة أو تسطيح التعليقات التوضيحية

{{% alert color="primary" %}}

 يمكن العثور على شرح مفصل لطرق التحسين في صفحة نظرة عامة على طرق التحسين.

{{% /alert %}}

## تحسين مستند PDF للويب

التحسين، أو التخطيط المباشر للويب، يشير إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح ويب. لتحسين ملف لعرض الويب:

1. افتح المستند الأصلي في كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1. احفظ المستند المُحسّن باستخدام طريقة [الحفظ](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

الشفرة التالية توضح كيفية تحسين مستند PDF للويب.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// تحسين للويب
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// حفظ المستند الناتج
pdfDocument.Save(dataDir);
```

## تقليل حجم PDF

طريقة [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) تتيح لك تقليل حجم المستند بإزالة المعلومات غير الضرورية.
[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) تسمح لك بتقليل حجم المستند عن طريق إزالة المعلومات غير الضرورية.

- يتم إزالة الموارد التي لا تُستخدم في صفحات المستند
- يتم دمج الموارد المتماثلة في كائن واحد
- يتم حذف الكائنات غير المستخدمة

الشفرة أدناه هي مثال. لاحظ، على الرغم من ذلك، أن هذه الطريقة لا يمكن أن تضمن تقليص حجم المستند.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح مستند
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// تحسين مستند PDF. لاحظ، على الرغم من ذلك، أن هذه الطريقة لا يمكن أن تضمن تقليص حجم المستند
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

## إدارة استراتيجية التحسين

يمكننا أيضًا تخصيص استراتيجية التحسين.
يمكننا أيضًا تخصيص استراتيجية التحسين.

### تقليص أو ضغط جميع الصور

لدينا طريقتان للتعامل مع الصور: تقليل جودة الصورة و/أو تغيير دقتها. في كلتا الحالتين، يجب تطبيق [خيارات ضغط الصور](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions). في المثال التالي، نقوم بتصغير الصور عن طريق خفض [جودة الصورة](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) إلى 50.

`جودة الصورة` تعمل بطريقة مشابهة لجودة JPEG، حيث أن القيمة 0 هي الأدنى والقيمة 100 هي الأعلى.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// فتح المستند
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// تهيئة خيارات التحسين
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// تعيين خيار ضغط الصور
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// تعيين خيار جودة الصورة
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// تحسين مستند PDF باستخدام خيارات التحسين
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

طريقة أخرى هي تغيير حجم الصور بدقة أقل. في هذه الحالة، يجب تعيين ResizeImages إلى true وMaxResolution إلى القيمة المناسبة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// تهيئة الوقت
var time = DateTime.Now.Ticks;
// مسار إلى مجلد الوثائق
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// فتح المستند
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// تهيئة خيارات التحسين
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// تعيين خيار CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// تعيين خيار ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// تعيين خيار ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// تعيين خيار MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// تحسين مستند PDF باستخدام OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```
مسألة مهمة أخرى هي وقت التنفيذ. لكن مرة أخرى، يمكننا إدارة هذا الإعداد أيضًا. حاليًا، يمكننا استخدام خوارزميتين - القياسية والسريعة. للتحكم في وقت التنفيذ يجب علينا تعيين خاصية [الإصدار](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). يوضح الجزء التالي خوارزمية السريع:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// تهيئة الوقت
var time = DateTime.Now.Ticks;
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// فتح المستند
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// تهيئة خيارات التحسين
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// تعيين خيار ضغط الصور
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// تعيين خيار جودة الصورة
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// تعيين إصدار ضغط الصورة إلى سريع
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// تحسين مستند PDF باستخدام خيارات التحسين
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
Console.WriteLine("العلامات: {0}", DateTime.Now.Ticks - time);
```
### إزالة الكائنات غير المستخدمة

قد يحتوي مستند PDF أحيانًا على كائنات PDF التي لا يشير إليها أي كائن آخر في المستند. قد يحدث هذا، على سبيل المثال، عندما يتم إزالة صفحة من شجرة صفحات المستند ولكن لا يتم إزالة كائن الصفحة نفسه. إزالة هذه الكائنات لا تجعل المستند غير صالح ولكنها تقلل من حجمه.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح المستند
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// تعيين خيار RemoveUsedObject
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// تحسين مستند PDF باستخدام OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

### إزالة التدفقات غير المستخدمة

أحيانًا يحتوي المستند على تدفقات موارد غير مستخدمة.
أحيانًا يحتوي المستند على تدفقات موارد غير مستخدمة.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح المستند
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// تعيين خيار إزالة التدفقات غير المستخدمة
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// تحسين مستند PDF باستخدام OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

### ربط تدفقات الموارد المكررة

قد يحتوي بعض المستندات على عدة تدفقات موارد متطابقة (مثل الصور، على سبيل المثال).
بعض الوثائق قد تحتوي على عدة تدفقات موارد متطابقة (مثل الصور، على سبيل المثال).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح الوثيقة
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// تعيين خيار LinkDuplcateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// تحسين وثيقة PDF باستخدام OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// حفظ الوثيقة المحدثة
pdfDocument.Save(dataDir);
```

بالإضافة إلى ذلك، يمكننا استخدام إعدادات [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
بالإضافة إلى ذلك، يمكننا استخدام إعدادات [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح المستند
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// تعيين خيار AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("البدء");
// تحسين مستند PDF باستخدام OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// حفظ المستند المحدث
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("الانتهاء");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("حجم الملف الأصلي: {0}. حجم الملف المخفض: {1}", fi1.Length, fi2.Length);
```
### إزالة تضمين الخطوط

إذا كان المستند يستخدم خطوطًا مضمنة، فهذا يعني أن جميع بيانات الخط مخزنة في المستند. الفائدة هي أن المستند يمكن مشاهدته بغض النظر عن ما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. لكن تضمين الخطوط يجعل المستند أكبر حجمًا. تقوم طريقة إزالة تضمين الخطوط بإزالة جميع الخطوط المضمنة. وبذلك، يقل حجم المستند لكن المستند ذاته قد يصبح غير قابل للقراءة إذا لم يكن الخط الصحيح مثبتًا.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح المستند
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// تعيين خيار UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Start");
// تحسين مستند PDF باستخدام OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// حفظ المستند المحدث
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finished");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
```
## طرق إضافية لتقليل حجم مستند PDF

### إزالة أو تسطيح التعليقات التوضيحية

يمكن حذف التعليقات التوضيحية عندما لا تكون ضرورية. عندما تكون ضرورية ولا تتطلب تحريرًا إضافيًا، يمكن تسطيحها. كلا هذه الأساليب سيقلل من حجم الملف.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// فتح المستند
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// تسطيح التعليقات التوضيحية
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// حفظ المستند المحدث
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### إزالة حقول النموذج

إذا احتوى مستند PDF على AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسطيح حقول النموذج.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// تحميل نموذج PDF المصدر
Document doc = new Document(dataDir + "input.pdf");

// تسطيح النماذج
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// حفظ المستند المحدث
doc.Save(dataDir);
```

### تحويل PDF من فضاء الألوان RGB إلى الرمادي

يتكون ملف PDF من نص، صورة، مرفق، تعليقات، رسوم بيانية، وغيرها من الكائنات.
ملف PDF يتضمن نصوص، صور، مرفقات، تعليقات، رسومات، وغيرها من العناصر.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// تحميل ملف PDF المصدر
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // الحصول على نسخة من صفحة معينة داخل PDF
        Page page = document.Pages[idxPage];
        // تحويل صور مساحة الألوان RGB إلى مساحة ألوان الرمادي
        strategy.Convert(page);
    }
    // حفظ الملف الناتج
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### ضغط FlateDecode

{{% alert color="primary" %}}

هذه الميزة مدعومة بواسطة الإصدار 18.12 أو أعلى.

{{% /alert %}}

يوفر Aspose.PDF لـ .NET دعم ضغط FlateDecode لوظائف تحسين PDF.
Aspose.PDF لـ .NET يدعم ضغط FlateDecode لوظيفة تحسين PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **تخزين الصورة في XImageCollection**

Aspose.PDF لـ .NET يوفر القدرة على تخزين صور جديدة في **XImageCollection** مع ضغط FlateDecode. لتفعيل هذا الخيار يمكنك استخدام علم **ImageFilterType.Flate**. يوضح الجزء التالي من الكود كيفية استخدام هذه الوظيفة:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

