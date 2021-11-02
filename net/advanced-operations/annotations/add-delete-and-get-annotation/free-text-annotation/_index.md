---
title: PDF Free Text Annotation using C#
linktitle: Free Text Annotation
type: docs
weight: 30
url: /net/free-text-annotation/
description: This article teaches how to add Free Text Annotation to PDF in C# using Aspose.PDF for .NET. Learn more about how to set Callout for such annotation.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add New (or Create) Free Text Annotation

A free text annotation displays text directly on the page. The [PdfContentEditor.CreateFreeText](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method allows creating this type of annotation. In the following snippet, we add free text annotation above the first occurrence of the string.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);
   
    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

## Set Callout Property for FreeTextAnnotation

For a more flexible configuration of annotation in the PDF document, Aspose.PDF for .NET provides [Callout](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) property of [FreeTextAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) class which allows specifying Array of point of callout line. The following code snippet show, how to use this functionality:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```

## Set Callout Property for XFDF File

If you use import from XFDF file please use callout-line name instead just Callout. The following code snippet shows, how to use this functionality:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document( dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

The following method is being used to CreateXfdf:

```csharp
/// <summary>
/// Create XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

## Invisible Annotation

Sometimes, it is necessary to create a watermark that isn’t visible in the document when viewing it but should be visible when the document is printed. Use annotation flags for this purpose. The following code snippet shows how.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Save output file
doc.Save(dataDir);
```

## Set Formatting of FreeTextAnnotation

This part looks at how to format the text in a free text annotation.

Annotations are contained in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object's [AnnotationCollection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. When adding a [FreeTextAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) to a PDF document, you can specify the formatting information such as font, size, color and so on using the [DefaultAppearance](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index) class. It is also possible to specify the formatting information using the TextStyle property. Furthermore, you can update the formatting of any FreeTextAnnotation already in the PDF document.

The [TextStyle](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) class supports working with the default style entry. This class allows you to set color, font size and font name:

- The FontName property gets or sets the font name (string).
- The FontSize property gets and sets the default text size (double).
- The System.Drawing.Color property gets and sets the text colour (color).
- The TextAlignment property gets and sets the annotation's text alignment (alignment).

The following code snippet shows how to add a FreeTextAnnotation with specific text formatting.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

When you change the contents or text style of a free text annotation, the annotation's appearance is regenerated to reflect changes.

{{% /alert %}}

## Strike Out Words using StrikeOutAnnotation

Aspose.PDF for .NET allows you to add, delete and update annotations in PDF documents. One of the classes allows you to strike out annotations too. This is useful when you want to strike out one or more text fragments in a documect. Annotations are held in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object's [AnnotationCollection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. A class named [StrikeOutAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) can be used to add strike out annotations to a PDF document.

To strike out a certain TextFragment:

1. Search for a TextFragment in the PDF file.
1. Get the TextFragment object's coordinates.
1. Use the coordinates to instantiate a StrikeOutAnnotation object.

The following code snippet shows how to search for a particular TextFragment and add a StrikeOutAnnotation to that object.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

This feature is supported by version 19.6 or greater.

{{% /alert %}}