---
title: تعليقات PDF اللاصقة باستخدام C#
linktitle: تعليق لاصق
type: docs
weight: 50
url: /ar/net/sticky-annotations/
description: هذا الموضوع عن التعليقات اللاصقة، كمثال نعرض التعليق التوضيحي للعلامة المائية في النص.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعليقات PDF اللاصقة باستخدام C#",
    "alternativeHeadline": "كيفية إضافة تعليقات لاصقة في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, التعليقات اللاصقة, التعليق التوضيحي للعلامة المائية",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "هذا الموضوع عن التعليقات اللاصقة، كمثال نعرض التعليق التوضيحي للعلامة المائية في النص."
}
</script>

الكود التالي يعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة تعليق توضيحي للعلامة المائية

يجب استخدام التعليق التوضيحي للعلامة المائية لتمثيل الرسومات التي يجب طباعتها بحجم وموقع ثابتين على الصفحة، بغض النظر عن أبعاد الصفحة المطبوعة.

يمكنك إضافة نص العلامة المائية باستخدام [WatermarkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) في موقع محدد من صفحة PDF. يمكن أيضًا التحكم في شفافية العلامة المائية باستخدام خاصية الشفافية.

يرجى التحقق من الكود التالي لإضافة WatermarkAnnotation.

```csharp
 //تحميل وثيقة
Aspose.PDF.Document doc = new Aspose.PDF.Document("source.pdf");

//تحميل كائن الصفحة لإضافة التعليق التوضيحي
Page page = doc.Pages[1];

//إنشاء التعليق التوضيحي
WatermarkAnnotation wa = new WatermarkAnnotation(page, new Aspose.PDF.Rectangle(100, 500, 400, 600));

//إضافة التعليق التوضيحي إلى مجموعة التعليقات التوضيحية للصفحة
page.Annotations.Add(wa);

//إنشاء حالة نص لإعدادات الخط
Aspose.PDF.Text.TextState ts = new Aspose.PDF.Text.TextState();

ts.ForegroundColor = Aspose.PDF.Color.Blue;
ts.Font = FontRepository.FindFont("Times New Roman");

ts.FontSize = 32;

//تعيين مستوى شفافية نص التعليق التوضيحي

wa.Opacity = 0.5;
//إضافة نص في التعليق التوضيحي

wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

//حفظ الوثيقة
doc.Save("Output.pdf");
```
## إضافة مرجع لصورة واحدة عدة مرات في مستند PDF

أحياناً نحتاج إلى استخدام نفس الصورة عدة مرات في مستند PDF. إضافة نسخة جديدة تزيد من حجم المستند النهائي. لقد أضفنا طريقة جديدة XImageCollection.Add(XImage) في Aspose.PDF لـ .NET 17.1.0. تتيح هذه الطريقة إضافة مرجع إلى نفس كائن PDF كما في الصورة الأصلية مما يعمل على تحسين حجم مستند PDF.

```csharp
 Aspose.PDF.Rectangle imageRectangle = new Aspose.PDF.Rectangle(0, 0, 30, 15);

using (Aspose.PDF.Document document = new Aspose.PDF.Document("input.pdf"))
{
    using (var imageStream = File.Open("icon.png", FileMode.Open))
    {
        XImage image = null;
        foreach (Page page in document.Pages)
        {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.Rect);
            XForm form = annotation.Appearance["N"];
            form.BBox = page.Rect;
            string name;
            if (image == null)
            {
                name = form.Resources.Images.Add(imageStream);
                image = form.Resources.Images[name];
            }
            else
            {
                name = form.Resources.Images.Add(image);
            }
            form.Contents.Add(new Operator.GSave());
            form.Contents.Add(new Operator.ConcatenateMatrix(new Aspose.PDF.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
            form.Contents.Add(new Operator.Do(name));
            form.Contents.Add(new Operator.GRestore());
            page.Annotations.Add(annotation, false);
            imageRectangle = new Aspose.PDF.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
        }
    }
    document.Save("output.pdf");
}
```

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

