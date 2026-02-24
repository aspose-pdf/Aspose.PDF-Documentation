---
title: Rotacionando Páginas PDF Usando Python
linktitle: Rotacionar Páginas PDF
type: docs
weight: 110
url: /pt/python-net/rotate-pages/
description: Este tópico descreve como girar a orientação da página em um arquivo PDF existente programaticamente com Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como girar páginas em PDF com Python
Abstract: Este artigo fornece um guia sobre como atualizar ou alterar programaticamente a orientação das páginas de um arquivo PDF existente usando Python. Utilizando Aspose.PDF para Python via .NET, os usuários podem alternar facilmente entre as orientações paisagem e retrato ajustando as propriedades MediaBox da página. O artigo inclui um trecho de código Python que demonstra como percorrer as páginas de um documento PDF, modificar as dimensões e posições do MediaBox e ajustar o CropBox, se necessário. Além disso, explica como definir o ângulo de rotação das páginas usando o método 'rotate' para obter a orientação desejada. O processo termina salvando o arquivo PDF atualizado.
---

Este tópico descreve como atualizar ou alterar a orientação das páginas de um arquivo PDF existente programaticamente com Python.

## Alterar Orientação da Página

Esta função gira cada página de um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 graus no sentido horário usando Aspose.PDF para Python.
É útil para corrigir problemas de orientação de página, como documentos escaneados que estão de lado. O PDF original permanece inalterado, e a versão girada é salva como um novo arquivo.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


