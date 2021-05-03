---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /java/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for Java that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-04-16"
---

## What's new in Aspose.PDF 21.02

Aspose.PDF v21.02 Sign PDF with PAdES LTV Signatures

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Sign PDF with PAdES LTV Signatures
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```