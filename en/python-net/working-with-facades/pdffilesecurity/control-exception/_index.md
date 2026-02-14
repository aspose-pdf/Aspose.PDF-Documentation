---
title: Control Exception PDF File
type: docs
weight: 30
url: /python-net/control-exception/
description: Learn how to handle exceptions in PDF processing and ensure smooth operations while working with PDFs using Aspose.PDF in Python.
lastmod: "2026-01-05"
---

[PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity) class allows you to control exceptions. To do this, you need to set [allow_exceptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#properties) property to false or true. If you set the operation to false, the result of [decrypt_file](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) will return true or false depending on the correctness of the password.

```python

from aspose.pdf.facades import PdfFileSecurity

def control_exception_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    pdf_path = data_dir + "sample_encrypted.pdf"
    output_path = data_dir + "SampleDecrtypted_out.pdf"

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(pdf_path)

    # Disallow exceptions (handle errors manually)
    file_security.allow_exceptions = False

    # Attempt to decrypt with an incorrect password
    if not file_security.decrypt_file("IncorrectPassword"):
        print("Something wrong...")
        print(f"Last exception: {file_security.last_exception.message}")

    # Save PDF document (will save only if decryption succeeds)
    file_security.save(output_path)
```

If you set [allow_exceptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#properties) property to true, then you can get the result of the operation using the try-catch operator.

```python

from aspose.pdf.facades import PdfFileSecurity

def control_exception_pdf_file2():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    pdf_path = data_dir + "sample_encrypted.pdf"
    output_path = data_dir + "SampleDecrtypted_out.pdf"

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(pdf_path)

    # Allow exceptions (raise errors automatically)
    file_security.allow_exceptions = True

    try:
        # Attempt to decrypt PDF document
        file_security.decrypt_file("IncorrectPassword")
    except Exception as ex:
        print("Something wrong...")
        print(f"Exception: {ex}")

    # Save PDF document
    file_security.save(output_path)
```