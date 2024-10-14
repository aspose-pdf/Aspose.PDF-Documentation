---
title: Establecer Privilegios, Encriptar y Desencriptar PDF
linktitle: Encriptar y Desencriptar Archivo PDF
type: docs
weight: 20
url: /net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encriptar archivo PDF con C# utilizando diferentes tipos y algoritmos de encriptación. También, desencriptar archivos PDF usando la contraseña del propietario.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Establecer Privilegios, Encriptar y Desencriptar PDF",
    "alternativeHeadline": "Cómo encriptar y desencriptar un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, encriptar pdf, desencriptar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "dateModified": "2022-02-04",
    "description": "Encriptar archivo PDF con C# utilizando diferentes tipos y algoritmos de encriptación. También, desencriptar archivos PDF usando la contraseña del propietario."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Establecer privilegios en un archivo PDF existente

Para establecer privilegios en un archivo PDF, crea un objeto de la clase [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) y especifica los derechos que deseas aplicar al documento. Una vez que se hayan definido los privilegios, pasa este objeto como argumento al método [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). El siguiente fragmento de código te muestra cómo establecer los privilegios de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Cargar un archivo PDF fuente
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Instanciar objeto de Privilegios de Documento
    // Aplicar restricciones en todos los privilegios
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Permitir solo la lectura en pantalla
    documentPrivilege.AllowScreenReaders = true;
    // Encriptar el archivo con contraseña de Usuario y Propietario.
    // Es necesario establecer la contraseña, para que una vez que el usuario visualice el archivo con la contraseña de usuario,
    // solo se habilite la opción de lectura en pantalla
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Guardar el documento actualizado
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## Cifrar archivo PDF utilizando diferentes tipos y algoritmos de cifrado

Puedes utilizar el método [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) para cifrar un archivo PDF. Puedes pasar la contraseña de usuario, la contraseña del propietario y los permisos al método [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). Además de eso, puedes pasar cualquier valor del enum [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Este enum proporciona diferentes combinaciones de algoritmos de cifrado y tamaños de clave. Puedes pasar el valor de tu elección. Finalmente, guarda el archivo PDF cifrado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>Por favor, especifica diferentes contraseñas de usuario y propietario al cifrar el archivo PDF.

- La **contraseña de usuario**, si se establece, es lo que necesitas proporcionar para abrir un PDF.
- La **contraseña del usuario**, si se establece, es lo que necesitas proporcionar para abrir un PDF.
- La **contraseña del propietario**, si se establece, controla permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader prohibirá estas cosas basadas en la configuración de permisos. Acrobat requerirá esta contraseña si quieres establecer/cambiar permisos.

El siguiente fragmento de código te muestra cómo encriptar archivos PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Abrir documento
Document document = new Document(dataDir+ "Encrypt.pdf");
// Encriptar PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// Guardar PDF actualizado
document.Save(dataDir);
```

## Desencriptar archivo PDF usando la contraseña del propietario

Cada vez más, los usuarios intercambian archivos PDF con encriptación para prevenir el acceso no autorizado a documentos, como imprimir/copiar/compartir/extraer información sobre el contenido de un archivo PDF.
Cada vez más, los usuarios están intercambiando archivos PDF con cifrado para prevenir el acceso no autorizado a los documentos, como imprimir/copiar/compartir/extraer información sobre el contenido de un archivo PDF.
En este sentido, existe la necesidad de acceder al archivo PDF cifrado, ya que dicho acceso solo puede ser obtenido por un usuario autorizado. Además, las personas están buscando diversas soluciones para descifrar archivos PDF a través de Internet.

Es mejor resolver este problema una vez utilizando la biblioteca Aspose.PDF.

Para descifrar el archivo PDF, primero necesitas crear un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) y abrir el PDF utilizando la contraseña del propietario.
Para descifrar el archivo PDF, primero necesita crear un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) y abrir el PDF usando la contraseña del propietario.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Abrir documento
Document document = new Document(dataDir + "Decrypt.pdf", "password");
// Descifrar PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// Guardar PDF actualizado
document.Save(dataDir);
```

## Cambiar la contraseña de un archivo PDF

Si desea cambiar la contraseña de un archivo PDF, primero necesita abrir el archivo PDF usando la contraseña del propietario con el objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Si desea cambiar la contraseña de un archivo PDF, primero necesita abrir el archivo PDF usando la contraseña del propietario con el objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- La contraseña del usuario, si se establece, es lo que necesita proporcionar para abrir un PDF. Acrobat/Reader solicitará al usuario que ingrese la contraseña del usuario. Si no es correcta, el documento no se abrirá.
>- La contraseña del propietario, si se establece, controla permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader prohibirá estas cosas basadas en la configuración de permisos. Acrobat requerirá esta contraseña si desea establecer/cambiar permisos.

El siguiente fragmento de código le muestra cómo cambiar la contraseña de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Abrir documento
Document document = new Document(dataDir + "ChangePassword.pdf", "owner");
// Cambiar contraseña
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// Guardar PDF actualizado
document.Save(dataDir);
```
## Cómo - determinar si el PDF fuente está protegido con contraseña

**Aspose.PDF for .NET** ofrece grandes capacidades para tratar con documentos PDF. Al usar la clase Document del espacio de nombres Aspose.PDF para abrir un documento PDF que está protegido por contraseña, necesitamos proporcionar la información de la contraseña como argumento al constructor del Documento y en caso de que esta información no se proporcione, se genera un mensaje de error. De hecho, al tratar de abrir un archivo PDF con el objeto Document, el constructor intenta leer el contenido del archivo PDF y en caso de que no se proporcione la contraseña correcta, se genera un mensaje de error (esto sucede para prevenir el acceso no autorizado del documento)

Cuando trates con archivos PDF encriptados, puedes encontrarte con el escenario donde te interesaría detectar si un PDF tiene una contraseña de apertura y/o una contraseña de edición.
Cuando se manejan archivos PDF encriptados, puedes encontrarte con el escenario donde te interesaría detectar si un PDF tiene una contraseña de apertura y/o una contraseña de edición.

### Obtener información sobre la seguridad del documento PDF

PdfFileInfo contiene tres propiedades para obtener información sobre la seguridad del documento PDF.

1. la propiedad PasswordType devuelve el valor de enumeración PasswordType:
    - PasswordType.None - el documento no está protegido por contraseña
    - PasswordType.User - el documento se abrió con contraseña de usuario (o contraseña de apertura del documento)
    - PasswordType.Owner - el documento se abrió con contraseña de propietario (o contraseña de permisos, edición)
    - PasswordType.Inaccessible - el documento está protegido por contraseña pero se necesita la contraseña para abrirlo mientras se suministró una contraseña inválida (o ninguna contraseña).
2. propiedad booleana HasOpenPassword - se utiliza para determinar si el archivo de entrada requiere una contraseña al abrirlo.
3. propiedad booleana HasEditPassword - se utiliza para determinar si el archivo de entrada requiere una contraseña para editar su contenido.

### Determinar la contraseña correcta desde un Array

### Determinar la contraseña correcta de un Array

A veces hay un requisito para determinar la contraseña correcta de un array de contraseñas y abrir el documento con la contraseña correcta. El siguiente fragmento de código demuestra los pasos para iterar a través del array de contraseñas y probar abrir el documento con la contraseña correcta.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Cargar archivo PDF fuente
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Determinar si el PDF fuente está cifrado
Console.WriteLine("El archivo está protegido con contraseña " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Número de páginas en el documento son = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Contraseña = " + passwords[passwordcount] + " no es correcta");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
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
```

