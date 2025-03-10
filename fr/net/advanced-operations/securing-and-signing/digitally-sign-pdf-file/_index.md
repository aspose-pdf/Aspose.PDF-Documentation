---
title: Ajouter une signature numérique ou signer numériquement un PDF en C#
linktitle: Signer numériquement un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/digitally-sign-pdf-file/
description: Signer numériquement des documents PDF en utilisant C# ou VB.NET. Vérifiez ou validez les PDF signés numériquement en utilisant C# ou VB.NET.
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
    "abstract": "Aspose.PDF for .NET introduit des capacités puissantes pour signer numériquement des documents PDF en utilisant C# ou VB.NET, améliorant l'intégrité et la sécurité des documents. Les utilisateurs peuvent mettre en œuvre divers types de signatures, y compris des signatures non détachées et détachées avec support pour PKCS7 et ECDSA, permettant des processus de signature personnalisables adaptés à des normes cryptographiques spécifiques. Cette fonctionnalité vérifie non seulement l'authenticité des documents, mais permet également le timestamping et la certification, garantissant un traitement de document de confiance.",
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
    "description": "Signer numériquement des documents PDF en utilisant C# ou VB.NET. Vérifiez ou validez les PDF signés numériquement en utilisant C# ou VB.NET."
}
</script>

Aspose.PDF for .NET prend en charge la fonctionnalité de signer numériquement les fichiers PDF en utilisant la classe SignatureField. Vous pouvez également certifier un fichier PDF avec un certificat PKCS12. Quelque chose de similaire à [Ajouter des signatures et de la sécurité dans Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Lorsque vous signez un document PDF en utilisant une signature, vous confirmez essentiellement son contenu "tel quel". Par conséquent, tout autre changement effectué par la suite invalide la signature et ainsi, vous sauriez si le document a été modifié. En revanche, certifier un document en premier vous permet de spécifier les modifications qu'un utilisateur peut apporter au document sans invalider la certification.

En d'autres termes, le document serait toujours considéré comme conservant son intégrité et le destinataire pourrait toujours faire confiance au document. Pour plus de détails, veuillez visiter Certifier et signer un PDF. En général, certifier un document peut être comparé à la signature de code d'un exécutable .NET.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Fonctionnalités de signature Aspose.PDF for .NET

Nous pouvons utiliser les classes et méthodes suivantes pour la signature PDF

- Classe [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature).
- Énumération [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions).
- Propriété [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) dans la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature).

Pour créer une signature numérique basée sur des certificats PKCS12 (extensions de fichier .p12, pfx), vous devez créer une instance de la classe `PdfFileSignature`, en passant l'objet document à celle-ci. Ensuite, vous devez spécifier la méthode de signature numérique souhaitée en créant un objet de l'une des classes :

- PKCS1.
- PKCS7.
- PKCS7Detached.

_Vous pouvez définir l'algorithme de hachage uniquement pour `PKCS7Detached`. Pour `PKCS1` et `PKCS7`, l'algorithme de hachage est toujours défini sur SHA-1._

Ensuite, vous devez utiliser l'objet d'algorithme de signature reçu dans la méthode `PdfFileSignature.Sign()`. La signature numérique sera définie pour le document après qu'il ait été enregistré.

## Signer un PDF avec des signatures numériques

L'exemple ci-dessous crée une signature PKCS7 non détachée avec l'algorithme de hachage SHA-1.
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

L'exemple ci-dessous crée une signature détachée au format PKCS7Detached avec l'algorithme de hachage SHA-256. L'algorithme de clé dépend de la clé du certificat. DSA, RSA, ECDSA sont pris en charge.

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

Vous pouvez vérifier les signatures en utilisant la méthode PdfFileSignature.VerifySignature(). Auparavant, la méthode `GetSignNames()` était utilisée pour obtenir les noms de signature. À partir de la version 25.02, la méthode `GetSignatureNames()` doit être utilisée, qui renvoie une liste de `SignatureName`. Le `SignatureName` empêche les collisions lors de la vérification des signatures avec les mêmes noms. Les méthodes qui acceptent le type `SignatureName` au lieu d'un nom de signature de chaîne doivent également être utilisées.

_Remarques, la méthode __PdfFileSignature.VerifySigned()__ est obsolète._

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

## Ajouter un timestamp à la signature numérique

### Comment signer numériquement un PDF avec un timestamp

Aspose.PDF for .NET prend en charge la signature numérique du PDF avec un serveur de timestamp ou un service Web.

Pour accomplir cette exigence, la classe [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) a été ajoutée à l'espace de noms Aspose.PDF. Veuillez jeter un œil au code suivant qui obtient un timestamp et l'ajoute au document PDF :

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

## Signer un PDF avec X509Certificate2 au format base64

Ce code signe le PDF en utilisant un certificat externe, interagissant éventuellement avec un serveur pour récupérer le hachage signé et intégrer la signature dans le document PDF.

Étapes pour signer un PDF :

1. Créer une instance de PdfFileSignature.
1. Définir le hachage de signature personnalisé.
1. Charger le certificat.
1. Signer les données.
1. Lier et signer le PDF.
1. Enregistrer le PDF signé.

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

## Signer un PDF avec une fonction de signature de hachage

En utilisant une fonction de signature de hachage personnalisée, l'autorité de signature peut mettre en œuvre des normes cryptographiques spécifiques ou des politiques de sécurité internes qui vont au-delà des méthodes de signature standard, garantissant l'intégrité du document. Cette approche aide à vérifier que le document n'a pas été modifié depuis que la signature a été appliquée et fournit une signature numérique légalement contraignante avec une preuve vérifiable de l'identité du signataire utilisant le certificat PFX.

Ce code montre comment signer numériquement un document PDF en utilisant un certificat PFX (PKCS#12) avec une fonction de signature de hachage personnalisée en C#.

Examinons de plus près le processus de signature DPF :

1. Définir les chemins de fichiers et les informations sur le certificat :

- inputPdf : Le chemin vers le document PDF d'entrée qui doit être signé.
- inputP12 : Le chemin vers le fichier de certificat .p12 (PFX) utilisé pour la signature.
- inputPfxPassword : Le mot de passe pour le certificat PFX.
- outputPdf : Le chemin où le PDF signé sera enregistré.

2. Processus de signature :

- Un objet `PdfFileSignature` est créé et lié au PDF d'entrée.
- Un objet `PKCS7` est initialisé en utilisant le certificat PFX et son mot de passe. La méthode 'CustomSignHash' est assignée comme fonction de signature de hachage personnalisée.
- La méthode `Sign` est appelée, spécifiant le numéro de page (1 dans ce cas), les détails de la signature (raison, cont, loc), et la position (un rectangle avec des coordonnées (0, 0, 500, 500)) pour la signature.
- Le PDF signé est ensuite enregistré au chemin de sortie spécifié.

3. Signature de hachage personnalisée :

- La méthode `CustomSignHash` accepte un tableau d'octets signableHash (le hachage à signer).
- Elle charge le même certificat PFX et récupère sa clé privée.
- La clé privée est utilisée pour signer le hachage en utilisant le `RSACryptoServiceProvider` et l'algorithme SHA-1.
- Les données signées (tableau d'octets) sont renvoyées pour être appliquées à la signature PDF.

L'algorithme de hachage peut être spécifié dans le constructeur PKCS7Detached. Un service tiers peut être appelé dans le délégué CustomSignHash. L'algorithme de signature utilisé dans CustomSignHash doit correspondre à l'algorithme de clé dans le certificat passé à PKCS7/PKCS7Detached.

L'exemple ci-dessous crée une signature non détachée avec l'algorithme RSA et l'algorithme de hachage SHA-1. Si vous utilisez PKCS7Detached au lieu de PKCS7, vous pouvez utiliser ECDCA et définir l'algorithme de hachage souhaité.

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

Pour créer une signature, une estimation préliminaire de la longueur de la future signature numérique est requise. Si vous utilisez SignHash pour créer une signature numérique, vous pouvez constater que le délégué est appelé deux fois pendant le processus d'enregistrement du document. Si pour une raison quelconque vous ne pouvez pas vous permettre deux appels, par exemple, si une demande de code PIN se produit pendant l'appel, vous pouvez utiliser l'option `AvoidEstimatingSignatureLength` pour les classes PKCS1, PKCS7, PKCS7Detached et ExternalSignature. Définir cette option évite l'étape d'estimation de la longueur de la signature en définissant une valeur fixe comme longueur attendue - `DefaultSignatureLength`. La valeur par défaut pour la propriété DefaultSignatureLength est de 3000 octets. L'option AvoidEstimatingSignatureLength ne fonctionne que si le délégué SignHash est défini dans la propriété CustomSignHash. Si la longueur de la signature résultante dépasse la longueur attendue spécifiée par la propriété DefaultSignatureLength, vous recevrez une `SignatureLengthMismatchException` indiquant la longueur réelle. Vous pouvez ajuster la valeur du paramètre DefaultSignatureLength à votre discrétion.

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

## Signature de documents PDF en utilisant ECDSA

Signer des documents PDF en utilisant ECDSA (Elliptic Curve Digital Signature Algorithm) implique d'utiliser la cryptographie à courbe elliptique pour générer des signatures numériques. Cela offre une sécurité et une efficacité élevées, en particulier pour les environnements mobiles et à ressources limitées. Cette approche garantit que vos documents PDF sont signés numériquement avec les avantages de sécurité de la cryptographie à courbe elliptique.

Aspose.PDF prend en charge la création et la vérification de signatures numériques basées sur ECDSA. Les courbes elliptiques suivantes sont prises en charge pour la création et la vérification de signatures numériques :

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

L'algorithme de hachage par défaut est SHA2 avec une longueur dépendant de la taille de la clé ECDSA. Vous pouvez spécifier l'algorithme de hachage dans le constructeur `PKCS7Detached`.

Les signatures numériques ECDSA avec les algorithmes de hachage suivants peuvent être signées : SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512. Les signatures numériques ECDSA avec les algorithmes de hachage suivants peuvent être vérifiées : SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

Vous pouvez vérifier la signature et la vérification en créant un certificat PFX(output.pfx) dans OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Les noms de courbes disponibles pour la signature et la vérification dans Aspose.PDF (la liste des courbes dans OpenSSL peut être obtenue avec la commande 'openssl ecparam -list_curves') : prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

Pour signer un document PDF en utilisant ECDSA, les étapes générales en C# seraient :

1. Vous aurez besoin d'un certificat ECDSA au format PFX ou P12. Ces certificats contiennent à la fois les clés publiques et privées nécessaires pour signer.
1. En utilisant une bibliothèque Aspose.PDF, vous liez le document à un gestionnaire de signature.
1. Utilisez la clé privée ECDSA pour signer le hachage du contenu du document.
1. Placez la signature générée à l'intérieur du fichier PDF avec des métadonnées telles que la raison de la signature, l'emplacement et les coordonnées de contact.

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