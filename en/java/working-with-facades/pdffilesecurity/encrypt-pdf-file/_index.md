---
title: Encrypt PDF File
linktitle: Encrypt PDF File
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: Learn how to encrypt a PDF and configure permissions in Java with the PdfFileSecurity facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Encrypt PDF files and define user permissions in Java
Abstract: Learn how to encrypt a PDF with Aspose.PDF for Java. The Java example set covers password-based encryption with restricted privileges, permission-focused encryption, and AES-based encryption with a 256-bit key size.
---
## Encrypt PDF file

Use `PdfFileSecurity` when you need to protect a PDF with passwords and privilege rules.

### Steps

1. Create a `PdfFileSecurity` instance.
2. Bind the source PDF with `bindPdf`.
3. Build a `DocumentPrivilege` object that matches the allowed actions.
4. Call the appropriate `encryptFile` overload for the key size and algorithm you need.
5. Save the secured file and close the object.

### Java examples

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
