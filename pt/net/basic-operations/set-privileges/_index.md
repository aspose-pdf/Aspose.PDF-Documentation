---
title: Definir Privilégios, Criptografar e Descriptografar PDF
linktitle: Criptografar e Descriptografar Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Criptografar Arquivo PDF com C# usando Diferentes Tipos e Algoritmos de Criptografia. Além disso, descriptografar Arquivos PDF usando Senha do Proprietário.
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
    "abstract": "O novo recurso permite que os usuários criptografem e descriptografem arquivos PDF de forma eficiente usando C# com uma variedade de tipos e algoritmos de criptografia. Ao utilizar senhas de usuário e proprietário, fornece controle robusto sobre o acesso e permissões do documento, garantindo a confidencialidade e integridade do conteúdo PDF enquanto simplifica a gestão de segurança para desenvolvedores.",
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
    "description": "Criptografar Arquivo PDF com C# usando Diferentes Tipos e Algoritmos de Criptografia. Além disso, descriptografar Arquivos PDF usando Senha do Proprietário."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Definir Privilégios em um Arquivo PDF Existente

Para definir privilégios em um arquivo PDF, crie um objeto da classe [DocumentPrivilege](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/documentprivilege) e especifique os direitos que você deseja aplicar ao documento. Uma vez que os privilégios tenham sido definidos, passe este objeto como um argumento para o método [Encrypt](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/encrypt/methods/1) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document). O seguinte trecho de código mostra como definir os privilégios de um arquivo PDF.

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

## Criptografar Arquivo PDF usando Diferentes Tipos e Algoritmos de Criptografia

Você pode usar o método [Encrypt](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/encrypt/methods/1) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document) para criptografar um arquivo PDF. Você pode passar a senha do usuário, a senha do proprietário e permissões para o método [Encrypt](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/encrypt/methods/1). Além disso, você pode passar qualquer valor do enum [CryptoAlgorithm](https://reference.aspose.com/pdf/pt/net/aspose.pdf/cryptoalgorithm). Este enum fornece diferentes combinações de algoritmos de criptografia e tamanhos de chave. Você pode passar o valor de sua escolha. Finalmente, salve o arquivo PDF criptografado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/save/methods/4) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).

>Por favor, especifique senhas de usuário e proprietário diferentes ao criptografar o arquivo PDF.

- A **senha do usuário**, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará que o usuário insira a senha do usuário. Se não estiver correta, o documento não será aberto.
- A **senha do proprietário**, se definida, controla permissões, como impressão, edição, extração, comentários, etc. O Acrobat/Reader não permitirá essas ações com base nas configurações de permissão. O Acrobat exigirá essa senha se você quiser definir/mudar permissões.

O seguinte trecho de código mostra como criptografar arquivos PDF.

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

## Descriptografar Arquivo PDF usando Senha do Proprietário

Cada vez mais, os usuários estão trocando arquivos PDF com criptografia para evitar acesso não autorizado a documentos, como impressão/cópia/compartilhamento/extração de informações sobre o conteúdo de um arquivo PDF. Hoje, é a melhor escolha para criptografar um arquivo PDF porque mantém a confidencialidade e integridade do conteúdo. 
Nesse sentido, há uma necessidade de acessar o arquivo PDF criptografado, uma vez que tal acesso só pode ser obtido por um usuário autorizado. Além disso, as pessoas estão em busca de várias soluções para descriptografar arquivos PDF na Internet.

É melhor resolver esse problema uma vez usando a biblioteca Aspose.PDF.

Para descriptografar o arquivo PDF, você primeiro precisa criar um objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document) e abrir o PDF usando a senha do proprietário. Depois disso, você precisa chamar o método [Decrypt](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/decrypt) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document). Finalmente, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/save/methods/4) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document). O seguinte trecho de código mostra como descriptografar o arquivo PDF.

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

## Mudar Senha de um Arquivo PDF

Se você deseja mudar a senha de um arquivo PDF, primeiro precisa abrir o arquivo PDF usando a senha do proprietário com o objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document). Depois disso, você precisa chamar o método [ChangePasswords](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/changepasswords) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document). Você precisa passar a senha do proprietário atual junto com a nova senha do usuário e a nova senha do proprietário para este método. Finalmente, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/save/methods/4) do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).

>- A senha do usuário, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará que o usuário insira a senha do usuário. Se não estiver correta, o documento não será aberto.
>- A senha do proprietário, se definida, controla permissões, como impressão, edição, extração, comentários, etc. O Acrobat/Reader não permitirá essas ações com base nas configurações de permissão. O Acrobat exigirá essa senha se você quiser definir/mudar permissões.

O seguinte trecho de código mostra como mudar a senha de um arquivo PDF.

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

## Como - determinar se o PDF de origem está protegido por senha

**Aspose.PDF for .NET** fornece grandes capacidades de lidar com documentos PDF. Ao usar a classe Document do namespace Aspose.PDF para abrir um documento PDF que está protegido por senha, precisamos fornecer as informações da senha como um argumento para o construtor Document e, caso essa informação não seja fornecida, uma mensagem de erro é gerada. Na verdade, ao tentar abrir um arquivo PDF com o objeto Document, o construtor tenta ler o conteúdo do arquivo PDF e, caso a senha correta não seja fornecida, uma mensagem de erro é gerada (isso acontece para evitar acesso não autorizado ao documento).

Ao lidar com arquivos PDF criptografados, você pode se deparar com o cenário em que estaria interessado em detectar se um PDF tem uma senha de abertura e/ou uma senha de edição. Às vezes, existem documentos que não requerem informações de senha ao abri-los, mas requerem informações para editar o conteúdo do arquivo. Portanto, para atender aos requisitos acima, a classe PdfFileInfo presente sob Aspose.PDF.Facades fornece as propriedades que podem ajudar a determinar as informações necessárias.

### Obter informações sobre a segurança do documento PDF

PdfFileInfo contém três propriedades para obter informações sobre a segurança do documento PDF.

1. A propriedade PasswordType retorna o valor da enumeração PasswordType:
    - PasswordType.None - o documento não está protegido por senha.
    - PasswordType.User - o documento foi aberto com a senha do usuário (ou senha de abertura do documento).
    - PasswordType.Owner - o documento foi aberto com a senha do proprietário (ou permissões, edição).
    - PasswordType.Inaccessible - o documento está protegido por senha, mas a senha é necessária para abri-lo enquanto uma senha inválida (ou nenhuma senha) foi fornecida.
2. A propriedade booleana HasOpenPassword - é usada para determinar se o arquivo de entrada requer uma senha ao abri-lo.
3. A propriedade booleana HasEditPassword - é usada para determinar se o arquivo de entrada requer uma senha para editar seu conteúdo.

### Determinar a senha correta a partir de um Array

Às vezes, há uma necessidade de determinar a senha correta a partir de um array de senhas e abrir o documento com a senha correta. O seguinte trecho de código demonstra os passos para iterar pelo array de senhas e tentar abrir o documento com a senha correta.

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