---
title: العمل مع العناوين في ملفات PDF
type: docs
url: /net/working-with-headings/
description: إنشاء ترقيم في عناوين مستند PDF الخاص بك باستخدام C#. يقدم Aspose.PDF لـ .NET أنواعًا مختلفة من أنماط الترقيم.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع العناوين في ملفات PDF",
    "alternativeHeadline": "إنشاء عناوين في ملفات PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, c#, العناوين في ملفات pdf",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2022-02-04",
    "description": "إنشاء ترقيم في عناوين مستند PDF الخاص بك باستخدام C#. يقدم Aspose.PDF لـ .NET أنواعًا مختلفة من أنماط الترقيم."
}
</script>
## تطبيق نمط الترقيم في العناوين

العناوين هي الأجزاء المهمة من أي مستند. يحاول الكتاب دائماً جعل العناوين أكثر بروزاً ومعنى لقرائهم. إذا كان هناك أكثر من عنوان في مستند، يمتلك الكاتب العديد من الخيارات لتنظيم هذه العناوين. أحد الأساليب الشائعة لتنظيم العناوين هو كتابتها بنمط الترقيم.

[Aspose.PDF for .NET](/pdf/net/) يقدم العديد من أنماط الترقيم المعرفة مسبقاً. تُخزن هذه الأنماط المعرفة مسبقاً في تعداد، NumberingStyle. القيم المعرفة مسبقاً لتعداد NumberingStyle ووصفها موضحة أدناه:

|**أنواع العناوين**|**الوصف**|
| :- | :- |
|NumeralsArabic|النوع العربي، على سبيل المثال، 1,1.1,...|
|NumeralsRomanUppercase|النوع الروماني العلوي، على سبيل المثال، I,I.II, ...|
|NumeralsRomanLowercase|النوع الروماني السفلي، على سبيل المثال، i,i.ii, ...|
|LettersUppercase|النوع الإنجليزي العلوي، على سبيل المثال، A,A.B, ...|
|LettersLowercase|النوع الإنجليزي السفلي، على سبيل المثال، a,a.b, ...|
تُستخدم خاصية **Style** لفئة **Aspose.PDF.Heading** لتعيين أنماط الترقيم للعناوين.
**خاصية** **الأنماط** في فئة **Aspose.PDF.Heading** تُستخدم لتحديد أنماط الترقيم للعناوين.

|**الشكل: أنماط الترقيم المُعرّفة مسبقًا**|
| :- |
الكود المصدري للحصول على النتيجة المعروضة في الشكل أعلاه موضح أدناه في المثال.

الشفرة التالية تعمل أيضًا مع واجهة رسومية جديدة [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Headings();

Document pdfDoc = new Document();
pdfDoc.PageInfo.Width = 612.0;
pdfDoc.PageInfo.Height = 792.0;
pdfDoc.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
pdfDoc.PageInfo.Margin.Left = 72;
pdfDoc.PageInfo.Margin.Right = 72;
pdfDoc.PageInfo.Margin.Top = 72;
pdfDoc.PageInfo.Margin.Bottom = 72;

Aspose.Pdf.Page pdfPage = pdfDoc.Pages.Add();
pdfPage.PageInfo.Width = 612.0;
pdfPage.PageInfo.Height = 792.0;
pdfPage.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
pdfPage.PageInfo.Margin.Left = 72;
pdfPage.PageInfo.Margin.Right = 72;
pdfPage.PageInfo.Margin.Top = 72;
pdfPage.PageInfo.Margin.Bottom = 72;

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox();
floatBox.Margin = pdfPage.PageInfo.Margin;

pdfPage.Paragraphs.Add(floatBox);

TextFragment textFragment = new TextFragment();
TextSegment segment = new TextSegment();

Aspose.Pdf.Heading heading = new Aspose.Pdf.Heading(1);
heading.IsInList = true;
heading.StartNumber = 1;
heading.Text = "List 1";
heading.Style = NumberingStyle.NumeralsRomanLowercase;
heading.IsAutoSequence = true;

floatBox.Paragraphs.Add(heading);

Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
heading2.IsInList = true;
heading2.StartNumber = 13;
heading2.Text = "List 2";
heading2.Style = NumberingStyle.NumeralsRomanLowercase;
heading2.IsAutoSequence = true;

floatBox.Paragraphs.Add(heading2);

Aspose.Pdf.Heading heading3 = new Aspose.Pdf.Heading(2);
heading3.IsInList = true;
heading3.StartNumber = 1;
heading3.Text = "القيمة، كما في تاريخ سريان الخطة، للممتلكات التي سيتم توزيعها بموجب الخطة بسبب كل موافقة";
heading3.Style = NumberingStyle.LettersLowercase;
heading3.IsAutoSequence = true;

floatBox.Paragraphs.Add(heading3);
dataDir = dataDir + "ApplyNumberStyle_out.pdf";
pdfDoc.Save(dataDir);
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
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
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

