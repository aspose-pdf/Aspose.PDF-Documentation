---
title: Manipular Tabelas em PDF existente
linktitle: Manipular Tabelas
type: docs
weight: 40
url: /net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Tabelas em PDF existente",
    "alternativeHeadline": "Como atualizar o conteúdo das Tabelas em um PDF existente",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, manipular tabelas",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## Manipular tabelas em PDFs existentes

Uma das primeiras funcionalidades suportadas pelo Aspose.PDF para .NET é a sua capacidade de Trabalhar com Tabelas, oferecendo ótimo suporte para adicionar tabelas em arquivos PDF que estão sendo gerados do zero ou em qualquer arquivo PDF existente. Você também obtém a capacidade de Integrar Tabela com Banco de Dados (DOM) para criar tabelas dinâmicas baseadas em conteúdos de banco de dados. Neste novo lançamento, implementamos a nova funcionalidade de buscar e analisar tabelas simples que já existem na página do documento PDF. Uma nova classe chamada **Aspose.PDF.Text.TableAbsorber** fornece essas capacidades. O uso do TableAbsorber é muito semelhante à classe TextFragmentAbsorber existente. O seguinte trecho de código mostra os passos para atualizar conteúdos em uma célula de tabela específica.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Carregar arquivo PDF existente
Document pdfDocument = new Document(dataDir + "input.pdf");
// Criar objeto TableAbsorber para encontrar tabelas
TableAbsorber absorber = new TableAbsorber();

// Visitar a primeira página com o absorvedor
absorber.Visit(pdfDocument.Pages[1]);

// Obter acesso à primeira tabela na página, sua primeira célula e fragmentos de texto nela
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// Mudar o texto do primeiro fragmento de texto na célula
fragment.Text = "oi mundo";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## Substituir uma tabela antiga por uma nova em um documento PDF

Caso você precise encontrar uma tabela específica e substituí-la pela desejada, você pode usar o método Replace() da classe [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) para fazer isso. O exemplo a seguir demonstra a funcionalidade para substituir a tabela dentro de um documento PDF:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Carregar documento PDF existente
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// Criar objeto TableAbsorber para encontrar tabelas
TableAbsorber absorber = new TableAbsorber();

// Visitar a primeira página com o absorvedor
absorber.Visit(pdfDocument.Pages[1]);

// Obter a primeira tabela na página
AbsorbedTable table = absorber.TableList[0];

// Criar nova tabela
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// Substituir a tabela pela nova
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// Salvar o documento
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
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

