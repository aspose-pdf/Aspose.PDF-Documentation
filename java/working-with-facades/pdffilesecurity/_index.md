---
title: Working with Facades
type: docs
weight: 112
url: /java/working-with-facades/
description: This section explains how to work with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-05-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## <ins>**Set Privileges on an Existing PDF File (facades)**
To set a PDF file's privileges, create a [PdfFileSecurity](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileSecurity) class object and bind the input PDF using binPdf method. Then you have to call the setPrivilege method to set privileges. You can specify the privileges using the [DocumentPrivilege](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/DocumentPrivilege) object and then pass this object to the setPrivilege method and save the output PDF using save method.

The following code snippet shows you how to set the privileges of a PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-SecurityAndSignatures-SetPrivilegesOnAnExistingPDFFile-.java" >}}