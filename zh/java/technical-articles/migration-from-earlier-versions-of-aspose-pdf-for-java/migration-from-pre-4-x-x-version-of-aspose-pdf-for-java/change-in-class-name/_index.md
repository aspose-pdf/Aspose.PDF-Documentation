---
title: 类名更改
type: docs
weight: 20
url: /zh/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java 的自动移植 MergedAPI 是从其兄弟 Aspose.PDF for .NET 移植过来的，在此迁移过程中，一些类的名称发生了变化。下面列出了在迁移活动后名称发生变化的类。

{{% /alert %}}

## PdfPrivilege 更改为 DocumentPrivilege

在自动移植的 Aspose.PDF for Java 中，PdfPrivilege 类更改为 DocumentPrivilege（与 .NET 一致）。

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege 改为 DocumentPrivilege, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // 原为 PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40);// 原为 PdfPrivilege.Copy

fileSecurity4.close();
```