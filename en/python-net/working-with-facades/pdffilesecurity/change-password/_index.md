---
title: Change Password of PDF File
type: docs
weight: 40
url: /python-net/change-password/
description: Explore how to modify the password of a PDF document in Python to improve file security with Aspose.PDF.
lastmod: "2026-01-05"
draft: false
---

## Change Password of a PDF File

In order to change password of a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity) object and then call the [change_password](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) method. You need to pass existing owner password and new user and owner passwords to the [change_password](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) method.

{{% alert color="primary" %}}

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

{{% /alert %}}

The following code snippet shows you how to change passwords of a PDF file.

```python

from aspose.pdf.facades import PdfFileInfo, PdfFileSecurity, DocumentPrivilege, KeySize

def change_password():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    pdf_path = data_dir + "sample_encrypted.pdf"
    output_path = data_dir + "sample_encrypted1.pdf"

    # Check if the PDF is encrypted
    pdf_info = PdfFileInfo(pdf_path)
    if pdf_info.is_encrypted:
        file_security = PdfFileSecurity()

        # Bind PDF document
        file_security.bind_pdf(pdf_path)

        # Change password
        file_security.change_password(
            "OwnerP@ssw0rd",        # current owner password
            "Pa$$w0rd1",            # new user password
            "Pa$$w0rd2",            # new owner password
            DocumentPrivilege.print,
            KeySize.x256
        )

        # Save updated PDF
        file_security.save(output_path)
```

