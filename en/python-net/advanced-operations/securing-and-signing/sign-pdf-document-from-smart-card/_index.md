---
title: How to add Smart Card signature to PDF
linktitle: PDF Signing with Smart Card
type: docs
weight: 30
url: /python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for Python via .NET allows you to sign PDF documents from a smart card using signature field.
lastmod: "2025-06-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Sign PDF documents from a Smart Card with Python
Abstract: This guide explains how to digitally sign PDF documents using a smart card with Aspose.PDF for Python via .NET. It demonstrates how to access certificates stored on hardware devices (such as USB tokens or smart cards) through the Windows Certificate Store and apply them for signing PDF files. The documentation includes code examples that show how to locate the appropriate certificate, configure signature properties, and embed the digital signature into the PDF. This enables secure, hardware-backed signing in compliance with digital signature standards, suitable for high-trust enterprise and legal workflows.  
---

Aspose.PDF provides robust capabilities for integrating visual and cryptographic signature components, ensuring both authenticity and professional presentation in digitally signed PDF documents.

## Sign With Smart Card Using Signature Field

This example demonstrates how to digitally sign a PDF document using an external certificate with Aspose.PDF for Python and apply a custom signature appearance image:

1. Opening the PDF document.

1. Creating a PdfFileSignature object and binding it to the document.

1. Retrieving a local digital certificate using a custom method (get_local_certificate()).

1. Setting up an ExternalSignature based on the selected certificate.

1. Applying a custom signature appearance image (e.g., a company logo or handwritten signature).

1. Digitally signing the first page of the document with specified metadata (reason, contact, location).

1. Saving the signed document to a new output file.

This method is ideal for cases where signatures must be applied programmatically using external certificates—such as hardware tokens, certificate stores, or trusted providers—and presented with a personalized visual layout.

Following are the code snippets to sign a PDF document from a smart card:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## Verify Digital Signatures

This code snippet demonstrates how to verify digital signatures in a PDF document using Aspose.PDF for Python:

1. Opening the PDF file.

1. Creating a 'PdfFileSignature object' and binding it to the document.

1. Retrieving the list of all signature field names using 'get_signature_names()'.

1. Iterating through each signature and verifying its validity with 'verify_signature()'.

1. Raising an exception if any signature fails verification.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## Sign with External Certificate

This code snippet demonstrates how to add and sign a digital signature field in a PDF document using Aspose.PDF for Python with an external certificate:

1. Opening the PDF file as a binary stream.

1. Creating a SignatureField and placing it on the first page of the document at a specified position.

1. Retrieving a local digital certificate using a custom method (get_local_certificate()).

1. Setting up an ExternalSignature with metadata such as authority, reason, and contact information.

1. Assigning a unique field name to the signature field (partial_name = "sig1").

1. Adding the signature field to the form fields of the PDF.

1. Signing the field with the external certificate.

1. Saving the signed document to an output file.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```

