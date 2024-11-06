---
title: Mudança no nome da classe
type: docs
weight: 20
url: pt/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

O MergedAPI autoportado do Aspose.PDF para Java é portado de seu parente Aspose.PDF para .NET e durante esta migração, os nomes de algumas classes foram alterados. Especificado abaixo está a lista de classes cujos nomes foram alterados após a atividade de migração.

{{% /alert %}}

## PdfPrivilege alterado para DocumentPrivilege

No Aspose.PDF autoportado para Java, a classe PdfPrivilege foi alterada para DocumentPrivilege (conforme .NET).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege veio para DocumentPrivilege, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // era PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40);// era PdfPrivilege.Copy

fileSecurity4.close();
```