---
title: العمل مع العناوين في PDF
type: docs
weight: 40
url: ar/python-net/working-with-headings/
description: إنشاء ترقيم في عنوان مستند PDF الخاص بك باستخدام Python. يوفر Aspose.PDF for Python عبر .NET أنواعًا مختلفة من أنماط الترقيم.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع العناوين في PDF",
    "alternativeHeadline": "إنشاء عناوين في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, العناوين في pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
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
    "description": "إنشاء ترقيم في عنوان مستند PDF الخاص بك باستخدام Python. يوفر Aspose.PDF for Python عبر .NET أنواعًا مختلفة من أنماط الترقيم."
}
</script>


## تطبيق نمط الترقيم في العناوين

العناوين هي الأجزاء المهمة في أي مستند. يحاول الكتاب دائمًا جعل العناوين أكثر بروزًا وذات مغزى لقرائهم. إذا كان هناك أكثر من عنوان واحد في مستند، فلدى الكاتب عدة خيارات لتنظيم هذه العناوين. واحدة من أكثر الطرق شيوعًا لتنظيم العناوين هي كتابة العناوين بنمط الترقيم.

يوفر [Aspose.PDF for Python عبر .NET](/pdf/python-net/) العديد من أنماط الترقيم المعرفة مسبقًا. يتم تخزين هذه الأنماط المعرفة مسبقًا في تعداد، [NumberingStyle](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/). القيم المعرفة مسبقًا لتعداد NumberingStyle ووصفها موضحة أدناه:

|**أنواع العناوين**|**الوصف**|
| :- | :- |
|NumeralsArabic|نوع عربي، على سبيل المثال، 1,1.1,...|
|NumeralsRomanUppercase|نوع روماني كبير، على سبيل المثال، I,I.II, ...|
|NumeralsRomanLowercase|نوع روماني صغير، على سبيل المثال، i,i.ii, ...|
|LettersUppercase|نوع إنجليزي كبير، على سبيل المثال، A,A.B, ...|

|LettersLowercase|نوع إنجليزي صغير، على سبيل المثال، a,a.b, ...|
The [style](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/#properties) الخاص بفئة [Heading](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/) يُستخدم لتعيين أنماط الترقيم للعناوين.

|**الشكل: أنماط الترقيم المعرفة مسبقًا**|
| :- |
يتم تقديم الشيفرة المصدرية للحصول على المخرجات الموضحة في الشكل أعلاه في المثال أدناه.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.page_info.width = 612.0
    document.page_info.height = 792.0
    document.page_info.margin = ap.MarginInfo()
    document.page_info.margin.left = 72
    document.page_info.margin.right = 72
    document.page_info.margin.top = 72
    document.page_info.margin.bottom = 72

    page = document.pages.add()
    page.page_info.width = 612.0
    page.page_info.height = 792.0
    page.page_info.margin = ap.MarginInfo()
    page.page_info.margin.left = 72
    page.page_info.margin.right = 72
    page.page_info.margin.top = 72
    page.page_info.margin.bottom = 72

    float_box = ap.FloatingBox()
    float_box.margin = page.page_info.margin

    page.paragraphs.add(float_box)

    heading = ap.Heading(1)
    heading.is_in_list = True
    heading.start_number = 1
    heading.text = "القائمة 1"
    heading.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading.is_auto_sequence = True

    float_box.paragraphs.add(heading)

    heading2 = ap.Heading(1)
    heading2.is_in_list = True
    heading2.start_number = 13
    heading2.text = "القائمة 2"
    heading2.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading2.is_auto_sequence = True

    float_box.paragraphs.add(heading2)

    heading3 = ap.Heading(2)
    heading3.is_in_list = True
    heading3.start_number = 1
    heading3.text = "القيمة، اعتبارًا من تاريخ سريان الخطة، للممتلكات التي سيتم توزيعها بموجب الخطة لحساب كل مسموح"
    heading3.style = ap.NumberingStyle.LETTERS_LOWERCASE
    heading3.is_auto_sequence = True

    float_box.paragraphs.add(heading3)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لمكتبة .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ Python عبر .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>