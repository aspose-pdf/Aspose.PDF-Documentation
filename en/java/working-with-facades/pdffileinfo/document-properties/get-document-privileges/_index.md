---
title: Get Document Privileges
type: docs
weight: 10
url: /java/get-document-privileges/
description: Learn how to inspect PDF document privileges in Java with the PdfFileInfo facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Retrieve PDF Document Privileges Using Aspose.PDF for Java
Abstract: Learn how to retrieve document privileges with Aspose.PDF for Java. The Java example creates a PdfFileInfo object, reads its DocumentPrivilege settings, and prints the permission flags for printing, copying, modification, annotations, form filling, screen readers, and assembly.
---
## Get document privileges

Use `PdfFileInfo.getDocumentPrivilege()` to inspect what operations the current PDF allows.

### Steps

1. Create a `PdfFileInfo` object for the input PDF.
2. Call `getDocumentPrivilege()` to retrieve the privilege set.
3. Read the relevant boolean flags from the returned `DocumentPrivilege` object.
4. Close the `PdfFileInfo` instance when finished.

### Java example

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
