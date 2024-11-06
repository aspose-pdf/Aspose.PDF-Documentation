---
title: Perubahan dalam nama kelas
type: docs
weight: 20
url: id/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

MergedAPI autoported dari Aspose.PDF untuk Java di-port dari saudara Aspose.PDF untuk .NET dan selama migrasi ini, nama beberapa kelas telah diubah. Di bawah ini adalah daftar kelas yang namanya telah diubah setelah aktivitas migrasi.

{{% /alert %}}

## PdfPrivilege diubah menjadi DocumentPrivilege

Dalam Aspose.PDF untuk Java yang di-port secara otomatis, kelas PdfPrivilege diubah menjadi DocumentPrivilege (sesuai .NET).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege menjadi DocumentPrivilege, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // sebelumnya PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40);// sebelumnya PdfPrivilege.Copy

fileSecurity4.close();
```