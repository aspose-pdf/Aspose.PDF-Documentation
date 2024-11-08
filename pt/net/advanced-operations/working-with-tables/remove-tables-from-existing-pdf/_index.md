---
title: Remover Tabelas de um PDF existente
linktitle: Remover Tabelas
type: docs
weight: 50
url: /pt/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remover Tabelas de um PDF existente",
    "alternativeHeadline": "Como Deletar Tabelas de um PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, remover tabela, deletar tabelas",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF para NET oferece a capacidade de inserir/criar uma tabela dentro de um documento PDF enquanto ele está sendo gerado do zero ou você também pode adicionar o objeto de tabela em qualquer documento PDF existente. No entanto, você pode ter a necessidade de [Manipular Tabelas em PDF existente](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) onde você pode atualizar os conteúdos nas células da tabela existente. No entanto, você pode se deparar com uma necessidade de remover objetos de tabela de um documento PDF existente.

{{% /alert %}}

Para remover as tabelas, precisamos usar a classe [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) para obter acesso às tabelas em PDF existente e, em seguida, chamar [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Remover Tabela do documento PDF

Adicionamos uma nova função, ou seja,
Nós adicionamos uma nova função, isto é:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Carregar documento PDF existente
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// Criar objeto TableAbsorber para encontrar tabelas
TableAbsorber absorber = new TableAbsorber();

// Visitar a primeira página com absorvedor
absorber.Visit(pdfDocument.Pages[1]);

// Obter a primeira tabela na página
AbsorbedTable table = absorber.TableList[0];

// Remover a tabela
absorber.Remove(table);

// Salvar PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## Remover Múltiplas Tabelas de um Documento PDF

Às vezes, um documento PDF pode conter mais de uma tabela e você pode precisar remover múltiplas tabelas dele. Para remover múltiplas tabelas de um documento PDF, use o seguinte trecho de código:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Carregar documento PDF existente
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// Criar objeto TableAbsorber para encontrar tabelas
TableAbsorber absorber = new TableAbsorber();

// Visitar a segunda página com absorvedor
absorber.Visit(pdfDocument.Pages[1]);

// Obter cópia da coleção de tabelas
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// Percorrer a cópia da coleção removendo tabelas
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// Salvar documento
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

Por favor, leve em consideração que a remoção ou substituição de uma tabela altera a coleção TableList. Portanto, no caso de remover/substituir tabelas em um loop, a cópia da coleção TableList é essencial.

{{% /alert %}}

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


