---
title: العمل مع العوامل
linktitle: العمل مع العوامل
type: docs
weight: 170
url: /ar/net/operators/
description: يشرح هذا الموضوع كيفية استخدام العوامل مع Aspose.PDF. توفر فئات العوامل ميزات رائعة للتلاعب بملفات PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع العوامل",
    "alternativeHeadline": "كيفية استخدام عوامل PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثائق PDF",
    "keywords": "pdf, c#, العوامل في pdf, استخدام عوامل pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا الموضوع كيفية استخدام العوامل مع Aspose.PDF. توفر فئات العوامل ميزات رائعة للتلاعب بملفات PDF."
}
</script>
## مقدمة في مشغلات PDF واستخداماتها

المشغل هو كلمة أساسية في PDF تحدد نوع الإجراء الذي يجب تنفيذه، مثل رسم شكل رسومي على الصفحة. تتميز كلمة المشغل الأساسية عن الكائن المسمى بعدم وجود حرف سلاش صلب أولي (2Fh). المشغلات ذات معنى فقط داخل تيار المحتوى.

تيار المحتوى هو كائن تيار PDF الذي تتكون بياناته من تعليمات تصف العناصر الرسومية التي سيتم رسمها على صفحة. يمكن العثور على المزيد من التفاصيل حول مشغلات PDF في [مواصفات PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### تفاصيل التنفيذ

يشرح هذا الموضوع كيفية استخدام المشغلات مع Aspose.PDF.

هذا الموضوع يشرح كيفية استخدام العوامل مع Aspose.PDF.

- يقوم العامل **GSave** بحفظ الحالة الرسومية الحالية لملف PDF.
- يُستخدم العامل **ConcatenateMatrix** (مصفوفة الدمج) لتحديد كيفية وضع الصورة على صفحة PDF.
- يقوم العامل **Do** برسم الصورة على الصفحة.
- يعيد العامل **GRestore** الحالة الرسومية.

لإضافة صورة إلى ملف PDF:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وفتح مستند PDF الذي تم إدخاله.
1. الحصول على الصفحة المعينة التي ستضاف إليها الصورة.
1. إضافة الصورة إلى مجموعة موارد الصفحة.
1. استخدام العوامل لوضع الصورة على الصفحة:
   - أولاً، استخدام عامل GSave لحفظ الحالة الرسومية الحالية.
   - ثم استخدام عامل ConcatenateMatrix لتحديد مكان وضع الصورة.
   - استخدام عامل Do لرسم الصورة على الصفحة.
1. أخيرًا، استخدام عامل GRestore لحفظ الحالة الرسومية المحدثة.

هذه القطعة البرمجية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).
```
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

الشفرة التالية تظهر كيفية استخدام عوامل تشغيل PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// فتح الوثيقة
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// تحديد الإحداثيات
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// الحصول على الصفحة التي يجب إضافة الصورة إليها
Page page = pdfDocument.Pages[1];
// تحميل الصورة في تيار
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// إضافة الصورة إلى مجموعة الصور في موارد الصفحة
page.Resources.Images.Add(imageStream);
// استخدام عامل التشغيل GSave: يحفظ هذا العامل حالة الرسومات الحالية
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// إنشاء مستطيل وكائنات مصفوفة
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// استخدام عامل ConcatenateMatrix (دمج المصفوفة): يحدد كيف يجب وضع الصورة
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// استخدام عامل العمل Do: يرسم هذا العامل الصورة
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// استخدام عامل GRestore: يستعيد هذا العامل حالة الرسومات
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// حفظ الوثيقة المحدثة
pdfDocument.Save(dataDir);
```
## رسم XForm على الصفحة باستخدام العوامل

هذا الموضوع يوضح كيفية استخدام عوامل GSave/GRestore وعامل ContatenateMatrix لوضع xForm وعامل Do لرسم xForm على صفحة.

الكود أدناه يلف محتويات ملف PDF الحالية بزوج العوامل GSave/GRestore. هذه الطريقة تساعد في الحصول على الحالة الرسومية الأولية في نهاية المحتويات الحالية. بدون هذه الطريقة، قد تبقى تحولات غير مرغوب فيها في نهاية سلسلة العوامل الحالية.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // العينة توضح
    // استخدام عوامل GSave/GRestore
    // استخدام عامل ContatenateMatrix لتحديد موقع xForm
    // استخدام عامل Do لرسم xForm على الصفحة

    // لف المحتويات الحالية بزوج العوامل GSave/GRestore
    //        هذا للحصول على الحالة الرسومية الأولية في نهاية المحتويات الحالية
    //        وإلا قد تبقى بعض التحولات غير المرغوب فيها في نهاية سلسلة العوامل الحالية
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // إضافة عامل حفظ الحالة الرسومية لتنظيف الحالة الرسومية بشكل صحيح بعد الأوامر الجديدة
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region إنشاء xForm

    // إنشاء xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // تحديد عرض الصورة وارتفاعها
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // تحميل الصورة في تيار
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // إضافة الصورة إلى مجموعة الصور في موارد XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // استخدام عامل Do: هذا العامل يرسم الصورة
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // وضع النموذج على الإحداثيات x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // رسم النموذج باستخدام عامل Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // وضع النموذج على الإحداثيات x=100 y=300
    pageContents Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // رسم النموذج باستخدام عامل Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // استعادة الحالة الرسومية بعد GSave باستخدام GRestore
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## إزالة الكائنات الرسومية باستخدام فئات المشغل

توفر فئات المشغل ميزات رائعة للتلاعب بملفات PDF. عندما يحتوي ملف PDF على رسومات لا يمكن إزالتها باستخدام طريقة [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) للفئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)، يمكن استخدام فئات المشغل لإزالتها بدلاً من ذلك.

يوضح الجزء التالي من الشفرة كيفية إزالة الرسومات. يرجى ملاحظة أنه إذا كان ملف PDF يحتوي على تسميات نصية للرسومات، فقد تظل مستمرة في ملف PDF، باستخدام هذه الطريقة. لذا ابحث عن مشغلات الرسومات لطريقة بديلة لحذف مثل هذه الصور.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir + "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// المشغلات المستخدمة في طلاء المسار
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir + "No_Graphics_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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
```

