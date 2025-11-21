---
title: Compare PDF documents
linktitle: Compare PDF 
type: docs
weight: 130
url: /python-net/compare-pdf-documents/
description: It's possible to compare PDF documents content with annotation marks and side-by-side output.
lastmod: "2025-05-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract:   
---

## Ways to Compare PDF Documents

When working with PDF documents, there are times when you need to compare the content of two documents to identify differences. The Aspose.PDF for Python via .NET library provides a powerful toolset for this purpose. In this article, we'll explore how to compare PDF documents using a couple of simple code snippets.

The comparison functionality in Aspose.PDF allows you to compare two PDF documents page by page. You can choose to compare either specific pages or entire documents. The resulting comparison document highlights differences, making it easier to identify changes between the two files.

Here is a list of possible ways to compare PDF documents using Aspose.PDF for Python via .NET library:

1. **Comparing Specific Pages** - Compare the first pages of two PDF documents.
1. **Comparing Entire Documents** - Compare the entire content of two PDF documents.
1. **Compare PDF documents graphically**:

- Compare PDF with 'comparer.get_difference' method - individual images where changes are marked.
- Compare PDF with 'comparer.compare_documents_to_pdf' method - PDF document with images where changes are marked.

## Comparing Specific Pages

The first code snippet demonstrates how to compare the first pages of two PDF documents using the SideBySidePdfComparer class.

1. Document Initialization.
1. Create a function to perform the comparison.
1. Comparison Process:

- document1.pages[1] and document2.pages[1]: - these specify the first page of each document for comparison. Note that page indexing starts from 1 in Aspose.PDF.
- SideBySideComparisonOptions - this class allows customization of the comparison behavior.
- additional_change_marks = True - enables the display of additional change markers, highlighting differences that might be present on other pages, even if they are not on the current page being compared.
- comparison_mode = ComparisonMode.IgnoreSpaces - sets the comparison mode to ignore spaces in the text, focusing only on changes within words.

1. The result of the comparison is saved as a new PDF file named ComparingSpecificPages_out.pdf in the specified data_dir.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## Comparing Entire Documents

The second code snippet expands the scope to compare the entire content of two PDF documents.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

The provided code demonstrates comparing two PDF documents using Aspose.PDF for Python via .NET. It utilizes the SideBySidePdfComparer class to perform a page-by-page comparison, generating a new PDF that displays the differences side by side. The comparison is configured with SideBySideComparisonOptions, where additional_change_marks is set to True to highlight changes not only on the current page but also on other pages, and comparison_mode is set to IgnoreSpaces to focus on meaningful content differences by ignoring whitespace variations.

## Compare Using GraphicalPdfComparer

When collaborating on documents, especially in professional environments, you often end up with multiple versions of the same file.
The provided code demonstrates how to visually compare specific pages of two PDF documents using Aspose.PDF for Python via .NET. By using the `GraphicalPdfComparer` class, it highlights differences between the first pages of the two PDFs and generates corresponding images to represent these differences.

You can set the following class properties:

- Resolution - resolution in DPI units for output images, as well as for images generated during the comparison.
- Color - the color of change marks.
- Threshold - change threshold in percent. The default value is zero. Setting a value other than zero allows you to ignore graphic changes that are insignificant to you.

With Aspose.PDF for Python via .NET, it's possible to compare documents and pages and output the comparison result to a PDF document or image file.

The `GraphicalPdfComparer` class has a method that allows you to get page image differences in a form suitable for further processing: `get_difference(document1.pages[1], document2.pages[1])`.

This method returns an object of the `images_difference` type, which contains an image of the first page being compared and an array of differences.

The `images_difference` object allows you to generate a different image and get an image of the second page being compared by applying an array of differences to the original image. To do this, use the `difference_to_image` and `get_destination_image` methods.

### Compare PDF with Get Difference Method

The provided code defines a method `get_difference` that compares two PDF documents and generates visual representations of the differences between them.

This method compares the first pages of two PDF files and generates two PNG images:

- One image highlights the differences between the pages in red.
- The other image is a visual representation of the destination (second) PDF page.

This process can be useful for visually comparing changes or differences between two versions of a document.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Compare PDF with CompareDocumentsToPdf Method

The provided code snippet uses the `compare_documents_to_pdf` method, which compares two documents and generates a PDF report of the comparison results.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

This example demonstrates how to perform a graphical comparison of two entire PDF documents using Aspose.PDF for Python via .NET. By leveraging the `GraphicalPdfComparer` class, it generates a new PDF file that visually highlights differences between the documents.

- The threshold property is set to 3.0, meaning that minor differences below this percentage are ignored during comparison, focusing on more significant changes.
- Differences are marked in blue by setting the color property to ap.Color.blue, allowing for clear visual distinction.
- The comparison is performed at a resolution of 300 DPI by setting the resolution property, ensuring detailed and clear output.

The `compare_documents_to_pdf` method compares all pages of both documents and outputs the result to a new PDF file, compareDocumentsToPdf_out.pdf, with differences visually highlighted. 
