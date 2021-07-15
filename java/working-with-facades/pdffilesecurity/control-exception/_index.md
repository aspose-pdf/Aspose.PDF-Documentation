---
title: Control Exception PDF File
type: docs
weight: 30
url: /java/control-exception/
description: This topic explains how control exception on PDF File using PdfFileSecurity Class Class.
lastmod: "2021-06-05"
draft: false
---

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Decrypt PDF document

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Something wrong...");
            System.out.println("Last exception: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```