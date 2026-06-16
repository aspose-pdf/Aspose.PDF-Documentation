---
title: Set Privileges on an Existing PDF File
linktitle: Set Privileges on an Existing PDF File
type: docs
weight: 40
url: /java/set-privileges/
description: Learn how to set PDF privileges in Java with the PdfFileSecurity facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF permissions and access controls in Java
Abstract: Learn how to control PDF permissions with Aspose.PDF for Java. The Java example set covers applying privileges without passwords, applying privileges with user and owner passwords, and a try-style privilege update workflow that returns a success flag.
---
## Set privileges on an existing PDF file

Use this workflow when you need to change what users can do with an existing PDF.

### Steps

1. Create a `PdfFileSecurity` instance.
2. Bind the source PDF with `bindPdf`.
3. Create a `DocumentPrivilege` object and configure the allowed actions.
4. Call the appropriate `setPrivilege` or `trySetPrivilege` overload.
5. Save the result if the update succeeds, then close the object.

### Java examples

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
