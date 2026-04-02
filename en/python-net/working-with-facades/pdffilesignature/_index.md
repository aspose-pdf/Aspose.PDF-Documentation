---
title: PdfFileSignature Class
type: docs
weight: 60
url: /python-net/pdffilesignature-class/
description: Explore how to add, verify, and remove digital signatures from PDF documents in Python using the PDFFileSignature class with Aspose.PDF.
lastmod: "2026-01-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


## Common setup

Before applying any signature, define a few helper functions that create the `PdfFileSignature` object, set the signature rectangle, load the certificate, and prepare a reusable `PKCS7` signature object.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```