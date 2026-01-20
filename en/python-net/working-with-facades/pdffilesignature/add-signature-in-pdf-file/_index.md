---
title: Add Signature in PDF File
type: docs
weight: 10
url: /python-net/add-signature-in-pdf/
description: This section explains how to add signature to PDF File using PdfFileSignature class.
lastmod: "2026-01-05"
---

## Add Digital Signature in a PDF File

[PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class allows you to add signature in a PDF file. You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class using input and output PDF files. You also need to create a [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle) object at which you want to add the signature and in order to set appearance you can specify an image using [signature_appearance](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) property of the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) object. Aspose.Pdf.Facades also provides different kinds of signatures like PKCS#1, PKCS#7, and PKCS#7Detached. In order to create a signature of a specific type, you need to create an object of the particular class like **PKCS1** , **PKCS7** or **PKCS7Detached** using the certificate file and the password.

Once the object of a particular signature type is created, you can use the [sign](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method of the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class to sign the PDF and pass the particular signature object to this class. You can also specify other attributes for this method. Finally, you need to save the signed PDF using [save](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method of the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class. The following code snippet shows you how to add signature in a PDF file.

```python

from aspose.pdf.facades import (
    PdfFileSignature,
    PKCS7Detached,
    Rectangle
)

def add_signature_to_pdf():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    output_pdf = data_dir + "SignedOutput.pdf"
    cert_file = data_dir + "certificate.pfx"
    cert_password = "your_cert_password"

    # Create PdfFileSignature object
    pdf_sign = PdfFileSignature()

    # Bind PDF document (input & output)
    pdf_sign.bind_pdf(input_pdf, output_pdf)

    # Define signature placement (page 1, rectangle coordinates)
    sig_rect = Rectangle(100, 500, 300, 650)

    # Create PKCS7Detached signature using certificate
    signature = PKCS7Detached(cert_file, cert_password)

    # Optionally set signature appearance
    pdf_sign.signature_appearance = data_dir + "signature_image.jpg"

    # Sign the PDF
    pdf_sign.sign(1, cert_file, cert_password, "Reason for signing", "Contact", "Location", sig_rect, signature)

    # Save the signed document
    pdf_sign.save()
```

The following code example shows us the ability to sign a document with two signatures. In our example, we put the first signature on the first page, and the second on the second page. You can specify the pages that you need.

```python

from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1
from aspose.pdf import Rectangle

def add_two_signatures():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    cert_file = data_dir + "rsa_cert.pfx"
    cert_password = "12345"

    # Create PdfFileSignature object
    pdf_signature = PdfFileSignature()

    # =========================
    # First signature
    # =========================
    pdf_signature.bind_pdf(input_pdf)

    rect1 = Rectangle(10, 10, 300, 50)
    signature1 = PKCS1(cert_file, cert_password)

    pdf_signature.sign(
        1,
        "I'm document author",
        "test@aspose-pdf-demo.local",
        "Aspose Pdf Demo, Australia",
        True,
        rect1,
        signature1
    )

    first_signed_pdf = data_dir + "DigitallySign_out.pdf"
    pdf_signature.save(first_signed_pdf)

    # =========================
    # Second signature
    # =========================
    pdf_signature.bind_pdf(first_signed_pdf)

    rect2 = Rectangle(10, 10, 300, 50)
    signature2 = PKCS1(cert_file, cert_password)

    pdf_signature.sign(
        2,
        "I'm document reviewer",
        "test02@aspose-pdf-demo.local",
        "Aspose Pdf Demo, Australia",
        True,
        rect2,
        signature2
    )

    pdf_signature.save(data_dir + "DigitallySign2_out.pdf")
```

For a document with forms or acroforms that needs to be signed, see the following example.
You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class using input and output PDF files. Use [bind_pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) for binding. Create a signature with the ability to add the required properties. In our example they are 'Reason' and 'CustomAppearance'.

```python

from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1, SignatureCustomAppearance

def add_pdf_file_signature_field():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    output_pdf = data_dir + "DigitallySign_out.pdf"
    cert_file = data_dir + "rsa_cert.pfx"
    cert_password = "12345"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Create PKCS#1 signature with custom appearance
    signature = PKCS1(cert_file, cert_password)
    signature.reason = "Sign as Author"

    appearance = SignatureCustomAppearance()
    appearance.font_size = 6
    appearance.font_family_name = "Calibri"
    signature.custom_appearance = appearance

    # Sign PDF using a named signature field
    pdf_signature.sign("Signature1", signature)

    # Save signed PDF
    pdf_signature.save(output_pdf)
```

If our document has two fields, the algorithm for signing it is similar to the first example.

```python

from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1, SignatureCustomAppearance

def add_pdf_file_signature_field2():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    cert_file = data_dir + "rsa_cert.pfx"
    cert_password = "12345"

    pdf_signature = PdfFileSignature()

    # =========================
    # First signature field
    # =========================
    pdf_signature.bind_pdf(input_pdf)

    signature1 = PKCS1(cert_file, cert_password)
    signature1.reason = "Sign as Author"

    appearance1 = SignatureCustomAppearance()
    appearance1.font_size = 6
    signature1.custom_appearance = appearance1

    pdf_signature.sign("Signature1", signature1)
    first_signed_pdf = data_dir + "DigitallySign_out.pdf"
    pdf_signature.save(first_signed_pdf)

    # =========================
    # Second signature field
    # =========================
    pdf_signature.bind_pdf(first_signed_pdf)

    signature2 = PKCS1(cert_file, cert_password)
    signature2.reason = "Sign as Reviewer"

    appearance2 = SignatureCustomAppearance()
    appearance2.font_size = 6
    signature2.custom_appearance = appearance2

    pdf_signature.sign("Signature2", signature2)
    pdf_signature.save(data_dir + "DigitallySign2_out.pdf")
```
