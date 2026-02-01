---
title: Working with PDF printing - Facades
type: docs
weight: 10
url: /python-net/working-with-pdf-printing-facades/
description: This section explains how to print PDF files with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Printing PDF with Aspose.PDF for Python

Aspose.PDF lets you print PDF files programmatically. In .NET examples, the PdfViewer class from the Aspose.Pdf.Facades namespace handles printing operations. In Python  we use a similar API exposed by Aspose.PDF for Python via .NET to:

- Print a PDF to the default printer
- Show or hide print dialogs
- Print to a file/printer (Soft printer or PostScript)
- Control page settings like paper size and margins
- Convert PDF pages to printed output

```python

import aspose.pdf as pdf

# Prepare viewer
viewer = pdf.facades.PdfViewer()

# Bind the PDF (open)
viewer.bind_pdf("PrintDocument.pdf")

# Adjust settings
viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False

# Create printer and page settings
ps = pdf.printing.PrinterSettings()
pgs = pdf.printing.PageSettings()

# You can explicitly specify printer name (optional)
# ps.printer_name = "Your Printer Name"

# Example: Set A4 page size
pgs.paper_size = pdf.printing.PaperSizes.A4

# Print
viewer.print_document_with_settings(pgs, ps)

# Release resources
viewer.close()
```

In order to display a print dialog, use the following code snippet.

```python

import aspose.pdf as pdf
import System
from System.Windows.Forms import PrintDialog, DialogResult

def printing_pdf_display_print_dialog():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        viewer.auto_resize = True
        viewer.auto_rotate = True

        # Show system print dialog
        print_dialog = PrintDialog()

        if print_dialog.ShowDialog() == DialogResult.OK:
            # Convert .NET PrinterSettings to Aspose equivalents
            ps = pdf.printing.PrinterSettings.to_aspose_printer_settings(
                print_dialog.PrinterSettings
            )

            pgs = pdf.printing.PageSettings.to_aspose_page_settings(
                print_dialog.PrinterSettings.DefaultPageSettings
            )

            # Print document using selected printer and page settings
            viewer.print_document_with_settings(pgs, ps)

    finally:
        # Release resources
        viewer.close()
```

## Print PDF to Soft Printer

There are printers that print to a file. To use them, set the name of the virtual printer, and, analogous to the previous example, make the settings.

```python

import aspose.pdf as pdf

viewer = pdf.facades.PdfViewer()
viewer.bind_pdf("PrintDocument.pdf")

viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False

ps = pdf.printing.PrinterSettings()
pgs = pdf.printing.PageSettings()

# Set soft printer and print to file
ps.printer_name = "Adobe PDF"  # Or another virtual printer
ps.print_file_name = "OutFile.pdf"
ps.print_to_file = True

pgs.paper_size = pdf.printing.PaperSizes.A4

viewer.print_document_with_settings(pgs, ps)
viewer.close()
```

## Printing Color PDF to XPS File as Grayscale

This Python example shows how to print a PDF document programmatically using Aspose.PDF for Python via .NET with full control over printing behavior and without displaying any print dialogs.

```python

import aspose.pdf as pdf

viewer = pdf.facades.PdfViewer()
viewer.bind_pdf("PrintDocument.pdf")

viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False
viewer.print_as_grayscale = True  # Print in grayscale

ps = pdf.printing.PrinterSettings()
pgs = pdf.printing.PageSettings()
ps.printer_name = "Microsoft XPS Document Writer"
pgs.paper_size = pdf.printing.PaperSizes.A4

viewer.print_document_with_settings(pgs, ps)
viewer.close()
```

## Hiding Print Dialog

Aspose.PDF for Python supports hiding the print dialog. For this, use the 'print_page_dialog' property.

The following code snippet shows how to hide the print dialog.

```python

import aspose.pdf as pdf

def printing_pdf_hide_print_dialog():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        # Print the file with adjusted size
        viewer.auto_resize = True
        # Print the file with adjusted rotation
        viewer.auto_rotate = True
        # Do not show the page number dialog
        viewer.print_page_dialog = False

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Set XPS/PDF printer name
        ps.printer_name = "OneNote for Windows 10"

        # Set page size (A4)
        pgs.paper_size = pdf.printing.PaperSizes.A4

        # Set page margins (left, right, top, bottom)
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Print document using printer and page settings
        viewer.print_document_with_settings(pgs, ps)

    finally:
        # Close viewer and release resources
        viewer.close()
```

## PDF to PostScript conversion

The [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer) class provides the capability to print PDF documents and with the help of this class, one can also convert PDF files to PostScript format. To convert a PDF file into PostScript, first install any PS printer and just print to file with the help of the `PdfViewer`.

The following code snippet shows how to print and convert a PDF to PostScript format.

```python

import aspose.pdf as pdf

def printing_pdf_to_postscript():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        viewer.auto_resize = True
        viewer.auto_rotate = True
        viewer.print_page_dialog = False
        viewer.print_as_image = False  # Do NOT convert pages to images

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Set PostScript printer name
        ps.printer_name = "HP Universal Printing PS (v7.0.0)"

        # Set output file and enable PrintToFile
        ps.print_file_name = data_dir + "PdfToPostScript_out.ps"
        ps.print_to_file = True

        # Set page size (A4)
        pgs.paper_size = pdf.printing.PaperSizes.A4

        # Set page margins (left, right, top, bottom)
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Print document using printer and page settings
        viewer.print_document_with_settings(pgs, ps)

    finally:
        # Release resources
        viewer.close()
```

## Checking Print Job Status

A PDF file can be printed to a physical printer as well as to the Microsoft XPS Document Writer, without showing a print dialog, using the [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer) class. When printing large PDF files, the process might take a long time so the user might not be certain whether the printing process completed or encountered an issue. To determine the status of a printing job, use the [print_status](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/#properties) property. The following code snippet shows how to print the PDF file to an XPS file and get the printing status.

```python

import aspose.pdf as pdf

def checking_print_job_status():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Instantiate PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        viewer.auto_resize = True
        viewer.auto_rotate = True
        viewer.print_page_dialog = False
        viewer.print_as_image = False

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Specify the printer name
        ps.printer_name = "Microsoft XPS Document Writer"

        # Set output file name and enable PrintToFile
        ps.print_file_name = data_dir + "CheckingPrintJobStatus_out.xps"
        ps.print_to_file = True

        # Set page size (A4)
        pgs.paper_size = pdf.printing.PaperSizes.A4

        # Set page margins
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Print document using printer and page settings
        viewer.print_document_with_settings(pgs, ps)

        # Check the print status
        if viewer.print_status is not None:
            # An exception was thrown during printing
            print(str(viewer.print_status))
        else:
            # Printing completed successfully
            print("Printing completed without any issue.")

    finally:
        # Release resources
        viewer.close()
```

## Printing pages in Simplex and Duplex mode

In a particular printing job, the pages of PDF document can either be printed in Duplex or in Simplex mode but you cannot print some pages as simplex and some pages as duplex within a single print job. However in order to accomplish the requirement, different page ranges and 'PrintingJobSettings' object can be used. The following code snippet shows how to print some pages of PDF file in Simplex and some pages in Duplex mode.

```python

import aspose.pdf as pdf
import os

class PrintingJobSettings:
    def __init__(self, from_page, to_page, output_file, duplex_mode):
        self.from_page = from_page
        self.to_page = to_page
        self.output_file = output_file
        self.mode = duplex_mode


def printing_pages_in_simplex_and_duplex_mode():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()
    output_dir = data_dir

    printing_job_index = 0
    printing_jobs = []

    # Create printing jobs
    printing_jobs.append(
        PrintingJobSettings(
            from_page=1,
            to_page=3,
            output_file=output_dir + "PrintPageRange_p1-3_out.xps",
            duplex_mode=pdf.printing.Duplex.Default
        )
    )

    printing_jobs.append(
        PrintingJobSettings(
            from_page=4,
            to_page=6,
            output_file=output_dir + "PrintPageRange_p4-6_out.xps",
            duplex_mode=pdf.printing.Duplex.Simplex
        )
    )

    printing_jobs.append(
        PrintingJobSettings(
            from_page=7,
            to_page=7,
            output_file=output_dir + "PrintPageRange_p7_out.xps",
            duplex_mode=pdf.printing.Duplex.Default
        )
    )

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "Print-PageRange.pdf")

        # Set printing attributes
        viewer.auto_resize = True
        viewer.auto_rotate = True
        viewer.print_page_dialog = False

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Set printer name
        ps.printer_name = "Microsoft XPS Document Writer"

        # Set initial job settings
        ps.print_to_file = True
        ps.print_range = pdf.printing.PrintRange.SomePages

        # Paper size and margins
        pgs.paper_size = pdf.printing.PaperSizes.A4
        ps.default_page_settings.paper_size = pgs.paper_size
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Helper to apply a print job
        def apply_print_job(index):
            job = printing_jobs[index]
            ps.print_file_name = os.path.abspath(job.output_file)
            ps.from_page = job.from_page
            ps.to_page = job.to_page
            ps.duplex = job.mode

        # Apply first job
        apply_print_job(printing_job_index)

        # EndPrint event handler (chain next jobs)
        def on_end_print(sender, args):
            nonlocal printing_job_index
            printing_job_index += 1

            if printing_job_index < len(printing_jobs):
                apply_print_job(printing_job_index)
                viewer.print_document_with_settings(pgs, ps)

        viewer.end_print += on_end_print

        # Start first print job
        viewer.print_document_with_settings(pgs, ps)

    finally:
        # Release resources
        viewer.close()
```

## Printing multiple PDF documents in a single print job

Sometimes, it is necessary to print multiple related documents together as a single print job. This ensures that these documents do not get interspersed with output from other users, especially with remote network printers. Aspose.PDF supports printing any number of documents in a single print job with shared printer settings via the static `print_documents` methods of the [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer) class. The documents to be printed can be provided as file paths, document streams, or [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) objects.

```python

import aspose.pdf as pdf
import os

def printing_multiple_documents_in_single_job():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Paths to documents to be printed
    path1 = os.path.join(data_dir, "PrintDocument.pdf")
    path2 = os.path.join(data_dir, "Print-PageRange.pdf")
    path3 = os.path.join(data_dir, "35925_1_3.xps")

    # Create printer settings
    printer_settings = pdf.printing.PrinterSettings()

    # Use default system printer (same idea as PrintDocument.PrinterSettings.PrinterName)
    # If you want to force a printer, uncomment and set it explicitly:
    # printer_settings.printer_name = "Microsoft XPS Document Writer"

    # Create page settings
    page_settings = pdf.printing.PageSettings()
    page_settings.paper_size = pdf.printing.PaperSizes.A4
    page_settings.margins = pdf.devices.Margins(0, 0, 0, 0)

    # Print multiple documents in a single print job
    pdf.facades.PdfViewer.print_documents(
        printer_settings,
        page_settings,
        path1,
        path2,
        path3
    )
```