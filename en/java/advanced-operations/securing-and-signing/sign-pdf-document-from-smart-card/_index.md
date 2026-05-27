---
title: Sign PDF Documents from a Smart Card in Java
linktitle: PDF Signing with Smart Card
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Review the current Java example coverage for certificate-based PDF signing in Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certificate-based PDF signing coverage in the current Java example set
Abstract: This page describes the current scope of signing examples available in the Java documentation source tree. The repository includes certificate-based PDF signing examples with PFX or PKCS7 credentials, but it does not currently include a dedicated smart-card certificate-store example for Java.
---
The current Java example set in this repository does not contain a dedicated smart-card signing sample that reads certificates directly from a hardware token or operating-system certificate store.

Available signing coverage is provided by `PdfFileSignatureExamples.java`, which includes:

- Signing a PDF with a certificate object.
- Signing a PDF with basic certificate parameters.
- Certifying a PDF with `DocMDPSignature`.
- Verifying signatures and extracting embedded certificates.

If you need hardware-backed signing, use the certificate-based signing APIs shown in the Java signing examples as the supported baseline, then integrate your certificate-loading flow separately in your application code.
