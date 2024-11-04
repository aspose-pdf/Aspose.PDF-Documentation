---
title: Converter formatos PDF para PDF/A em Python
linktitle: Converter formatos PDF para PDF/A
type: docs
weight: 100
url: /python-java/convert-pdf-to-pdfa/
lastmod: "2023-04-06"
description: Este tópico mostra como o Aspose.PDF para Python permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para Python** permite converter um arquivo PDF em um arquivo PDF compatível com <abbr title="Portable Document Format / A">PDF/A</abbr>. Antes de fazer isso, o arquivo deve ser validado. Este tópico explica como.

{{% alert color="primary" %}}

Por favor, note que seguimos o Adobe Preflight para validar a conformidade com PDF/A. Todas as ferramentas no mercado têm sua própria "representação" de conformidade com PDF/A. Por favor, verifique este artigo sobre ferramentas de validação PDF/A para referência. Escolhemos produtos Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo o que está conectado ao PDF.

{{% /alert %}}

Converta o arquivo usando o método Convert da classe Document.
 Antes de converter o PDF para um arquivo compatível com PDF/A, valide o PDF usando o método Validate. O resultado da validação é armazenado em um arquivo XML e então esse resultado também é passado para o método Convert. Você também pode especificar a ação para os elementos que não podem ser convertidos usando a enumeração ConvertErrorAction.

{{% alert color="success" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para Python apresenta a você um aplicativo online gratuito ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Converter arquivo PDF para PDF/A-1b

O trecho de código a seguir mostra como converter arquivos PDF para PDF/A-1b compatível com PDF.

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
# Abrir documento PDF
document = Api.Document(input_pdf)
# Converter para documento compatível com PDF/A
document.convert(output_log, Api.PdfFormat.PDF_A_1B, Api.ConvertErrorAction.Delete)
# Salvar documento de saída
document.save(output_pdf)
```