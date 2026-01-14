---
title: PdfFileEditor Class
type: docs
weight: 10
url: /python-net/pdffileeditor-class/
description: Explore how to edit and manipulate PDF files using the PDFFileEditor class in Python with Aspose.PDF.
lastmod: "2026-01-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Working with PDF documents includes various functions. Managing the pages of a PDF file is an important part of this job. Aspose.Pdf.Facaded provide the `PdfFileEditor` class for this purpose.

PdfFileEditor class contains the methods which help manipulate individual pages; this class doesn't edit or manipulate the contents of a page. You can insert a new page, delete existing page, split the pages or you can specify imposition of the pages using PdfFileEditor.

The features provided by this class can be divided into three main categories i.e. File Editing, PDF Imposition, and Splitting. We're going to discuss these sections in detail below:

## File Editing

The features which we can include in this section are Insert, Append, Delete, Concatenate and Extract. You can insert a new page at a specified location using Insert method, or append the pages at the end of the file. You can also delete any number of pages from the file using Delete method, by specifying an integer array containing the numbers of pages to be deleted. Concatenate method helps you to join pages from multiple PDF files. You can extract any number of pages using Extract method, and save these pages into another PDF file or memory stream.

This section explores the capabilities of this class and explains the purpose of its methods.

- [Concatenate PDF documents](/pdf/python-net/concatenate-pdf-documents/)
- [Extract PDF pages](/pdf/python-net/extract-pdf-pages/)
- [Insert PDF pages](/pdf/python-net/insert-pdf-pages/)
- [Delete PDF pages](/pdf/python-net/delete-pdf-pages/)

## Using Page Brakes

Page Break is a special feature that allows to reflow of the document.

- [Page Break in existing PDF](/pdf/python-net/page-break-in-existing-pdf/)

## PDF Imposition

Imposition is the process of arranging pages correctly prior to printing. `PdfFileEditor` provides two methods for this purpose i.e. `MakeBooklet` and `MakeNUp`. MakeBooklet method helps to arrange pages so that it'll be easy to fold or bind them after printing, however, MakeNUp method allows to print multiple pages on one page of the PDF file.

- [Make Booklet of PDF](/pdf/python-net/make-booklet-of-pdf/)
- [Make NUp of PDF files](/pdf/python-net/make-nup-of-pdf-files/)

## Splitting

Splitting feature allows you to divide an existing PDF file into different parts. You can either split the front part of the PDF file or the rear part. As PdfFileEditor provides a variety of method for splitting purposes, you can also split a file into individual pages or many sets of multiple pages.

- [Split PDF pages](/pdf/python-net/split-pdf-pages/)
