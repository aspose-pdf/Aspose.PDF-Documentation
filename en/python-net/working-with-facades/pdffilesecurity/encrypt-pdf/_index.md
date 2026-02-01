---
title: Encrypt PDF File
type: docs
weight: 10
url: /python-net/encrypt-pdf-file/
description: This topic explains how to Encrypt PDF File using PdfFileSecurity Class.
lastmod: "2026-01-05"
---

Encrypting a PDF document protects its content from unauthorized access from outside, especially during file sharing or archiving.

Confidential PDF documents can be encrypted and password protected. Only user who know the password will be able to decrypt, open and view these documents.

Let's take a look at how PDF encryption works with Aspose.PDF library.

## Encrypt PDF File using Different Encryption Types and Algorithms

In order to encrypt a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity) object and then call the [encrypt_file](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) method. You can pass user password, owner password and privileges to [encrypt_file](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/#methods) method. You also need to pass KeySize and Algorithm values to this method.

Review a possible list of such [CryptoAlgorithm](https://reference.aspose.com/pdf/python-net/aspose.pdf/cryptoalgorithm):

|**Member name**|**Value**|**Description**|
| :- | :- | :- |
|RC4x40|0|RC4 with key length 40.|
|RC4x128|1|RC4 with key length 128.|
|AESx128|2|AES with key length 128.|
|AESx256|3|AES with key length 256.|

The following code snippet shows you how to encrypt PDF file.

```python

from aspose.pdf.facades import (
    PdfFileSecurity,
    DocumentPrivilege,
    KeySize,
    Algorithm
)

def encrypt_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    output_pdf = data_dir + "SampleEncrypted_out.pdf"

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(input_pdf)

    # Encrypt PDF using 256-bit AES encryption
    file_security.encrypt_file(
        "User_P@ssw0rd",          # user password
        "OwnerP@ssw0rd",          # owner password
        DocumentPrivilege.print, # permissions
        KeySize.x256,             # key size
        Algorithm.AES             # encryption algorithm
    )

    # Save encrypted PDF
    file_security.save(output_pdf)
```

