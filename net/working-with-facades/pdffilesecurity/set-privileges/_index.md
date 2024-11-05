---
title: Set Privileges on PDF 
type: docs
weight: 50
url: /net/set-privileges/
description: This topic explains how to set privileges on an existing PDF file using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## Set Privileges on an Existing PDF File

To set a PDF file's privileges, create a [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and call the SetPrivilege method. You can specify the privileges using the DocumentPrivilege object and then pass this object to the SetPrivilege method. The following code snippet shows you how to set the privileges of a PDF file.

```csharp
public static void SetPrivilege1()
{
    // Create DocumentPrivileges object
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Create PdfFileSecurity object
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

See the following method with specifying a password:

```csharp
public static void SetPrivilege2()
{
    // Create DocumentPrivileges object
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Create PdfFileSecurity object
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## Remove Extended Rights Feature from the PDF

PDF documents support the extended rights feature to enable end-user to fill data into form fields by using Adobe Acrobat Reader and then save a copy of the filled form. However, it ensures that PDF file is not modified and if any modification to the structure of the PDF is made, the extended rights feature is lost. When viewing such a document, an error message is displayed, stating that extended rights are removed because the document was modified. Recently, we received a requirement to remove extended rights from PDF document.

To remove the extended rights from a PDF file, a new method named RemoveUsageRights() has been added to the PdfFileSignature class. Another method named ContainsUsageRights() is added to determine if source PDF contains extended rights.

{{% alert color="primary" %}}
Starting Aspose.PDF for .NET 9.5.0, names of following methods are updated. Please note that the previous methods are still in the API but they have been marked as obsolete and will be removed. Therefore, its recommended to try using the updated methods.

- The IsContainSignature(.) method was renamed ContainsSignature(..).
- The IsCoversWholeDocument(..) method was renamed CoversWholeDocument(..).
{{% /alert %}}

The following code shows ho to remove usage rights from the document:

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```