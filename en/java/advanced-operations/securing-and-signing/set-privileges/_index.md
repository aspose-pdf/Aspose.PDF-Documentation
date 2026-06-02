---
title: Encrypt and Decrypt PDF Files in Java
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Learn how to set PDF privileges, encrypt files, decrypt protected PDFs, and change passwords in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set PDF permissions and manage encryption in Java
Abstract: This article explains how to secure PDF files using Aspose.PDF for Java. It covers encrypting documents with user and owner passwords, applying permission restrictions, decrypting files, changing passwords, and setting privileges with or without exception-safe methods.
---
Aspose.PDF for Java exposes PDF security operations through the `PdfFileSecurity` facade.

## Encrypt a PDF with user and owner passwords

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to encrypt a PDF with user and owner passwords.
3. Save the document or inspect the result, depending on the scenario.

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
```

## Encrypt a PDF with a specific algorithm

`encryptPdfWithEncryptionAlgorithm` uses `KeySize.x256` together with `Algorithm.AES` to apply stronger encryption settings.

## Decrypt a protected PDF

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to decrypt a protected PDF.
3. Save the document or inspect the result, depending on the scenario.

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

The example set also includes `tryDecryptPdfWithoutException`, which returns `false` instead of throwing when decryption fails.

## Change passwords and reset security

The `PdfFileSecurityExamples` class demonstrates:

- `changeUserAndOwnerPassword` to replace both passwords.
- `changePasswordAndResetSecurity` to change passwords and reapply privileges in one step.
- `tryChangePasswordWithoutException` for a non-throwing password-change flow.

## Set document privileges

To restrict actions such as printing and copying:

1. Load the PDF document or object that will be updated.
2. Apply the settings shown in the example to set document privileges.
3. Save the document if the change should persist.

```java
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
```

You can also use `setPdfPrivilegesWithoutPasswords` and `trySetPdfPrivilegesWithoutException` depending on the workflow.
