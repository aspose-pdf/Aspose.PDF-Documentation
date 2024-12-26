---
title: Compare PDF documents
linktitle: Compare PDF 
type: docs
weight: 130
url: /net/compare-pdf-documents/
description: Since 24.7 release it's possible to compare PDF documents content with annotation marks and side-by-side output
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "The new PDF comparison feature in Aspose.PDF for .NET allows users to efficiently identify differences between two PDF documents, either by specific pages or the entire content. With side-by-side outputs and customizable options such as additional change markers and various comparison modes, this powerful tool enhances collaboration by making revisions easy to track and review",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1180",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Please note that all comparing tools are available in [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/) library.

## Ways to compare PDF Documents

When working with PDF documents, there are times when you need to compare the content of two documents to identify differences. The Aspose.PDF for .NET library provides a powerful toolset for this purpose. In this article, we'll explore how to compare PDF documents using a couple of simple code snippets.

The comparison functionality in Aspose.PDF allows you to compare two PDF documents page by page. You can choose to compare either specific pages or entire documents. The resulting comparison document highlights differences, making it easier to identify changes between the two files.

Here is a list of possible ways to compare PDF documents using Aspose.PDF for  .NET library:

1. **Comparing Specific Pages** - Compare the first pages of two PDF documents.

1. **Comparing Entire Documents** - Compare the entire content of two PDF documents.

1. **Compare PDF documents graphically**:

- Compare PDF with GetDifference method - individual images where changes are marked.

- Compare PDF with CompareDocumentsToPdf method - PDF document with images where changes are marked.

## Comparing Specific Pages

The first code snippet demonstrates how to compare the first pages of two PDF documents.

Steps:

1. Document Initialization.
The code starts by initializing two PDF documents using their respective file paths (documentPath1 and documentPath2). The paths are specified as empty strings for now, but in practice, you would replace these with the actual file paths.

2. Comparison Process.

- Page Selection - the comparison is limited to the first page of each document ('Pages[1]').
- Comparison Options:

'AdditionalChangeMarks = true'- this option ensures that additional change markers are displayed. These markers highlight differences that might be present on other pages, even if they are not on the current page being compared.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - this mode tells the comparer to ignore spaces in the text, focusing only on changes within words.

3. The resulting comparison document, which highlights the differences between the two pages, is saved to the file path specified in 'resultPdfPath'.

```cs
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    var documentPath1 = dataDir + "ComparingSpecificPages1.pdf";
    var documentPath2 = dataDir + "ComparingSpecificPages2.pdf";
    var resultPdfPath = dataDir + "ComparingSpecificPages_out.pdf";

    // Open documents
    using (var document1 = new Aspose.Pdf.Document(documentPath1))
    {
        using (var document2 = new Aspose.Pdf.Document(documentPath2))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## Comparing Entire Documents

The second code snippet expands the scope to compare the entire content of two PDF documents.

Steps:

1. Document Initialization.
Just like in the first example, two PDF documents are initialized with their file paths.

2. Comparison Process.

- Entire Document Comparison - unlike the first snippet, this code compares the entire content of the two documents.

- Comparison Options - the options are the same as in the first snippet, ensuring that spaces are ignored, and additional change markers are displayed.

3. The comparison result, which highlights differences across all pages of the two documents, is saved in the file specified by 'resultPdfPath'.

```cs
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    var documentPath1 = dataDir + "ComparingEntireDocuments1.pdf";
    var documentPath2 = dataDir + "ComparingEntireDocuments2.pdf";
    var resultPdfPath = dataDir + "ComparingEntireDocuments_out.pdf";

    // Open documents
    using (var document1 = new Aspose.Pdf.Document(documentPath1))
    {
        using (var document2 = new Aspose.Pdf.Document(documentPath2))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                resultPdfPath,
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

The comparison results generated by these snippets are PDF documents that you can open in a viewer like Adobe Acrobat. If you use the Two-page view in Adobe Acrobat, you'll see the changes side by side:

- Deletions - these are noted on the left page.
- Insertions - these are noted on the right page.

By setting 'AdditionalChangeMarks' to 'true', you can also see markers for changes that may occur on other pages, even if those changes aren't on the current page being viewed.

**Aspose.PDF for .NET** provides robust tools for comparing PDF documents, whether you need to compare specific pages or entire documents. By using options like 'AdditionalChangeMarks' and different 'ComparisonMode settings', you can tailor the comparison process to your specific needs. The resulting document provides a clear, side-by-side view of changes, making it easier to track revisions and ensure document accuracy.

## Compare PDF documents using GraphicalPdfComparer

When collaborating on documents, especially in professional environments, you often end up with multiple versions of the same file.

You can use the [GraphicalPdfComparer](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) class to compare PDF documents and pages. The class is suitable for comparing changes in a page's graphic content.

With Aspose.PDF for .NET, it's possible to compare documents and pages and output the comparison result to a PDF document or image file.

You can set the following class properties:

- Resolution - resolution in DPI units for output images, as well as for images generated during the comparison.
- Color - the color of change marks.
- Threshold - change threshold in percent. The default value is zero. Setting a value other than zero allows you to ignore graphic changes that are insignificant to you.

The class has a method that allows you to get page image differences in a form suitable for further processing: **ImagesDifference GetDifference(Page page1, Page page2)**.

This method returns an object of the [ImagesDifference](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) class, which contains an image of the first page being compared and an array of differences. The array of differences and the original image has the **RGB24bpp** pixel format.

ImagesDifference allows you to generate a different image and get an image of the second page being compared by adding an array of differences to the original image. To do this, use the **ImagesDifference.GetDestinationImage and ImagesDifference.DifferenceToImage** methods.

### Compare PDF with GetDifference method

The provided code defines a method [GetDifference](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) that compares two PDF documents and generates visual representations of the differences between them.

This method compares the first pages of two PDF files and generates two PNG images:

- One image (diffPngFilePath) highlights the differences between the pages in red.
- The other image (destPngFilePath) is a visual representation of the destination (second) PDF page.

This process can be useful for visually comparing changes or differences between two versions of a document.

```cs
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    var doc1Path = dataDir + "ComparePDFWithGetDifferenceMethod1.pdf";
    var doc2Path = dataDir + "ComparePDFWithGetDifferenceMethod2.pdf";
    string destPngFilePath = dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png";
    string diffPngFilePath = dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png";

    // Open documents
    using (var document1 = new Aspose.Pdf.Document(doc1Path))
    {
        using (var document2 = new Aspose.Pdf.Document(doc2Path))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(diffPngFilePath);
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(destPngFilePath);
                }
            }
        }
    }
}
```

### Compare PDF with CompareDocumentsToPdf method

The provided code snippet used the  [CompareDocumentsToPdf](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) method, which compares two documents and generates a PDF report of the comparison results.

```cs
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    var document1Path = dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf";
    var document2Path = dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf";

    string resultPdfPath = dataDir + "compareDocumentsToPdf_out.pdf";

    // Open documents
    using (var document1 = new Aspose.Pdf.Document(document1Path))
    {
        using (var document2 = new Aspose.Pdf.Document(document2Path))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, resultPdfPath);
        }
    }
}
```