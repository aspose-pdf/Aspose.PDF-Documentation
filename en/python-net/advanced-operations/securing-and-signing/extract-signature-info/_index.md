---
title: Extract Image and Signature Information
linktitle: Extract Image and Signature Information
type: docs
weight: 20
url: /python-net/extract-image-and-signature-information/
description: How to extract image and digital signature information from PDF documents using Aspose.PDF for Python.
lastmod: "2025-06-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get Image and Signature Info with Python
Abstract: This article demonstrates how to extract image and digital signature information from PDF documents using Aspose.PDF for Python. It provides step-by-step instructions and code samples for identifying, accessing, and saving embedded images, as well as retrieving metadata and validation status of digital signatures. 
---

## Extracting Image from Signature Field

Aspose.PDF for Python via .NET supports the feature to digitally sign the PDF files using the [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) class.

This code snippet demonstrates how to extract digital signature images from a PDF document using Aspose.PDF for Python.

Steps:

1. Opening the PDF document.
1. Iterating through the form fields to locate any SignatureField objects.
1. Extracting the image associated with each signature (if available).
1. Saving the extracted signature image as a JPEG file.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## Extract Signature Information

Aspose.PDF for Python via .NET supports the feature to digitally sign the PDF files using the SignatureField class. Currently, we can also determine the validity of the certificate but we cannot extract the whole certificate. The information which can be extracted is a public key, thumbprint, issuer, etc.

To extract signature information, we have introduced the [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) method to the [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) class. Please take a look at the following code snippet which demonstrates the steps to extract the certificate from SignatureField object:

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

You can get information about document signature algorithms.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## Checking signatures for compromise

This code snippet demonstrates how to detect compromised digital signatures in a PDF document using Aspose.PDF for Python.

The steps include:

1. Opening the PDF document.
1. Creating a 'SignaturesCompromiseDetector' instance to analyze the document.
1. Checking for any compromised (invalid or altered) digital signatures.
1. Printing the names of any compromised signatures found.
1. Reporting the signature coverage—indicating how much of the document is protected by valid signatures.

This feature is critical in use cases where document authenticity and integrity must be verified, such as legal, financial, and compliance-driven environments. It allows developers to automatically detect tampering or corruption of signed PDFs.

Aspose.PDF offers a comprehensive set of tools for digital signature validation, making it easier to build secure, signature-aware applications that uphold document trustworthiness.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```