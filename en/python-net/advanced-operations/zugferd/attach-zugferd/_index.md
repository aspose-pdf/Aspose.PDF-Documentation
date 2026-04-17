---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in Python
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Learn how to generate a PDF document with ZUGFeRD in Aspose.PDF for Python via .NET
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to attach ZUGFeRD to a PDF document 
Abstract: The article provides a step-by-step guide on how to attach ZUGFeRD (a format for electronic invoices) to a PDF document using the Aspose.PDF library. The procedure begins with importing the necessary library and setting up the directory paths for input and output files. It involves loading the target PDF file into a Document object, and creating a FileSpecification object for the XML invoice metadata file. Key properties like `mime_type` and `af_relationship` are set to ensure proper integration of the metadata. The XML file is then added to the PDF's embedded files collection, effectively attaching it as metadata. Subsequently, the PDF document is converted to the PDF/A-3A format, which is suitable for archiving electronic documents, before saving the final PDF with the embedded ZUGFeRD. The article concludes with a Python code snippet that demonstrates the implementation of these steps, showcasing the integration of ZUGFeRD with a PDF for enhanced document management.
---

## Attach ZUGFeRD to PDF

We recommend following steps to attach ZUGFeRD to PDF:

1. Import the Aspose.PDF library and give it an alias of ap for convenience.
1. Define the path to the directory where the input and output PDF files are located.
1. Define the path to the PDF file that will be processed.
1. Load the PDF file from the path variable and create a Document object.
1. Create a FileSpecification object for the XML file that contains the invoice metadata. Use the path variable and a description string to create the FileSpecification object.
1. Set the `mime_type` and the `af_relationship` properties of the FileSpecification object to `text/xml` and `ALTERNATIVE`, respectively.
1. Add the fileSpecification object to the document object's embedded files collection. This attaches the XML file to the PDF document as an invoice metadata file.
1. Convert the PDF document to the PDF/A-3A format. Use the path to log file, the `PdfFormat.PDF_A_3A` enumeration, and the `ConvertErrorAction.DELETE` enumeration to convert the document object.
1. Save the PDF document with the attached ZUGFeRD.

```python
import sys
import os
import aspose.pdf as ap

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def attach_invoice_zugferd_format(infile, invoice, outfile):
    """
    Attach Factur-X/ZUGFeRD invoice XML to PDF and convert to PDF/A-3A format.

    Args:
        infile (str): Input PDF filename
        invoice (str): Invoice XML filename (Factur-X/ZUGFeRD compliant)
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        attach_invoice_zugferd_format("input.pdf", "factur-x.xml", "output.pdf")

    Note:
        Embeds invoice XML as alternative file conforming to ZUGFeRD standard.
        Converts PDF to PDF/A-3A format to ensure long-term archival compliance.
    """
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
