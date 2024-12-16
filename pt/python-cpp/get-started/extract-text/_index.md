---
title: Extrair Texto de PDF usando Python
linktitle: Extrair Texto de PDF
type: docs
weight: 10
url: /pt/python-cpp/extract-text/
description: Esta seção descreve como extrair texto de um documento PDF usando a biblioteca Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas do Documento PDF

Extrair texto de PDF não é fácil. Não muitos leitores de PDF conseguem extrair texto de imagens PDF ou PDFs digitalizados. Mas a ferramenta **Aspose.PDF para Python via C++** permite que você extraia facilmente texto de qualquer arquivo PDF.

Confira o trecho de código e siga os passos para extrair texto do seu PDF:

1. Importe a biblioteca Aspose.PDF para Python
1. Crie um novo objeto extractor, que é usado para extrair texto e imagens de documentos PDF.
1. Vincule o objeto extractor a um arquivo PDF, que é a fonte da extração.
1. Extraia todo o texto do documento PDF e coloque-o em alguma variável.

1. Faça o que quiser, imprima o texto extraído no console, faça a busca de alguns fragmentos etc.

```python
from AsposePdfPython import *

extator = Extract()
extractor_bind_pdf(extator,"blank_pdf_document.pdf")
text = extractor_extract_text(extator)

print(text)
```