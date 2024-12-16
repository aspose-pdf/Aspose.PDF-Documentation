---
title: Changement de nom de classe
type: docs
weight: 20
url: /fr/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

L'API fusionnée autoportée d'Aspose.PDF pour Java est portée à partir de son homologue Aspose.PDF pour .NET et lors de cette migration, les noms de certaines classes ont été modifiés. Vous trouverez ci-dessous la liste des classes dont les noms ont été modifiés après l'activité de migration.

{{% /alert %}}

## PdfPrivilege changé en DocumentPrivilege

Dans Aspose.PDF pour Java autoporté, la classe PdfPrivilege est changée en DocumentPrivilege (comme dans .NET).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = new com.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege est devenu DocumentPrivilege, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = new com.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // était PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = new com.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40);// était PdfPrivilege.Copy

fileSecurity4.close();
```