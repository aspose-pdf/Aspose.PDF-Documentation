---
title: Agregar firma digital o firmar digitalmente PDF en C#
linktitle: Firmar digitalmente PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/digitally-sign-pdf-file/
description: Firmar digitalmente documentos PDF utilizando C# o VB.NET. Verificar o validar los PDFs firmados digitalmente utilizando C# o VB.NET.
lastmod: "2025-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add digital signature or digitally sign PDF in C#",
    "alternativeHeadline": "Working with digitally sign PDF",
    "abstract": "Aspose.PDF for .NET introduce potentes capacidades para firmar digitalmente documentos PDF utilizando C# o VB.NET, mejorando la integridad y seguridad del documento. Los usuarios pueden implementar varios tipos de firma, incluyendo firmas no separadas y separadas con soporte para PKCS7 y ECDSA, permitiendo procesos de firma personalizables adaptados a estándares criptográficos específicos. Esta característica no solo verifica la autenticidad de los documentos, sino que también permite la estampillado de tiempo y certificación, asegurando un manejo de documentos confiable.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "digital signature, digitally sign PDF, C#, PDF signing, PKCS12 certificate, verify PDF signature, ECDSA signing, timestamp server, custom hash signing, Aspose.PDF for .NET",
    "wordcount": "2020",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2025-02-07",
    "description": "Firmar digitalmente documentos PDF utilizando C# o VB.NET. Verificar o validar los PDFs firmados digitalmente utilizando C# o VB.NET."
}
</script>

Aspose.PDF for .NET admite la función de firmar digitalmente los archivos PDF utilizando la clase SignatureField. También puede certificar un archivo PDF con un certificado PKCS12. Algo similar a [Agregar firmas y seguridad en Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Al firmar un documento PDF utilizando una firma, básicamente confirmas su contenido "tal cual". En consecuencia, cualquier otro cambio realizado posteriormente invalida la firma y, por lo tanto, sabrías si el documento fue alterado. Por otro lado, certificar un documento primero te permite especificar los cambios que un usuario puede hacer al documento sin invalidar la certificación.

En otras palabras, el documento seguiría considerándose que mantiene su integridad y el destinatario aún podría confiar en el documento. Para más detalles, visita Certificando y firmando un PDF. En general, certificar un documento puede compararse con firmar un ejecutable .NET.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Características de firma de Aspose.PDF for .NET

Podemos usar las siguientes clases y métodos para la firma de PDF

- Clase [DocMDPSignature](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/docmdpsignature).
- Enumeración [DocMDPAccessPermissions](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/docmdpaccesspermissions).
- Propiedad [IsCertified](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) en la clase [PdfFileSignature](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature).

Para crear una firma digital basada en certificados PKCS12 (extensiones de archivo .p12, pfx), debes crear una instancia de la clase `PdfFileSignature`, pasando el objeto del documento a ella. A continuación, debes especificar el método de firma digital deseado creando un objeto de una de las clases:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_Puedes establecer el algoritmo de digestión solo para `PKCS7Detached`. Para `PKCS1` y `PKCS7`, el algoritmo de digestión siempre se establece en SHA-1._

A continuación, necesitas usar el objeto del algoritmo de firma recibido en el método `PdfFileSignature.Sign()`. La firma digital se establecerá para el documento después de que se guarde.

## Firmar PDF con firmas digitales

El ejemplo a continuación crea una firma no separada PKCS7 con el algoritmo de digestión SHA-1.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345");
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

El ejemplo a continuación crea una firma separada en formato PKCS7Detached con el algoritmo de digestión SHA-256. El algoritmo de clave depende de la clave del certificado. DSA, RSA, ECDSA son compatibles.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object using the opened document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password, Aspose.Pdf.DigestHashAlgorithm.Sha256);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

Puedes verificar firmas utilizando el método PdfFileSignature.VerifySignature(). Anteriormente, se utilizaba el método `GetSignNames()` para obtener nombres de firma. A partir de la versión 25.02, se debe utilizar el método `GetSignatureNames()`, que devuelve una lista de `SignatureName`. El `SignatureName` previene colisiones al verificar firmas con los mismos nombres. También se deben utilizar métodos que acepten el tipo `SignatureName` en lugar de un nombre de firma de cadena.

_Notas, el método __PdfFileSignature.VerifySigned()__ está obsoleto._

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {         
            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## Agregar estampillado de tiempo a la firma digital

### Cómo firmar digitalmente un PDF con estampillado de tiempo

Aspose.PDF for .NET admite firmar digitalmente el PDF con un servidor de estampillado de tiempo o servicio web.

Para cumplir con este requisito, se ha agregado la clase [TimestampSettings](https://reference.aspose.com/pdf/es/net/aspose.pdf/timestampsettings) al espacio de nombres Aspose.PDF. Por favor, echa un vistazo al siguiente fragmento de código que obtiene el estampillado de tiempo y lo agrega al documento PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithTimeStampServer(string pfxFilePath, string password)
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);
            // Create TimestampSettings settings
            var timestampSettings = new Aspose.Pdf.TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password can be omitted
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Create any of the three signature types
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySignWithTimeStamp_out.pdf");
        }
    }
}
```

## Firmar PDF con X509Certificate2 en formato base64

Este código firma el PDF utilizando un certificado externo, posiblemente interactuando con un servidor para recuperar el hash firmado e incrustar la firma en el documento PDF.

Pasos para firmar PDF:

1. Crear una instancia de PdfFileSignature.
1. Definir el hash de firma personalizado.
1. Cargar el certificado.
1. Firmar los datos.
1. Vincular y firmar el PDF.
1. Guardar el PDF firmado.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create a delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving a response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## Firmar un PDF con función de firma HASH

Utilizando una función de firma de hash personalizada, la autoridad de firma puede implementar estándares criptográficos específicos o políticas de seguridad internas que van más allá de los métodos de firma estándar, asegurando la integridad del documento. Este enfoque ayuda a verificar que el documento no ha sido alterado desde que se aplicó la firma y proporciona una firma digital legalmente vinculante con prueba verificable de la identidad del firmante utilizando el certificado PFX.

Este fragmento de código demuestra cómo firmar digitalmente un documento PDF utilizando un certificado PFX (PKCS#12) con una función de firma de hash personalizada en C#.

Veamos más de cerca el proceso de firma DPF:

1. Definir rutas de archivos e información del certificado:

- inputPdf: La ruta al documento PDF de entrada que necesita ser firmado.
- inputP12: La ruta al archivo de certificado .p12 (PFX) utilizado para la firma.
- inputPfxPassword: La contraseña para el certificado PFX.
- outputPdf: La ruta donde se guardará el PDF firmado.

2. Proceso de firma:

- Se crea un objeto `PdfFileSignature` y se vincula al PDF de entrada.
- Se inicializa un objeto `PKCS7` utilizando el certificado PFX y su contraseña. El método 'CustomSignHash' se asigna como la función de firma de hash personalizada.
- Se llama al método `Sign`, especificando el número de página (1 en este caso), detalles de la firma (razón, cont, loc) y la posición (un rectángulo con coordenadas (0, 0, 500, 500)) para la firma.
- El PDF firmado se guarda en la ruta de salida especificada.

3. Firma de hash personalizada:

- El método `CustomSignHash` acepta un arreglo de bytes signableHash (el hash a firmar).
- Carga el mismo certificado PFX y recupera su clave privada.
- La clave privada se utiliza para firmar el hash utilizando el `RSACryptoServiceProvider` y el algoritmo SHA-1.
- Los datos firmados (arreglo de bytes) se devuelven para ser aplicados a la firma PDF.

El algoritmo de digestión se puede especificar en el constructor de PKCS7Detached. Se puede llamar a un servicio de terceros en el delegado CustomSignHash. El algoritmo de firma utilizado en CustomSignHash debe coincidir con el algoritmo de clave en el certificado pasado a PKCS7/PKCS7Detached.

El ejemplo a continuación crea una firma no separada con el algoritmo RSA y el algoritmo de digestión SHA-1. Si utilizas PKCS7Detached en lugar de PKCS7, puedes usar ECDCA y establecer el algoritmo de digestión deseado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

Para crear una firma, se requiere una estimación preliminar de la longitud de la futura firma digital. Si utilizas SignHash para crear una firma digital, puedes encontrar que el delegado se llama dos veces durante el proceso de guardado del documento. Si por alguna razón no puedes permitirte dos llamadas, por ejemplo, si ocurre una solicitud de código PIN durante la llamada, puedes utilizar la opción `AvoidEstimatingSignatureLength` para las clases PKCS1, PKCS7, PKCS7Detached y ExternalSignature. Establecer esta opción evita el paso de estimación de longitud de firma al establecer un valor fijo como la longitud esperada - `DefaultSignatureLength`. El valor predeterminado para la propiedad DefaultSignatureLength es 3000 bytes. La opción AvoidEstimatingSignatureLength solo funciona si el delegado SignHash se establece en la propiedad CustomSignHash. Si la longitud de la firma resultante excede la longitud esperada especificada por la propiedad DefaultSignatureLength, recibirás una `SignatureLengthMismatchException` que indica la longitud real. Puedes ajustar el valor del parámetro DefaultSignatureLength a tu discreción.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Set an option to avoiding twice SignHash calling.
        pkcs7.AvoidEstimatingSignatureLength = true;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

## Firmar documentos PDF utilizando ECDSA

Firmar documentos PDF utilizando ECDSA (Algoritmo de Firma Digital de Curva Elíptica) implica utilizar criptografía de curva elíptica para generar firmas digitales. Esto ofrece alta seguridad y eficiencia, especialmente para entornos móviles y con recursos limitados. Este enfoque asegura que tus documentos PDF estén firmados digitalmente con las ventajas de seguridad de la criptografía de curva elíptica.

Aspose.PDF admite la creación y verificación de firmas digitales basadas en ECDSA. Las siguientes curvas elípticas son compatibles para la creación y verificación de firmas digitales:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

El algoritmo de digestión predeterminado es SHA2 con una longitud dependiente del tamaño de la clave ECDSA. Puedes especificar el algoritmo de digestión en el constructor de `PKCS7Detached`.

Las firmas digitales ECDSA con los siguientes algoritmos de digestión se pueden firmar: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512. Las firmas digitales ECDSA con los siguientes algoritmos de digestión se pueden verificar: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

Puedes verificar la firma y la verificación creando un certificado PFX(output.pfx) en OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Nombres de curva disponibles para firma y verificación en Aspose.PDF (la lista de curvas en OpenSSL se puede obtener con el comando 'openssl ecparam -list_curves'): prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

Para firmar un documento PDF utilizando ECDSA, los pasos generales en C# serían:

1. Necesitarás un certificado ECDSA en formato PFX o P12. Estos certificados contienen tanto las claves públicas como privadas necesarias para la firma.
1. Usando una biblioteca Aspose.PDF, vinculas el documento a un manejador de firma.
1. Utiliza la clave privada ECDSA para firmar el hash del contenido del documento.
1. Coloca la firma generada dentro del archivo PDF junto con metadatos como la razón para firmar, ubicación y detalles de contacto.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifyEcda()
{
   // The path to the documents directory
   var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

   // Open PDF document
   using (var document = new Aspose.Pdf.Document(dataDir + "signed_ecdsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Check if the document contains any digital signatures
            if (!signature.ContainsSignature())
            {
                throw new Exception("Not contains signature");
            }

            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}

private static void SignEcdsa(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures(); 

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create an instance of PdfFileSignature to sign the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create a PKCS7Detached object using the provided certificate and password
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, "12345", Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Sign the first page of the document, setting the signature's appearance at the specified location
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);

            // Save PDF document
            signature.Save(dataDir + "SignEcdsa_out.pdf");
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