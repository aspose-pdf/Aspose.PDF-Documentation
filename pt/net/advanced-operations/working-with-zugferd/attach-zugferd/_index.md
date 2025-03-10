---
title: Criando PDF compatível com PDF/3-A e anexando fatura ZUGFeRD em C#
linktitle: Anexar ZUGFeRD ao PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/attach-zugferd/
description: Aprenda como gerar um documento PDF com ZUGFeRD em Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "Descubra a nova funcionalidade que permite aos desenvolvedores gerar documentos PDF compatíveis com PDF/A-3B e anexar faturas ZUGFeRD de forma integrada usando C#. Este recurso simplifica o processo de incorporação de metadados de fatura em arquivos PDF, garantindo a preservação a longo prazo dos documentos e a conformidade com os padrões de faturamento eletrônico.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Anexar ZUGFeRD ao PDF

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Recomendamos os seguintes passos para anexar ZUGFeRD ao PDF:

* Defina uma variável de caminho que aponte para uma pasta onde os arquivos PDF de entrada e saída estão localizados.
* Crie um objeto de documento carregando um arquivo PDF existente (por exemplo, "ZUGFeRD-test.pdf") do caminho.
* Crie um objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) fornecendo o caminho e a descrição de outro arquivo chamado "factur-x.xml", que contém metadados da fatura em conformidade com o padrão ZUGFeRD.
* Adicione propriedades ao objeto de especificação de arquivo, como a descrição, tipo MIME e relação AF. A relação AF indica como o arquivo incorporado está relacionado ao documento PDF. Neste caso, está definido como "Alternativa", significando que o arquivo incorporado é uma representação alternativa do conteúdo PDF.
* Adicione o objeto de especificação de arquivo à coleção de arquivos incorporados do documento. O nome do arquivo deve ser especificado de acordo com o padrão ZUGFeRD, por exemplo, "factur-x.xml".
* Converta o documento para o formato PDF/A-3B, um subconjunto do PDF que garante a preservação a longo prazo de documentos eletrônicos. O PDF/A-3B permite a incorporação de arquivos de qualquer formato em documentos PDF.
* Salve o documento convertido como um novo arquivo PDF (por exemplo, "ZUGFeRD-res.pdf").

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

O método de conversão recebe um stream, um formato PDF e uma ação de erro de conversão como parâmetros. O parâmetro de stream pode ser usado para salvar o log de conversão. O parâmetro de ação de erro de conversão especifica o que fazer se ocorrerem erros durante a conversão. Neste caso, está definido como "Excluir", o que significa que quaisquer elementos que não estejam em conformidade com o formato PDF/A-3B serão excluídos do documento.