---
title: Criar Carimbo de Borracha com Arquivo de Aparência
type: docs
weight: 20
url: /pt/python-net/create-rubber-stamp-with-appearance-file/
description: O exemplo associa um PDF de entrada, cria um carimbo de borracha na página 1 usando um arquivo de imagem como a aparência do carimbo e salva o PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Carimbo de Borracha com Aparência Personalizada em um PDF usando PdfContentEditor
Abstract: Este exemplo demonstra como adicionar uma anotação de carimbo de borracha com uma aparência personalizada (imagem) a um documento PDF usando Aspose.PDF for Python via a API Facades. Carimbos personalizados permitem incluir logotipos, assinaturas ou elementos visuais de marca como parte do carimbo.
---

As anotações de carimbo de borracha podem ser personalizadas não apenas com texto, mas também usando um arquivo de imagem como sua aparência. Essa abordagem é útil para adicionar logotipos de empresa, carimbos de assinatura ou qualquer indicador visual às suas páginas PDF.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para o carimbo.
1. Use um arquivo de imagem personalizado para definir a aparência do carimbo de borracha.
1. Defina o texto e a cor do carimbo.
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
