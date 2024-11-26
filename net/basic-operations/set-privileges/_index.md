---
title: Set Privileges, Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 70
url: /net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encrypt PDF File with C# using Different Encryption Types and Algorithms. Also, decrypt PDF Files using Owner Password.
lastmod: "2024-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges, Encrypt and Decrypt PDF",
    "alternativeHeadline": "Set PDF Privileges and Secure with Encryption with C#",
    "abstract": "The new feature allows users to efficiently encrypt and decrypt PDF files using C# with a variety of encryption types and algorithms. By utilizing user and owner passwords, it provides robust control over document access and permissions, ensuring the confidentiality and integrity of PDF content while simplifying security management for developers",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1586",
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
                "telephone": "\u002B1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Encrypt PDF File with C# using Different Encryption Types and Algorithms. Also, decrypt PDF Files using Owner Password."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Set Privileges on an Existing PDF File

To set privileges on a PDF file, create an object of the [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege)class and specify the rights you want to apply to the document. Once the privileges have been defined, pass this object as an argument to the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object's [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) method. The following code snippet shows you how to set the privileges of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Load a source PDF file
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Instantiate Document Privileges object
    // Apply restrictions on all privileges
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Only allow screen reading
    documentPrivilege.AllowScreenReaders = true;
    // Encrypt the file with User and Owner password.
    // Need to set the password, so that once the user views the file with user password,
    // Only screen reading option is enabled
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Save updated document
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```

## Encrypt PDF File using Different Encryption Types and Algorithms

You can use the [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object to encrypt a PDF file. You can pass the user password, owner password, and permissions to the [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) method. In addition to that, you can pass any value of the [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) enum. This enum provides different combinations of encryption algorithms and key sizes. You can pass the value of your choice. Finally, save the encrypted PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.

>Please specify different user and owner passwords while encrypting the PDF file.

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The following code snippet shows you how to encrypt PDF files.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Open document
Document document = new Document(dataDir +  "Encrypt.pdf");
// Encrypt PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
// Save updated PDF
document.Save(dataDir + "Encrypt_out.pdf");
```

## Decrypt PDF File using Owner Password

Increasingly, users are exchanging PDF files with encryption to prevent unauthorized access to documents, such as printing/copying/sharing / extracting information about the contents of a PDF file. Today, it is the best choice for encrypting a PDF file because it maintains the confidentiality and integrity of the content.
In this regard, there is a need to access the encrypted PDF file, since such access can only be obtained by an authorized user. Also, people are looking for various solutions to decrypt PDF files over the Internet.

It is better to solve this problem once by using the Aspose.PDF library.

In order to decrypt the PDF file, you first need to create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object and open the PDF using the owner's password. After that, you need to call [Decrypt](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. Finally, save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. The following code snippet shows you how to decrypt the PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Open document
Document document = new Document(dataDir +  "Decrypt.pdf", "password");
// Decrypt PDF
document.Decrypt();
// Save updated PDF
document.Save(dataDir + "Decrypt_out.pdf");
```

## Change Password of a PDF File

If you want to change the password of a PDF file, you first need to open the PDF file using owner password with the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. After that, you need to call the [ChangePasswords](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. You need to pass the current owner password along with the new user password and new owner password to this method. Finally, save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)  object.

>- The User password, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
>- The Owner password, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The following code snippet shows you how to change the password of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Open document
Document document = new Document(dataDir +  "ChangePassword.pdf", "owner");
// Change password
document.ChangePasswords("owner", "newuser", "newowner");
// Save updated PDF
document.Save(dataDir + "ChangePassword_out.pdf");
```

## How to - determine if the source PDF is password protected

**Aspose.PDF for .NET** provides great capabilities of dealing with PDF documents. When using Document class of Aspose.PDF namespace to open a PDF document that is password-protected, we need to provide the password information as an argument to Document constructor and in case this information is not provided, an error message is generated. In fact, when trying to open a PDF file with Document object, the constructor is trying to read the contents of PDF file and in case correct password is not provided, an error message is generated (it happens to prevent unauthorized access of document).

When dealing with encrypted PDF files, you may come across the scenario where you would be interested to detect if a PDF has an open password and/or an edit password. Sometimes there are documents that do not require password information while opening them, but they require information in order to edit the contents of the file. So in order to fulfill the above requirements, PdfFileInfo class present under Aspose.PDF.Facades provides the properties which can help in determining the required information.

### Get information about PDF document security

PdfFileInfo contains three properties to get information about PDF document security.

1. property PasswordType returns PasswordType enumeration value:
    - PasswordType.None - the document is not password protected.
    - PasswordType.User - the document was opened with user (or document open) password.
    - PasswordType.Owner - the document was opened with owner (or permissions, edit) password.
    - PasswordType.Inaccessible - the document is password protected but the password is needed to open it while an invalid password (or no password) was supplied.
2. boolean property HasOpenPassword - is used to determine if the input file requires a password, when opening it.
3. boolean property HasEditPassword - its used to determine if the input file requires a password to edit its contents.

### Determine correct password from Array

Sometimes there is a requirement to determine the correct password from an array of passwords and open the document with the correct password. The following code snippet demonstrates the steps to iterate through the array of passwords and try opening the document with the correct password.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Load source PDF file
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Determine if the source PDF is encrypted
Console.WriteLine("File is password protected " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document document = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (document.Pages.Count > 0)
        {
            Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
        }
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
