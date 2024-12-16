---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in Python
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Learn how to generate a PDF document with ZUGFeRD in Aspose.PDF for Python via .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
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
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```
