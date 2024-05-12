---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: /python-cpp/encrypt-decrypt-pdf/
description: Encrypt and Decrypt PDF File with Python via C++ application.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encrypt PDF File using Different Encryption Types and Algorithms

One effective way to safeguard PDF files is through encryption. In this article, we'll explore how to encrypt PDF documents using Python with the help of the Aspose.PDF library.

PDF encryption involves scrambling the content of a PDF document using cryptographic algorithms to prevent unauthorized access. Encrypted PDF files require a password to open and may have restrictions on actions like printing, copying, and editing.

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it’s not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The following code snippet shows you how to encrypt PDF files.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Set the directory path for the sample files
    dataDir = os.path.join(os.getcwd(), "samples")

    # Set the input file path
    input_file = os.path.join(dataDir, "sample.pdf")

    # Set the output file path
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # Load the PDF document using AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # Define the permissions for the encrypted document
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # Define the encryption algorithm to be used
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # Encrypt the document with the specified user and owner passwords, permissions, and encryption algorithm
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # Save the encrypted document to the specified output file
    document.save(output_file)
```

## Decrypt PDF File using Owner Password



```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Set the directory path for the sample files
    dataDir = os.path.join(os.getcwd(), "samples")

    # Set the input file path
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # Set the output file path
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # Create a new instance of the Document class from the AsposePDFPythonWrappers module
    document = apw.Document(input_file, "owner")

    # Decrypt the document using the decrypt() method
    document.decrypt()

    # Save the decrypted document to the output file path using the save() method
    document.save(output_file)
```

