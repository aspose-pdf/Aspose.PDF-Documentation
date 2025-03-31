---
title: Establecer privilegios, cifrar y descifrar PDF
linktitle: Cifrar y descifrar archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Cifrar archivo PDF con C# utilizando diferentes tipos de cifrado y algoritmos. Además, descifrar archivos PDF utilizando la contraseña del propietario.
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
    "abstract": "La nueva función permite a los usuarios cifrar y descifrar archivos PDF de manera eficiente utilizando C# con una variedad de tipos de cifrado y algoritmos. Al utilizar contraseñas de usuario y propietario, proporciona un control robusto sobre el acceso y los permisos del documento, asegurando la confidencialidad e integridad del contenido PDF mientras simplifica la gestión de seguridad para los desarrolladores.",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Cifrar archivo PDF con C# utilizando diferentes tipos de cifrado y algoritmos. Además, descifrar archivos PDF utilizando la contraseña del propietario."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Establecer privilegios en un archivo PDF existente

Para establecer privilegios en un archivo PDF, crea un objeto de la clase [DocumentPrivilege](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/documentprivilege) y especifica los derechos que deseas aplicar al documento. Una vez que se han definido los privilegios, pasa este objeto como argumento al método [Encrypt](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/encrypt/methods/1) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). El siguiente fragmento de código te muestra cómo establecer los privilegios de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegesOnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate Document Privileges object
        // Apply restrictions on all privileges
        var documentPrivilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
        // Only allow screen reading
        documentPrivilege.AllowScreenReaders = true;
        // Encrypt the file with User and Owner password
        // Need to set the password, so that once the user views the file with user password
        // Only screen reading option is enabled
        document.Encrypt("user", "owner", documentPrivilege, Aspose.Pdf.CryptoAlgorithm.AESx128, false);
        // Save PDF document
        document.Save(dataDir + "SetPrivileges_out.pdf");
    }
}
```

## Cifrar archivo PDF utilizando diferentes tipos de cifrado y algoritmos

Puedes usar el método [Encrypt](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/encrypt/methods/1) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document) para cifrar un archivo PDF. Puedes pasar la contraseña de usuario, la contraseña de propietario y los permisos al método [Encrypt](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/encrypt/methods/1). Además de eso, puedes pasar cualquier valor del enum [CryptoAlgorithm](https://reference.aspose.com/pdf/es/net/aspose.pdf/cryptoalgorithm). Este enum proporciona diferentes combinaciones de algoritmos de cifrado y tamaños de clave. Puedes pasar el valor de tu elección. Finalmente, guarda el archivo PDF cifrado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/save/methods/4) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document).

>Por favor, especifica diferentes contraseñas de usuario y propietario al cifrar el archivo PDF.

- La **contraseña de usuario**, si se establece, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader pedirá al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si se establece, controla los permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader no permitirá estas cosas según la configuración de permisos. Acrobat requerirá esta contraseña si deseas establecer/cambiar permisos.

El siguiente fragmento de código te muestra cómo cifrar archivos PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Encrypt.pdf"))
    {
        // Encrypt PDF
        document.Encrypt("user", "owner", 0, Aspose.Pdf.CryptoAlgorithm.RC4x128);
        // Save PDF document
        document.Save(dataDir + "Encrypt_out.pdf");
    }
}
```

## Descifrar archivo PDF utilizando la contraseña del propietario

Cada vez más, los usuarios están intercambiando archivos PDF con cifrado para prevenir el acceso no autorizado a documentos, como imprimir/copiar/compartir / extraer información sobre el contenido de un archivo PDF. Hoy en día, es la mejor opción para cifrar un archivo PDF porque mantiene la confidencialidad y la integridad del contenido. 
En este sentido, hay una necesidad de acceder al archivo PDF cifrado, ya que dicho acceso solo puede ser obtenido por un usuario autorizado. Además, las personas están buscando diversas soluciones para descifrar archivos PDF en Internet.

Es mejor resolver este problema una vez utilizando la biblioteca Aspose.PDF.

Para descifrar el archivo PDF, primero necesitas crear un objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document) y abrir el PDF utilizando la contraseña del propietario. Después de eso, necesitas llamar al método [Decrypt](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/decrypt) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). Finalmente, guarda el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/save/methods/4) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). El siguiente fragmento de código te muestra cómo descifrar el archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "Decrypt.pdf", "password"))
    {
        // Decrypt PDF
        document.Decrypt();
        // Save PDF document
        document.Save(dataDir + "Decrypt_out.pdf");
    }
}
```

## Cambiar la contraseña de un archivo PDF

Si deseas cambiar la contraseña de un archivo PDF, primero necesitas abrir el archivo PDF utilizando la contraseña del propietario con el objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). Después de eso, necesitas llamar al método [ChangePasswords](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/changepasswords) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). Necesitas pasar la contraseña actual del propietario junto con la nueva contraseña de usuario y la nueva contraseña de propietario a este método. Finalmente, guarda el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/save/methods/4) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document).

>- La contraseña de usuario, si se establece, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader pedirá al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
>- La contraseña de propietario, si se establece, controla los permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader no permitirá estas cosas según la configuración de permisos. Acrobat requerirá esta contraseña si deseas establecer/cambiar permisos.

El siguiente fragmento de código te muestra cómo cambiar la contraseña de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "ChangePassword.pdf", "owner"))
    {
        // Change password
        document.ChangePasswords("owner", "newuser", "newowner");
        // Save PDF document
        document.Save(dataDir + "ChangePassword_out.pdf");
    }
}
```

## Cómo - determinar si el PDF de origen está protegido por contraseña

**Aspose.PDF for .NET** proporciona grandes capacidades para tratar con documentos PDF. Al usar la clase Document del espacio de nombres Aspose.PDF para abrir un documento PDF que está protegido por contraseña, necesitamos proporcionar la información de la contraseña como argumento al constructor de Document y en caso de que esta información no se proporcione, se genera un mensaje de error. De hecho, al intentar abrir un archivo PDF con el objeto Document, el constructor intenta leer el contenido del archivo PDF y en caso de que no se proporcione la contraseña correcta, se genera un mensaje de error (esto sucede para prevenir el acceso no autorizado al documento).

Al tratar con archivos PDF cifrados, puedes encontrarte con el escenario en el que estarías interesado en detectar si un PDF tiene una contraseña de apertura y/o una contraseña de edición. A veces hay documentos que no requieren información de contraseña al abrirlos, pero requieren información para editar el contenido del archivo. Así que, para cumplir con los requisitos anteriores, la clase PdfFileInfo presente en Aspose.PDF.Facades proporciona las propiedades que pueden ayudar a determinar la información requerida.

### Obtener información sobre la seguridad del documento PDF

PdfFileInfo contiene tres propiedades para obtener información sobre la seguridad del documento PDF.

1. La propiedad PasswordType devuelve el valor de enumeración PasswordType:
    - PasswordType.None - el documento no está protegido por contraseña.
    - PasswordType.User - el documento se abrió con la contraseña de usuario (o contraseña de apertura del documento).
    - PasswordType.Owner - el documento se abrió con la contraseña de propietario (o permisos, edición).
    - PasswordType.Inaccessible - el documento está protegido por contraseña pero se necesita la contraseña para abrirlo mientras se proporcionó una contraseña inválida (o ninguna contraseña).
2. La propiedad booleana HasOpenPassword - se utiliza para determinar si el archivo de entrada requiere una contraseña al abrirlo.
3. La propiedad booleana HasEditPassword - se utiliza para determinar si el archivo de entrada requiere una contraseña para editar su contenido.

### Determinar la contraseña correcta de un arreglo

A veces hay un requisito para determinar la contraseña correcta de un arreglo de contraseñas y abrir el documento con la contraseña correcta. El siguiente fragmento de código demuestra los pasos para iterar a través del arreglo de contraseñas y tratar de abrir el documento con la contraseña correcta.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineCorrectPasswordFromArray()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var info = new  Aspose.Pdf.Facades.PdfFileInfo())
    {
        // Bind PDF document
        info.BindPdf(dataDir + "IsPasswordProtected.pdf");
        // Determine if the source PDF is encrypted
        Console.WriteLine("File is password protected " + info.IsEncrypted);
    
        String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
    
        for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
        {
            try
            {
                using (var document = new Aspose.Pdf.Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]))
                {
                    if (document.Pages.Count > 0)
                    {
                        Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
                    }
                }
            }
            catch (Aspose.Pdf.InvalidPasswordException)
            {
                Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
            }
        }
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