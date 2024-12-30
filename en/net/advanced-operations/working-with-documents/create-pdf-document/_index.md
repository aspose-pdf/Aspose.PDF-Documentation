---
title: How to Create PDF using C#
linktitle: Create PDF Document
type: docs
weight: 10
url: /net/create-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "The new functionality in Aspose.PDF for .NET empowers developers to effortlessly create and format PDF documents using C#. With this intuitive API, users can generate searchable PDFs, manipulate tagged content for accessibility, and seamlessly integrate PDF generation into various .NET applications, enhancing productivity and streamlining workflows",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Create and format the PDF Document with Aspose.PDF for .NET."
}
</script>

We are always looking for a way to generate PDF documents and work with them in C# projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in .NET.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Create (or Generate) PDF document using C# language

Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.

### How to Create Simple PDF File

To create a PDF file using C#, the following steps can be used.

1. Create an object of [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.
1. Add a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object to the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) collection of the Document object.
1. Add [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) to [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) collection of the page.
1. Save the resultant PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void CreateHelloWorldPdf()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Initialize document object
    using (var document = new Aspose.Pdf.Document())
	{
		// Add page
		var page = document.Pages.Add();

		// Add text to new page
		page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));

		// Save updated PDF
		document.Save(dataDir + "HelloWorld_out.pdf");
	}
}
```

### How to Create a Searchable PDF document

Aspose.PDF for .NET provides the feature to create as well as manipulate existing PDF documents. When adding Text elements inside PDF file, the resultant PDF is searchable. However if we are converting an Image containing text to PDF file, the contents inside PDF are not searchable. However as a workaround, we can use OCR over the resultant file, so that it becomes searchable.

This logic specified below recognizes text for PDF images. For recognition you may use outer OCR supports HOCR standard. For testing purposes, we have used a free Google tesseract OCR. Therefore first you need to install Tesseract-OCR on your system, and you will have tesseract console application.

Following is complete code to accomplish this requirement:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ConvertDocumentWithHocr(string file)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(file))
    {
        bool convertResult = false;
        try
        {
            // Attempt to convert the document with HOCR
            convertResult = document.Convert(CallBackGetHocr);
        }
        catch (Exception ex)
        {
            // Log the exception message
            Console.WriteLine(ex.Message);
        }

        // Save the document
        document.Save(file);
    }
}

static string CallBackGetHocr(System.Drawing.Image img)
{
    string tmpFile = Path.GetTempFileName();
    try
    {
        var bmp = new System.Drawing.Bitmap(img);

        bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        string inputFile = string.Concat('"', tmpFile, '"');
        string outputFile = string.Concat('"', tmpFile, '"');
        string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
            {
                UseShellExecute = true,
                CreateNoWindow = true,
                WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
            };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### How to Create an accessible PDF using low-level functions

This code snippet works with a PDF document and its tagged content, utilizing an Aspose.PDF library to process it.

The example creates a new span element in the tagged content of the first page of a PDF, finds all BDC elements, and associates them with the span. The modified document is then saved.

You can create a bdc statement specifying mcid, lang, and expansion text using the BDCProperties object:

```cs
BDC bdc = new BDC(PdfConsts.P, new BDCProperties(1, "de", "Hallo, welt!"));
```

After creating the structure tree, it is possible to bind the BDC operator to the specified element of the structure with method Tag on the element object:

```cs
SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

Steps to creating an accessible PDF:

1. Load the PDF Document.
1. Access Tagged Content.
1. Create a Span Element.
1. Append Span to Root Element.
1. Iterate Over Page Contents.
1. Check for BDC Elements and Tag Them.
1. Save the Modified Document.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ProcessTaggedContent(string somePdfFilePath, string output)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(somePdfFilePath))
	{
		// Get the tagged content
		var content = document.TaggedContent;

		// Create a SpanElement
		var span = content.CreateSpanElement();

		// Append the span to the root element
		content.RootElement.AppendChild(span);

		// Process operations on the first page
		foreach (var op in document.Pages[1].Contents)
		{
			if (op is Aspose.Pdf.Operators.BDC bdc)
			{
				// Tag the BDC operation
				span.Tag(bdc);
			}
		}

		// Save the document
		document.Save(output);
	}
}
```

This code modifies a PDF by creating a span element within the document's tagged content and tagging specific content (BDC operations) from the first page with this span. The modified PDF is then saved to a new file.

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
