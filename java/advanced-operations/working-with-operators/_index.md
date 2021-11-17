---
title: Working with Operators
linktitle: Working with Operators
type: docs
weight: 170
url: /java/operators/
description: This topic explains how to use operators with Aspose.PDF. The operator classes provide great features for PDF manipulation.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Implementation Details

This topic explains how to use operators with Aspose.PDF. The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), and [GRestore](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- The [GSave](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) operator saves the PDF’s current graphical state.
- The This topic explains how to use operators with Aspose.PDF. The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), and [GRestore](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).
 (concatenate matrix) operator is used to define how an image should be placed on the PDF page.
- The [Do](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) operator draws the image on the page.
- The [GRestore](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) operator restores the graphical state.

To add an image into a PDF file:

1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object and open the input PDF document.
1. Get the particular page the image is going to be added to.
1. Add the image into the page’s Resources collection.
1. Use the operators to place the image on the page:
   - First, use the [GSave](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) operator to save the current graphical state.
   - Then use the [ConcatenateMatrix](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) operator to specify where the image is to be placed.
   - Use the [Do](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) operator to draw the image on the page.
1. Finally, use [GRestore](https://apireference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) operator to save the updated graphical state.

The following code snippet shows how to use PDF operators.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // Create a new PDF document
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // Get the page where image needs to be added
        Page page = pdfDocument.getPages().get_Item(1);

        // Set coordinates
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Load image into stream
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // Add image to Images collection of Page Resources
        page.getResources().getImages().add(imageStream);

        // Using GSave operator: this operator saves current graphics state
        page.getContents().add(new GSave());
        // Create Rectangle and Matrix objects
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must
        // be placed
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Using Do operator: this operator draws image
        page.getContents().add(new Do(ximage.getName()));
        // Using GRestore operator: this operator restores graphics state
        page.getContents().add(new GRestore());

        // Save updated document
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```

## Draw XForm on Page using Operators

This topic demonstrates how to use the GSave/GRestore operators, the ContatenateMatrix operator to position an xForm and the Do operator to draw an xForm on a page.

The code below wraps a PDF file’s existing contents with the GSave/GRestore operator pair. This approach helps get the initial graphics state at the and of the existing contents. Without this approach, undesirable transformations might remain at the end of the existing operator chain.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // The sample demonstrates
        // GSave/GRestore operators usage
        // ContatenateMatrix operator usage to position xForm
        // Do operator usage to draw xForm on page

        // Wrap existing contents with GSave/GRestore operators pair
        // this is to get initial graphics state at the and of existing contents
        // otherwise there might remain some undesirable transformations at the end of
        // existing operators chain
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // Add save graphics state operator to properly clear graphics state after
        // new commands
        pageContents.add(new GSave());

        // Create xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // Define image width and height
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // Add image to Images collection of the XForm Resources
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Using Do operator: this operator draws image
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // Place form to the x=100 y=500 coordinates
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Draw form with Do operator
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // Place form to the x=100 y=300 coordinates
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Draw form with Do operator
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // Restore grahics state with GRestore after the GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```

## Remove Graphics Objects using Operator Classes

The operator classes provide great features for PDF manipulation. When a PDF file contains graphics that cannot be removed using the [PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class’ [DeleteImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) method, the operator classes can be used to remove them instead.

The following code snippet shows how to remove graphics. Please note that if the PDF file contains text labels for the graphics, they might persist in the PDF file, using this approach. Therefore search the graphic operators for an alternate method to delete such images.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();
        
        // Used path-painting operators
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };
        
        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");                
    }
```
