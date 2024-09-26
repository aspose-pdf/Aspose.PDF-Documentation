---
title: Extrair e Salvar um Anexo
linktitle: Extrair e Salvar um Anexo
type: docs
weight: 20
url: /net/extract-and-save-an-attachment/
description: Aspose.PDF para .NET permite que você obtenha todos os anexos de um documento PDF. Além disso, você pode obter um anexo individual do seu documento.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extrair e Salvar um Anexo",
    "alternativeHeadline": "Como extrair e salvar um anexos",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, salvar anexos, extrair anexos",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET permite que você obtenha todos os anexos de um documento PDF. Além disso, você pode obter um anexo individual do seu documento."
}
</script>

## Obter Todos os Anexos

Com o Aspose.PDF, é possível obter todos os anexos de um documento PDF. Isso é útil tanto quando você deseja salvar os documentos separadamente do PDF, quanto se você precisa remover anexos de um PDF.

Para obter todos os anexos de um arquivo PDF:

1. Percorra a coleção [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). A coleção [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) contém todos os anexos. Cada elemento desta coleção representa um objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Cada iteração do loop foreach pela coleção [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) retorna um objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
Os seguintes trechos de código mostram como obter todos os anexos de um documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// Obter coleção de arquivos embutidos
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// Obter quantidade de arquivos embutidos
Console.WriteLine("Total de arquivos : {0}", embeddedFiles.Count);

int count = 1;

// Percorrer a coleção para obter todos os anexos
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("Nome: {0}", fileSpecification.Name);
    Console.WriteLine("Descrição: {0}",
    fileSpecification.Description);
    Console.WriteLine("Tipo MIME: {0}", fileSpecification.MIMEType);

    // Verificar se o objeto de parâmetros contém os parâmetros
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("Checksum: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("Data de Criação: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("Data de Modificação: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("Tamanho: {0}", fileSpecification.Params.Size);
    }

    // Obter o anexo e escrever para arquivo ou fluxo
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## Obter Anexo Individual

Para obter um anexo individual, podemos especificar o índice do anexo no objeto `EmbeddedFiles` da instância do Documento. Por favor, tente usar o seguinte trecho de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// Obter arquivo embutido específico
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// Obter as propriedades do arquivo
Console.WriteLine("Nome: {0}", fileSpecification.Name);
Console.WriteLine("Descrição: {0}", fileSpecification.Description);
Console.WriteLine("Tipo MIME: {0}", fileSpecification.MIMEType);

// Verificar se o objeto de parâmetro contém os parâmetros
if (fileSpecification.Params != null)
{
    Console.WriteLine("Checksum: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("Data de Criação: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("Data de Modificação: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("Tamanho: {0}", fileSpecification.Params.Size);
}

// Obter o anexo e escrever para arquivo ou stream
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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

