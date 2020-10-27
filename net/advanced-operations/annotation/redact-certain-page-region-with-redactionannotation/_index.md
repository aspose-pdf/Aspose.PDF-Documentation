---
title: Redact certain page region with RedactionAnnotation
type: docs
weight: 20
url: /net/redact-certain-page-region-with-redactionannotation/
---
# Redact certain page region with RedactionAnnotation
Aspose.PDF for .NET supports the feature to add as well as manipulate Annotations in an existing PDF file. Recently some of our customers posted a required to redact (remove text, image, etc elements from) a certain page region of PDF document. In order to fulfill this requirement, a class named RedactionAnnotation is provided, which can be used to redact certain page regions or it can be used to manipulate existing RedactionAnnotations and redact them (i.e. flatten annotation and remove the text under it).
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document doc = new Document(dataDir + "input.pdf");

// Create RedactionAnnotation instance for specific page region
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Text to be printed on redact annotation
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Repat Overlay text over redact Annotation
annot.Repeat = true;
// Add annotation to annotations collection of first page
doc.Pages[1].Annotations.Add(annot);
// Flattens annotation and redacts page contents (i.e. removes text and image
// Under redacted annotation)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
## Facades approach
Aspose.PDF.Facades namespace also has a class named *PdfAnnotationEditor* which provides the feature to manipulate existing Annotations inside PDF file. This class contains a method named *RedactArea(..)* which provides the capability to remove certain page regions.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// Redact certain page region
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save( dataDir + "FacadesApproach_out.pdf");
```
