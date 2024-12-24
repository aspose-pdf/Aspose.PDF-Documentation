---
title: Change Password of PDF File
type: docs
weight: 40
url: /net/change-password/
description: Explore how to modify the password of a PDF document in .NET to improve file security with Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "Easily enhance your PDF security by changing its password with the PdfFileSecurity class. This functionality allows users to modify both user and owner passwords, ensuring robust protection against unauthorized access while managing permissions effectively. Optimize your document security settings effortlessly with a straightforward implementation",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Change Password of a PDF File

In order to change password of a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) method. You need to pass existing owner password and new user and owner passwords to the [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) method.

{{% alert color="primary" %}}

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

{{% /alert %}}

The following code snippet shows you how to change passwords of a PDF file.

```csharp
// For complete examples and data files, check for https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ChangePassword()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)
        {
            using (PdfFileSecurity fileSecurity = new PdfFileSecurity())
            {
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                // Save the document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```

