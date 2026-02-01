---
title: Decrypt PDF File
type: docs
weight: 20
url: /python-net/decrypt-pdf-file/
description: Explore methods to decrypt password-protected PDF files in Python, ensuring access to the document's content using Aspose.PDF.
lastmod: "2026-01-05"
---

A PDF document encrypted with a password or certificate must be unlocked before another operation can be performed on it. If you try to operate on an encrypted PDF document, you will throw an exception. After unlocking an encrypted PDF, you can perform one or more operations on it.

## Decrypt PDF File using Owner Password

In order to decrypt a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity) object and then call the [decrypt_file](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) method. You also need to pass the owner password to [decrypt_file](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) method. The following code snippet shows you how to decrypt PDF file.

```python

from aspose.pdf.facades import PdfFileInfo, PdfFileSecurity

def decrypt_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "sample_encrypted.pdf"
    output_pdf = data_dir + "SampleDecrtypted_out.pdf"

    # Check whether the PDF is encrypted
    pdf_info = PdfFileInfo(input_pdf)
    if pdf_info.is_encrypted:
        file_security = PdfFileSecurity()

        # Bind PDF document
        file_security.bind_pdf(input_pdf)

        # Decrypt PDF document using password
        file_security.decrypt_file("P@ssw0rd")

        # Save decrypted PDF
        file_security.save(output_pdf)
```
