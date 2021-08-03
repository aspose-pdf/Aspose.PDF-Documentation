---
title: Set Privileges on an Existing PDF File
type: docs
weight: 50
url: /java/set-privileges/
description: This topic explains how to set privileges on an existing PDF file using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## Set Privileges on an Existing PDF File (facades)

To set a PDF file's privileges, create a [PdfFileSecurity](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSecurity) class object and bind the input PDF using binPdf method. Then you have to call the setPrivilege method to set privileges. You can specify the privileges using the [DocumentPrivilege](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/DocumentPrivilege) object and then pass this object to the setPrivilege method and save the output PDF using save method.

The following code snippet shows you how to set the privileges of a PDF file.

```java
public static void SetPrivilege1() {
        // Create DocumentPrivileges object
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Create PdfFileSecurity object
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```

See the following method with specifying a password:

```java
 public static void SetPrivilege2() {
        // Create DocumentPrivileges object
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Create PdfFileSecurity object
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```