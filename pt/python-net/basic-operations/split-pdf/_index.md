---
title: Dividir arquivos PDF em Python
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /pt/python-net/split-pdf/
description: Aprenda como dividir páginas de PDF em arquivos PDF separados em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividindo páginas de PDF usando Python
Abstract: O artigo discute o processo de dividir páginas de PDF em arquivos individuais usando Python, destacando a utilidade desse recurso para gerenciar documentos PDF grandes. Ele faz referência ao Aspose.PDF Splitter, uma ferramenta online projetada para demonstrar a funcionalidade de divisão de PDF. O artigo fornece um método detalhado para alcançar isso em aplicações Python, envolvendo a iteração pelas páginas de um documento PDF através da `PageCollection` do objeto `Document`. Para cada página, um novo objeto `Document` é criado, a página é adicionada a ele e o novo arquivo PDF é salvo usando o método `save()`. Um trecho de código Python acompanhante ilustra esse processo, mostrando as etapas necessárias para dividir um documento PDF em arquivos separados ao iterar pelas suas páginas e salvar cada uma como um PDF individual.
---

Dividir páginas de PDF pode ser um recurso útil para quem deseja dividir um arquivo grande em páginas individuais ou grupos de páginas.

Use este fluxo de trabalho quando precisar dividir PDFs grandes em arquivos de uma página ou conjuntos de documentos menores para distribuição, revisão ou processamento subsequente.

## Exemplo ao Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) é um aplicativo web gratuito online que permite investigar como a funcionalidade de divisão de apresentações funciona.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações Python. Para dividir páginas de PDF em arquivos PDF de página única usando Python, siga os passos abaixo:

1. Percorra as páginas do documento PDF através do [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto [Coleção de Páginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) coleção
1. Para cada iteração, crie um novo objeto Document e adicione o individual [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objeto no documento vazio
1. Salvar o novo PDF usando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método

## Dividir PDF em vários arquivos ou PDFs separados em Python

O trecho de código Python a seguir mostra como dividir as páginas do PDF em arquivos PDF individuais.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

## Tópicos Relacionados ao Documento

- [Trabalhar com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Mesclar arquivos PDF em Python](/pdf/pt/python-net/merge-pdf-documents/)
- [Otimizar arquivos PDF em Python](/pdf/pt/python-net/optimize-pdf/)
- [Manipular documentos PDF em Python](/pdf/pt/python-net/manipulate-pdf-document/)

