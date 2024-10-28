---
title: استخراج المحتوى الموسوم من PDF
linktitle: استخراج المحتوى الموسوم
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: يشرح هذا المقال كيفية استخراج المحتوى الموسوم من مستند PDF باستخدام Aspose.PDF لـ .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استخراج المحتوى الموسوم من PDF",
    "alternativeHeadline": "كيفية وسم الصورة في PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "وسم, pdf, استخراج",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية استخراج المحتوى الموسوم من مستند PDF باستخدام Aspose.PDF لـ .NET"
}
</script>
في هذه المقالة ستتعلم كيفية استخراج المحتوى الموسوم من مستند PDF باستخدام C#.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## الحصول على محتوى PDF الموسوم

من أجل الحصول على محتوى مستند PDF مع النص الموسوم، يقدم Aspose.PDF خاصية [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

يوضح الشفرة التالية كيفية الحصول على محتوى مستند PDF مع النص الموسوم:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

//
// العمل مع محتوى Pdf الموسوم
//

// تحديد العنوان واللغة للمستند
taggedContent.SetTitle("مستند Pdf الموسوم البسيط");
taggedContent.SetLanguage("en-US");

// حفظ مستند Pdf الموسوم
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## الحصول على البنية الجذرية

للحصول على البنية الجذرية لمستند PDF الموسوم، يقدم Aspose.PDF خاصية [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) لواجهة [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) و [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). يوضح الجزء التالي من الكود كيفية الحصول على البنية الجذرية لمستند PDF الموسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// تعيين العنوان واللغة للمستند
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// الخصائص StructTreeRootElement و RootElement تستخدم للوصول إلى
// كائن StructTreeRoot لمستند pdf وإلى عنصر البنية الجذرية (عنصر بنية المستند).
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## الوصول إلى العناصر الفرعية

للوصول إلى العناصر الفرعية لمستند PDF الموسوم، تقدم Aspose.PDF فئة [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist). يوضح الشفرة التالية كيفية الوصول إلى العناصر الفرعية لمستند PDF موسوم:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح مستند Pdf
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// الوصول إلى العنصر الجذر
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // الحصول على الخصائص
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// الوصول إلى العناصر الفرعية للعنصر الأول في العنصر الجذر
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // تعيين الخصائص
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// حفظ مستند PDF الموسوم
document.Save(dataDir + "AccessChildElements.pdf");
```
## وسم الصور في مستند PDF موجود

لوسم الصور في مستند PDF موجود، تقدم Aspose.PDF طريقة [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) من فئة [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). يمكنك إضافة نص بديل للأشكال باستخدام خاصية [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) من فئة [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement).

يوضح الشفرة التالية كيفية وسم الصور في مستند PDF موجود:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// فتح المستند
Document document = new Document(inFile);

// يحصل على المحتوى الموسوم وعنصر الهيكل الجذري
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// تعيين عنوان لمستند PDF الموسوم
taggedContent.SetTitle("مستند بالصور");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // تعيين نص بديل للشكل
    figureElement.AlternativeText = "نص بديل للشكل (تقنية 2)";


    // إنشاء وتعيين خاصية BBox
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// نقل عنصر Span إلى فقرة (العثور على span وفقرة خاطئة في أول TD)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// نقل عنصر Span إلى الفقرة
spanElement.ChangeParentElement(paragraph);


// حفظ المستند
document.Save(outFile);



// التحقق من الامتثال PDF/UA للمستند الناتج
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("الامتثال لـ PDF/UA: {0}", isPdfUaCompliance));
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

