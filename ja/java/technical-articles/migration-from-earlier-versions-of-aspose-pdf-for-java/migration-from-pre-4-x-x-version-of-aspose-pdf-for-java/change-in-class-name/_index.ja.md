---
title: クラス名の変更
type: docs
weight: 20
url: /java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java の自動移植された MergedAPI は、その兄弟である Aspose.PDF for .NET から移植され、この移行中にいくつかのクラス名が変更されました。以下に、移行活動後に名前が変更されたクラスのリストを示します。

{{% /alert %}}

## PdfPrivilege が DocumentPrivilege に変更されました

自動移植された Aspose.PDF for Java では、PdfPrivilege クラスが DocumentPrivilege に変更されました (.NET に従って)。

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = new com.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege が DocumentPrivilege に変更され、true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = new com.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // PdfPrivilege.AllowAll だった

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = new com.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40); // PdfPrivilege.Copy だった

fileSecurity4.close();
```