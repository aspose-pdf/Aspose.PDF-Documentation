---
title: Converter HTML para PDF em Python
linktitle: Converter arquivo HTML para PDF
type: docs
weight: 40
url: /pt/python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: Este tópico mostra como converter HTML para PDF e MHTML para PDF usando Aspose.PDF para Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visão Geral

Aspose.PDF para Python via .NET é uma solução profissional que permite criar arquivos PDF a partir de páginas da web e código HTML bruto em suas aplicações.

Este artigo explica como **converter HTML para PDF usando Python**. Ele cobre os seguintes tópicos.

_Formato_: **HTML**
- [Python HTML para PDF](#python-html-to-pdf)
- [Python Converter HTML para PDF](#python-html-to-pdf)
- [Python Como converter HTML para PDF](#python-html-to-pdf)

## Conversão de HTML para PDF em Python

**Aspose.PDF para Python** é uma API de manipulação de PDF que permite converter qualquer documento HTML existente em PDF de forma perfeita. O processo de conversão de HTML para PDF pode ser personalizado de forma flexível.

## Converter HTML para PDF

O exemplo de código Python a seguir mostra como converter um documento HTML em PDF.

```python
import aspose.pdf as ap

# Carregar o documento HTML
html_document = "sample.html"

# Criar um objeto de documento PDF
pdf_document = ap.Document()

# Adicionar uma página ao documento PDF
pdf_page = pdf_document.pages.add()

# Criar um objeto HtmlFragment a partir do HTML
html_fragment = ap.HtmlFragment(html_document)

# Adicionar o HtmlFragment à página PDF
pdf_page.paragraphs.add(html_fragment)

# Salvar o documento PDF
pdf_document.save("output.pdf")
```

# Fim do exemplo


1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Inicialize o objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Salve o documento PDF de saída chamando o método **Document.Save()**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

A Aspose apresenta a você o aplicativo online gratuito ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF HTML para PDF usando App Gratuito](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}