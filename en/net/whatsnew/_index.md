---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /net/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for .NET that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-10-18"
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

## What's new in Aspose.PDF 24.11

A `PageCollection` extension method has been added to update the page number and date header/footer artifacts when adding or inserting new pages. Settings for the page number and date format should be stored in the original document according to the PDF specification, as implemented by Adobe Acrobat.

The following code snippet demonstrates how to update pagination in the document:
```csharp
private static void UpdatePagination()
{
    // Document that contains at least one page with pagination artifacts.
    var inputDocumentPath = "DocumentWithPaginationArtifacts.pdf";
    var outputDocumentPath = "DocumentWithUpdatedPagination.pdf";

    using (var document = new Aspose.Pdf.Document(inputDocumentPath))
    {
        document.Pages.Insert(1, document.Pages[2]);
        document.Pages.Add();
        document.Pages.UpdatePagination();

        document.Save(outputDocumentPath);
    }
}
```

Since version 24.11, we have added the ability to choose a hashing algorithm for Pkcs7Detached. The default is SHA-256. For ECDSA digital signatures, the default digest algorithm depends on the key length.

ECDSA supports SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, and SHA3-512. The SHA3-256, SHA3-384, and SHA3-512 algorithms are supported only for .NET 8 and newer versions. For details on supported platforms for SHA-3, refer to the [documentation](https://learn.microsoft.com/en-us/dotnet/standard/security/cross-platform-cryptography#sha-3).

RSA supports SHA-1, SHA-256, SHA-384, and SHA-512.

DSA supports only SHA-1. Please note that SHA-1 is outdated and does not meet current security standards.

The following code snippet demonstrates setting of hashing algorithm for Pkcs7Detached:
```csharp
private static void SignWithManualDigestHashAlgorithm(string cert, string pass, string inputPdfFile, string outPdfSigned)
{
    using (var document = new Aspose.Pdf.Document(inputPdfFile))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass,  DigestHashAlgorithm.Sha512);
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            signature.Save(outPdfSigned);
        }
        document.Save(outPdfSigned);
    }
}
```

A new `FontEncodingStrategy` property has been added to the `HtmlSaveOptions` class. The PDF specification recommends using the `ToUnicode` table to extract text content from PDFs. However, using the font's CMap table can produce better results for certain types of documents. Starting with version 24.11, you can choose which table to use for decoding. By default, the `ToUnicode` table is used.

The following sample demonstrates the new option using:
```csharp
private static void ConvertPdfToHtmlUsingCMap(string inputPdfFile, string outputHtmlFile)
{
    using (var document = new Aspose.Pdf.Document(inputPdfFile))
    {
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            FontEncodingStrategy = Aspose.Pdf.HtmlSaveOptions.FontEncodingRules.DecreaseToUnicodePriorityLevel
        };
        document.Save(outputHtmlFile, options);
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
private static void Sign(string cert, string inputPdfFile, string signedPdfFile)
{
    using (var document = new Aspose.Pdf.Document(inputPdfFile))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, "12345");
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            signature.Save(signedPdfFile);
        }
    }
}

private static void Verify(string signedPdfFile)
{
    using (var document = new Aspose.Pdf.Document(signedPdfFile))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = signature.GetSignNames();
            foreach (var sigName in sigNames)
            {
                bool isValid = signature.VerifySignature(sigName);
                Console.WriteLine("Signature '{0}' validation returns {1}", sigName, isValid);
            }
        }
    }
}
```

Sometimes, it is necessary to crop an image before inserting it into a PDF. We have added an overloaded version of the `AddImage()` method to support adding cropped images:

```cs
private static void InsertCroppedImageToPdf(string imageFile, string resultPdf)
{
    using (var document = new Aspose.Pdf.Document())
    {
        using (Stream imgStream = File.OpenRead(imageFile))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);                    

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add a new page to the document
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document to the specified file path
        document.Save(resultPdf);
    }
}
```

## What's new in Aspose.PDF 24.9

Since version 24.9, it has been possible to generate a crash report when the library throws an exception. A crash report includes information about the type of exception, application title, Aspose.PDF version, OS version, error message, and stack trace.

The following code snippet demonstrates a common scenario for generating a crash report:

```cs
try
{
    //some code that generates exception
    throw new Exception("message", new Exception("inner message"));
}
catch (Exception ex)
{
    Aspose.Pdf.PdfException.GenerateCrashReport(new Aspose.Pdf.CrashReportOptions(ex));
}
```

Extracting an PDF document layer elements and saving into new PDF stream are available from now. In PDF documents, layers (also known as Optional Content Groups or OCGs) are used for various purposes, primarily to manage and control the visibility of content within the document. This functionality is particularly useful in design, engineering, and publishing. For example: blueprint aspects, complex diagram components, language versions of the same content.

```cs
private static void ExtractPdfLayer(string inputPdfPath, string outputPdfName)
{
    using (var inputDocument = new Aspose.Pdf.Document(inputPdfPath))
    {
        var inputPage = inputDocument.Pages[1];

        var layers = inputPage.Layers;

        foreach (var layer in layers)
        {
            var extractedLayerPdfName = string.Format("{0}_{1}.pdf", outputPdfName, layer.Id);

            using (var stream = File.Create(extractedLayerPdfName))
            {
                layer.Save(stream);
            }
        }
    }
}
```

The `GraphicalPdfComparer` class is added for the graphic comparison of PDF documents and pages. Graphic comparison deals with document page images. It returns the result as an `ImagesDifference` object or as a PDF document that contains images merged from the original and the differences. Graphic comparison is most useful for documents that have minor differences in text or graphic content.

The following code snippet demonstrates the graphic comparison of two PDF documents and saves an image with the differences into the resultant PDF document:

```cs
private static void PdfGraphicComparison(string firstDocumentPath, string secondDocumentPath, string comparisonResultPdfPath)
{
    using (var firstDocument = new Aspose.Pdf.Document(firstDocumentPath))
    {
        using (var secondDocument = new Aspose.Pdf.Document(secondDocumentPath))
        {
            var comparer = new Aspose.Pdf.Comparison.GraphicalComparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Color.Red,
                Resolution = new Resolution(300)
            };
            comparer.CompareDocumentsToPdf(firstDocument, secondDocument, comparisonResultPdfPath);
        }
    }
}
```

API implemented for integrating FileFormat.HEIC and Aspose.PDF. The HEIC (High-Efficiency Image Coding) is a modern image file format introduced by Apple with iOS 11 in 2017 as the default image format for iPhones and iPads.

To convert HEIC images to PDF user should add the reference to `FileFormat.HEIC` NuGet package and use the following code snippet:

```cs
private static void HeicToPdf(string heicImagePath, string resultPdfPath)
{
    using (var fs = new FileStream(heicImagePath, FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(FileFormat.Heic.Decoder.PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

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
            document.Save(resultPdfPath);
        }
    }
}
```

## What's new in Aspose.PDF 24.8

Converting PDF Documents into PDF/A-4 format

Since version 24.8, it has been possible to convert PDF documents into PDF/A-4. Part 4 of the standard, based on PDF 2.0, was published in late 2020.

The following code snippet demonstrates how to convert a document into PDF/A-4 format, assuming the input document is PDF 2.x.

```cs
string documentPath = "";
string conversionLogPath = "";
string resultPdfPath = "";

using (var document = new Document(documentPath))
{
    // Only PDF-2.x documents can be converted to PDF/A-4
    document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.Save(resultPdfPath);
}
```

The second code snippet demonstrates how to convert a document into PDF/A-4 format when the input document is an earlier version.

```cs
string documentPath = "";
string conversionLogPath = "";
string resultPdfPath ="";

using (var document = new Document(documentPath))
{
    document.Convert(Stream.Null, PdfFormat.v_2_0, ConvertErrorAction.Delete);

    document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.Save(resultPdfPath);
}
```

Since 24.8 we introduced a method for flattening transparent content in PDF documents:

```cs
string documentPath = "";
string resultPdfPath = "";

using (var document = new Document(documentPath))
{
    document.FlattenTransparency();
    document.Save(resultPdfPath);
}
```


## What's new in Aspose.PDF 24.7

Comparing PDF Documents with Aspose.PDF for .NET

Since 24.7 it's possible to compare PDF documents content with annotation marks and side-by-side output:

The first code snippet demonstrates how to compare the first pages of two PDF documents.

```cs
string documentPath1 = "";
string documentPath2 = "";

string resultPdfPath = "";

using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
{
    SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
    {
        AdditionalChangeMarks = true,
        ComparisonMode = ComparisonMode.IgnoreSpaces
    });
}
```

The second code snippet expands the scope to compare the entire content of two PDF documents.

```cs
string documentPath1 = "";
string documentPath2 = "";

string resultPdfPath = "";

using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
{
    SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
    {
        AdditionalChangeMarks = true,
        ComparisonMode = ComparisonMode.IgnoreSpaces
    });
}
```

Files are attached to the task. The result was obtained in the mode:

AdditionalChangeMarks = true
ComparisonMode = ComparisonMode.ParseSpaces

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

Since the 24.7 release, as part of the editing tagged PDF, were added methods on **Aspose.Pdf.LogicalStructure.Element**:

- Tag (add tags to specific operators like images, text, and links)
- InsertChild
- RemoveChild
- ClearChilds

These methods allow you to edit PDF file tags, for example:

```cs

var document = new Document(input);
var page = document.Pages[1];
// The marked content operator on page for the image.
BDC imageBdc = null;
// The marked content operator on page for the text.
BDC text1BDC = null;
// The marked content operator on page for the link1.
BDC link1Bdc = null;
// The marked content operator on page for the link2.
BDC link2Bdc = null;
// The marked content operator on page for the Hello text.
BDC helloBdc = null;
// Find the marked content operators for the elements on the page.
for (int i = 1; i <= page.Contents.Count; i++)
{
    Operator op = page.Contents[i];
    BDC bdc = op as BDC;
    if (bdc != null)
    {
        // The text operator with marked content id = 0 was found.
        if (bdc.Properties.MCID == 0)
        {
            helloBdc = bdc;
        }
    }

    Do doXobj = op as Do;
    if (doXobj != null)
    {
        // Wrap the image XObject with makred content operator.
        imageBdc = new BDC(PdfConsts.Figure);
        page.Contents.Insert(i - 2, imageBdc);
        i++;
        page.Contents.Insert(i + 1, new EMC());
        i++;
    }

    TextShowOperator tx = op as TextShowOperator;
    if (tx != null)
    {
        // Wrap the text operator on page with makred content operator.
        if (tx.Text.Contains("efter Ukendt forfatter er licenseret under"))
        {
            text1BDC = new BDC(PdfConsts.P);
            page.Contents.Insert(i - 1, text1BDC);
            i++;
            page.Contents.Insert(i + 1, new EMC());
            i++;
        }
        // Wrap the text operator on page with makred content operator.
        if (tx.Text.Contains("CC"))
        {
            link1Bdc = new BDC(PdfConsts.Link);
            page.Contents.Insert(i - 1, link1Bdc);
            i++;
            page.Contents.Insert(i + 1, new EMC());
            i++;
        }
        // Wrap the text operator on page with makred content operator.
        if (tx.Text.Contains("Dette billede"))
        {
            link2Bdc = new BDC(PdfConsts.Link);
            page.Contents.Insert(i - 1, link2Bdc);
            i++;
            page.Contents.Insert(i + 1, new EMC());
            i++;
        }
    }
}

var tagged = document.TaggedContent;

// Find exist struct element in document.
var helloParagraph = tagged.RootElement.ChildElements[1];

// Clear the subtree of an existing structure tree element.
helloParagraph.ClearChilds();

// Tag paragraph struct element to text on page.
var helloMCR = helloParagraph.Tag(helloBdc);

// Get the struct element attributes.
var helloAttrs = helloMCR.ParentStructureElement.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

// Fill the paragraph struct element spaceAfter attribute.
var helloSpaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
helloSpaceAfter.SetNumberValue(30.625);
helloAttrs.SetAttribute(helloSpaceAfter);

// Create a figure element and place it to root element in second position.
var figure = tagged.CreateFigureElement();
tagged.RootElement.InsertChild(figure, 2);

// Set an alternative text for the figure.
figure.AlternativeText = "A fly.";

// Tag figure struct element to image element on page.
var figureMCR = figure.Tag(imageBdc);

// Get the figure struct element attributes.
var figureAttrs = figureMCR.ParentStructureElement.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

// Fill the figure struct element spaceAfter attribute.
var figureSpaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
figureSpaceAfter.SetNumberValue(3.625);
figureAttrs.SetAttribute(figureSpaceAfter);

// Fill the figure struct element BBox attribute.
var figureBBox = new StructureAttribute(AttributeKey.BBox);
figureBBox.SetArrayNumberValue(new double?[] { 71.9971, 375.839, 523.299, 714.345 });
figureAttrs.SetAttribute(figureBBox);

// Fill the figure struct element placement attribute.
var figurePlacement = new StructureAttribute(AttributeKey.Placement);
figurePlacement.SetNameValue(AttributeName.Placement_Block);
figureAttrs.SetAttribute(figurePlacement);

// Find exist struct element in document.
var p2 = (StructureElement)tagged.RootElement.ChildElements[3];

// Clear the subtree of an existing structure tree element.
p2.ClearChilds();

// Create the span struct element.
var span1 = tagged.CreateSpanElement();

// Get the span1 struct element attributes.
var span1Attrs = span1.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

// Fill the span1 struct element textDecorationType attribute.
var span1TextDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
span1TextDecorationType.SetNameValue(AttributeName.TextDecorationType_Underline);
span1Attrs.SetAttribute(span1TextDecorationType);

// Fill the span1 struct element textDecorationThickness attribute.
var span1TextDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
span1TextDecorationThickness.SetNumberValue(0);
span1Attrs.SetAttribute(span1TextDecorationThickness);

// Fill the span1 struct element textDecorationColor attribute.
var span1TextDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
span1TextDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
span1Attrs.SetAttribute(span1TextDecorationColor);

// Append the span element to the paragraph element in the struct tree.
p2.AppendChild(span1);

// Tag paragraph struct element to text element on page.
var text1MCR = p2.Tag(text1BDC);

// Get the mcr struct element attributes.
var text1Attrs = text1MCR.ParentStructureElement.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

// Fill the text1 MCR struct element textAlign attribute.
var text1TextAlign = new StructureAttribute(AttributeKey.TextAlign);
text1TextAlign.SetNameValue(AttributeName.TextAlign_Center);
text1Attrs.SetAttribute(text1TextAlign);

// Create the span struct element.
var span2 = tagged.CreateSpanElement();

// Get the span2 struct element attributes.
var span2Attrs = span2.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

// Fill the span2 struct element textDecorationType attribute.
var textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
textDecorationType.SetNameValue(AttributeName.TextDecorationType_Underline);
span2Attrs.SetAttribute(textDecorationType);

// Fill the span2 struct element textDecorationThickness attribute.
var textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
textDecorationThickness.SetNumberValue(0);
span2Attrs.SetAttribute(textDecorationThickness);

// Fill the span2 struct element textDecorationColor attribute.
var textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
textDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
span2Attrs.SetAttribute(textDecorationColor);

// Append the span struct element to the struct element tree.
p2.AppendChild(span2);

// Create the link struct element.
var link2 = tagged.CreateLinkElement();
// Set an id attribute of struct element.
link2.SetId(Guid.NewGuid().ToString());
// Append the link struct element to the struct element tree.
span2.AppendChild(link2);
// Tag link struct element to the page annotation element.
link2.Tag(page.Annotations[1]);
// Tag link struct element to text element on page.
link2.Tag(link2Bdc);

// Create the link struct element.
var link1 = tagged.CreateLinkElement();
// Set an id attribute of struct element.
link1.SetId(Guid.NewGuid().ToString());
// Append the link struct element to the struct element tree.
span1.AppendChild(link1);
// Tag link struct element to the page annotation element.
link1.Tag(page.Annotations[2]);
// Tag link struct element to text element on page.
link1.Tag(link1Bdc);

// Remove the struct element at index 0 from the struct tree.
tagged.RootElement.RemoveChild(0);

// Save PDF document
document.Save(output);
```

Also, in this release possible to create an accessible PDF using low-level functions:

The next code snippet works with a PDF document and its tagged content, utilizing an Aspose.PDF library to process it.

```cs
var document = new Document(somepdffilepath);
ITaggedContent content = document.TaggedContent;
SpanElement span = content.CreateSpanElement();
content.RootElement.AppendChild(span);
foreach (var op in document.Pages[1].Contents)
{
    BDC bdc = op as BDC;
    if (bdc != null)
    {
        span.Tag(bdc);
    }
}

document.Save(output);
```

Since 24.6 Aspose.PDF for .NET allows to sign PDF with X509Certificate2 in base64 format:

```cs
var base64Str = "sign";
using (var pdfSign = new PdfFileSignature())
{
    var sign = new ExternalSignature(base64Str, false); // Without Private Key
    sign.ShowProperties = false;
    SignHash customSignHash = delegate (byte[] signableHash)
    {
        // Simulated Server Part (This will probably just be sending data and receiving a response)
        var signerCert = new X509Certificate2(inputP12, "123456", X509KeyStorageFlags.Exportable);//must have Private Key
        var rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    };
    sign.CustomSignHash = customSignHash;
    pdfSign.BindPdf(inputPdf);
    pdfSign.Sign(1, "second approval", "secondexample@mail.com", "Australia", false,
                    new System.Drawing.Rectangle(200, 200, 200, 100),
                    sign);
    pdfSign.Save(outputPdf);
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
var document = new Document(input);
var page = document.Pages[1];
var layer = page.Layers[0];

layer.Lock();

document.Save(output);
```

### Extract PDF layer elements

The Aspose.PDF for .NET library allows extracts of each layer from the first page and saves each layer to a separate file.

To create a new PDF from a layer, the following code snippet can be used:

```cs
var document = new Document(inputPath);
var layers = document.Pages[1].Layers;

foreach (var layer in layers)
{
    layer.Save(outputPath);
}
```

### Flatten a layered PDF

Aspose.PDF for .NET library opens a PDF, iterates through each layer on the first page, and flattens each layer, making it permanent on the page.

```cs
var document = new Document(input);
var page = document.Pages[1];

foreach (var layer in page.Layers)
{
    layer.Flatten(true);
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
var document = new Document(input);
var page = document.Pages[1];

page.MergeLayers("NewLayerName");

// Or page.MergeLayers("NewLayerName", "OC1");

document.Save(output);
```

## What's new in Aspose.PDF 24.4

This release supports applying a clipping mask to images:

```cs
Document document = new Document("input.pdf");
using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
using (var fs2 = new FileStream("mask2.png", FileMode.Open))
{
    document.Pages[1].Resources.Images[1].AddStencilMask(fs1);
    document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
}
```

Since 24.4 you can select the Choose paper source by PDF page size in the print dialog using the API

Beginning with Aspose.PDF 24.4 this preference can be switched on and off using the Document.PickTrayByPdfSize property or the PdfContentEditor facade:

```cs
using (Document document = new Document())
{
    Page page = document.Pages.Add();
    page.Paragraphs.Add(new TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;
    document.Save("result.pdf");
}
```

```cs
using (PdfContentEditor contentEditor = new PdfContentEditor())
{
    contentEditor.BindPdf("input.pdf");

    // Set the flag to choose a paper tray using the PDF page size
    contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
    contentEditor.Save("result.pdf");
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
 
Since the 24.4 release, choosing paper source by PDF page size in the print dialog is possible. The next code snippet enables picking a printer tray based on the PDF's page size.

This preference can be switched on and off using the 'Document.PickTrayByPdfSize' property or the 'PdfContentEditor' facade:

```cs
using (Document document = new Document())
{
    Page page = document.Pages.Add();
    page.Paragraphs.Add(new TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;
    document.Save("result.pdf");
}
```

```cs
using (PdfContentEditor contentEditor = new PdfContentEditor())
{
    contentEditor.BindPdf("input.pdf");

    // Set the flag to choose a paper tray using the PDF page size
    contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
    contentEditor.Save("result.pdf");
}
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
var regexes = new Regex[]
{
    new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)+", RegexOptions.IgnoreCase),
    new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:?", RegexOptions.IgnoreCase),
    new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
    new Regex("Vested in:", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
};
var document = new Document(input);
var absorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
document.Pages.Accept(absorber);
// Get result
var result = absorber.RegexResults
```

Since 24.3 possible to add an empty signature field on every page to the PDF/A file

```cs
static void Main(string[] args)
{
    try
    {
        var lic = new Aspose.Pdf.License();
        lic.SetLicense("Aspose.Total.lic");

        string source = "source.pdf";
        string fieldName = "signature_1234";
        string dest = "source_fieldNotInAllPages.pdf";
        addFieldSingle_NewCode(source, dest, fieldName, 1);
    }
    catch (Exception e)
    {
        Console.WriteLine(e.ToString());
    }
    Console.ReadLine(); 
}

private static void addFieldSingle_NewCode(string source, string dest, string fieldName, int page)
{
    File.Copy(source, dest, true);
    using (var fs = new FileStream(dest, FileMode.Open))
    {
        // The new suggested code, using SignatureField object (this code works fine)
        var document = new Document(fs);
        var f = new SignatureField(document.Pages[page], new Rectangle(10, 10, 100, 100));
        // Add the default appearance for the signature field
        f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
        var newAddedField = document.Form.Add(f, fieldName, page);

        // How can now get newAddedField visible in alla pages?
        Aspose.Pdf.Annotations.Annotation addedField = null;
        foreach (Aspose.Pdf.Annotations.Annotation a in document.Pages[1].Annotations)
        {
            if (a.FullName == fieldName)
            {
                addedField = a;
                break;
            }
        }

        if (addedField != null)
        {
            for (int p = 1; p <= document.Pages.Count; p++)
            {
                if (p == page)
                {
                    continue;
                }
                document.Pages[p].Annotations.Add(addedField);
            }
        }

        document.Save();
    }
    System.Diagnostics.Process.Start(dest);
}
```

## What's new in Aspose.PDF 24.2

Since 24.2 possible to get the vector data from a PDF file

It was implemented GraphicsAbsorber to get vector data from documents:

```cs
var document = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(document.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## What's new in Aspose.PDF 24.1

Since 24.1 release possible to import FDF format annotations to PDF:

```cs
var fdfPath = Params.InputPath + "50745.fdf";
var templatePath = Params.InputPath + "Empty.pdf";
var outputPath = Params.OutputPath + "50745_form.pdf";

using (var form = new Aspose.Pdf.Facades.Form(templatePath))
{
    using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
    {
        form.ImportFdf(fdfInputStream);
    }

    form.Save(outputPath);
}
```

Also, supports for access to Page Dictionary or Document Catalog.

Here are examples of code for DictionaryEditor:

- Add new values

```cs
// example of key's names
string KEY_NAME = "name";
string KEY_STRING = "str";
string KEY_BOOL = "bool";
string KEY_NUMBER = "number";

var outputPath = "page_dictionary_editor.pdf";
using (var document = new Document())
{
    var page = document.Pages.Add();
    var dictionaryEditor = new DictionaryEditor(page);

    dictionaryEditor.Add(KEY_NAME, new CosPdfName("name data"));
    dictionaryEditor.Add(KEY_STRING, new CosPdfString("string data"));
    dictionaryEditor.Add(KEY_BOOL, new CosPdfBoolean(true));
    dictionaryEditor.Add(KEY_NUMBER, new CosPdfNumber(11.2));

    document.Save(outputPath);
}
```

- Add and set values to dictionary

```cs
using (var document = new Document())
{
    var page = document.Pages.Add();
    var dictionaryEditor = new DictionaryEditor(page);
    dictionaryEditor.Add(KEY_NAME, new CosPdfName("Old name"));
    // or 
    dictionaryEditor[KEY_NAME] = new CosPdfName("New name");
}
```

- Get value from dictionary

```cs
using (var document = new Document())
{
    var page = document.Pages.Add();
    var dictionaryEditor = new DictionaryEditor(page);
    dictionaryEditor[KEY_NAME] = new CosPdfName("name");
    var value = dictionaryEditor[KEY_NAME];
    // or 
    ICosPdfPrimitive primitive;
    dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
}
```

- Remove value from dictionary

```cs
using (var document = new Document())
{
    var page = document.Pages.Add();
    var dictionaryEditor = new DictionaryEditor(page);
    dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
    dictionaryEditor.Remove(KEY_NAME);
}
```

## What's new in Aspose.PDF 23.12

The form can be found and the text can be replaced using the following code snippet:

```cs
var document = new Document(input);
var forms = document.Pages[1].Resources.Forms;

foreach (var form in forms)
{
    if (form.IT == "Typewriter" && form.Subtype == "Form")
    {
        var absorber = new TextFragmentAbsorber();
        absorber.Visit(form);

        foreach (var fragment in absorber.TextFragments)
        {
            fragment.Text = "";
        }
    }
}

document.Save(output);
```            

Or, the form can be completely removed:

```cs
var document = new Document(input);
var forms = document.Pages[1].Resources.Forms;

for (int i = 1; i <= forms.Count; i++)
{
    if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
    {
        forms.Delete(forms[i].Name);
    }
}

document.Save(output);
```            

Another variant of removing the form:

```cs
var document = new Document(input);
var forms = document.Pages[1].Resources.Forms;

foreach (var form in forms)
{
    if (form.IT == "Typewriter" && form.Subtype == "Form")
    {
        var name = forms.GetFormName(form);
        forms.Delete(name);
    }
}

document.Save(output);
``` 

- All forms can be deleted using the following code snippet:

```cs
var document = new Document(input);
var forms = document.Pages[1].Resources.Forms;

forms.Clear();

document.Save(output);
```

- Implement PDF to Markdown conversion:

```cs
string markdownOutputFilePath = "output.md"
string inputPdfPath = "input.pdf"
using (Document document = new Document(inputPdfPath))
{
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.ResourcesDirectoryName = "images"; 
    document.Save(markdownOutputFilePath, saveOptions);
}
```

- Implement OFD to PDF conversion:

```cs
var document = new Document("sample.ofd", new OfdLoadOptions());
document.Save("sample.pdf");
```

From this release added the Merger plugin:

```cs
// Path to the output merged PDF file.
var outputPath = "TestMerge.pdf";

// Create a new instance of Merger.
var merger = new Merger();

// Create MergeOptions.
var opt = new MergeOptions();
opt.AddInput(new FileDataSource(inputPath1));
opt.AddInput(new FileDataSource(inputPath2));
opt.AddOutput(new FileDataSource(outputPath));

// Process the PDF merging.
merger.Process(opt);
```

Also, from this release added the ChatGPT plugin:

```cs
using (var plugin = new PdfChatGpt())
{
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
    options.ApiKey = "Your API key."; // You need to provide the key to access the API.
    options.MaxTokens = 1000; // The maximum number of tokens to generate in the chat completion.

    // Add the request messages.
    options.Messages.Add(new Message
    {
        Content = "You are a helpful assistant.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "What is the biggest pizza diameter ever made?",
        Role = Role.User
    });

    // Process the request.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // The ChatGPT API chat completion object.
}
```

## What's new in Aspose.PDF 23.11

From this release possible to remove hidden text from PDF file:

```cs
var document = new Document(inputFile);
var textAbsorber = new TextFragmentAbsorber();

// This option can be used to prevent other text fragments from moving after hidden text replacement.
textAbsorber.TextReplaceOptions = new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None);

document.Pages.Accept(textAbsorber);

foreach (var fragment in textAbsorber.TextFragments)
{
    if (fragment.TextState.Invisible)
    {
        fragment.Text = "";
    }
}

document.Save(outputFile);
```

Since 23.11 supports for thread interruption:

```cs
public void InterruptExample()
{
    string outputFile = testdata + "sample.pdf";
    //this is some large text, used Lorem Ipsum in 8350 characters to cause suspension 
    string text = ExampleApp.LongText;
    using (InterruptMonitor monitor = new InterruptMonitor())
    {
        RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
        Thread thread = new Thread(new ThreadStart(worker.Work));
        thread.Start();

        // The timeout should be less than the time required for full document save (without interruption).
        Thread.Sleep(500);

        // Interrupt the process
        monitor.Interrupt();

        // Wait for interruption...
        thread.Join();
    }

    private class RowSpanWorker
    {
        private readonly string outputPath;
        private readonly InterruptMonitor monitor;

        public RowSpanWorker(string outputPath, InterruptMonitor monitor)
        {
            this.outputPath = outputPath;
            this.monitor = monitor;
        }

        public void Work()
        {
            string text = InterruptMonitorTests.LongText;
            using (var document = new Document())
            {
                InterruptMonitor.ThreadLocalInstance = this.monitor;
                var page = document.Pages.Add();

                var table = new Aspose.Pdf.Table
                {
                    DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
                };

                var row0 = table.Rows.Add();

                // add a cell that spans for two rows and contains a long-long text
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
                    document.Save(this.outputPath);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
        }
    }
}
```
## What's new in Aspose.PDF 23.10

The current update presents three versions of Removing tags from tagged PDFs.

- Remove some node element from a documentElement (root tree element):

```cs
var document = new Document("some tagged pdf");
var structure = document.LogicalStructure;
var documentElement = structure.Children[0];
var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
if (documentElement.Children.Remove(structElement))
{
    // element removed
    document.Save(outputPath);
}

// You can also delete the structElement itself
//if (structElement != null)
//{
//    structElement.Remove();
//    document.Save(outputPath);
//}
```

- Remove all marked elements tags from the document, but keep the structure elements:

```cs
var document = new Document("some tagged pdf");
var structure = document.LogicalStructure;
var root = structure.Children[0];
var queue = new Queue<Element>();
queue.Enqueue(root);
while(queue.TryDequeue(out var element))
{
    foreach (var child in element.Children)
    {
        queue.Enqueue(child);
    }

    if (element is TextElement || element is FigureElement)
    {
        element.Remove();
    }
}
```

- Remove tags at all:

```cs
var document = new Document("some tagged pdf");
var structure = document.LogicalStructure;
var documentElement = structure.Children[0];
documentElement.Remove();
document.Save(outputPath);
```

Since 23.10 was implemented a new feature to measure character height. Use the following code to measure the height of a character.

```cs
var document = new Document(input);
var absorber = new TextFragmentAbsorber();
absorber.Visit(document.Pages[1]);
var height = absorber.TextFragments[1].TextState.MeasureHeight('A');
```

Note that the measurement is based on the font embedded in the document. If any information for a dimension is missing, this method returns 0.

Also, this release provides the Sign a PDF using a signed HASH:

```cs
public void PDFNET_54566()
{
    var inputPdf = "54566.pdf";
    var inputP12 = "54566.p12";
    var inputPfxPassword = "123456";
    var outputPdf = "54566_out.pdf";
    using (var sign = new PdfFileSignature())
    {
        sign.BindPdf(inputPdf);
        var pkcs7 = new PKCS7(inputP12, inputPfxPassword);
        pkcs7.CustomSignHash = CustomSignHash;
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        sign.Save(outputPdf);
    }
    using (var sign = new PdfFileSignature())
    {
        sign.BindPdf(outputPdf);
        if (!sign.VerifySignature("Signature1"))
        {
            throw new Exception("Not verified");
        }
    }
}

private byte[] CustomSignHash(byte[] signableHash)
{
    var inputP12 = "54566.p12";
    var inputPfxPassword = "123456";
    X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
    RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
    var xmlString = signerCert.PrivateKey.ToXmlString(true);
    rsaCSP.FromXmlString(xmlString);
    byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
    return signedData;
}
```

One more new feature is Print Dialog Presets Page Scaling:

```cs
Document document = new Document();
document.Pages.Add();
document.PrintScaling = PrintScaling.None;
document.Save("output.pdf");
```

## What's new in Aspose.PDF 23.9

Since 23.9 support to remove a child annotation from a fillable field.

```cs
var document = new Document("field-ref-add.pdf");
field = (Field)document.Form[fieldName];
var annotation = field[1];
document.Pages[annotation .PageIndex].Annotations.Remove(annotation);
document.Save("field-ref-delete.pdf");
```

## What's new in Aspose.PDF 23.8

Since 23.8 support to add Incremental Updates detection.

The function for detecting Incremental Updates in a PDF document has been added. This function returns 'true' if a document was saved with incremental updates; otherwise, it returns 'false'.

```cs
var path = @"C:\test.pdf";
var document = new Document(path);
Console.WriteLine(document.HasIncrementalUpdate());
```

Also, 23.8 supports the ways to work with nested checkbox fields. Many fillable PDF forms have checkbox fields that act as radio groups:

- Create multi-value checkbox field:

```cs
using (var document = new Document())
{
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Set the first checkbox group option value
    checkbox.ExportValue = "option 1";

    // Add new option right under existing ones
    checkbox.AddOption("option 2");

    // Add new option at the given rectangle
    checkbox.AddOption("option 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // Select the added checkbox
    checkbox.Value = "option 2";
    document.Save("checkbox_group.pdf");
}
```

- Get and set value of a multi-value checkbox:

```cs
using (Document document = new Document("example.pdf"))
{
    Form form = document.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // Allowed values may be retrieved from the AllowedStates collection
    // Set the checkbox value using Value property
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // the previously set value, e.g. "option 1"

    // The value should be any element of AllowedStates
    checkbox.Value = "option 2";
    checkboxValue = checkbox.Value; // option 2

    // Uncheck boxes by either setting Value to "Off" or setting Checked to false
    checkbox.Value = "Off";
    // or, alternately:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
}
```

## What's new in Aspose.PDF 23.7

From Aspose.PDF 23.7 support to add the shape extraction:

```cs
public void PDFNET_46298()
{
    var input1 = "46298_1.pdf";
    var input2 = "46298_2.pdf";

    var source = new Document(input1);
    var dest = new Document(input2);

    var graphicAbsorber = new GraphicsAbsorber();
    graphicAbsorber.Visit(source.Pages[1]);
    var area = new Rectangle(90, 250, 300, 400);
    dest.Pages[1].AddGraphics(graphicAbsorber.Elements, area);
}
```

Also supports the ability to detect Overflow when adding text:

```cs
var document = new Document();
var paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
var rectangle = new Rectangle(100, 600, 500, 700, false);
var paragraph = new TextParagraph();
var fragment = new TextFragment(paragraphContent);
paragraph.VerticalAlignment = VerticalAlignment.Top;
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
paragraph.Rectangle = rectangle;
var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
while (!isFitRectangle)
{
    fragment.TextState.FontSize -= 0.5f;
    isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
}
paragraph.AppendLine(fragment);
TextBuilder builder = new TextBuilder(document.Pages.Add());
builder.AppendParagraph(paragraph);
document.Save(output);
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
var document = new Document(Params.InputPath + "53357.pdf");

var htmlSaveOptions = new HtmlSaveOptions
{
    ExplicitListOfSavedPages = new[] { 1 },
    SplitIntoPages = false,
    FixedLayout = true,
    CompressSvgGraphicsIfAny = false,
    SaveTransparentTexts = true,
    SaveShadowedTextsAsTransparentTexts = true,
    FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
    RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
    PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
    Title = "Title for page" // new Property
};

document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```

## What's new in Aspose.PDF 23.5

Since 23.5 support to add RedactionAnnotation FontSize option. Use the next code snippet to solve this task:

```cs
Document document = new Document(dataDir + "test_factuur.pdf");

// Create RedactionAnnotation instance for specific page region
RedactionAnnotation annot = new RedactionAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
annot.FillColor = Aspose.Pdf.Color.Black;

annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Text to be printed on redact annotation
annot.OverlayText = "(Unknown)";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Repat Overlay text over redact Annotation
annot.Repeat = false;
// New property there !
annot.FontSize = 20;
// Add annotation to annotations collection of first page
document.Pages[1].Annotations.Add(annot);
// Flattens annotation and redacts page contents (i.e. removes text and image
// Under redacted annotation)
annot.Redact();
// Save result document
document.Save(dataDir + "47704_RedactPage_out_NETCORE.pdf");
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

Version 23.3 introduced support for adding a resolution to an image. Two methods can be used to solve this problem:

```cs
var table = new Table
{
    ColumnWidths = "600"
};

for(var j = 0; j < 2; j ++)
{
    var row = table.Rows.Add();
    var cell = row.Cells.Add();
    cell.Paragraphs.Add(new Image()
    {
        IsApplyResolution = true,
        File = imageFile
    });
}

page.Paragraphs.Add(table);
```

And the second approach:

```cs
page.Paragraphs.Add(new Image()
{
    IsApplyResolution = true,
    File = imageFile
});
page.Paragraphs.Add(new Image()
{
    IsApplyResolution = true,
    File = imageFile
});
```

The image will be placed with scaled resolution or u can set FixedWidth or FixedHeight properties in combination with IsApplyResolution

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

var outFile = myDir + "ColorBarTest.pdf");

using (var document = new Document())
{
    Page page = document.Pages.Add();
    page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);
    AddAnnotations(page);
    document.Save(outFile);
}

void AddAnnotations(Page page)
{
    var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
    var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
    var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

    var colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    var colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    var colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.ColorOfCMYK = ColorsOfCMYK.Magenta;
    var colorBarYellow = new ColorBarAnnotation(page, new Aspose.Pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.Annotations.Add(colorBarBlack);
    page.Annotations.Add(colorBarCyan);
    page.Annotations.Add(colorBaMagenta);
    page.Annotations.Add(colorBarYellow);
}
```
Also support the vector images extraction. Try using the following code to detect and extract vector graphics:

```cs
var document = new Document(input);
try 
{
    document.Pages[1].TrySaveVectorGraphics(outputSvg);
}
catch (Exception)
{
}
```

## What's new in Aspose.PDF 22.12

From this release support to convert PDF to DICOM Image

```cs
Document document = new Document("source.pdf");
DicomDevice dicom = new DicomDevice();
FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
dicom.Process(document.Pages[1], outStream);
```    

## What's new in Aspose.PDF 22.09

Since 22.09 support adding property for modify the order of the subject rubrics (E=, CN=, O=, OU=, ) into the signature.

```cs
using (var fileSign = new PdfFileSignature())
{
    fileSign.BindPdf(inputPdf);
    var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
    var signature = new PKCS7Detached(inputPfx, "123456789");
    signature.CustomAppearance = new SignatureCustomAppearance()
    {
        UseDigitalSubjectFormat = true,
        DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.CN, SubjectNameElements.O }
        //or
        //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
    };
    fileSign.Sign(1, true, rect, signature);
    fileSign.Save(outputPdf);
}
```

## What's new in Aspose.PDF 22.6

Since 22.5 support to extract SubScript and SuperScript text from PDF.

If the PDF document contains SubScript and SuperScript text such as H2O, then extracting the text from the PDF must also extract their formatting information (in the extracted plain text).
If the PDF contains text in italics, it must also be included in the extracted content.

```cs
Document document = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(document.Pages[1]);
```

## What's new in Aspose.PDF 22.4

This release includes information for Aspose.PDF for .NET:

- PDF to ODS: Recognize text in subscript and superscript;

**example**

```cs
Document document = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
document.Save("output.ods"), options);
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
Example of using:
var inputPdf = "51168.pdf";
var inputPfx = "51168.pfx";
var inputPfxPassword = "111111";
var outputPdf = "51168.pdf";

using (var document = new Document(inputPdf))
{
    using (PdfFileSignature signature = new PdfFileSignature(document))
    {
        var pkcs = new PKCS7(inputPfx, inputPfxPassword)
        {
            UseLtv = true,
            TimestampSettings = new TimestampSettings("http://freetsa.org/tsr", string.Empty, DigestHashAlgorithm.Sha256)
        };
        signature.Sign(1, false, new System.Drawing.Rectangle(300, 100, 1, 1), pkcs);
        signature.Save(outputPdf);
    }
}
```

## What's new in Aspose.PDF 22.1

Now, Aspose.PDF for .NET supports loading documents from one of the most popular document formats, Portable Document Format (PDF) version 2.0.

## What's new in Aspose.PDF 21.11

### Allow non-latin characters in password

```csharp
Aspose.Pdf.Facades.PdfFileSecurity fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity();
fileSecurity.AllowExceptions = true;
try
{
    fileSecurity.BindPdf(exportDoc);
    bool res = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
    Console.WriteLine(res);
    fileSecurity.Save(output("encrypted.pdf"));
}
catch (Exception e)
{
    Console.WriteLn("Exception: " + e.Message);
}
```

## What's new in Aspose.PDF 21.10

### How to detect hidden text?

Please use TextState.Invisible to get information about invisibility of text out of rendering mode setting.

We used the following code for testing:

```csharp
Document pdf = new Document(dataDir + "TestPage.pdf");
Console.WriteLine(pdf.FileName);
var page = pdf.Pages[1];
var textFragmentAbsorber = new TextFragmentAbsorber();
page.Accept(textFragmentAbsorber);
var textFragmentCollection = textFragmentAbsorber.TextFragments;
for (int i = 1; i <= textFragmentCollection.Count; i++)
{
    TextFragment fragment = textFragmentCollection[i];
    Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
    Console.WriteLine("Text: {0}", fragment.Text);
    Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
    Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
    Console.WriteLine("---");
}
```

### How do get information about the number of layers in a PDF document?

```csharp
Please use code snippet:
var inFile = "1234.pdf";
Document document = new Document(inFile);
List layers = document.Pages[1].Layers;
```

## What's new in Aspose.PDF 21.9

Customize background color for signature appearance and the font color of the labels in the signature area with Aspose.PDF for .NET.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {
        // Set colors
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## What's new in Aspose.PDF 21.8

### How to change text color in Digital Signature?

In the 21.8 version  ForegroundColor property, it allows changing text color in Digital Signature.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    // Create a rectangle for signature location
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {
        // Set text color
        ForegroundColor = Color.Green
    };
    // Sign the PDF file
    pdfSign.Sign(1, true, rect, pkcs);
    // Save PDF document
    pdfSign.Save(outFile);
}
```

## What's new in Aspose.PDF 21.7

### PDF creation based on XML and XLS with parameters

To add XSL params we need to create own [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) and set as property in [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). The following snippet shows how to use this class with the sample files described above.

```csharp
public static void Example_XSLFO_to_PDF()
{
    var XmlContent = File.ReadAllText(dataDir + "employees.xml");
    var XsltContent = File.ReadAllText(dataDir + "employees.xslt");

    var options = new Aspose.Pdf.XslFoLoadOptions();

    // Example of using XsltArgumentList
        XsltArgumentList argsList = new XsltArgumentList();
    argsList.AddParam("isBoldName", "", "yes");

    var document = new Document(TransformXml(XmlContent, XsltContent, argsList), options);
    document.Save(dataDir + "data_xml.pdf");
}

public static MemoryStream TransformXml(string inputXml, string xsltString, XsltArgumentList argsList=null)
{
    var transform = new XslCompiledTransform();
    using (var reader = XmlReader.Create(new StringReader(xsltString)))
    {
        transform.Load(reader);
    }
    var memoryStream = new MemoryStream();

    var results = new StreamWriter(memoryStream);
    using (var reader = XmlReader.Create(new StringReader(inputXml)))
    {
        transform.Transform(reader, argsList, results);
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```

## What's new in Aspose.PDF 21.6

With Aspose.PDF for .NET you can hide images using ImagePlacementAbsorber from the document:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document document = new Document("test.pdf");
   // Hide image on first page
   document.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   document.Save("test_out.pdf");
}
```

## What's new in Aspose.PDF 21.5

### How to extract font full name from it description/resource at PDF?

You can get a full font with the prefix with  BaseFont property for the Font class.

```csharp
using (Document document = new Document(dataDir + @"testfont.pdf"))
{
    Font[] fonts = pdf.FontUtilities.GetAllFonts();
    foreach (Font font in fonts)
    {
        Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
    }
}
```

## What's new in Aspose.PDF 21.4

### Add API for merging images

Aspose.PDF 21.4 allows you to combine Images. Follow the next code snippet:

```csharp
private static void MergeAsJpeg()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.jpg", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\49616_600.jpg", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream =
                 PdfConverter.MergeImages(inputImagesStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.jpg", FileMode.Create))
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
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.tiff", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\600.tiff", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream = PdfConverter.MergeImagesAsTiff(inputImagesStreams))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.tiff", FileMode.Create))
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
 public void Azure_Information_Protection()
 {
     string inputFile = @"c:\pdf.pdf";
     Document document = new Document(inputFile);
     if (document.EmbeddedFiles[1].AFRelationship == AFRelationship.EncryptedPayload)
     {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
              // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
              // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
              // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
     }
}
```

## What's new in Aspose.PDF 21.1

### Add support of retrieving the background color of TextFragment

In this version of Aspose.PDF, the function became available to retrieve the background color. You need to specify searchOptions.SearchForTextRelatedGraphics = true; in the options of TextFragmentAbsorber object.

Please consider the following code:

```csharp
Document document = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Accept the absorber for all the pages
document.Pages.Accept(textFragmentAbsorber);

// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text: '{0}'", textFragment.Text);
    Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```

### After conversion to HTML the font is fully embedded in the output

Also, in Aspose.PDF 21.1, after converting PDF to HTML, became available embedded fonts in an output HTML document. It is possible with the new boolean save option HtmlSaveParameter.SaveFullFont.

Here is the code snippet:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
