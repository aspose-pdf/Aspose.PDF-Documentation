---
title: Working with Signature in PDF File
type: docs
weight: 40
url: /python-net/working-with-signature-in-a-pdf-file/
description: This section explains how to to extract signature information, extract image from signature, change language, and etc using PdfFileSignature class.
lastmod: "2026-01-05"
---

## How to Extract Signature Information

Aspose.PDF for Python via .NET supports the feature to digitally sign PDF files using the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) class. Currently, it is also possible to determine the validity of a certificate but we cannot extract the whole certificate. The information that can be extracted is the public key, thumbprint, and issuer, etc.

To extract signature information, we have introduced the [extract_certificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method to the PdfFileSignature class. Please take a look at the following code snippet which demonstrates the steps to extract certificate from the PdfFileSignature object:

```python

from aspose.pdf.facades import PdfFileSignature

def extract_signature_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    pdf_signature = PdfFileSignature()
    pdf_signature.bind_pdf(data_dir + "signed_rsa.pdf")

    signature_names = pdf_signature.get_signature_names()
    if signature_names:
        sig_name = signature_names[0]

        # Extract certificate as a stream
        cer_stream = pdf_signature.extract_certificate(sig_name)
        if cer_stream is not None:
            with open(data_dir + "extracted_cert.pfx", "wb") as fs:
                fs.write(cer_stream.read())
```

## Extracting Image from Signature Field (PdfFileSignature)

Aspose.PDF for Python via .NET supports the feature to digitally sign the PDF files using the PdfFileSignature class and while signing the document, you can also set an image for SignatureAppearance. Now this API also provides the capability to extract signature information as well as the image associated with the signature field.

In order to extract signature information, we have introduced the [extract_image](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method to the PdfFileSignature class. Please take a look at the following code snippet which demonstrates the steps to extract image from the PdfFileSignature object:

```python

from aspose.pdf.facades import PdfFileSignature

def extract_signature_image():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    signature = PdfFileSignature()
    signature.bind_pdf(data_dir + "ExtractingImage.pdf")

    if signature.contains_signature():
        for sig_name in signature.get_signature_names():
            image_stream = signature.extract_image(sig_name)
            if image_stream:
                with open(data_dir + "ExtractedImage_out.jpg", "wb") as fs:
                    fs.write(image_stream.read())
```

## Suppress Location and Reason

Aspose.PDF functionality allows flexible configuration for digital sign instance. [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature)class provides ability sign PDF file. Sign method implementation allows to sign the PDF and pass the particular signature object to this class. Sign method contains set of attributes for the customization of output digital sing. In case if you need to suppress some text attributes from result sing you can leave them empty. The following code snippet demonstrate how to suppress Location and Reason two rows from signature block:

```python

from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1
from aspose.pdf import Rectangle

def suppress_location_and_reason():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    pdf_signature = PdfFileSignature()
    pdf_signature.bind_pdf(data_dir + "input.pdf")

    rect = Rectangle(10, 10, 300, 50)
    signature = PKCS1(data_dir + "rsa_cert.pfx", "12345")

    # Suppress reason and location by leaving empty strings
    pdf_signature.sign(
        1,
        "",  # empty reason
        "test01@aspose-pdf-demo.local",
        "",  # empty location
        True,
        rect,
        signature
    )
    pdf_signature.save(data_dir + "DigitallySign_out.pdf")
```

## Customization Features for Digital Sign

This example demonstrates how to customize the visual appearance of a digital signature in a PDF document. It shows how to control signature text formatting—such as font size, font family, and the 'Signed by' label—while applying a PKCS#1 digital signature at a specified location on a page using the PdfFileSignature class.

```python

from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1, SignatureCustomAppearance
from aspose.pdf import Rectangle

def customize_signature_appearance():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    pdf_signature = PdfFileSignature()
    pdf_signature.bind_pdf(data_dir + "input.pdf")

    rect = Rectangle(10, 10, 300, 50)
    signature = PKCS1(data_dir + "rsa_cert.pfx", "12345")

    appearance = SignatureCustomAppearance()
    appearance.font_size = 6
    appearance.font_family_name = "Times New Roman"
    appearance.digital_signed_label = "Signed by:"
    signature.custom_appearance = appearance

    pdf_signature.sign(1, True, rect, signature)
    pdf_signature.save(data_dir + "DigitallySign_out.pdf")
```

## Change Language In Digital Sign Text

Our library shows how to apply a digital signature to a PDF document with a custom visual appearance that includes an image. It shows how to display a logo or graphic inside the signature field, configure text properties such as font and label, and place the signature at a specified location on the page using the PdfFileSignature class.

```python

from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1, SignatureCustomAppearance
from aspose.pdf import Rectangle

def signature_with_image():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()
    image_path = data_dir + "aspose-logo.jpg"

    pdf_signature = PdfFileSignature()
    pdf_signature.bind_pdf(data_dir + "input.pdf")

    rect = Rectangle(10, 10, 300, 50)
    signature = PKCS1(data_dir + "rsa_cert.pfx", "12345")

    appearance = SignatureCustomAppearance()
    appearance.font_size = 6
    appearance.font_family_name = "Times New Roman"
    appearance.digital_signed_label = "Signed by:"
    appearance.is_foreground_image = True  # show image on top

    signature.custom_appearance = appearance

    # Set the appearance image
    pdf_signature.signature_appearance = image_path

    pdf_signature.sign(1, True, rect, signature)
    pdf_signature.save(data_dir + "DigitallySign_out.pdf")
```
