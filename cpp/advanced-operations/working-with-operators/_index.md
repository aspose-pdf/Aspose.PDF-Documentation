---
title: Working with Operators using C++
linktitle: Working with Operators
type: docs
weight: 170
url: /cpp/operators/
description: This topic explains how to use operators with Aspose.PDF in C++. The operator classes provide great features for PDF manipulation.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Implementation Details

This topic explains how to use operators with Aspose.PDF. The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do), and [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- The **GSave** operator saves the PDF’s current graphical state.
- The **ConcatenateMatrix** (concatenate matrix) operator is used to define how an image should be placed on the PDF page.
- The **Do** operator draws the image on the page.
- The **GRestore** operator restores the graphical state.

To add an image into a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) object and open the input PDF document.
1. Get the particular page the image is going to be added to.
1. Add the image into the page’s Resources collection.
1. Use the operators to place the image on the page:
   - First, use the GSave operator to save the current graphical state.
   - Then use the ConcatenateMatrix operator to specify where the image is to be placed.
   - Use the Do operator to draw the image on the page.
1. Finally, use GRestore operator to save the updated graphical state.

The following code snippet shows how to use PDF operators.

```cpp
void ExampleUsingOperators()
{
    // Open document
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // Set coordinates
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // Get the page where image needs to be added
    auto page = document->get_Pages()->idx_get(1);

    // Load image into stream
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // Add image to Images collection of Page Resources
    page->get_Resources()->get_Images()->Add(imageStream);

    // Using GSave operator: this operator saves current graphics state
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Create Rectangle and Matrix objects
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Using Do operator: this operator draws image
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // Using GRestore operator: this operator restores graphics state
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // Save updated document
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```

## Draw XForm on Page using Operators

This topic demonstrates how to use the GSave/GRestore operators, the ContatenateMatrix operator to position an xForm and the Do operator to draw an xForm on a page.

The code below wraps a PDF file’s existing contents with the GSave/GRestore operator pair. This approach helps get the initial graphics state at the and of the existing contents. Without this approach, undesirable transformations might remain at the end of the existing operator chain.

```cpp
void DrawXFormOnPageUsingOperators() {
    // Open document
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // The sample demonstrates
    // GSave/GRestore operators usage
    // ContatenateMatrix operator usage to position xForm
    // Do operator usage to draw xForm on page

    // Wrap existing contents with GSave/GRestore operators pair
    //        this is to get initial graphics state at the and of existing contents
    //        otherwise there might remain some undesirable transformations at the end of existing operators chain
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Add save graphics state operator to properly clear graphics state after new commands
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Create xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Define image width and heigh
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // Load image into stream
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // Add image to Images collection of the XForm Resources
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Using Do operator: this operator draws image
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Place form to the x=100 y=500 coordinates
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Draw form with Do operator
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Place form to the x=100 y=300 coordinates
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Draw form with Do operator
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Restore grahics state with GRestore after the GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## Remove Graphics Objects using Operator Classes

The operator classes provide great features for PDF manipulation. When a PDF file contains graphics that cannot be removed using the [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor) class' [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) method, the operator classes can be used to remove them instead.

The following code snippet shows how to remove graphics. Please note that if the PDF file contains text labels for the graphics, they might persist in the PDF file, using this approach. Therefore search the graphic operators for an alternate method to delete such images.

```cpp
void RemoveGraphicsObjects() {
    // Open document
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // Used path-painting operators
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```
