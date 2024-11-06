---
title: 클래스 이름 변경
type: docs
weight: 20
url: ko/java/change-in-class-name/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java의 자동 포팅된 MergedAPI는 .NET의 Aspose.PDF에서 포팅되었으며, 이 마이그레이션 중 일부 클래스의 이름이 변경되었습니다. 아래에 마이그레이션 후 이름이 변경된 클래스 목록이 지정되어 있습니다.

{{% /alert %}}

## PdfPrivilege가 DocumentPrivilege로 변경됨

자동 포팅된 Aspose.PDF for Java에서 PdfPrivilege 클래스는 DocumentPrivilege로 변경되었습니다 (.NET에 따라).

```java
String inFile = "c:/pdftest/Alignment_DOM.pdf";

String outFile1 = "c:/pdftest/TestEncrypt1.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile1);

// PdfPrivilege가 DocumentPrivilege로 변경됨, true -> KeySize.x128

fileSecurity.encryptFile(null, "mypassword", com.aspose.pdf.facades.DocumentPrivilege.getScreenReaders(), com.aspose.pdf.facades.KeySize.x128);

fileSecurity.close();

String outFile2 = "c:/pdftest/TestEncrypt2.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity2 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile2);

fileSecurity2.encryptFile("", "owner", com.aspose.pdf.facades.DocumentPrivilege.getAllowAll(), com.aspose.pdf.facades.KeySize.x128); // PdfPrivilege.AllowAll이었습니다.

fileSecurity2.close();

String outFile4 = "c:/pdftest/TestEncrypt4.pdf";

com.aspose.pdf.facades.PdfFileSecurity fileSecurity4 = newcom.aspose.pdf.facades.PdfFileSecurity(inFile, outFile4);

fileSecurity4.encryptFile("user", "owner", com.aspose.pdf.facades.DocumentPrivilege.getCopy(), com.aspose.pdf.facades.KeySize.x40); // PdfPrivilege.Copy였습니다.

fileSecurity4.close();
```