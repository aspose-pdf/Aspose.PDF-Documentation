---
title: How to digitally sign PDF
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /php-java/digitally-sign-pdf-file/
description: Explore how to digitally sign PDF documents in PHP using Aspose.PDF to protect document integrity and verify authorship.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

When signing a PDF document using a signature, you basically confirm that its contents should remain “as is”. Consequently, any changes made afterwards invalidate the signature and thus, you know if the document has been altered. Certifying a document first, allows you to specify the changes that a user can make to the document without invalidating the certification.

In other words, the document would still be considered to retain its integrity and the recipient could still trust the document. For further details, please visit Certifying and signing a PDF.

## Sign PDF with digital signatures

```php

    // Open document
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // Use PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // Save output PDF file
    $signature->save($outputFile);    
    $document->close();
```

