---
title: Compare PDF documents
linktitle: Compare PDF 
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Since 25.2 release it's possible to compare PDF documents content with annotation marks and side-by-side output
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


## Ways to compare PDF Documents

When working with PDF documents, there are times when you need to compare the content of two documents to identify differences. The Aspose.PDF for .NET library provides a powerful toolset for this purpose. In this article, we'll explore how to compare PDF documents using a couple of simple code snippets.

The comparison functionality in Aspose.PDF allows you to compare two PDF documents page by page. You can choose to compare either specific pages or entire documents. The resulting comparison document highlights differences, making it easier to identify changes between the two files.

Here is a list of possible ways to compare PDF documents using Aspose.PDF for  .NET library:

1. **Comparing Specific Pages** - Compare the first pages of two PDF documents.

1. **Comparing Entire Documents** - Compare the entire content of two PDF documents.

1. **Compare PDF documents graphically**:

- Compare PDF with GetDifference method - individual images where changes are marked.

- Compare PDF with CompareDocumentsToPdf method - PDF document with images where changes are marked.

## Comparing Specific Pages

The first code snippet demonstrates how to compare the first pages of two PDF documents.

Steps:

1. Document Initialization.
The code starts by initializing two PDF documents using their respective file paths (documentPath1 and documentPath2). The paths are specified as empty strings for now, but in practice, you would replace these with the actual file paths.

2. Comparison Process.

- Page Selection - the comparison is limited to the first page of each document ('getPages().get_Item(1)').
- Comparison Options:

'setAdditionalChangeMarks(true)'- this option ensures that additional change markers are displayed. These markers highlight differences that might be present on other pages, even if they are not on the current page being compared.

'setComparisonMode(ComparisonMode.IgnoreSpaces)' - this mode tells the comparer to ignore spaces in the text, focusing only on changes within words.

3. The resulting comparison document, which highlights the differences between the two pages, is saved to the file path specified in 'resultPdfPath'.

```java

    private static void ComparingSpecificPages() {
        // The path to the documents directory
        String dataDir = "C:\\test\\";

        // Open PDF documents
        Document document1 = new Document(dataDir + "ComparingSpecificPages1.pdf");
        Document document2 = new Document(dataDir + "ComparingSpecificPages2.pdf");

        com.aspose.pdf.comparison.sidebysidecomparison.SideBySideComparisonOptions options = new com.aspose.pdf.comparison.sidebysidecomparison.SideBySideComparisonOptions();

        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(com.aspose.pdf.comparison.sidebysidecomparison.ComparisonMode.IgnoreSpaces);
        com.aspose.pdf.comparison.sidebysidecomparison.SideBySidePdfComparer.compare(
                document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                dataDir + "ComparingSpecificPages_out.pdf", options);
        document1.close();
        document2.close();
    }
```

## Comparing Entire Documents

The second code snippet expands the scope to compare the entire content of two PDF documents.

Steps:

1. Document Initialization.
Just like in the first example, two PDF documents are initialized with their file paths.

2. Comparison Process.

- Entire Document Comparison - unlike the first snippet, this code compares the entire content of the two documents.

- Comparison Options - the options are the same as in the first snippet, ensuring that spaces are ignored, and additional change markers are displayed.

3. The comparison result, which highlights differences across all pages of the two documents, is saved in the file specified by 'resultPdfPath'.

```java

    private static void ComparingEntireDocuments()
    {
        // The path to the documents directory
        String dataDir = "C:\\test\\";

        // Open PDF documents
        Document document1 = new Document(dataDir + "ComparingSpecificPages1.pdf");
        Document document2 = new Document(dataDir + "ComparingSpecificPages2.pdf");

        com.aspose.pdf.comparison.sidebysidecomparison.SideBySideComparisonOptions options = new com.aspose.pdf.comparison.sidebysidecomparison.SideBySideComparisonOptions();

        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(com.aspose.pdf.comparison.sidebysidecomparison.ComparisonMode.IgnoreSpaces);
        com.aspose.pdf.comparison.sidebysidecomparison.SideBySidePdfComparer.compare(
                document1, document2,
                dataDir + "ComparingSpecificPages_out.pdf", options);
        document1.close();
        document2.close();
    }

```

The comparison results generated by these snippets are PDF documents that you can open in a viewer like Adobe Acrobat. If you use the Two-page view in Adobe Acrobat, you'll see the changes side by side:

- Deletions - these are noted on the left page.
- Insertions - these are noted on the right page.

By setting 'AdditionalChangeMarks' to 'true', you can also see markers for changes that may occur on other pages, even if those changes aren't on the current page being viewed.

**Aspose.PDF for Java** provides robust tools for comparing PDF documents, whether you need to compare specific pages or entire documents. By using options like 'AdditionalChangeMarks' and different 'ComparisonMode settings', you can tailor the comparison process to your specific needs. The resulting document provides a clear, side-by-side view of changes, making it easier to track revisions and ensure document accuracy.

## Compare PDF documents using GraphicalPdfComparer

When collaborating on documents, especially in professional environments, you often end up with multiple versions of the same file.

You can use the [GraphicalPdfComparer] class to compare PDF documents and pages. The class is suitable for comparing changes in a page's graphic content.

With Aspose.PDF for Java, it's possible to compare documents and pages and output the comparison result to a PDF document or image file.

You can set the following class properties:

- Resolution - resolution in DPI units for output images, as well as for images generated during the comparison.
- Color - the color of change marks.
- Threshold - change threshold in percent. The default value is zero. Setting a value other than zero allows you to ignore graphic changes that are insignificant to you.

The class has a method that allows you to get page image differences in a form suitable for further processing: **ImagesDifference GetDifference(Page page1, Page page2)**.

This method returns an object of the [ImagesDifference] class, which contains an image of the first page being compared and an array of differences. The array of differences and the original image has the **RGB24bpp** pixel format.

ImagesDifference allows you to generate a different image and get an image of the second page being compared by adding an array of differences to the original image. To do this, use the **ImagesDifference.getDestinationImage() and ImagesDifference.differenceToImage()** methods.

### Compare PDF with GetDifference method

The provided code defines a method [GetDifference] that compares two PDF documents and generates visual representations of the differences between them.

This method compares the first pages of two PDF files and generates two PNG images:

- One image (diffPngFilePath) highlights the differences between the pages in red.
- The other image (destPngFilePath) is a visual representation of the destination (second) PDF page.

This process can be useful for visually comparing changes or differences between two versions of a document.

```java

    private static void ComparePDFWithGetDifferenceMethod() throws IOException {
        // The path to the documents directory
        String dataDir = "C:\\test\\";


        Document document1 = new Document(dataDir + "ComparingSpecificPages1.pdf");
        Document document2 = new Document(dataDir + "ComparingSpecificPages2.pdf");
        // Create comparer
        com.aspose.pdf.comparison.graphicalcomparison.GraphicalPdfComparer comparer =
                new com.aspose.pdf.comparison.graphicalcomparison.GraphicalPdfComparer();

        // Compare
        com.aspose.pdf.comparison.graphicalcomparison.ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1), document2.getPages().get_Item(1));
        java.awt.image.BufferedImage diffImg = imagesDifference.differenceToImage(Color.getRed(), Color.getWhite());
        // Specify the output file
        File outputFile = new File(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
        // Save the image as a PNG file
        ImageIO.write(diffImg, "png", outputFile);

        java.awt.image.BufferedImage destImg = imagesDifference.getDestinationImage();
        //Specify the output DestinationImage file
        File destOutputFile = new File(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
        // Save the image as a PNG file
        ImageIO.write(destImg, "png", destOutputFile);
    }
```

### Compare PDF with CompareDocumentsToPdf method

The provided code snippet used the  [CompareDocumentsToPdf] method, which compares two documents and generates a PDF report of the comparison results.

```java

private static void ComparePDFWithCompareDocumentsToPdfMethod() {
        // The path to the documents directory
        String dataDir = "C:\\test\\";


        Document document1 = new Document(dataDir + "ComparingSpecificPages1.pdf");
        Document document2 = new Document(dataDir + "ComparingSpecificPages2.pdf");

        // Create comparer
        com.aspose.pdf.comparison.graphicalcomparison.GraphicalPdfComparer comparer =
                new com.aspose.pdf.comparison.graphicalcomparison.GraphicalPdfComparer();

        comparer.setThreshold(3.0);
        comparer.setColor(Color.getBlue());
        comparer.setResolution(new com.aspose.pdf.devices.Resolution(300));

        // Compare
        comparer.compareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
    }
```