---
title: Definir Privilégios, Criptografar e Descriptografar PDF
linktitle: Criptografar e Descriptografar Arquivo PDF
type: docs
weight: 20
url: /net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Criptografar arquivo PDF com C# usando diferentes tipos e algoritmos de criptografia. Também, descriptografar arquivos PDF usando a senha do proprietário.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Definir Privilégios, Criptografar e Descriptografar PDF",
    "alternativeHeadline": "Como criptografar e descriptografar arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, criptografar pdf, descriptografar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "description": "Criptografar arquivo PDF com C# usando diferentes tipos e algoritmos de criptografia. Também, descriptografar arquivos PDF usando a senha do proprietário."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Definir Privilégios em um Arquivo PDF Existente

Para definir privilégios em um arquivo PDF, crie um objeto da classe [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) e especifique os direitos que deseja aplicar ao documento. Uma vez que os privilégios tenham sido definidos, passe este objeto como um argumento para o método [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). O seguinte trecho de código mostra como definir os privilégios de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Carregar um arquivo PDF fonte
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Instanciar objeto de Privilégios de Documento
    // Aplicar restrições em todos os privilégios
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Permitir apenas a leitura de tela
    documentPrivilege.AllowScreenReaders = true;
    // Criptografar o arquivo com senha de Usuário e Proprietário.
    // É necessário definir a senha, para que, uma vez que o usuário visualize o arquivo com a senha do usuário,
    // Apenas a opção de leitura de tela seja habilitada
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Salvar o documento atualizado
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## Criptografar arquivo PDF usando diferentes tipos e algoritmos de criptografia

Você pode usar o método [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) para criptografar um arquivo PDF. Você pode passar a senha do usuário, senha do proprietário e permissões para o método [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). Além disso, você pode passar qualquer valor do enum [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Este enum oferece diferentes combinações de algoritmos de criptografia e tamanhos de chave. Você pode passar o valor de sua escolha. Finalmente, salve o arquivo PDF criptografado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>Por favor, especifique diferentes senhas de usuário e proprietário ao criptografar o arquivo PDF.

- A **senha do usuário**, se configurada, é o que você precisa fornecer para abrir um PDF.
- A **Senha do usuário**, se configurada, é o que você precisa fornecer para abrir um PDF.
- A **Senha do proprietário**, se configurada, controla permissões, como imprimir, editar, extrair, comentar, etc. O Acrobat/Reader irá proibir essas ações com base nas configurações de permissão. O Acrobat exigirá essa senha se você quiser configurar/alterar permissões.

O seguinte trecho de código mostra como criptografar arquivos PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Abrir documento
Document document = new Document(dataDir+ "Encrypt.pdf");
// Criptografar PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// Salvar PDF atualizado
document.Save(dataDir);
```

## Descriptografar arquivo PDF usando Senha do Proprietário

Cada vez mais, os usuários estão trocando arquivos PDF com criptografia para evitar o acesso não autorizado aos documentos, como imprimir/copiar/compartilhar / extrair informações sobre o conteúdo de um arquivo PDF.
Cada vez mais, os usuários estão trocando arquivos PDF com criptografia para evitar o acesso não autorizado a documentos, como impressão/cópia/compartilhamento/extrair informações sobre o conteúdo de um arquivo PDF.
A esse respeito, há uma necessidade de acessar o arquivo PDF criptografado, uma vez que tal acesso só pode ser obtido por um usuário autorizado. Além disso, as pessoas estão procurando várias soluções para descriptografar arquivos PDF pela Internet.

É melhor resolver esse problema de uma vez usando a biblioteca Aspose.PDF.

Para descriptografar o arquivo PDF, você primeiro precisa criar um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) e abrir o PDF usando a senha do proprietário.
Para descriptografar o arquivo PDF, você primeiro precisa criar um objeto [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document) e abrir o PDF usando a senha do proprietário.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Abrir documento
Document document = new Document(dataDir + "Decrypt.pdf", "password");
// Descriptografar PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// Salvar o PDF atualizado
document.Save(dataDir);
```

## Alterar Senha de um Arquivo PDF

Se você deseja alterar a senha de um arquivo PDF, primeiro você precisa abrir o arquivo PDF usando a senha do proprietário com o objeto [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Se você deseja alterar a senha de um arquivo PDF, primeiro você precisa abrir o arquivo PDF usando a senha do proprietário com o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- A senha do usuário, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará que o usuário insira a senha do usuário. Se não estiver correta, o documento não será aberto.
>- A senha do proprietário, se definida, controla permissões, como impressão, edição, extração, comentários, etc. O Acrobat/Reader proibirá essas coisas com base nas configurações de permissão. O Acrobat exigirá essa senha se você quiser definir/alterar permissões.

O seguinte trecho de código mostra como alterar a senha de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Abrir documento
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// Mudar senha
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// Salvar PDF atualizado
document.Save(dataDir);
```
## Como - determinar se o PDF de origem é protegido por senha

**Aspose.PDF para .NET** oferece grandes capacidades de manipulação de documentos PDF. Ao usar a classe Document do namespace Aspose.PDF para abrir um documento PDF que está protegido por senha, precisamos fornecer a informação da senha como um argumento para o construtor do Documento e, caso essa informação não seja fornecida, uma mensagem de erro é gerada. De fato, ao tentar abrir um arquivo PDF com o objeto Document, o construtor tenta ler o conteúdo do arquivo PDF e, caso a senha correta não seja fornecida, uma mensagem de erro é gerada (isso acontece para prevenir o acesso não autorizado ao documento)

Ao lidar com arquivos PDF criptografados, você pode encontrar o cenário em que estaria interessado em detectar se um PDF possui uma senha de abertura e/ou uma senha de edição.
Ao lidar com arquivos PDF criptografados, você pode se deparar com o cenário em que estaria interessado em detectar se um PDF possui uma senha de abertura e/ou uma senha de edição.

### Obter informações sobre a segurança do documento PDF

PdfFileInfo contém três propriedades para obter informações sobre a segurança do documento PDF.

1. propriedade PasswordType retorna o valor da enumeração PasswordType:
    - PasswordType.None - o documento não é protegido por senha
    - PasswordType.User - o documento foi aberto com a senha do usuário (ou senha de abertura do documento)
    - PasswordType.Owner - o documento foi aberto com a senha do proprietário (ou senha de permissões, edição)
    - PasswordType.Inaccessible - o documento é protegido por senha, mas a senha é necessária para abri-lo enquanto uma senha inválida (ou nenhuma senha) foi fornecida.
2. propriedade booleana HasOpenPassword - é usada para determinar se o arquivo de entrada requer uma senha ao abri-lo.
3. propriedade booleana HasEditPassword - é usada para determinar se o arquivo de entrada requer uma senha para editar seu conteúdo.

### Determinar a senha correta a partir de um Array

### Determinar a senha correta de um Array

Às vezes, há uma necessidade de determinar a senha correta de um array de senhas e abrir o documento com a senha correta. O seguinte trecho de código demonstra os passos para iterar pelo array de senhas e tentar abrir o documento com a senha correta.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Carregar o arquivo PDF original
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Determinar se o PDF original está criptografado
Console.WriteLine("O arquivo está protegido por senha " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Número de páginas no documento são = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Senha = " + passwords[passwordcount] + " não está correta");
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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

