---
title: Cambio en el nombre de la clase
type: docs
weight: 20
url: /java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

El MergedAPI autoportado de Aspose.PDF para Java se ha portado de su homólogo Aspose.PDF para .NET y durante esta migración, los nombres de algunas clases han cambiado. A continuación se especifica la lista de clases cuyos nombres han cambiado después de la actividad de migración.

{{% /alert %}}

## PdfPrivilege cambiado a DocumentPrivilege

En Aspose.PDF para Java autoportado, la clase PdfPrivilege se ha cambiado a DocumentPrivilege (según .NET).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege cambiado a DocumentPrivilege, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // era PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40); // era PdfPrivilege.Copy

fileSecurity4.close();
```