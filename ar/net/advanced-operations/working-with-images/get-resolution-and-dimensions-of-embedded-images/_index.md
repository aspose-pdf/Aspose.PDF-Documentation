---
title: الحصول على الدقة والأبعاد للصور
linktitle: الحصول على الدقة والأبعاد
type: docs
weight: 40
url: /ar/net/get-resolution-and-dimensions-of-embedded-images/
description: هذا القسم يظهر التفاصيل في الحصول على الدقة والأبعاد للصور المضمنة
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "الحصول على الدقة والأبعاد للصور",
    "alternativeHeadline": "كيفية الحصول على الدقة والأبعاد للصور المضمنة",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, الحصول على الدقة, الحصول على الأبعاد",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "هذا القسم يظهر التفاصيل في الحصول على الدقة والأبعاد للصور المضمنة"
}
</script>
يعمل الجزء التالي من الشيفرة أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

يشرح هذا الموضوع كيفية استخدام فئات العمليات في فضاء الأسماء Aspose.PDF والتي توفر القدرة على الحصول على معلومات الدقة والأبعاد عن الصور دون الحاجة إلى استخراجها.

هناك طرق مختلفة لتحقيق ذلك. يشرح هذا المقال كيفية استخدام `arraylist` و[فئات تحديد مكان الصورة](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. أولاً، قم بتحميل ملف PDF المصدر (الذي يحتوي على الصور).
1. ثم قم بإنشاء كائن ArrayList لحفظ أسماء أي صور في الوثيقة.
1. احصل على الصور باستخدام خاصية Page.Resources.Images.
1. قم بإنشاء كائن stack لحفظ حالة الرسومات للصورة واستخدمه لتتبع حالات الصورة المختلفة.
1.
1. بما أننا نستطيع تعديل المصفوفة باستخدام ConcatenateMatrix، قد نحتاج أيضًا إلى العودة إلى حالة الصورة الأصلية. استخدم العوامل GSave و GRestore. يتم إقران هذه العوامل معًا، لذا يجب استدعاؤهما معًا. على سبيل المثال، إذا قمت ببعض الأعمال الرسومية مع تحويلات معقدة وأخيرًا تعيد التحويلات إلى الحالة الأولية، سيكون النهج كما يلي:

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

نتيجة لذلك، يتم رسم النص بشكل عادي ولكن تتم بعض التحويلات بين عوامل النص. من أجل عرض الصورة أو لرسم الأشكال والصور، نحتاج إلى استخدام العامل Do.

لدينا أيضًا صف يسمى XImage يوفر خاصيتين، العرض والارتفاع، والتي يمكن استخدامها للحصول على أبعاد الصورة.

1.
1.
1. عرض المعلومات في نافذة الأوامر بالإضافة إلى اسم الصورة.

الشفرة التالية توضح كيفية الحصول على أبعاد الصورة ودقتها دون استخراج الصورة من مستند PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// تحميل ملف PDF المصدر
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// تحديد دقة الصورة الافتراضية
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// تحديد كائن قائمة الصفائف الذي سيحتفظ بأسماء الصور
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// إدراج كائن إلى الكومة
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// الحصول على جميع المشغلين في الصفحة الأولى من المستند
foreach (Operator op in doc.Pages[1].Contents)
{
    // استخدام مشغلي GSave/GRestore لإعادة التحويلات إلى الحالة التي تم تعيينها سابقًا
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // إنشاء كائن ConcatenateMatrix حيث يحدد مصفوفة التحويل الحالية.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // إنشاء مشغل Do الذي يرسم الأشياء من الموارد. يرسم أشياء النموذج وأشياء الصورة
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // حفظ الحالة السابقة ودفع الحالة الحالية إلى أعلى الكومة
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // التخلص من الحالة الحالية واستعادة الحالة السابقة
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // ضرب المصفوفة الحالية بمصفوفة الحالة
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // في حالة كون هذا مشغل رسم الصورة
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // إنشاء كائن XImage لحفظ صور الصفحة الأولى من PDF
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // الحصول على أبعاد الصورة
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // الحصول على معلومات الارتفاع والعرض للصورة
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // حساب الدقة بناءً على المعلومات السابقة
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // عرض معلومات البعد والدقة لكل صورة
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
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

