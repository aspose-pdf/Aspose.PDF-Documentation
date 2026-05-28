---
title: Revision and Permissions
type: docs
weight: 40
url: /java/revision-permissions/
description: Review the current Java sample coverage for revision and certification-permission inspection with PdfFileSignature.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Check Java sample coverage for revision and signature permission inspection
Abstract: The current `PdfFileSignatureExamples` source for Aspose.PDF for Java does not include a dedicated example for reading signature revision numbers, total document revisions, or certified access permissions from an existing PDF. The nearest related Java coverage is `certifyPdfWithMdpSignature`, which applies `DocMDPAccessPermissions.FillingInForms` during certification.
---
There is no dedicated Java example for reading revision counts or certification permission data from an existing signed PDF in the current `PdfFileSignatureExamples` class.

The nearest related workflow is `certifyPdfWithMdpSignature`, which demonstrates how certification permissions are assigned when a document is signed.
