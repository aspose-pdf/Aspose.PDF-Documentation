---
title: PdfFileSignature Class
type: docs
weight: 70
url: /java/pdffilesignature-class/
description: This section explains how to work with Aspose.PDF Facades using PdfFileSignature class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Digital Signature in a PDF File (facades)

[**PdfFileSignature**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSignature) class allows you to add signature in a PDF file. You need to create an object of [**PdfFileSignature**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSignature) class using input and output PDF files. You also need to create a Rectangle object at which you want to add the signature and in order to set appearance you can specify an image using setSignatureAppearance property of the [**PdfFileSignature**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSignature) object.

Aspose.Pdf.Facades also provides different kinds of signatures like PKCS#1, PKCS#7, and PKCS#7Detached. In order to create a signature of a specific type, you need to create an object of the particular class like PKCS1 , PKCS7 or PKCS7Detached using the certificate file and the password.

Once the object of a particular signature type is created, you can use the sign method of the [**PdfFileSignature**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSignature) class to sign the PDF and pass the particular signature object to this class. You can also specify other attributes for this method. Finally, you need to save the signed PDF using save method of the [**PdfFileSignature**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSignature) class. The following code snippet shows you how to add signature in a PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-SecurityAndSignatures-AddDigitalSignatureInAPDFFile-.java" >}}

