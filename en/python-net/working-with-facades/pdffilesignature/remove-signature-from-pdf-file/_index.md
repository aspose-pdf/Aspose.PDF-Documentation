---
title: Remove Signature from PDF File
type: docs
weight: 20
url: /python-net/remove-signature-from-pdf/
description: This section explains how to remove signature from PDF File using PdfFileSignature class.
lastmod: "2026-01-05"
---

## Remove Digital Signature from the PDF File

When a signature has been added to a PDF files, it is possible to remove it. You can remove either a particular signature, or all signatures in a file. The fastest method for removing the signature also removes the signature field, but it is possible to just remove the signature, keeping the signature field so the file can be signed again.

The [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class RemoveSignature method allows you to remove a signature from a PDF file. This method takes the signature name as an input. Either specify the signature name directly, to remove all signatures, get the signature names using the [get_sign_names](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method.

The following code snippet shows how to remove digital signature from the PDF file.

```python

from aspose.pdf.facades import PdfFileSignature

def remove_signature():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"
    output_pdf = data_dir + "RemoveSignature_out.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Get list of signature names
    signature_names = pdf_signature.get_sign_names()

    # Remove all signatures
    for name in signature_names:
        print(f"Removed {name}")
        pdf_signature.remove_signature(name)

    # Save PDF without signatures
    pdf_signature.save(output_pdf)
```

### Remove Signature but Keep the Signature field

As shown above, the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class [remove_signature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method lets you remove signature fields from PDF files. When using this method with versions prior to 9.3.0, both the signature and signature field are removed. Some develoeprs want to remove only the signature and keep the signature field so that it can be used to resign the document. To keep the signature field and only remove the signature, please use the following code snippet.

```python

from aspose.pdf.facades import PdfFileSignature

def remove_signature_but_keep_field():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"
    output_pdf = data_dir + "RemoveSignature_out.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Remove signature but keep the signature field
    pdf_signature.remove_signature("Signature1", False)

    # Save updated PDF
    pdf_signature.save(output_pdf)
```

The following example shows how to remove all signatures from fields.

```python

from aspose.pdf.facades import PdfFileSignature

def remove_signature_but_keep_field2():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"
    output_pdf = data_dir + "RemoveSignature_out.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Get all signature field names
    signature_names = pdf_signature.get_signature_names()

    # Remove signatures but keep fields
    for sig_name in signature_names:
        pdf_signature.remove_signature(sig_name, False)

    # Save updated PDF
    pdf_signature.save(output_pdf)
```
