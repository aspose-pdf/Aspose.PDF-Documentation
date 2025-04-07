---
title: What's new
linktitle: What's new
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /net/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for .NET that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-01-31"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats new",
    "alternativeHeadline": "Discover the latest enhancements in Aspose.PDF for .NET",
    "abstract": "Discover the latest enhancements in Aspose.PDF for .NET, including the introduction of the Elliptic Curve Digital Signature Algorithm (ECDSA) for robust document signing and verification, along with support for multiple elliptic curves. Additionally, the new feature allows for image cropping upon insertion into PDFs and the generation of crash reports for improved error handling. These updates streamline PDF management and bolster security in document workflows",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "8022",
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
    "url": "/net/whatsnew/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whatsnew/"
    },
    "dateModified": "2024-12-04",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## What's new in Aspose.PDF 25.2

**Most significant changes**

In the Aspose.PDF 25.2 we have added:
* support [PDF to PDF/X-4](https://docs.aspose.com/pdf/net/convert-pdf-to-pdfx/) standard conversion.
* [an option](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-a-pdf-with-hash-signing-function) to avoid twice call of the CustomSignHash delegate during signing.
* new `GetSignatureNames()` method to get information about [digital signatures](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-pdf-with-digital-signatures) of PDF.
* possibility of creating a [TextBoxField](https://docs.aspose.com/pdf/net/create-form/#adding-radiobuttonfield) with several widget annotations.
> [!NOTE]
> Detailed information about the changes and samples of using can be found on the [Aspose.PDF 25.2 Release Notes](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-2-release-notes/) page.

**Other notable enhancements**

* Image compression without quality loss on [PDF optimization](https://docs.aspose.com/pdf/net/optimize-pdf/#shrinking-or-compressing-all-images) enhanced. Compressed document size reduced.
* The Document [Repair](https://reference.aspose.com/pdf/net/aspose.pdf/document/repair/) method improved. It can check and fix values in the Annotation.Rect array from now.
* System.Text.Json dependency version updated to avoid possible vulnerability CVE-2024-43485.
* PDF signature attack detection improved to prevent obtaining false positive results.
* A public API for redacting resources dictionary provided:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingNewExtGState()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Graphics state parameter dictionary new name
    var gsName = "GS0";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var page = doc.Pages[1];
        var dictionaryEditor = new DictionaryEditor(page.Resources);
        var states = dictionaryEditor["ExtGState"].ToCosPdfDictionary();

        var newGs = CosPdfDictionary.CreateEmptyDictionary(doc);
        var pairs = new KeyValuePair<string, ICosPdfPrimitive>[3]
        {
            new KeyValuePair<string, ICosPdfPrimitive>("CA", new CosPdfNumber(1)),
            new KeyValuePair<string, ICosPdfPrimitive>("ca", new CosPdfNumber(0.5)),
            new KeyValuePair<string, ICosPdfPrimitive>("BM", new CosPdfName("Normal"))
        };

        foreach (var p in pairs)
        {
            newGs.Add(p);
        }
        states.Add(gsName, newGs);

        // Save PDF document
        doc.Save(outputPath);
    }
}
```

## What's new in Aspose.PDF 25.1

In the Aspose.PDF 25.1 we have added:
* an option to save PDF to HTML with skipping all raster images.
* possibility to validate a PDF signature using a Certificate Authority (CA) Server.
* cross-platform PDF signature validation using SHA-3 hashing algorithms.

Detailed information about the changes and samples of using can be found on the [Aspose.PDF 25.1 Release Notes](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-1-release-notes/) page.


## What's new in Aspose.PDF 24.12

The ability to pass the path to the external ICC profile for PDF/X and PDF/A conversion has already existed in the library for some years, enabled by the PdfFormatConversionOptions.IccProfileFileName property. Now it's also possible to pass data to fill OutputIntent properties using an object of the OutputIntent class.

The following snippet shows how to convert annotation document to PDF/X-1 using annotation FOGRA39 ICC profile:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfx1UsingCustomIccProfile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create conversion options to convert the document to PDF/X-1a with the given ICC profile
        var options = new PdfFormatConversionOptions(PdfFormat.PDF_X_1A, ConvertErrorAction.Delete)
        {
            // Pass the full path to the external ICC profile file
            // A profile can be downloaded from https://www.color.org/registry/Coated_Fogra39L_VIGC_300.xalter
            IccProfileFileName = "Coated_Fogra39L_VIGC_300.icc",

            // Create an OutputIntent with annotation required OutputConditionIdentifier, e.g. FOGRA39
            // If necessary, an OutputCondition and annotation RegistryName may be provided as well
            OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39")
        };

        // During the conversion process, the validation is also performed
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "outputPdfx.pdf");
    }
}
```

An analyzer has been added to find the most suitable font for document generation, conversion, and text replacement. Search of most suitable font is performed in the case source PDF contains not enough font information to accomplish requested operation. "Most suitable" font is detemined between fonts installed in the environment based on the information about PDF font and also requested text language and character set.

The following sample show how this can be used in PDF to PNG conversion to avoid text gets turned into blank squares.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToPngWithAnalyzingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.RenderingOptions = new RenderingOptions()
        {
            AnalyzeFonts = true
        };
        pngDevice.Process(document.Pages[1], dataDir + "converted.png");
    }
}
```

Starting from Aspose.PDF 24.12 auto-adjustment the font size can be applied to adding text stamp into annotation PDF file.

The following code snippet demonstrates how to add annotation text stamp to annotation PDF file and automatically adjust the font size to fit the stamp rectangle.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```

The following code snippet demonstrates how to add annotation text stamp to annotation PDF file and automatically adjust the font size to fit the page size.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
    }
}
```


## What's new in Aspose.PDF 24.11

A `PageCollection` extension method has been added to update the page number and date header/footer artifacts when adding or inserting new pages. Settings for the page number and date format should be stored in the original document according to the PDF specification, as implemented by Adobe Acrobat.

The following code snippet demonstrates how to update pagination in the document:
```csharp
private static void UpdatePagination()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document that contains at least one page with pagination artifacts
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithPaginationArtifacts.pdf"))
    {
        // Update pages
        document.Pages.Insert(1, document.Pages[2]);
        document.Pages.Add();

        // Update pagination artifacts
        document.Pages.UpdatePagination();

        // Save PDF document
        document.Save(dataDir + "DocumentWithUpdatedPagination.pdf");
    }
}
```

Since version 24.11, we have added the ability to choose a hashing algorithm for Pkcs7Detached. The default is SHA-256. For ECDSA digital signatures, the default digest algorithm depends on the key length.

ECDSA supports SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, and SHA3-512. The SHA3-256, SHA3-384, and SHA3-512 algorithms are supported only for .NET 8 and newer versions. For details on supported platforms for SHA-3, refer to the [documentation](https://learn.microsoft.com/en-us/dotnet/standard/security/cross-platform-cryptography#sha-3).

RSA supports SHA-1, SHA-256, SHA-384, and SHA-512.

DSA supports only SHA-1. Please note that SHA-1 is outdated and does not meet current security standards.

The following code snippet demonstrates setting of hashing algorithm for Pkcs7Detached:
```csharp
private static void SignWithManualDigestHashAlgorithm(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass, Aspose.Pdf.DigestHashAlgorithm.Sha512);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

A new `FontEncodingStrategy` property has been added to the `HtmlSaveOptions` class. The PDF specification recommends using the `ToUnicode` table to extract text content from PDFs. However, using the font's CMap table can produce better results for certain types of documents. Starting with version 24.11, you can choose which table to use for decoding. By default, the `ToUnicode` table is used.

The following sample demonstrates the new option using:
```csharp
private static void ConvertPdfToHtmlUsingCMap()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // New option there
            FontEncodingStrategy = Aspose.Pdf.HtmlSaveOptions.FontEncodingRules.DecreaseToUnicodePriorityLevel
        };
        // Save HTML document
        document.Save(dataDir + "CmapFontHTML_out.html", options);
    }
}
```


## What's new in Aspose.PDF 24.10

The Elliptic Curve Digital Signature Algorithm (ECDSA) is a modern cryptographic algorithm known for providing strong security with smaller key sizes compared to traditional algorithms. Since version 24.10, it has been possible to sign PDF documents using ECDSA, as well as verify ECDSA signatures. The following elliptic curves are supported for creating and verifying digital signatures:
* P-256 (secp256r1).
* P-384 (secp384r1).
* P-521 (secp521r1).
* brainpoolP256r1.
* brainpoolP384r1.
* brainpoolP512r1.

The SHA-256 hash algorithm is used for generating the signature. ECDSA signatures can be verified using the following hash algorithms: SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, and SHA3-512.

You can use your usual code to sign documents with ECDSA and to verify signatures:
 
```cs
private static void Sign(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}

private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign_out.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Get annotation list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                bool isValid = signature.VerifySignature(sigName);
                Console.WriteLine("Signature '{0}' validation returns {1}", sigName, isValid);
            }
        }
    }
}
```

Sometimes, it is necessary to crop an image before inserting it into a PDF. We have added an overloaded version of the `AddImage()` method to support adding cropped images:

```cs
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (Stream imgStream = File.OpenRead(Path.Combine(dataDir, "Images", "Sample-01.jpg")))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## What's new in Aspose.PDF 24.9

Since version 24.9, it has been possible to generate a crash report when the library throws an exception. A crash report includes information about the type of exception, application title, Aspose.PDF version, OS version, error message, and stack trace.

The following code snippet demonstrates a common scenario for generating a crash report:

```cs
private static void GenerateCrashReportExample()
{
    try
    {
        // some code
        // ....

        // Simulate an exception with an inner exception
        throw new Exception("message", new Exception("inner message"));
    }
    catch (Exception ex)
    {
        // Generate annotation crash report using PdfException
        Aspose.Pdf.PdfException.GenerateCrashReport(new Aspose.Pdf.CrashReportOptions(ex));
    }
}
```

Extracting an PDF document layer elements and saving into new PDF stream are available from now. In PDF documents, layers (also known as Optional Content Groups or OCGs) are used for various purposes, primarily to manage and control the visibility of content within the document. This functionality is particularly useful in design, engineering, and publishing. For example: blueprint aspects, complex diagram components, language versions of the same content.

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

The `GraphicalPdfComparer` class is added for the graphic comparison of PDF documents and pages. Graphic comparison deals with document page images. It returns the result as an `ImagesDifference` object or as a PDF document that contains images merged from the original and the differences. Graphic comparison is most useful for documents that have minor differences in text or graphic content.

The following code snippet demonstrates the graphic comparison of two PDF documents and saves an image with the differences into the resultant PDF document:

```cs
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare and save result
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```

API implemented for integrating FileFormat.HEIC and Aspose.PDF. The HEIC (High-Efficiency Image Coding) is a modern image file format introduced by Apple with iOS 11 in 2017 as the default image format for iPhones and iPads.

To convert HEIC images to PDF user should add the reference to `FileFormat.HEIC` NuGet package and use the following code snippet:

```cs
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(FileFormat.Heic.Decoder.PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```


## What's new in Aspose.PDF 24.8

Converting PDF Documents into PDF/A-4 format

Since version 24.8, it has been possible to convert PDF documents into PDF/A-4. Part 4 of the standard, based on PDF 2.0, was published in late 2020.

The following code snippet demonstrates how to convert a document into PDF/A-4 format when the input document is an earlier PDF version than 2.0.

```cs
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```

Since 24.8 we introduced a method for flattening transparent content in PDF documents:

```cs
private static void FlattenTransparency()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTransparentImage.pdf"))
    {
        // Flatten image transparency
        document.FlattenTransparency();
        // Save PDF document
        document.Save(dataDir + "PdfWithFlattenedImage.pdf");
    }
}
```


## What's new in Aspose.PDF 24.7

Comparing PDF Documents with Aspose.PDF for .NET

Since 24.7 it's possible to compare PDF documents content with annotation marks and side-by-side output:

The first code snippet demonstrates how to compare the first pages of two PDF documents.

```cs
private static void ComparingSpecificPagesSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1],
                dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

The second code snippet expands the scope to compare the entire content of two PDF documents.

```cs
private static void ComparingEntireDocumentsSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Also, from this release added the Aspose.PDF Security for .NET plugin:

Encryption feature:

```cs
var input = "sample.pdf";
var output = "encrypted.pdf";

var plugin = new Security();
var opt = new EncryptionOptions("123456789", "123", DocumentPrivilege.ForbidAll);
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

Decryption feature:

```cs
var input = "encrypted.pdf";
var output = "decrypted.pdf";

var plugin = new Security();
var opt = new DecryptionOptions("123456789");
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

## What's new in Aspose.PDF 24.6

Since the 24.6 release, as part of the editing tagged PDF, were added methods on **Aspose.Pdf.LogicalStructure.Element**:

- Tag (add tags to specific operators like images, text, and links)
- InsertChild
- RemoveChild
- ClearChilds

Also, in this release possible to create an accessible PDF using low-level functions:

The next code snippet works with a PDF document and its tagged content, utilizing an Aspose.PDF library to process it.

```cs
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create annotation span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

Since 24.6 Aspose.PDF for .NET allows to sign PDF with X509Certificate2 in base64 format:

```cs
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create annotation delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving annotation response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## What's new in Aspose.PDF 24.5

This release allows us to work with PDF layers. For example:

- lock a PDF layer
- extract PDF layer elements
- flatten a layered PDF
- merge All Layers inside the PDF into one

### Lock a PDF layer

Since the 24.5 release, you can open a PDF, lock a specific layer on the first page, and save the document with the changes. There are two new methods and one property was added:

Layer.Lock(); -  Locks the layer.
Layer.Unlock(); - Unlocks the layer.
Layer.Locked; - Property, indicating the layer locked state.

```cs
private static void LockLayerInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

### Extract PDF layer elements

The Aspose.PDF for .NET library allows extracts of each layer from the first page and saves each layer to a separate file.

To create a new PDF from a layer, the following code snippet can be used:

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

### Flatten a layered PDF

Aspose.PDF for .NET library opens a PDF, iterates through each layer on the first page, and flattens each layer, making it permanent on the page.

```cs
private static void FlattenPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }

        // Save PDF document
        document.Save(dataDir + "FlattenedLayersPdf_out.pdf");
    }
}
```

The 'Layer.Flatten(bool cleanupContentStream)' method accepts the boolean parameter that specifies whether to remove optional content group markers from the content stream. Setting the cleanupContentStream parameter to false speeds up the process of flattening.

### Merge All Layers inside the PDF into one

The Aspose.PDF for .NET library allows merges either all PDF layers or a specific layer on the first page into a new layer and saves the updated document.

Two methods were added to merge all layers on the page:

- void MergeLayers(string newLayerName);
- void MergeLayers(string newLayerName, string newOptionalContentGroupId); 

The second parameter allows renaming the optional content group marker. The default value is "oc1" (/OC /oc1 BDC).

```cs
private static void MergePdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        page.MergeLayers("NewLayerName");
        // Or
        // page.MergeLayers("NewLayerName", "OC1");

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```

## What's new in Aspose.PDF 24.4

This release supports applying a clipping mask to images:

```cs
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
    }
}
```

Since 24.4 you can select the Choose paper source by PDF page size in the print dialog using the API

Beginning with Aspose.PDF 24.4 this preference can be switched on and off using the Document.PickTrayByPdfSize property or the PdfContentEditor facade:

```cs
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose annotation paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```

```cs
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using (var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

        // Set the flag to choose annotation paper tray using the PDF page size
        contentEditor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PickTrayByPDFSize);

        // Save PDF document
        contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
    }
}
```

From this release added the Aspose.PDF Signature for .NET plugin:

- Example with creating new field and options:

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set extra options
opt.Reason = "my Reason";
opt.Contact = "my Contact";
opt.Location = "my Location";
// perform the process
plugin.Process(opt);
```

- Example with existing empty field

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path with empty signature field
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set name of existing signature field
opt.Name = "Signature1";
// perform the process
plugin.Process(opt);
```


## What's new in Aspose.PDF 24.3

From this release added the PDF/A Converter for .NET plugin:

```cs
var options = new PdfAConvertOptions
{
    PdfAVersion = PdfAStandardVersion.PDF_A_3B
};

// Add the source file
options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // replace with your actual file path

// Add the path to save the converted file
options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

// Create the plugin instance
var plugin = new PdfAConverter();

// Run the conversion
plugin.Process(options);
```

- Implement a search through a list of phrases in a TextFragmentAbsorber:

```cs
private static void SearchMultipleRegex()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

Since 24.3 possible to add an empty signature field on every page to the PDF/A file

```cs
private static void AddEmptySignatureFieldOnEveryPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var fieldName = "signature_1234";

    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // The new suggested code, using SignatureField object
        var signatureField = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(10, 10, 100, 100));

        // Add the default appearance for the signature field
        signatureField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
        var newAddedField = document.Form.Add(signatureField, fieldName, 1);

        // Find annotation associated with the field
        Aspose.Pdf.Annotations.Annotation addedAnnotation = null;
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            if (annotation.FullName == fieldName)
            {
                addedAnnotation = annotation;
                break;
            }
        }

        // Add the annotation to every page except of initial
        if (addedAnnotation != null)
        {
            for (int p = 2; p <= document.Pages.Count; p++)
            {
                document.Pages[p].Annotations.Add(addedAnnotation);
            }
        }

        // Save PDF document
        document.Save(dataDir + "outputPdfaWithSignatureFields.pdf");
    }
}
```

## What's new in Aspose.PDF 24.2

Since 24.2 possible to get the vector data from a PDF file

It was implemented GraphicsAbsorber to get vector data from documents:

```cs
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

## What's new in Aspose.PDF 24.1

Since 24.1 release possible to import FDF format annotations to PDF:

```cs
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

Also, supports for access to Page Dictionary or Document Catalog.

Here are examples of code for DictionaryEditor:

- Add new values

```cs
/private static void AddNewKeysToPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // example of key's names
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("name data"));
        dictionaryEditor.Add(KEY_STRING, new Aspose.Pdf.DataEditor.CosPdfString("string data"));
        dictionaryEditor.Add(KEY_BOOL, new Aspose.Pdf.DataEditor.CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new Aspose.Pdf.DataEditor.CosPdfNumber(11.2));

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditor_out.pdf");
    }
}
```

- Add and set values to dictionary

```cs
private static void ModifyKeysInPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("Old data"));
        // Modify existing value
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("New data");

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorEdit_out.pdf");
    }
}
```

- Get value from dictionary

```cs
private static void GetValuesFromPdfPageDicrionary()
{
    string KEY_NAME = "name";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // or 
        Aspose.Pdf.DataEditor.ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
}
```

- Remove value from dictionary

```cs
private static void RemoveFromPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";
    string EXPECTED_NAME = "name data";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorRemove_out.pdf");
    }
}
```

## What's new in Aspose.PDF 23.12

The form can be found and the text can be replaced using the following code snippet:

```cs
private static void ReplaceTextInPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

Or, the form can be completely removed:

```cs
private static void DeleteSpecifiedForm1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

Another variant of removing the form:

```cs
private static void DeleteSpecifiedForm2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
``` 

- All forms can be deleted using the following code snippet:

```cs
private static void RemoveAllForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

- Implement PDF to Markdown conversion:

```cs
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        };
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

- Implement OFD to PDF conversion:

```cs
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```

From this release added the Merger plugin:

```cs
private static void PdfMergeUsingPlugin()
{
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Create annotation new instance of Merger
    using (var merger = new Aspose.Pdf.Plugins.Merger())
    {
        // Create MergeOptions
        var opt = new Aspose.Pdf.Plugins.MergeOptions();
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat1.pdf"));
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat2.pdf"));
        opt.AddOutput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "ConcatenatePdfFiles_out.pdf"));

        // Process the PDF merging
        merger.Process(opt);
    }
}
```

Also, from this release added the ChatGPT plugin:

```cs
private static async void InvokeChatGptPlugin()
{
    using (var plugin = new Aspose.Pdf.Plugins.PdfChatGpt())
    {
        var options = new Aspose.Pdf.Plugins.PdfChatGptRequestOptions();
        options.AddOutput(new Aspose.Pdf.Plugins.FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
        options.ApiKey = "Your API key."; // You need to provide the key to access the API.
        options.MaxTokens = 1000; // The maximum number of tokens to generate in the chat completion.

        // Add the request messages.
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "You are annotation helpful assistant.",
            Role = Aspose.Pdf.Plugins.Role.System
        });
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "What is the biggest pizza diameter ever made?",
            Role = Aspose.Pdf.Plugins.Role.User
        });

        // Process the request.
        var result = await plugin.ProcessAsync(options);

        var fileResultPath = result.ResultCollection[0].Data;

        // The ChatGPT API chat completion object.
        var chatCompletionObject = result.ResultCollection[1].Data as Aspose.Pdf.Plugins.ChatCompletion;
    }
}
```

## What's new in Aspose.PDF 23.11

From this release possible to remove hidden text from PDF file:

```cs
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
    }
}
```

Since 23.11 supports for thread interruption:

```cs
private static void InterruptExample()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var monitor = new Aspose.Pdf.Multithreading.InterruptMonitor())
    {
        // An class that can produce long-drawn-out work
        RowSpanWorker worker = new RowSpanWorker(dataDir + "RowSpanWorker_out.pdf", monitor);

        var thread = new System.Threading.Thread(new System.Threading.ThreadStart(worker.Work));
        thread.Start();

        // The timeout should be less than the time required for full document save (without interruption)
        System.Threading.Thread.Sleep(500);

        // Interrupt the process
        monitor.Interrupt();

        // Wait for interruption...
        thread.Join();
    }
}

private class RowSpanWorker
{
    private readonly string outputPath;
    private readonly Aspose.Pdf.Multithreading.InterruptMonitor monitor;

    public RowSpanWorker(string outputPath, Aspose.Pdf.Multithreading.InterruptMonitor monitor)
    {
        this.outputPath = outputPath;
        this.monitor = monitor;
    }

    public void Work()
    {
        // This is some large text, used Lorem Ipsum in 10000 characters to cause suspension in processing
        string text = RunExamples.GetLoremIpsumString(10000);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            Aspose.Pdf.Multithreading.InterruptMonitor.ThreadLocalInstance = this.monitor;
            var page = document.Pages.Add();

            var table = new Aspose.Pdf.Table
            {
                DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
            };

            var row0 = table.Rows.Add();

            // Add annotation cell that spans for two rows and contains annotation long-long text
            var cell00 = row0.Cells.Add(text);
            cell00.RowSpan = 2;
            cell00.IsWordWrapped = true;
            row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
            row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

            var row1 = table.Rows.Add();
            row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
            row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

            page.Paragraphs.Add(table);

            try
            {
                // Save PDF document
                document.Save(this.outputPath);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
```


## What's new in Aspose.PDF 23.10

The current update presents three versions of Removing tags from tagged PDFs.

- Remove some node element from a documentElement (root tree element):

```cs
private static void RemoveStructElement()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as Aspose.Pdf.Structure.StructElement : null;

        if (documentElement.Children.Remove(structElement))
        {
            // Element removed. Save PDF document.
            document.Save(dataDir + "StructureElementsRemoved.pdf");
        }

        // You can also delete the structElement itself
        //if (structElement != null)
        //{
        //    structElement.Remove();
        //    document.Save(outputPdfPath);
        //}
    }
}
```

- Remove all marked elements tags from the document, but keep the structure elements:

```cs
private static void RemoveMarkedElementsTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var root = structure.Children[0];
        var queue = new Queue<Aspose.Pdf.Structure.Element>();
        queue.Enqueue(root);

        while (queue.TryDequeue(out var element))
        {
            foreach (var child in element.Children)
            {
                queue.Enqueue(child);
            }

            if (element is Aspose.Pdf.Structure.TextElement || element is Aspose.Pdf.Structure.FigureElement)
            {
                element.Remove();
            }
        }

        // Save PDF document
        document.Save(dataDir + "MarkedElementsTagsRemoved.pdf");
    }
}
```

- Remove tags at all:

```cs
private static void RemoveTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        documentElement.Remove();

        // Save PDF document
        document.Save(dataDir + "TagsRemoved.pdf");
    }
}
```

Since 23.10 was implemented a new feature to measure character height. Use the following code to measure the height of a character.

```cs
private static void DisplayCharacterHeight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextFragmentAbsorber to get information about state of document text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Get height of 'A' character being displayed with font of first text fragment
        var textState = absorber.TextFragments[1].TextState;
        var height = textState.MeasureHeight('A');
        Console.WriteLine("The height of 'A' character displayed with {0} font size of {1} is {2:N3}", textState.Font.FontName, textState.FontSize,height);
    }
}
```

Note that the measurement is based on the font embedded in the document. If any information for a dimension is missing, this method returns 0.

Also, this release provides the Sign a PDF using a signed HASH:

```cs
private static void SignPdfUsingSignedHash(string certP12, string pfxPassword)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(certP12, pfxPassword);

        // Create a delegate to external sign
        pkcs7.CustomSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            X509Certificate2 signerCert = new X509Certificate2(certP12, pfxPassword, X509KeyStorageFlags.Exportable);
            RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);    //not supported on core 2.0
            rsaCSP.FromXmlString(xmlString);                            //not supported on core 2.0

            byte[] signedData = rsaCSP.SignHash(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };

        // Sign PDF file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);

        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Verify
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "SignWithCertificate_out.pdf");

        if (!sign.VerifySignature("Signature1"))
        {
            throw new Exception("Not verified");
        }
    }
}
```

One more new feature is Print Dialog Presets Page Scaling:

```cs
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```

## What's new in Aspose.PDF 23.9

Since 23.9 support to remove a child annotation from a fillable field.

```cs
private static void RemoveChildAnnotationFromFillableField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldWithChildAnnots.pdf"))
    {
        // Get field with child annotations
        var field = (Aspose.Pdf.Forms.Field)document.Form["1 Vehicle Identification Number"];
        // Get first child annotation
        var annotation = field[1];
        // Remove the annotation
        document.Pages[annotation.PageIndex].Annotations.Remove(annotation);

        // Save PDF document
        document.Save(dataDir + "RemoveChildAnnotation_out.pdf");
    }
}
```

## What's new in Aspose.PDF 23.8

Since 23.8 support to add Incremental Updates detection.

The function for detecting Incremental Updates in a PDF document has been added. This function returns 'true' if a document was saved with incremental updates; otherwise, it returns 'false'.

```cs
private static bool HasIncrementalUpdate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithIncrementalUpdate.pdf"))
    {
        // New method
        bool hasIncrementalUpdate = document.HasIncrementalUpdate();

        Console.WriteLine("Document {0} incremental update check returns: {1}", document.FileName, hasIncrementalUpdate);
        return hasIncrementalUpdate;
    }
}
```

Also, 23.8 supports the ways to work with nested checkbox fields. Many fillable PDF forms have checkbox fields that act as radio groups:

- Create multi-value checkbox field:

```cs
private static void CreateMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var checkbox = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 50, 70, 70));

        // Set the first checkbox group option value
        checkbox.ExportValue = "option 1";

        // Add new option right under existing ones
        checkbox.AddOption("option 2");

        // Add new option at the given rectangle
        checkbox.AddOption("option 3", new Aspose.Pdf.Rectangle(100, 100, 120, 120));

        document.Form.Add(checkbox);

        // Select the added checkbox
        checkbox.Value = "option 2";

        // Save PDF document
        document.Save(dataDir + "MultivalueCheckboxField.pdf");
    }
}
```

- Get and set value of a multi-value checkbox:

```cs
private static void GetAndSetValueOfMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MultivalueCheckboxField.pdf"))
    {
        var form = document.Form;
        var checkbox = form.Fields[0] as Aspose.Pdf.Forms.CheckboxField;

        // Allowed values may be retrieved from the AllowedStates collection
        // Set the checkbox value using Value property
        checkbox.Value = checkbox.AllowedStates[0];
        var checkboxValue = checkbox.Value; // the previously set value, e.g. "option 1"

        // The value should be any element of AllowedStates
        checkbox.Value = "option 2";
        checkboxValue = checkbox.Value; // option 2

        // Uncheck boxes by either setting Value to "Off" or setting Checked to false
        checkbox.Value = "Off";
        // or, alternately:
        // checkbox.Checked = false;
        checkboxValue = checkbox.Value; // Off
    }
}
```

## What's new in Aspose.PDF 23.7

From Aspose.PDF 23.7 support to add the shape extraction:

```cs
private static void CopyShape()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Create PDF document
        using (var destDocument = new Aspose.Pdf.Document())
        {
            // Absorb vector graphics from the source document
            var graphicAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();
            graphicAbsorber.Visit(sourceDocument.Pages[1]);

            // Copy the graphics into the destination document specified page and area
            var area = new Aspose.Pdf.Rectangle(90, 250, 300, 400);
            destDocument.Pages[1].AddGraphics(graphicAbsorber.Elements, area);

            // Save PDF document
            destDocument.Save(dataDir + "CopyShape_out.pdf");
        }
    }
}
```

Also supports the ability to detect Overflow when adding text:

```cs
private static void FitTextIntoRectangle()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document()) 
    {
        // Generate text to add: "Lorem Ipsum" text of 1000 characters
        var paragraphContent = RunExamples.GetLoremIpsumString(1000);
        // Create a text fragment with the desired text
        var fragment = new Aspose.Pdf.Text.TextFragment(paragraphContent);
        // Declare the rectangle to fit text into
        var rectangle = new Aspose.Pdf.Rectangle(100, 600, 500, 700, false);
        
        // Check whether the text fits into the rectangle
        var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);

        // Iteratively decrease font size until text fits the rectangle
        while (!isFitRectangle)
        {
            fragment.TextState.FontSize -= 0.5f;
            isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
        }

        // Create a paragraph from the text fragment in the specified rectangle. Now you may be sure it fits.
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        paragraph.Rectangle = rectangle;
        paragraph.AppendLine(fragment);

        // Create a text builder to place the paragraph on the document page
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages.Add());
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "FitTextIntoRectangle_out.pdf");
    }
}
```

## What's new in Aspose.PDF 23.6

From Aspose.PDF 23.6 support to add the next plugins:

- Aspose PdfConverter Html to PDF 
- Aspose PdfOrganizer Resize API
- Aspose PdfOrganizer Compress API

Update the Aspose.PdfForm 
- add feature ‘Export "Value's from fields in document to CSV file"
- add the ability to set properties for a separate fields

Also support the add the ability to set the title of the HTML, Epub page:

```cs
private static void SetHtmlTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            ExplicitListOfSavedPages = new[] { 1 },
            SplitIntoPages = false,
            FixedLayout = true,
            CompressSvgGraphicsIfAny = false,
            SaveTransparentTexts = true,
            SaveShadowedTextsAsTransparentTexts = true,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            // New property
            Title = "Title for page"
        };

        // Save HTML document
        document.Save(dataDir + "SetHtmlTitle_out.html", options);
    }
}
```

## What's new in Aspose.PDF 23.5

Since 23.5 support to add RedactionAnnotation FontSize option. Use the next code snippet to solve this task:

```cs
private static void AddRedactionAnnotationFontSize() 
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf")) 
    {
        // Create RedactionAnnotation instance for specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1],
            new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
        annot.FillColor = Aspose.Pdf.Color.Black;

        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;
        // Text to be printed on redact annotation
        annot.OverlayText = "(Unknown)";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Repat Overlay text over redact Annotation
        annot.Repeat = false;

        // New property
        annot.FontSize = 20;

        // Add annotation to annotations collection of first page
        document.Pages[1].Annotations.Add(annot);
        // Flattens annotation and redacts page contents (i.e. removes text and image under redacted annotation)
        annot.Redact();
        // Save PDF document
        document.Save(dataDir + "AddRedactionAnnotationFontSize_out.pdf");
    }
}
```

## What's new in Aspose.PDF 23.4

Aspose.PDF announced the release of .NET 7 SDK.

## What's new in Aspose.PDF 23.3.1

From Aspose.PDF 23.3 support to add the next plugins:

- Aspose.PdfForm
- Aspose.PdfConverter PDF to HTML
- Aspose.PdfConverter PDF to XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator for Images

## What's new in Aspose.PDF 23.3

Version 23.3 introduced support for keeping image proportions and resolution while inserting on the page. Two methods can be used to solve this problem:

```cs
private static void InsertImageWithNativeResolutionAsTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "600"
        };

        for (var j = 0; j < 2; j++)
        {
            var row = table.Rows.Add();
            var cell = row.Cells.Add();
            cell.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsTable_out.pdf");
    }
}
```

And the second approach:

```cs
private static void InsertImageWithNativeResolutionAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        for (var j = 0; j < 2; j++)
        {
            page.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsParagraph_out.pdf");
    }
}
```

The image will be placed in a scaled size and native resolution. You can set FixedWidth or FixedHeight properties in combination with IsApplyResolution.


## What's new in Aspose.PDF 23.1.1

From Aspose.PDF 23.1.1 support to add the next plugins:

- Aspose.PdfOrganizer plugin
- Aspose.PdfExtractor plugin

## What's new in Aspose.PDF 23.1

Since 23.1 version support to create PrinterMark annotation.

Printer's marks are graphic symbols or text added to a page to assist production personnel in identifying components of a multiple-plate job and maintaining consistent output during production. Examples commonly used in the printing industry include:

- Registration targets for aligning plates
- Gray ramps and colour bars for measuring colours and ink densities
- Cut marks showing where the output medium is to be trimmed

We will show the example of the option with color bars for measuring colors and ink densities. There is a basic abstract class PrinterMarkAnnotation and from it child ColorBarAnnotation - which already implements these stripes. Let's check the example:

```cs
private static void AddPrinterMarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);

        var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
        var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
        var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

        var colorBarBlack = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectBlack);
        var colorBarCyan = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectCyan,
            Aspose.Pdf.Annotations.ColorsOfCMYK.Cyan);
        var colorBarMagenta = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectMagenta);
        colorBarMagenta.ColorOfCMYK = Aspose.Pdf.Annotations.ColorsOfCMYK.Magenta;
        var colorBarYellow = new Aspose.Pdf.Annotations.ColorBarAnnotation(page,
            new Aspose.Pdf.Rectangle(400, 250, 450, 700), Aspose.Pdf.Annotations.ColorsOfCMYK.Yellow);

        page.Annotations.Add(colorBarBlack);
        page.Annotations.Add(colorBarCyan);
        page.Annotations.Add(colorBarMagenta);
        page.Annotations.Add(colorBarYellow);

        // Save PDF document
        document.Save(dataDir + "PrinterMarkAnnotation_out.pdf");
    }
}
```
Also support the vector images extraction. Try using the following code to detect and extract vector graphics:

```cs
private static void SavePdfVectorGraphicToSvg()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Attempt to save the vector graphics into a specified SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "PdfVectorGraphicToSvg.svg");
    }
}
```

## What's new in Aspose.PDF 22.12

From this release support to convert PDF to DICOM Image

```cs
private static void PdfToDicom()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PagesToImages.pdf"))
    {
        var dicom = new Aspose.Pdf.Devices.DicomDevice();
        FileStream outStream = new FileStream(dataDir + "PdfToDicom_out.dcm", FileMode.Create, FileAccess.ReadWrite);
        dicom.Process(document.Pages[1], outStream);
    }
}
```    

## What's new in Aspose.PDF 22.09

Since 22.09 support adding property for modify the order of the subject rubrics (E=, CN=, O=, OU=, ) into the signature.

```cs
private static void SignPdfWithModifiedOrderOfSubjectRubrics(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password);

        // Set signature custom appearance
        signature.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.CN, Aspose.Pdf.Forms.SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.OU, Aspose.Pdf.Forms.SubjectNameElements.S, Aspose.Pdf.Forms.SubjectNameElements.C }
        };

        // Sign PDF file
        fileSign.Sign(1, true, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithModifiedOrderOfSubjectRubrics_out.pdf");
    }
}
```

## What's new in Aspose.PDF 22.6

Since 22.5 support to extract SubScript and SuperScript text from PDF.

If the PDF document contains SubScript and SuperScript text such as H2O, then extracting the text from the PDF must also extract their formatting information (in the extracted plain text).
If the PDF contains text in italics, it must also be included in the extracted content.

```cs
private static void ExtractTextSuperscript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextWithSubscriptsSuperscripts.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Iterate through text fragments to find superscript text
        foreach (var textFragment in absorber.TextFragments) 
        {
            if (textFragment.TextState.Superscript)
            {
                Console.WriteLine(String.Format("Text {0} at {1} is superscript!", textFragment.Text, textFragment.Position));
            }
        }
    }
}
```

## What's new in Aspose.PDF 22.4

This release includes information for Aspose.PDF for .NET:

- PDF to ODS: Recognize text in subscript and superscript;

**example**

```cs
private static void ConvertPdfToOds()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            // Specify the desired table file format
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

- PDF to XMLSpreadSheet2003: Recognize text in subscript and superscript;

- PDF to Excel: Recognize text in subscript and superscript;

- Remove UR signatures while saving document;

- Remove Suspects flag in MarkInfo while saving document;

- Remove Info while saving document

## What's new in Aspose.PDF 22.3

This release includes the following updates:

- Support for AFRelationship;

- PDF header validation;

- Remove adbe.x509.rsa_sha1 subfilter while saving document;

- Format Field as Number and Date Format;

- Prohibit use RC4 encryption in FDF 2.0ю

## What's new in Aspose.PDF 22.2

From the 22.2 version it is possible to sign a document using PdfFileSignature with LTV, and with being able to change the hashing from SHA1 to SHA256.

```csharp
private static void SignPdfWithSha256(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(300, 100, 1, 1);
        var signature = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password)
        {
            UseLtv = true,
            TimestampSettings = new Aspose.Pdf.TimestampSettings("http://freetsa.org/tsr", string.Empty, Aspose.Pdf.DigestHashAlgorithm.Sha256)
        };

        // Sign PDF file
        fileSign.Sign(1, false, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithSha256_out.pdf");
    }
}
```

## What's new in Aspose.PDF 22.1

Now, Aspose.PDF for .NET supports loading documents from one of the most popular document formats, Portable Document Format (PDF) version 2.0.

## What's new in Aspose.PDF 21.11

### Allow non-latin characters in password

```csharp
private static void EncriptPdfNonlatinPassCharacters()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        bool isSuccessful = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print,
            Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
        Console.WriteLine(isSuccessful);
        // Save PDF document
        fileSecurity.Save(dataDir + "PdfNonlatinPassEncrypted_out.pdf");
    }
}
```

## What's new in Aspose.PDF 21.10

### How to detect hidden text?

Please use TextState.Invisible to get information about invisibility of text out of rendering mode setting.

We used the following code for testing:

```csharp
private static void DisplayTextInvisibility()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithHiddenText.pdf"))
    {
        Console.WriteLine(document.FileName);

        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);
        var textFragmentCollection = absorber.TextFragments;

        // Iterate through text fragments to find hidden text
        for (int i = 1; i <= textFragmentCollection.Count; i++)
        {
            var fragment = textFragmentCollection[i];
            Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
            Console.WriteLine("Text: {0}", fragment.Text);
            Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
            Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
            Console.WriteLine("---");
        }
    }
}
```

### How do get information about the number of layers in a PDF document?

```csharp
private static void GetPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithLayers.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;
        // Save each layer to the output path
        foreach (var layer in layers)
        {
            Console.WriteLine("Document {0} contains a layer named: {1} ", document.FileName, layer.Name);
        }
    }
}
```

## What's new in Aspose.PDF 21.9

Customize background color for signature appearance and the font color of the labels in the signature area with Aspose.PDF for .NET.

```csharp
private static void SignPdfWithCustomColorsInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set colors
            ForegroundColor = Aspose.Pdf.Color.DarkGreen,
            BackgroundColor = Aspose.Pdf.Color.LightSeaGreen,
        };
        // Sign PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "SignPdfWithCustomColorsInAppearance_out.pdf");
    }
}
```

## What's new in Aspose.PDF 21.8

### How to change text color in Digital Signature?

In the 21.8 version  ForegroundColor property, it allows changing text color in Digital Signature.

```csharp
private static void SignPdfWithForegroundColorInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set text color
            ForegroundColor = Aspose.Pdf.Color.Green
        };
        // Sign PDF file
        pdfSign.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfSign.Save(dataDir + "SignPdfWithForegroundInAppearance_out.pdf");
    }
}
```

## What's new in Aspose.PDF 21.7

### PDF creation based on XML and XLS with parameters

To add XSL params we need to create own [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) and set as property in [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). The following snippet shows how to use this class with the sample files described above.

```csharp
private static void ConvertXslfoToPdfWithArgumentList()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");

    // Example of using XsltArgumentList
    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XslfoToPdfWithArgumentList_out.pdf");
    }
}
```

## What's new in Aspose.PDF 21.6

With Aspose.PDF for .NET you can hide images using ImagePlacementAbsorber from the document:

```csharp
private static void HideImageInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImagePlacement.pdf"))
    {
        // Create ImagePlacementAbsorber instance
        var absorber = new Aspose.Pdf.ImagePlacementAbsorber();
        // Load the images of the first page
        document.Pages[1].Accept(absorber);

        // Iterate through each image placement on the first page
        foreach (var imagePlacement in absorber.ImagePlacements)
        {
            // Hide image
            imagePlacement.Hide();
        }

        // Save PDF document
        document.Save(dataDir + "HideImageInPdf_out.pdf");
    }
}
```

## What's new in Aspose.PDF 21.5

### How to extract font full name from it description/resource at PDF?

You can get a full font with the prefix with  BaseFont property for the Font class.

```csharp
private static void DisplayFontFullNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf"))
    {
        // Get document fonts
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through the fonts
        foreach (var font in fonts)
        {
            // Show font names
            Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
        }
    }
}
```

## What's new in Aspose.PDF 21.4

### Add API for merging images

Aspose.PDF 21.4 allows you to combine Images. Follow the next code snippet:

```csharp
private static void MergeAsJpeg()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImages to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(inputImagesStreams,
                  Aspose.Pdf.Drawing.ImageFormat.Jpeg, Aspose.Pdf.Facades.ImageMergeMode.Vertical, 1, 1))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.jpg", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

Also you may merge you images as Tiff format:

```csharp
private static void MergeAsTiff()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImagesAsTiff to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(inputImagesStreams))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.tiff", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

## What's new in Aspose.PDF 21.3

### Public expose of property to detect Azure Information Protection

With the next code snippet, you should be able to get access to the encrypted payload of your PDF files, protected with Azure Information Protection:

```csharp
private static void AzureInformationProtection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        if (document.EmbeddedFiles[1].AFRelationship == Aspose.Pdf.AFRelationship.EncryptedPayload)
        {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
                // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
                // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
                // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
        }
    }
}
```

## What's new in Aspose.PDF 21.1

### Add support of retrieving the background color of TextFragment

In this version of Aspose.PDF, the function became available to retrieve the background color. You need to specify searchOptions.SearchForTextRelatedGraphics = true; in the options of TextFragmentAbsorber object.

Please consider the following code:

```csharp
private static void DisplayPdfTextBackgroundColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTextBackgroundColor.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        var searchOptions = new Aspose.Pdf.Text.TextSearchOptions(false);
        // Setting this option into the 'true' is necessary 
        searchOptions.SearchForTextRelatedGraphics = true;
        textFragmentAbsorber.TextSearchOptions = searchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);
        
        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            Console.WriteLine("Text: '{0}'", textFragment.Text);
            Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
            Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
            Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
        }
    }
}
```

### After conversion to HTML the font is fully embedded in the output

Also, in Aspose.PDF 21.1, after converting PDF to HTML, became available embedded fonts in an output HTML document. It is possible with the new boolean save option HtmlSaveParameter.SaveFullFont.

Here is the code snippet:

```csharp
private static void PdfToHtmlWithFullFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            LettersPositioningMethod = Aspose.Pdf.HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF,
            SaveTransparentTexts = true,
            // New option
            SaveFullFont = true
        };
        // Save HTML document
        document.Save(dataDir + "PdfToHtmlWithFullFont_out.html", options);
    }
}
```
