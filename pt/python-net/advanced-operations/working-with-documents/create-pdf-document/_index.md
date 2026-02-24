---
title: Como criar PDF usando Python
linktitle: Criar documento PDF
type: docs
weight: 10
url: /pt/python-net/create-pdf-document/
description: Criar e formatar o documento PDF com Aspose.PDF para Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar arquivo PDF com Python
Abstract: Aspose.PDF for Python via .NET é uma API versátil projetada para desenvolvedores manipularem arquivos PDF dentro de aplicações Python direcionadas ao framework .NET. Ela permite que os usuários criem, carreguem, modifiquem e convertam documentos PDF sem esforço. Este artigo fornece um guia passo a passo para criar um arquivo PDF simples usando Aspose.PDF. O processo envolve inicializar um objeto `Document`, adicionar uma `Page` ao documento, inserir um `TextFragment` nos parágrafos da página e salvar o arquivo como PDF. O trecho de código Python incluído demonstra essas etapas criando um documento PDF que contém o texto "Hello World!". Esta API simplifica o manuseio de PDF com código mínimo, aumentando a produtividade dos desenvolvedores que trabalham com PDFs em ambientes .NET.
---

**Aspose.PDF for Python via .NET** é uma API de manipulação de PDF que permite aos desenvolvedores criar, carregar, modificar e converter arquivos PDF diretamente do Python para aplicações .NET com apenas algumas linhas de código.

## Como criar um arquivo PDF simples

Para criar um PDF usando Python via .NET com Aspose.PDF, você pode seguir estas etapas:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à coleção [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) do objeto Document
1. Adicione [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à coleção [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página
1. Salve o documento PDF resultante

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


