---
title: Set Privileges on PDF 
type: docs
weight: 50
url: /python-net/set-privileges/
description: Discover how to modify user privileges in PDF files, restricting certain actions using Aspose.PDF in Python.
lastmod: "2026-01-05"
---

## Set Privileges on an Existing PDF File

To set a PDF file's privileges, create a [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity) object and call the SetPrivilege method. You can specify the privileges using the DocumentPrivilege object and then pass this object to the SetPrivilege method. The following code snippet shows you how to set the privileges of a PDF file.

```python

from aspose.pdf.facades import PdfFileSecurity, DocumentPrivilege

def set_privilege_1():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "sample.pdf"
    output_pdf = data_dir + "SamplePrivileges_out.pdf"

    # Create DocumentPrivilege object and configure permissions
    privilege = DocumentPrivilege.forbid_all
    privilege.change_allow_level = 1
    privilege.allow_print = True
    privilege.allow_copy = True

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(input_pdf)

    # Apply privileges
    file_security.set_privilege(privilege)

    # Save PDF with updated privileges
    file_security.save(output_pdf)
```

See the following method with specifying a password:

```python

from aspose.pdf.facades import PdfFileSecurity, DocumentPrivilege

def set_privilege_with_password():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "sample.pdf"
    output_pdf = data_dir + "SamplePrivilegesPassword_out.pdf"

    # Create DocumentPrivilege object and configure permissions
    privilege = DocumentPrivilege.forbid_all
    privilege.change_allow_level = 1
    privilege.allow_print = True
    privilege.allow_copy = True

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(input_pdf)

    # Set privilege with passwords
    # user_password is empty, owner_password is set
    file_security.set_privilege(
        "",                 # user password
        "P@ssw0rd",         # owner password
        privilege
    )

    # Save PDF with updated privileges
    file_security.save(output_pdf)
```

## Remove Extended Rights Feature from the PDF

PDF documents support the extended rights feature to enable end-user to fill data into form fields by using Adobe Acrobat Reader and then save a copy of the filled form. However, it ensures that PDF file is not modified and if any modification to the structure of the PDF is made, the extended rights feature is lost. When viewing such a document, an error message is displayed, stating that extended rights are removed because the document was modified. Recently, we received a requirement to remove extended rights from PDF document.

The following code shows how to remove usage rights from the document:

```python

from aspose.pdf.facades import PdfFileSignature

def remove_extended_rights():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    input_pdf = data_dir + "DigitallySign.pdf"
    output_pdf = data_dir + "RemoveRights_out.pdf"

    pdf_sign = PdfFileSignature()

    # Bind PDF document
    pdf_sign.bind_pdf(input_pdf)

    # Check and remove usage rights if present
    if pdf_sign.contains_usage_rights():
        pdf_sign.remove_usage_rights()

    # Save updated PDF document
    pdf_sign.document.save(output_pdf)
```