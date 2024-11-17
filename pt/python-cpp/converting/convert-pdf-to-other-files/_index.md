---
title: Converter PDF para Texto em Python
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
description: Este tópico mostra como converter um arquivo PDF para outros formatos de arquivo, como Texto, usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para Texto

**Aspose.PDF para Python** oferece suporte à conversão de todo o documento PDF e de uma única página para um arquivo de Texto.

### Converter documento PDF para arquivo de Texto

Você pode converter um documento PDF para um arquivo TXT usando a classe 'TextDevice'.

1. Criando o caminho para o arquivo de entrada e saída
1. Criando uma instância da fachada do extrator de PDF com [extractor_create]
(https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Vinculando o arquivo PDF ao extrator com [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)

1. Extraindo o texto do arquivo PDF usando [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Escrevendo o texto extraído no arquivo de saída
1. Salve o PDF de saída com o método 'document.save'.

O trecho de código a seguir explica como extrair os textos de todas as páginas.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```