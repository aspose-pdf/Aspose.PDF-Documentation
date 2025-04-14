---
title: Adicionar assinatura digital ou assinar digitalmente PDF em C#
linktitle: Assinar digitalmente PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/digitally-sign-pdf-file/
description: Assine digitalmente documentos PDF usando C# ou VB.NET. Verifique ou valide os PDFs assinados digitalmente usando C# ou VB.NET.
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
    "abstract": "Aspose.PDF for .NET introduz capacidades poderosas para assinar digitalmente documentos PDF usando C# ou VB.NET, melhorando a integridade e segurança do documento. Os usuários podem implementar vários tipos de assinatura, incluindo assinaturas não destacadas e destacadas com suporte para PKCS7 e ECDSA, permitindo processos de assinatura personalizáveis adaptados a padrões criptográficos específicos. Este recurso não apenas verifica a autenticidade dos documentos, mas também permite a marcação de tempo e certificação, garantindo um manuseio confiável do documento.",
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
    "description": "Assine digitalmente documentos PDF usando C# ou VB.NET. Verifique ou valide os PDFs assinados digitalmente usando C# ou VB.NET."
}
</script>

Aspose.PDF for .NET suporta o recurso de assinar digitalmente os arquivos PDF usando a classe SignatureField. Você também pode certificar um arquivo PDF com um Certificado PKCS12. Algo semelhante a [Adicionando Assinaturas e Segurança no Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Ao assinar um documento PDF usando uma assinatura, você basicamente confirma seu conteúdo "como está". Consequentemente, quaisquer outras alterações feitas posteriormente invalidam a assinatura e, assim, você saberia se o documento foi alterado. Por outro lado, certificar um documento primeiro permite que você especifique as alterações que um usuário pode fazer no documento sem invalidar a certificação.

Em outras palavras, o documento ainda seria considerado como mantendo sua integridade e o destinatário ainda poderia confiar no documento. Para mais detalhes, visite Certificando e assinando um PDF. Em geral, certificar um documento pode ser comparado a Assinar um executável .NET.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Recursos de assinatura do Aspose.PDF for .NET

Podemos usar as seguintes classes e métodos para assinatura de PDF

- Classe [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature).
- Enumeração [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions).
- Propriedade [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) na classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature).

Para criar uma assinatura digital baseada em certificados PKCS12 (extensões de arquivo .p12, pfx), você deve criar uma instância da classe `PdfFileSignature`, passando o objeto do documento para ela. Em seguida, você deve especificar o método de assinatura digital desejado criando um objeto de uma das classes:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_Você pode definir o algoritmo de digestão apenas para `PKCS7Detached`. Para `PKCS1` e `PKCS7`, o algoritmo de digestão é sempre definido como SHA-1._

Em seguida, você precisa usar o objeto do algoritmo de assinatura recebido no método `PdfFileSignature.Sign()`. A assinatura digital será definida para o documento após ele ser salvo.

## Assinar PDF com assinaturas digitais

O exemplo abaixo cria uma assinatura não destacada PKCS7 com o algoritmo de digestão SHA-1.
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

O exemplo abaixo cria uma assinatura destacada no formato PKCS7Detached com o algoritmo de digestão SHA-256. O algoritmo de chave depende da chave do certificado. DSA, RSA, ECDSA são suportados.

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

Você pode verificar assinaturas usando o método PdfFileSignature.VerifySignature(). Anteriormente, o método `GetSignNames()` era usado para obter nomes de assinatura. A partir da versão 25.02, o método `GetSignatureNames()` deve ser usado, que retorna uma lista de `SignatureName`. O `SignatureName` evita colisões ao verificar assinaturas com os mesmos nomes. Métodos que aceitam o tipo `SignatureName` em vez de um nome de assinatura em string também devem ser usados.

_Observações, o método __PdfFileSignature.VerifySigned()__ está obsoleto._

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

## Verificar assinaturas digitais com verificação de certificado

Ao verificar uma assinatura digital, você pode verificar o certificado de assinatura quanto à revogação.

Infelizmente, o Aspose.PDF não pode verificar a autenticidade dos certificados raiz ou intermediários na cadeia de certificados. Portanto, apenas o status de revogação do certificado de assinatura é verificado usando CRL e OCSP.

Para configurar a validação do certificado, você pode usar o parâmetro `ValidationOptions`.

A opção `ValidationMode` oferece três modos de validação:

- **None** – o certificado não é verificado.
- **Strict** – a revogação do certificado afeta o resultado do método `Verify`.
- **OnlyCheck** – permite verificar o certificado sem afetar o resultado da verificação da assinatura.

O `ValidationMethod` especifica o método usado para verificar o certificado:

- **Auto** – seleção automática do método. OCSP é preferido. O status de revogação é determinado pelo método que realiza a verificação com sucesso.
- **Ocsp** – a revogação é verificada usando OCSP.
- **Crl** – a revogação é verificada usando CRL.
- **All** – ambos os métodos são usados para verificar o certificado. Para que a validação passe, ambos os métodos devem confirmar que o certificado não está revogado.

A opção `CheckCertificateChain` permite verificar a presença de uma cadeia de certificados na assinatura. Se a cadeia de certificados não for encontrada, o resultado da verificação do certificado será `Undefined`.

O resultado da verificação pode ser obtido através de um parâmetro de saída do tipo `ValidationResult`. Os possíveis status são: `Valid`, `Invalid` e `Undefined`. `Undefined` geralmente significa que o certificado não pôde ser validado ou que a cadeia de certificados está faltando.

Definir tanto `CheckCertificateChain` quanto `ValidationMode = ValidationMode.Strict` corresponde ao comportamento do Adobe Acrobat. Se o Adobe Acrobat não conseguir encontrar a cadeia de certificados, ele não verifica o status de revogação, e a assinatura é considerada inválida.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifySignatureWithCertificateCheck(string filePath)
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(filePath))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Find all signatures
            foreach (var signName in pdfSign.GetSignatureNames())
            {
                // Create a certificate validation option
                var options = new Aspose.Pdf.Security.ValidationOptions();
                options.ValidationMode = ValidationMode.Strict;
                options.ValidationMethod = ValidationMethod.Auto;
                options.CheckCertificateChain = true;
                options.RequestTimeout = 20000;

                Aspose.Pdf.Security.ValidationResult validationResult;
                // Verify a digital signature
                bool verified = pdfSign.VerifySignature(signName, options, out validationResult);
                Console.WriteLine("Certificate validation resul: " + validationResult.Status);
                Console.WriteLine("Is verified: " + verified);
            } 
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifySignatureWithCertificateCheck(string filePath)
{
    // Open PDF document
    using var document = new Aspose.Pdf.Document(filePath);
    
    // Create an instance of PdfFileSignature for working with signatures in the document
    using var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document);
    
    // Find all signatures
    foreach (var signName in pdfSign.GetSignatureNames())
    {
        // Create a certificate validation option
        var options = new Aspose.Pdf.Security.ValidationOptions();
        options.ValidationMode = ValidationMode.Strict;
        options.ValidationMethod = ValidationMethod.Auto;
        options.CheckCertificateChain = true;
        options.RequestTimeout = 20000;

        Aspose.Pdf.Security.ValidationResult validationResult;
        // Verify a digital signature
        bool verified = pdfSign.VerifySignature(signName, options, out validationResult);
        Console.WriteLine($"Certificate validation resul: {validationResult.Status}");
        Console.WriteLine($"Is verified: {verified}" );
    }             
}
```
{{< /tab >}}
{{< /tabs >}}


## Adicionar timestamp à assinatura digital

### Como assinar digitalmente um PDF com timestamp

Aspose.PDF for .NET suporta assinar digitalmente o PDF com um servidor de timestamp ou serviço Web.

Para atender a esse requisito, a classe [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) foi adicionada ao namespace Aspose.PDF. Por favor, dê uma olhada no seguinte trecho de código que obtém o timestamp e o adiciona ao documento PDF:

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

## Assinar PDF com X509Certificate2 em formato base64

Este código assina o PDF usando um certificado externo, possivelmente interagindo com um servidor para recuperar o hash assinado e incorporar a assinatura no documento PDF.

Passos para assinar PDF:

1. Crie uma instância de PdfFileSignature.
1. Defina o Hash de Assinatura Personalizado.
1. Carregando o certificado.
1. Assinando os dados.
1. Vinculando e Assinando o PDF.
1. Salvando o PDF Assinado.

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

## Assinar um PDF com função de assinatura HASH

Usando uma função de assinatura de hash personalizada, a autoridade de assinatura pode implementar padrões criptográficos específicos ou políticas de segurança internas que vão além dos métodos de assinatura padrão, garantindo a integridade do documento. Essa abordagem ajuda a verificar se o documento não foi alterado desde que a assinatura foi aplicada e fornece uma assinatura digital legalmente vinculativa com prova verificável da identidade do signatário usando o certificado PFX.

Este trecho de código demonstra a assinatura digital de um documento PDF usando um certificado PFX (PKCS#12) com uma função de assinatura de hash personalizada em C#.

Vamos dar uma olhada mais de perto no processo de assinatura DPF:

1. Defina os Caminhos dos Arquivos e as Informações do Certificado:

- inputPdf: O caminho para o documento PDF de entrada que precisa ser assinado.
- inputP12: O caminho para o arquivo de certificado .p12 (PFX) usado para assinatura.
- inputPfxPassword: A senha para o certificado PFX.
- outputPdf: O caminho onde o PDF assinado será salvo.

2. Processo de Assinatura:

- Um objeto `PdfFileSignature` é criado e vinculado ao PDF de entrada.
- Um objeto `PKCS7` é inicializado usando o certificado PFX e sua senha. O método 'CustomSignHash' é atribuído como a função de assinatura de hash personalizada.
- O método `Sign` é chamado, especificando o número da página (1 neste caso), detalhes da assinatura (razão, cont, loc) e a posição (um retângulo com coordenadas (0, 0, 500, 500)) para a assinatura.
- O PDF assinado é então salvo no caminho de saída especificado.

3. Assinatura de Hash Personalizada:

- O método `CustomSignHash` aceita um array de bytes signableHash (o hash a ser assinado).
- Ele carrega o mesmo certificado PFX e recupera sua chave privada.
- A chave privada é usada para assinar o hash usando o `RSACryptoServiceProvider` e o algoritmo SHA-1.
- Os dados assinados (array de bytes) são retornados para serem aplicados à assinatura do PDF.

O algoritmo de digestão pode ser especificado no construtor PKCS7Detached. Um serviço de terceiros pode ser chamado no delegado CustomSignHash. O algoritmo de assinatura usado em CustomSignHash deve corresponder ao algoritmo de chave no certificado passado para PKCS7/PKCS7Detached.

O exemplo abaixo cria uma assinatura não destacada com o algoritmo RSA e o algoritmo de digestão SHA-1. Se você usar PKCS7Detached em vez de PKCS7, pode usar ECDCA e definir o algoritmo de digestão desejado.

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

Para criar uma assinatura, uma estimativa preliminar do comprimento da futura assinatura digital é necessária. Se você usar SignHash para criar uma assinatura digital, pode descobrir que o delegado é chamado duas vezes durante o processo de salvamento do documento. Se por algum motivo você não puder suportar duas chamadas, por exemplo, se um pedido de código PIN ocorrer durante a chamada, você pode usar a opção `AvoidEstimatingSignatureLength` para as classes PKCS1, PKCS7, PKCS7Detached e ExternalSignature. Definir esta opção evita a etapa de estimativa do comprimento da assinatura, definindo um valor fixo como o comprimento esperado - `DefaultSignatureLength`. O valor padrão para a propriedade DefaultSignatureLength é 3000 bytes. A opção AvoidEstimatingSignatureLength só funciona se o delegado SignHash estiver definido na propriedade CustomSignHash. Se o comprimento da assinatura resultante exceder o comprimento esperado especificado pela propriedade DefaultSignatureLength, você receberá uma `SignatureLengthMismatchException` indicando o comprimento real. Você pode ajustar o valor do parâmetro DefaultSignatureLength a seu critério.

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

## Assinando documentos PDF usando ECDSA

Assinar documentos PDF usando ECDSA (Algoritmo de Assinatura Digital de Curva Elíptica) envolve a utilização de criptografia de curva elíptica para gerar assinaturas digitais. Isso oferece alta segurança e eficiência, especialmente para ambientes móveis e com recursos limitados. Essa abordagem garante que seus documentos PDF sejam assinados digitalmente com as vantagens de segurança da criptografia de curva elíptica.

Aspose.PDF suporta a criação e verificação de assinaturas digitais baseadas em ECDSA. As seguintes curvas elípticas são suportadas para criação e verificação de assinaturas digitais:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

O algoritmo de digestão padrão é SHA2 com um comprimento dependente do tamanho da chave ECDSA. Você pode especificar o algoritmo de digestão no construtor `PKCS7Detached`.

Assinaturas digitais ECDSA com os seguintes algoritmos de digestão podem ser assinadas: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512. Assinaturas digitais ECDSA com os seguintes algoritmos de digestão podem ser verificadas: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

Você pode verificar a assinatura e a verificação criando um certificado PFX(output.pfx) no OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Nomes de curvas disponíveis para assinatura e verificação no Aspose.PDF (a lista de curvas no OpenSSL pode ser obtida com o comando 'openssl ecparam -list_curves'): prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

Para assinar um documento PDF usando ECDSA, os passos gerais em C# seriam:

1. Você precisará de um certificado ECDSA em formato PFX ou P12. Esses certificados contêm tanto as chaves públicas quanto privadas necessárias para a assinatura.
1. Usando a biblioteca Aspose.PDF, você vincula o documento a um manipulador de assinatura.
1. Use a chave privada ECDSA para assinar o hash do conteúdo do documento.
1. Coloque a assinatura gerada dentro do arquivo PDF junto com metadados, como a razão para assinar, localização e detalhes de contato.

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