---
title: Decrypt PDF File
linktitle: Decrypt PDF File
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Learn how to decrypt a PDF in Java with the PdfFileSecurity facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove PDF security restrictions with Java
Abstract: Learn how to decrypt a PDF with Aspose.PDF for Java. The Java example set includes direct owner-password decryption and a try-style decryption workflow that lets you handle failure without raising an exception.
---
## Decrypt PDF file

Use this workflow when you have the owner password and need to remove security from a PDF.

### Steps

1. Create a `PdfFileSecurity` instance.
2. Bind the encrypted PDF with `bindPdf`.
3. Call `decryptFile` or `tryDecryptFile` with the owner password.
4. Save the output if decryption succeeds.
5. Close the security object.

### Java examples

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
