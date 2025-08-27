---
title: Securing and signing PDF in Python
linktitle: Securing and signing in PDF
type: docs
weight: 210
url: /python-net/securing-and-signing/
description: This section describes the features of using a signature and securing your PDF document using Python
lastmod: "2025-06-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Sign PDF documents with Python
Abstract: This section of the Aspose.PDF for Python via .NET documentation provides comprehensive guidance on securing and signing PDF documents programmatically. It covers essential topics including password protection, encryption algorithms, applying and verifying digital signatures, certificate handling, and document permissions. Developers will learn how to implement various levels of security to protect sensitive content, ensure document integrity, and comply with regulatory standards. The examples and API references enable quick integration of security features into Python applications, making it easy to safeguard PDF workflows with confidence.
---

This section explains how to securely apply digital signatures to PDF documents using Python Library. While the terms electronic signature and digital signature are sometimes used interchangeably, they are not the same. A digital signature is backed by a [certificate authority](https://en.wikipedia.org/wiki/Certificate_authority), providing a trusted seal that protects the document against tampering. In contrast, an electronic signature is typically used to indicate a person’s intent to sign a document, without the same level of security validation.

Aspose.PDF supports digital signatures:

- PKCS1 with RSA signature algorithm and SHA-1 digest.
- PKCS7 with RSA signature algorithm and SHA-1 digest.
- PKCS7 detached with DSA, RSA and ECDSA signature algorithms. The supported digest algorithms depend on the signature algorithm.
- Timestamp signature.

Digest algorithms for PKCS7 detached:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

It is recommended to avoid digital signatures with the SHA-1 digest algorithm due to its insecurity.

- [Digitally sign PDF file](/pdf/python-net/digitally-sign-pdf-file/)
- [Set Privileges, Encrypt and Decrypt PDF File](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extract Image and Signature Information](/pdf/python-net/extract-image-and-signature-information/)
- [Sign PDF Document From Smart Card](/pdf/python-net/sign-pdf-document-from-smart-card/)