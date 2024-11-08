---
title: تغيير في اسم الفئة
type: docs
weight: 20
url: /ar/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تم ترحيل MergedAPI التلقائي للـ Aspose.PDF لـ Java من شقيقه Aspose.PDF لـ .NET وخلال هذه الهجرة، تم تغيير أسماء بعض الفئات. يتم تحديد أدناه قائمة الفئات التي تم تغيير أسمائها بعد نشاط الهجرة.

{{% /alert %}}

## تم تغيير PdfPrivilege إلى DocumentPrivilege

في Aspose.PDF لـ Java التلقائي، تم تغيير فئة PdfPrivilege إلى DocumentPrivilege (كما هو الحال في .NET).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege جاء إلى DocumentPrivilege، true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // كانت PdfPrivilege.AllowAll

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40);// كانت PdfPrivilege.Copy

fileSecurity4.close();
```