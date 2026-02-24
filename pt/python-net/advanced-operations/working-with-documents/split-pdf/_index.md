---
title: Dividir PDF programaticamente em Python
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /pt/python-net/split-pdf-document/
description: Este tópico mostra como dividir páginas PDF em arquivos PDF individuais em suas aplicações Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividindo páginas PDF usando Python
Abstract: O artigo discute o processo de dividir páginas PDF em arquivos individuais usando Python, destacando a utilidade de tal recurso para gerenciar documentos PDF grandes. Ele faz referência ao Aspose.PDF Splitter, uma ferramenta online projetada para demonstrar a funcionalidade de divisão de PDFs. O artigo fornece um método detalhado para alcançar isso em aplicações Python, envolvendo a iteração pelas páginas de um documento PDF através da coleção `PageCollection` do objeto `Document`. Para cada página, um novo objeto `Document` é criado, a página é adicionada a ele e o novo arquivo PDF é salvo usando o método `save()`. Um trecho de código Python anexo ilustra esse processo, mostrando as etapas necessárias para dividir um documento PDF em arquivos separados, iterando pelas suas páginas e salvando cada uma como um PDF individual.
---

Dividir páginas PDF pode ser um recurso útil para quem deseja dividir um arquivo grande em páginas separadas ou grupos de páginas.

## Exemplo ao Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) é uma aplicação web gratuita online que permite investigar como funciona a funcionalidade de divisão de PDFs.

[![Aspose Dividir PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tópico mostra como dividir páginas PDF em arquivos PDF individuais em suas aplicações Python. Para dividir páginas PDF em arquivos PDF de página única usando Python, os seguintes passos podem ser seguidos:

1. Percorra as páginas do documento PDF através da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Para cada iteração, crie um novo objeto Document e adicione o objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) individual ao documento vazio
1. Salve o novo PDF usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

## Dividir PDF em múltiplos arquivos ou PDFs separados em Python

O trecho de código Python a seguir mostra como dividir páginas PDF em arquivos PDF individuais.

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


