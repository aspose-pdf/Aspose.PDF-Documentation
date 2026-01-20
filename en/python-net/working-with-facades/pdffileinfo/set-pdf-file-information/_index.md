---
title: Set PDF File Information
type: docs
weight: 40
url: /python-net/set-pdf-file-information/
description: This section explains how to set PDF File Information with Aspose.PDF Facades.
lastmod: "2026-01-05"
---

[PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo) class allows you to set file specific information of a PDF file. You need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo) class and then set different file specific properties like Author, Title, Keyword, and Creator etc. Finally, save the updated PDF file using [save_new_info](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/#methods) method of the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo) object.

The following code snippet shows you how to set PDF file information.

```python

from aspose.pdf.facades import PdfFileInfo

def set_pdf_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Create PdfFileInfo object to work with PDF metadata
    pdf_info = PdfFileInfo(data_dir + "sample.pdf")

    # Set PDF information
    pdf_info.author = "Aspose"
    pdf_info.title = "Hello World!"
    pdf_info.keywords = "Peace and Development"
    pdf_info.creator = "Aspose"

    # Save the PDF with updated information
    pdf_info.save_new_info(data_dir + "SetFileInfo_out.pdf")
```

## Set Meta Info

The [set_meta_info](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) method allows you to add any information. In our example, we added a field. Check next code snippet:

```python

from aspose.pdf.facades import PdfFileInfo

def set_meta_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Create PdfFileInfo object
    pdf_info = PdfFileInfo(data_dir + "sample.pdf")

    # Set a custom metadata attribute
    pdf_info.set_meta_info("Reviewer", "Aspose.PDF user")

    # Save the updated PDF
    pdf_info.save_new_info(data_dir + "SetMetaInfo_out.pdf")
```