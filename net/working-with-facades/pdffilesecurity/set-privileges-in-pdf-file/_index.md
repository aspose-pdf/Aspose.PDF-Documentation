---
title: Set Privileges in PDF with PdfFileSecurity
type: docs
weight: 10
url: /net/set-privileges-in-pdf-file/
description: This topic explains how to Encrypt, Decrypt and Set Privileges on PDF File using PdfFileSecurity Class Class.
lastmod: "2021-12-17"
---
## Set Privileges on an Existing PDF File

To set a PDF file's privileges, create a [PdfFileSecurity](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and call the SetPrivilege method. You can specify the privileges using the DocumentPrivilege object and then pass this object to the SetPrivilege method. The following code snippet shows you how to set the privileges of a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Security-Signatures-SetPrivilegesOnFile-SetPrivilegesOnFile.cs" >}}

## Change Password of a PDF File

In order to change password of a PDF file, you need to create [PdfFileSecurity](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [ChangePassword](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) method. You need to pass existing owner password and new user and owner passwords to the [ChangePassword](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) method.

{{% alert color="primary" %}}

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

{{% /alert %}}

The following code snippet shows you how to change passwords of a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Security-Signatures-ChangeFilePassword-ChangeFilePassword.cs" >}}

## Remove Extended Rights Feature from the PDF

PDF documents support the extended rights feature to enable end-user to fill data into form fields by using Adobe Acrobat Reader and then save a copy of the filled form. However, it ensures that PDF file is not modified and if any modification to the structure of the PDF is made, the extended rights feature is lost. When viewing such a document, an error message is displayed, stating that extended rights are removed because the document was modified. Recently, we received a requirement to remove extended rights from PDF document.

To remove the extended rights from a PDF file, a new method named RemoveUsageRights() has been added to the PdfFileSignature class. Another method named ContainsUsageRights() is added to determine if source PDF contains extended rights.

{{% alert color="primary" %}}
Starting Aspose.PDF for .NET 9.5.0, names of following methods are updated. Please note that the previous methods are still in the API but they have been marked as obsolete and will be removed. Therefore, its recommended to try using the updated methods.

- The IsContainSignature(.) method was renamed ContainsSignature(..).
- The IsCoversWholeDocument(..) method was renamed CoversWholeDocument(..).
{{% /alert %}}

The following code shows ho to remove usage rights from the document:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Security-Signatures-RemoveRights-RemoveRights.cs" >}}
