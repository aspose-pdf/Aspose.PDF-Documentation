---
title: Criar Carimbo de Borracha com Fluxo de Aparência
type: docs
weight: 30
url: /pt/python-net/create-rubber-stamp-with-appearance-stream/
description: Este exemplo carrega um PDF, cria um carimbo de borracha na página 1 usando um arquivo de imagem para sua aparência e salva o documento modificado. ✨
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Carimbo de Borracha com Aparência de Imagem Personalizada Usando PdfContentEditor em Python
Abstract: Este exemplo mostra como criar uma anotação de carimbo de borracha com uma aparência de imagem personalizada em um PDF usando Aspose.PDF for Python via a API Facades. Essa abordagem permite aplicar carimbos com marca ou visualmente ricos, como logotipos, selos ou assinaturas.
---

Anotações de carimbo de borracha podem ser personalizadas usando um arquivo de imagem externo. Em vez de depender apenas de carimbos baseados em texto, você pode definir uma aparência visual (por exemplo, um logotipo da empresa ou um selo de aprovação) e colocá-la em uma página.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para a localização do carimbo.
1. Use um arquivo de imagem como a aparência do carimbo.
1. Aplique configurações de texto e cor.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
