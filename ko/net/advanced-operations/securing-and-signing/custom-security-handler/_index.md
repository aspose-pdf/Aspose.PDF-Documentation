---
title: C#에서 사용자 지정 보안 처리기를 사용하여 디지털 서명 추가
linktitle: 사용자 지정 보안 처리기
type: docs
weight: 40
url: /ko/net/custom-security-handler/
description: C#에서 사용자 지정 보안 처리기를 사용하여 디지털 서명 추가
lastmod: "2025-04-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add digital signature with a custom security handler in C#",
    "alternativeHeadline": "Add digital signature with a custom security handler in C#",
    "abstract": "Aspose.PDF for .NET은 C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명을 추가하는 강력한 기능을 소개하여 문서의 무결성과 보안을 향상시킵니다. 사용자는 PKCS7 및 ECDSA를 지원하는 비분리형 및 분리형 서명을 포함한 다양한 서명 유형을 구현할 수 있으며, 특정 암호화 표준에 맞춘 사용자 지정 서명 프로세스를 허용합니다. 이 기능은 문서의 진위를 확인할 뿐만 아니라 타임스탬프 및 인증을 가능하게 하여 신뢰할 수 있는 문서 처리를 보장합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "digital signature, digitally sign PDF, C#, PDF signing, PKCS12 certificate, verify PDF signature, ECDSA signing, timestamp server, custom hash signing, custom security handler, Aspose.PDF for .NET",
    "wordcount": "1518",
    "proficiencyLevel": "Advanced",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/custom-security-handler/"
    },
    "dateModified": "2025-04-09",
    "description": "C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명을 추가합니다. C# 또는 VB.NET을 사용하여 디지털 서명된 PDF를 확인하거나 검증합니다."
}
</script>

원하는 암호화 알고리즘을 적용하여 자신만의 보안 처리기를 만들 수 있습니다.
Adobe Acrobat은 이러한 파일을 열 수 없지만 Aspose.Pdf를 사용하여 작업할 수 있습니다.
처리기를 만들려면 인터페이스를 구현해야 합니다:

```csharp
public interface ICustomSecurityHandler
{   
    string Filter { get; }     
	
    string SubFilter { get; }  
	
    int Version { get; }     
	
    int Revision { get; }
   
    int KeyLength { get; }
   
    byte[] EncryptPermissions(int permissions);
	
    byte[] GetOwnerKey(string userPassword, string ownerPassword);
  
    byte[] GetUserKey(string userPassword);
  
    void Initialize(EncryptionParameters parameters);
   
    byte[] CalculateEncryptionKey(string password);
   
    byte[] Encrypt(byte[] data, int objectNumber, int generation, byte[] key);
	
    byte[] Decrypt(byte[] data, int objectNumber, int generation, byte[] key);
   
    bool IsOwnerPassword(string password);
   
    bool IsUserPassword(string password);
}
```

인터페이스의 간단한 구현 예(데모용):

```csharp
/// <summary>
/// The custom security handler interface.
/// </summary>
class CustomSecurityHandler : ICustomSecurityHandler
{
    private EncryptionParameters _parameters;
    
   /// <summary>
    /// Gets the filter name.
    /// </summary>
    public string Filter 
    { 
        get 
        {
            return "TestFilter";
        } 
    }
    
    /// <summary>
    /// Gets the sub-filter name.
    /// </summary>
    public string SubFilter 
    { 
        get 
        {
            return "TestsSubFilter";
        } 
    }
    
    /// <summary>
    /// Gets the handler or encryption algorithm version.
    /// </summary>
    public int Version  
    {
        get { return 1; }
    }
    
    /// <summary>
    /// Gets the handler or encryption algorithm revision.
    /// </summary>
    public int Revision  
    {
         get { return 2; }
    }
    
     /// <summary>
     /// Gets the key length.
     /// </summary>
    public int KeyLength  
    {
         get { return 8; }
    }
    
    /// <summary>
    /// Encrypt the document's permissions field. The result will be written to the Perms encryption dictionary field.
    /// When opening a document, the value can be obtained in <see cref="EncryptionParameters"/> via the Perms field.
    /// Allows you to check if the document permissions have changed.
    /// </summary>
    /// <param name="permissions">The document permissions in integer representation.</param>
    /// <returns>The encrypted array.</returns>
    public byte[] EncryptPermissions(int permissions)
    {
        byte[] perms = new byte[16];

        perms[0] = (byte) (permissions & 0xff);
        perms[1] = (byte) ((permissions >> 8) & 0xff);
        perms[2] = (byte) ((permissions >> 16) & 0xff);
        perms[3] = (byte) ((permissions >> 24) & 0xff);
        perms[4] = 0xff;
        perms[5] = 0xff;
        perms[6] = 0xff;
        perms[7] = 0xff;
        perms[8] = (byte) 'F';
        perms[9] = (byte) 'a';
        perms[10] = (byte) 'd';
        perms[11] = (byte) 'b';

        Random rnd = new Random();
        perms[12] = (byte) rnd.Next(0, 0xff);// The random salt for example
        perms[13] = (byte) rnd.Next(0, 0xff);// The random salt for example
        perms[14] = (byte) rnd.Next(0, 0xff);// The random salt for example
        perms[15] = (byte) rnd.Next(0, 0xff);// The random salt for example

        for (var index = 0; index < perms.Length; index++)
        {
            perms[index] ^= 123;
        }

        return perms;
    }

    /// <summary>
    /// Called to initialize the current instance for encryption.
    /// Note that when encrypting, it will be filled with the data of the transferred properties <see cref="ICustomSecurityHandler"/>, and when opening the document from the encryption dictionary.
    /// If the method is called during new encryption, then <see cref="EncryptionParameters.UserKey"/> and <see cref="EncryptionParameters.OwnerKey"/> will be null.
    /// </summary>
    /// <param name="parameters">The encryption parameters.</param>
    public void Initialize(EncryptionParameters parameters)
    {
        _parameters = parameters;
    }

    /// <summary>
    /// Calculate the EncryptionKey. Generally the key is calculated based on the UserKey.
    /// You can use values from EncryptionParams, which contains the current parameters at the time of the call.
    /// This value is passed as the key argument in <see cref="Encrypt"/> and <see cref="Decrypt"/>.
    /// </summary>
    /// <param name="password">Password entered by the user.</param>
    /// <returns>The array of encryption key.</returns>
    public byte[] CalculateEncryptionKey(string password)
    {
        string userPassword;
        if (IsUserPassword(password))
        {
            userPassword = password;
        }
        else
        {
            userPassword = Encoding.UTF8.GetString(GetUserPassword(password));
        }
        
        string encKey = userPassword + Encoding.UTF8.GetString(_parameters.OwnerKey) + Encoding.UTF8.GetString(_parameters.UserKey);
        byte[] bytes = Encoding.UTF8.GetBytes(encKey);
        int sum = 0;
        foreach (var b in bytes)
        {
            sum += b;
        }

        sum %= 127;
        return new byte[] { (byte)sum};
        
    }
    
    /// <summary>
    /// Encrypt the data array.
    /// </summary>
    /// <param name="data">Data to encrypt.</param>
    /// <param name="objectNumber">Number of the object containing the encrypted data.</param>
    /// <param name="generation">Generation of the object.</param>
    /// <param name="key">Key obtained by the CalculateEncryptionKey method</param>
    /// <returns>The encrypted data.</returns>
    public byte[] Encrypt(byte[] data, int objectNumber, int generation, byte[] key)
    {
        byte[] result = new byte[data.Length];

        for (int i = 0; i < data.Length; i++)
        {
            result[i] = (byte)(data[i] ^ key[0]);
        }

        return result;
    }
    
    /// <summary>
    /// Decrypt the data array.
    /// </summary>
    /// <param name="data">Data to decrypt.</param>
    /// <param name="objectNumber">Number of the object containing the encrypted data.</param>
    /// <param name="generation">Generation of the object.</param>
    /// <param name="key">Key obtained by the CalculateEncryptionKey method</param>
    /// <returns>The decrypted data.</returns>
    public byte[] Decrypt(byte[] data, int objectNumber, int generation, byte[] key)
    {
        byte[] result = new byte[data.Length];

        for (int i = 0; i < data.Length; i++)
        {
            result[i] = (byte)(data[i] ^ key[0]);
        }
        return result;
    }
    
    /// <summary>
    /// Check if the password is the document owner's password.
    /// The method is called after Initialize. The method call is used in the PDF API.
    /// </summary>
    /// <param name="password">The password.</param>
    /// <returns>True, if it is an owner password.</returns>
    public bool IsOwnerPassword(string password)
    {
       // Just for the demonstration.
       return !IsUserPassword(password);
    }

    /// <summary>
    /// Check if the password belongs to the user (password for opening the document).
    /// The method is called after Initialize. The method call is used in the PDF API.
    /// </summary>
    /// <param name="password">The password.</param>
    /// <returns>True, if it is a password for opening the document.</returns>
    public bool IsUserPassword(string password)
    {
        string u = Encoding.UTF8.GetString(_parameters.UserKey);
       
        // So that an empty password is not determined part of the line.
        if (u.Length != 0 && password.Length == 0)
        {
            return false;
        }
        
        return u.Contains(password);
    }
    
    /// <summary>
    /// Creates an encoded array based on passwords that will be written to the O field of the encryption dictionary.
    /// Should only rely on the arguments passed. The user password can be calculated from this field using the owner password.
    /// Called during encryption to prepare it and populate the encryption dictionary.
    /// The value will be available in <see cref="CalculateEncryptionKey"/> to get the key from the UserKey.
    /// The passwords specified by the user when calling document encryption will be passed.
    /// Passwords may not be specified or only one may be specified.
    /// </summary>
    /// <param name="userPassword">The user password.</param>
    /// <param name="ownerPassword">The owner password.</param>
    /// <returns>The array of owner key.</returns>
    public byte[] GetOwnerKey(string userPassword, string ownerPassword)
    {
        byte[] bytes = Encoding.UTF8.GetBytes(ownerPassword);
        int encKeyForUserPass = 0;
        foreach (var b in bytes)
        {
            encKeyForUserPass += b;
        }

        encKeyForUserPass %= 127;
        
        byte[] userBytes = Encoding.UTF8.GetBytes(userPassword);
        for (var index = 0; index < userBytes.Length; index++)
        {
            userBytes[index] ^= (byte)encKeyForUserPass;
        }

        return userBytes;
    }    
    
    /// <summary>
    /// Creates an encoded array based on the user's password.
    /// This value is typically used to check if the password belongs to the user or owner, and to get the encryption key.
    /// Called during encryption to prepare it and populate the encryption dict.
    /// The user-specified password is passed as an argument when calling document encryption.
    /// </summary>
    /// <param name="userPassword">The user password.</param>
    /// <returns>The array of user key.</returns>
    public byte[] GetUserKey(string userPassword)
    {
        string userKey = userPassword + "_123";
        return Encoding.UTF8.GetBytes(userKey);
    }
    
    /// <summary>
    /// Extract user password from the owner key.
    /// </summary>
    /// <param name="ownerPassword">The owner password.</param>
    /// <returns>The array of user password.</returns>
    private byte[] GetUserPassword(string ownerPassword)
    {
        byte[] bytes = Encoding.UTF8.GetBytes(ownerPassword);
        int encKeyForUserPass = 0;
        foreach (var b in bytes)
        {
            encKeyForUserPass += b;
        }

        encKeyForUserPass %= 127;
        
        byte[] userPassword = new byte[_parameters.OwnerKey.Length];
        for (var index = 0; index < _parameters.OwnerKey.Length; index++)
        {
            userPassword[index] = (byte)(_parameters.OwnerKey[index] ^ (byte)encKeyForUserPass);
        }

        return userPassword;
    }
}
```

문서 암호화 예:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptDocument(string outputPath)
{     
     var handler = new Aspose.Pdf.Security.CustomSecurityHandler();
    
     // Create PDF document
     using (var document = new Aspose.Pdf.Document())
     {
        document.Info.Title = "TestTitle";
        document.Info.Author = "TestAuthor";
        
        // Add page
        var page = document.Pages.Add();
        
        // Add two text lines
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Test text1."));
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Test text2."));
        
        // Encrypt the document
        document.Encrypt("user_password", "owner_password", Aspose.Pdf.Facades.DocumentPrivilege.AllowAll, handler);
       
        // Save PDF document
        document.Save(outputPath);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptDocument(string outputPath)
{     
     var handler = new Aspose.Pdf.Security.CustomSecurityHandler();
     
     // Create PDF document
     using var document = new Aspose.Pdf.Document();     
     document.Info.Title = "TestTitle";
     document.Info.Author = "TestAuthor";
     
     // Add page
     var page = document.Pages.Add();
     
     // Add two text lines
     page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Test text1."));
     page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Test text2."));

     // Encrypt the document
     document.Encrypt("user_password", "owner_password", Aspose.Pdf.Facades.DocumentPrivilege.AllowAll, handler);
     
     // Save PDF document
     document.Save(outputPath);
    
}
```
{{< /tab >}}
{{< /tabs >}}

암호화된 문서 열기 예:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenEncryptedDocument(string inputPdfPath)
{
    var handler = new Aspose.Pdf.Security.CustomSecurityHandler();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(inputPdfPath, "user_password", handler))
    {
        Console.WriteLine(document.Info.Title);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenEncryptedDocument(string inputPdfPath)
{
    var handler = new Aspose.Pdf.Security.CustomSecurityHandler();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(inputPdfPath, "user_password", handler);
    Console.WriteLine(document.Info.Title);    
}
```
{{< /tab >}}
{{< /tabs >}}

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