---
title: Add Free text Annotation
type: docs
weight: 30
url: /net/add-free-text-annotation/
---
# Add Free text Annotation

## Set Callout Property for FreeTextAnnotation
For a more flexible configuration of annotation in the PDF document, Aspose.PDF for .NET provides Callout property of FreeTextAnnotation class which allows specifying Array of point of callout line. The following code snippet show, how to use this functionality:
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
```
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
```
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
```
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
