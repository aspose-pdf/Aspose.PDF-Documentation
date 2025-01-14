---
title: Working with Operators
linktitle: Working with Operators
type: docs
weight: 90
url: /net/working-with-operators/
description: This topic explains how to use operators with Aspose.PDF. The operator classes provide great features for PDF manipulation.
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
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "The Operators feature in Aspose.PDF for .NET enhances PDF manipulation capabilities by allowing users to utilize specific operator classes for tasks such as adding images and removing graphics. This functionality simplifies the process of defining graphical elements and their states within a PDF, providing developers with powerful tools for fine-tuned document editing and processing",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "This topic explains how to use operators with Aspose.PDF. The operator classes provide great features for PDF manipulation."
}
</script>

## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Implementation details

This topic explains how to use operators with Aspose.PDF. The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/28), [ConcatenateMatrix](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/10), [Do](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/14), and [GRestore](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/26).

- The **GSave** operator saves the PDF's current graphical state.
- The **ConcatenateMatrix** (concatenate matrix) operator is used to define how an image should be placed on the PDF page.
- The **Do** operator draws the image on the page.
- The **GRestore** operator restores the graphical state.

To add an image into a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object and open the input PDF document.
1. Get the particular page the image is going to be added to.
1. Add the image into the page's Resources collection.
1. Use the operators to place the image on the page:
   - First, use the GSave operator to save the current graphical state.
   - Then use the ConcatenateMatrix operator to specify where the image is to be placed.
   - Use the Do operator to draw the image on the page.
1. Finally, use GRestore operator to save the updated graphical state.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following code snippet shows how to use PDF operators.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new System.IO.FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## Draw XForm on Page using Operators

This topic demonstrates how to use the GSave/GRestore operators, the ContatenateMatrix operator to position an xForm and the Do operator to draw an xForm on a page.

The code below wraps a PDF file's existing contents with the GSave/GRestore operator pair. This approach helps get the initial graphics state at the and of the existing contents. Without this approach, undesirable transformations might remain at the end of the existing operator chain.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## Remove Graphics Objects using Operator Classes

The operator classes provide great features for PDF manipulation. When a PDF file contains graphics that cannot be removed using the [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class’ [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) method, the operator classes can be used to remove them instead.

The following code snippet shows how to remove graphics. Please note that if the PDF file contains text labels for the graphics, they might persist in the PDF file, using this approach. Therefore search the graphic operators for an alternate method to delete such images.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
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
