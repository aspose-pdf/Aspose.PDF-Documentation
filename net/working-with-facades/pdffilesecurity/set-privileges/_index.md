---
title: Set Privileges on an Existing PDF File
type: docs
weight: 50
url: /net/set-privileges/
description: This topic explains how to set privileges on an existing PDF file using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## Set Privileges on an Existing PDF File

To set a PDF file's privileges, create a [PdfFileSecurity](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/pdffilesecurity) object and call the SetPrivilege method. You can specify the privileges using the DocumentPrivilege object and then pass this object to the SetPrivilege method. The following code snippet shows you how to set the privileges of a PDF file.

```csharp
public static void SetPrivilege1()
 {
    // Create DocumentPrivileges object
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Create PdfFileSecurity object
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

See the following method with specifying a password:

```csharp
 public static void SetPrivilege2()
 {
    // Create DocumentPrivileges object
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Create PdfFileSecurity object
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```