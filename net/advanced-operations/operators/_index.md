---
title: Working with Operators
linktitle: Working with Operators
type: docs
weight: 170
url: /net/operators/
description: This topic explains how to use operators with Aspose.PDF. The operator classes provide great features for PDF manipulation.
aliases:
    - /net/working-with-operators/
    - /net/operator/
lastmod: "2020-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Implementation Details

This topic explains how to use operators with Aspose.PDF. The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://apireference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/28), [ConcatenateMatrix](https://apireference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/10), [Do](https://apireference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/14), and [GRestore](https://apireference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/26).

- The **GSave** operator saves the PDF’s current graphical state.
- The **ConcatenateMatrix** (concatenate matrix) operator is used to define how an image should be placed on the PDF page.
- The **Do** operator draws the image on the page.
- The **GRestore** operator restores the graphical state.

To add an image into a PDF file:

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object and open the input PDF document.
1. Get the particular page the image is going to be added to.
1. Add the image into the page’s Resources collection.
1. Use the operators to place the image on the page:
   - First, use the GSave operator to save the current graphical state.
   - Then use the ConcatenateMatrix operator to specify where the image is to be placed.
   - Use the Do operator to draw the image on the page.
1. Finally, use GRestore operator to save the updated graphical state.

The following code snippet shows how to use PDF operators.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// Open document
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// Set coordinates
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Get the page where image needs to be added
Page page = pdfDocument.Pages[1];
// Load image into stream
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// Add image to Images collection of Page Resources
page.Resources.Images.Add(imageStream);
// Using GSave operator: this operator saves current graphics state
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Create Rectangle and Matrix objects
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Using Do operator: this operator draws image
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Using GRestore operator: this operator restores graphics state
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

## Draw XForm on Page using Operators

This topic demonstrates how to use the GSave/GRestore operators, the ContatenateMatrix operator to position an xForm and the Do operator to draw an xForm on a page.

The code below wraps a PDF file’s existing contents with the GSave/GRestore operator pair. This approach helps get the initial graphics state at the and of the existing contents. Without this approach, undesirable transformations might remain at the end of the existing operator chain.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // The sample demonstrates
    // GSave/GRestore operators usage
    // ContatenateMatrix operator usage to position xForm
    // Do operator usage to draw xForm on page

    // Wrap existing contents with GSave/GRestore operators pair
    //        this is to get initial graphics state at the and of existing contents
    //        otherwise there might remain some undesirable transformations at the end of existing operators chain
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Add save graphics state operator to properly clear graphics state after new commands
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region create xForm

    // Create xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // Define image width and heigh
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // Load image into stream
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // Add image to Images collection of the XForm Resources
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Using Do operator: this operator draws image
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Place form to the x=100 y=500 coordinates
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Draw form with Do operator
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Place form to the x=100 y=300 coordinates
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Draw form with Do operator
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Restore grahics state with GRestore after the GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```

## Remove Graphics Objects using Operator Classes

The operator classes provide great features for PDF manipulation. When a PDF file contains graphics that cannot be removed using the [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class’ [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) method, the operator classes can be used to remove them instead.

The following code snippet shows how to remove graphics. Please note that if the PDF file contains text labels for the graphics, they might persist in the PDF file, using this approach. Therefore search the graphic operators for an alternate method to delete such images.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// Used path-painting operators
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
```
