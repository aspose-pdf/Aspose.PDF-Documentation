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
lastmod: "2021-12-24"
---

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

using (var doc = new Document(inputPdf))
{
    using (PdfFileSignature signature = new PdfFileSignature(doc))
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
    catch(Exception e)
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
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
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
    {//set colors
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
    //create a rectangle for signature location
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//set text color
        ForegroundColor = Color.Green
    };
    // sign the PDF file
    pdfSign.Sign(1, true, rect, pkcs);
    //save output PDF file
    pdfSign.Save(outFile);
}
```

## What's new in Aspose.PDF 21.7

### PDF creation based on XML and XLS with parameters

To add XSL params we need to create own [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) and set as property in [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). The following snippet shows how to use this class with the sample files described above.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //Example of using XsltArgumentList
         XsltArgumentList argsList = new XsltArgumentList();
        argsList.AddParam("isBoldName", "", "yes");
        //---------------------

        var pdfDocument = new Aspose.Pdf.Document(TransformXml(XmlContent, XsltContent, argsList), options);
        pdfDocument.Save(_dataDir + "data_xml.pdf");
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
   Document doc = new Document("test.pdf");
   // Hide image on first page
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## What's new in Aspose.PDF 21.5

### How to extract font full name from it description/resource at PDF?

You can get a full font with the prefix with  BaseFont property for the Font class.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
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
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

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
