---
title: Converter HTML para PDF em Python
linktitle: Converter arquivo HTML para PDF
type: docs
weight: 40
url: /pt/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: Este tópico mostra como converter HTML para PDF e MHTML para PDF usando Aspose.PDF. para Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visão Geral 

Aspose.PDF para Python via Java é uma solução profissional que permite criar arquivos PDF a partir de páginas da web e código HTML bruto em suas aplicações.

Este artigo explica como **converter HTML para PDF usando Python**. Ele abrange os seguintes tópicos.

_Formato_: **HTML**
- [Python HTML para PDF](#python-html-to-pdf)
- [Python Converter HTML para PDF](#python-html-to-pdf)
- [Python Como converter HTML para PDF](#python-html-to-pdf)

## Conversão de HTML para PDF em Python

**Aspose.PDF para Python** é uma API de manipulação de PDF que permite converter qualquer documento HTML existente em PDF de forma contínua. O processo de conversão de HTML para PDF pode ser customizado de forma flexível.

## Converter HTML para PDF

O exemplo de código Python a seguir mostra como converter um documento HTML para PDF.

```python
# Exemplo de código Python para converter HTML para PDF
import aspose.pdf as ap

# Criar uma instância do objeto Document
doc = ap.Document()

# Adicionar uma página vazia ao documento
page = doc.pages.add()

# Carregar o conteúdo HTML
html_content = "<html><body><h1>Exemplo de HTML para PDF</h1></body></html>"

# Converter o conteúdo HTML para PDF
page.paragraphs.add(ap.HtmlFragment(html_content))

# Salvar o documento PDF
doc.save("saida.pdf")


1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Inicialize o objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Salve o documento PDF de saída chamando o método **Document.Save()**.

```python

from asposepdf import Api


# inicializar licença
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversão de array de bytes
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# conversão de arquivo
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

A Aspose apresenta a você o aplicativo online gratuito ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF de HTML para PDF usando Aplicativo Gratuito](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}