---
title: Rotacionar Páginas PDF em Python
linktitle: Rotacionando Páginas PDF
type: docs
weight: 110
url: /pt/python-net/rotate-pages/
description: Aprenda como rotacionar páginas PDF e alterar a orientação da página em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como rotacionar Páginas em PDF com Python
Abstract: Este artigo fornece um guia sobre como atualizar ou alterar programaticamente a orientação das páginas de um arquivo PDF existente usando Python. Utilizando Aspose.PDF for Python via .NET, os usuários podem alternar facilmente entre orientações paisagem e retrato ajustando as propriedades MediaBox da página. O artigo inclui um trecho de código Python que demonstra como iterar pelas páginas de um documento PDF, modificar suas dimensões e posições MediaBox e ajustar o CropBox, se necessário. Além disso, explica como definir o ângulo de rotação das páginas usando o método 'rotate' para alcançar a orientação desejada. O processo termina com a gravação do arquivo PDF atualizado.
---

Este tópico descreve como atualizar ou alterar a orientação das páginas de um arquivo PDF existente programaticamente com Python.

Use esta página quando precisar alternar páginas entre orientação retrato e paisagem ou aplicar ângulos de rotação ao conteúdo PDF existente.

## Alterar Orientação da Página

Esta função rotaciona cada página de um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 graus no sentido horário usando Aspose.PDF for Python.
É útil para corrigir problemas de orientação de página, como documentos digitalizados que estão de lado. O PDF original permanece inalterado, e a versão rotacionada é salva como um novo arquivo.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Tópicos Relacionados à Página

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Alterar o tamanho da página PDF em Python](/pdf/pt/python-net/change-page-size/)
- [Cortar páginas de PDF em Python](/pdf/pt/python-net/crop-pages/)
- [Obter e definir propriedades de página de PDF em Python](/pdf/pt/python-net/get-and-set-page-properties/)