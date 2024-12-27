---
title: Working with Headings in PDF
type: docs
url: /net/working-with-headings/
weight: 70
description: Create numbering in heading your PDF document with C#. Aspose.PDF for .NET offers different kinds of numbering styles.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Headings in PDF",
    "alternativeHeadline": "Enhance PDF Headings with Custom Numbering Styles",
    "abstract": "Enhance your PDF documents with customizable heading numbering using Aspose.PDF for .NET. This new feature allows you to apply various pre-defined numbering styles, such as Roman numerals and alphabetical listings, to organize your headings effectively, improving the document readability and structure. Streamline your PDF creation process by integrating this versatile functionality into your C# applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF, C#, headings in PDF, numbering style, Aspose.PDF for .NET, pre-defined numbering styles, NumberingStyle enumeration, document generation, Heading class, pdf document manipulation",
    "wordcount": "453",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-25",
    "description": "Create numbering in heading your PDF document with C#. Aspose.PDF for .NET offers different kinds of numbering styles."
}
</script>


## Apply Numbering Style in Heading

Headings are the important parts of any document. Writers always try to make headings more prominent and meaningful to its readers. If there are more than one headings in a document, a writer has several options to organize these headings. One of the most common approach to organize headings is to write headings in Numbering Style.

[Aspose.PDF for .NET](/pdf/net/) offers many pre-defined numbering styles. These pre-defined numbering styles are stored in an enumeration, NumberingStyle. The pre-defined values of NumberingStyle enumeration and their descriptions are given below:

|**Heading Types**|**Description**|
| :- | :- |
|NumeralsArabic|Arab type,for example, 1,1.1,...|
|NumeralsRomanUppercase|Roman upper type, for example, I,I.II, ...|
|NumeralsRomanLowercase|Roman lower type, for example, i,i.ii, ...|
|LettersUppercase|English upper type, for example, A,A.B, ...|
|LettersLowercase|English lower type, for example, a,a.b, ...|
The **Style** property of **Aspose.Pdf.Heading** class is used to set the numbering styles of the headings.

|**Figure: Pre-defined numbering styles**|
| :- |
The source code, to obtain the output shown in the above figure, is given below in the example.

The next code snippet also works with [Aspose.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ApplyNumberStyleToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create a new PDF document
    using(var document = new Aspose.Pdf.Document())
	{
		document.PageInfo.Width = 612.0;
		document.PageInfo.Height = 792.0;
		document.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
		document.PageInfo.Margin.Left = 72;
		document.PageInfo.Margin.Right = 72;
		document.PageInfo.Margin.Top = 72;
		document.PageInfo.Margin.Bottom = 72;

		// Add a new page to the document
		var pdfPage = document.Pages.Add();
		pdfPage.PageInfo.Width = 612.0;
		pdfPage.PageInfo.Height = 792.0;
		pdfPage.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
		pdfPage.PageInfo.Margin.Left = 72;
		pdfPage.PageInfo.Margin.Right = 72;
		pdfPage.PageInfo.Margin.Top = 72;
		pdfPage.PageInfo.Margin.Bottom = 72;

		// Create a floating box with the same margin as the page
		var floatBox = new Aspose.Pdf.FloatingBox();
		floatBox.Margin = pdfPage.PageInfo.Margin;

		// Add the floating box to the page
		pdfPage.Paragraphs.Add(floatBox);

		// Add headings with numbering styles
		var heading = new Aspose.Pdf.Heading(1);
		heading.IsInList = true;
		heading.StartNumber = 1;
		heading.Text = "List 1";
		heading.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
		heading.IsAutoSequence = true;
		floatBox.Paragraphs.Add(heading);

		var heading2 = new Aspose.Pdf.Heading(1);
		heading2.IsInList = true;
		heading2.StartNumber = 13;
		heading2.Text = "List 2";
		heading2.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
		heading2.IsAutoSequence = true;
		floatBox.Paragraphs.Add(heading2);

		var heading3 = new Aspose.Pdf.Heading(2);
		heading3.IsInList = true;
		heading3.StartNumber = 1;
		heading3.Text = "the value, as of the effective date of the plan, of property to be distributed under the plan on account of each allowed";
		heading3.Style = Aspose.Pdf.NumberingStyle.LettersLowercase;
		heading3.IsAutoSequence = true;
		floatBox.Paragraphs.Add(heading3);

		// Save the document with the applied number style
		document.Save(dataDir + "ApplyNumberStyle_out.pdf");
	}
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
