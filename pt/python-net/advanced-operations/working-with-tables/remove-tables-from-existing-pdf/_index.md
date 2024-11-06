---
title: Remover Tabelas de PDF Existente
linktitle: Remover Tabelas
type: docs
weight: 50
url: pt/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remover Tabelas de PDF Existente",
    "alternativeHeadline": "Como Excluir Tabelas de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, remover tabela, excluir tabelas",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF para Python via .NET oferece as capacidades de inserir/criar Tabela dentro do documento PDF enquanto está sendo gerado do zero ou você também pode adicionar o objeto tabela em qualquer documento PDF existente. No entanto, você pode ter um requisito para [Manipular Tabelas em PDF existente](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/) onde você pode atualizar os conteúdos nas células de tabela existentes. No entanto, você pode se deparar com um requisito para remover objetos de tabela de um documento PDF existente.

{{% /alert %}}

Para remover as tabelas, precisamos usar a classe [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para obter as tabelas em um PDF existente e então chamar [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## Remover Tabela do documento PDF

Nós adicionamos uma nova função, ou seja.
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) para a classe existente [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) a fim de remover a tabela do documento PDF. Uma vez que o absorvedor encontra com sucesso as tabelas na página, ele se torna capaz de removê-las. Por favor, verifique o trecho de código a seguir mostrando como remover uma tabela de um documento PDF:

```python

    import aspose.pdf as ap

    # Carregar documento PDF existente
    pdf_document = ap.Document(input_file)
    # Criar objeto TableAbsorber para encontrar tabelas
    absorber = ap.text.TableAbsorber()
    # Visitar a primeira página com o absorvedor
    absorber.visit(pdf_document.pages[1])
    # Obter a primeira tabela na página
    table = absorber.table_list[0]
    # Remover a tabela
    absorber.remove(table)
    # Salvar PDF
    pdf_document.save(output_file)
```

## Remover Múltiplas Tabelas de um Documento PDF

Às vezes, um documento PDF pode conter mais de uma tabela e você pode ter a necessidade de remover múltiplas tabelas dele. Para remover várias tabelas de um documento PDF, por favor use o seguinte trecho de código:

```python

    import aspose.pdf as ap

    # Carregar documento PDF existente
    pdf_document = ap.Document(input_file)
    # Criar objeto TableAbsorber para encontrar tabelas
    absorber = ap.text.TableAbsorber()
    # Visitar a segunda página com o absorvedor
    absorber.visit(pdf_document.pages[1])
    # Obter cópia da coleção de tabelas
    tables = absorber.table_list
    #  Percorrer a cópia da coleção e remover tabelas
    for table in tables:
        absorber.remove(table)
    # Salvar documento
    pdf_document.save(output_file)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>