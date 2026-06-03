---
title: Change Password of PDF File
type: docs
weight: 10
url: /java/change-password/
description: Learn how to change PDF passwords in Java with the PdfFileSecurity facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Update PDF user and owner passwords in Java
Abstract: Learn how to change PDF passwords with Aspose.PDF for Java. The Java example set covers changing user and owner passwords directly, changing passwords while resetting security settings, and a try-style password change workflow that returns a success flag.
---
## Change password of PDF file

Use `PdfFileSecurity` when you need to rotate credentials on an already secured PDF.

### Steps

1. Create a `PdfFileSecurity` instance.
2. Bind the secured PDF with `bindPdf`.
3. Call the appropriate `changePassword` overload, depending on whether you also want to reset privileges and key size.
4. Save the updated file and close the security object.

### Java examples

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
