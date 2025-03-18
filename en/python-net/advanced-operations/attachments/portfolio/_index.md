---
title: Working with Portfolio in PDF using Python
linktitle: Portfolio
type: docs
weight: 20
url: /python-net/portfolio/
description: How to Create a PDF Portfolio with Python. You should use a Microsoft Excel File, a Word document, and an image file to create a PDF Portfolio.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on creating PDF portfolios using Python
Abstract: The article "Working with Portfolio in PDF using Python" published by the Aspose.PDF Doc Team, provides a beginner-friendly guide on creating PDF portfolios using Python. A PDF portfolio is a convenient way to consolidate various file types such as text documents, images, and spreadsheets into a single, organized PDF document. The article explains how to utilize the Aspose.PDF for Python via .NET library to create and manage PDF portfolios. It includes a step-by-step tutorial on adding files to a PDF portfolio using the `Document` and `FileSpecification` classes, as well as a method to save the portfolio. Additionally, it covers how to remove files from an existing PDF portfolio. The article is supported by code snippets and examples, demonstrating the process of assembling a PDF portfolio with an Excel file, a Word document, and an image. The content is aimed at those interested in modern document management and presentation techniques, offering insights into leveraging Python for PDF document generation.
---

Creating a PDF portfolio allows consolidating and archiving different types of files into a single, consistent document. Such a document could include text files, images, spreadsheets, presentations, and other materials, and ensure that all relevant material is stored and organized in one place.

The PDF portfolio will help to show your presentation in a high-quality way, wherever you use it. In general, creating a PDF portfolio is a very current and modern task.

## How to Create a PDF Portfolio

Aspose.PDF for Python via .NET allows creating PDF Portfolio documents using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Add a file into a document.collection object after getting it with the [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) class. When the files have been added, use the Document class' [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method to save the portfolio document.

The following example uses a Microsoft Excel File, a Word document and an image file to create a PDF Portfolio.

The code below results in the following portfolio.

### A PDF Portfolio created with Aspose.PDF for Python

![A PDF Portfolio created with Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## Remove Files from PDF Portfolio

In order to delete/remove files from PDF portfolio, try using the following code lines.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```

