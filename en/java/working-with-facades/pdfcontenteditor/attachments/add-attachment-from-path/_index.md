---
title: Add Attachment from Path
linktitle: Add Attachment from Path
type: docs
weight: 20
url: /java/add-attachment-from-path/
description: Review the current Java coverage for adding attachments with PdfContentEditor and see how it relates to path-based attachment workflows.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Check Java sample coverage for path-based PDF attachments
Abstract: The current `PdfContentEditorExamples` source for Aspose.PDF for Java does not include a dedicated `addAttachmentFromPath` method. The nearest Java coverage is `addAttachment`, which opens the attachment as a stream before calling the facade API and saving the updated PDF.
---
There is no dedicated Java example named `addAttachmentFromPath` in the current `PdfContentEditorExamples` class.

For the closest source-backed workflow, see `addAttachment`, which demonstrates how to:

- bind the source PDF
- open the attachment content as a stream
- call `addDocumentAttachment(...)`
- save the updated document
