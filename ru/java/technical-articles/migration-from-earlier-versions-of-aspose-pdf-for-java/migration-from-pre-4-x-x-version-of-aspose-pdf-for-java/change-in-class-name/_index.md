---
title: Изменение имени класса
type: docs
weight: 20
url: /ru/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Автопортированная MergedAPI Aspose.PDF для Java портирована из своего аналога Aspose.PDF для .NET, и в ходе этой миграции имена некоторых классов были изменены. Ниже приведен список классов, имена которых были изменены после миграции.

{{% /alert %}}

## PdfPrivilege изменен на DocumentPrivilege

В автопортированном Aspose.PDF для Java класс PdfPrivilege изменен на DocumentPrivilege (как в .NET).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege стал DocumentPrivilege, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // было PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40);// было PdfPrivilege.Copy

fileSecurity4.close();
```