---
title: Adicionar Carimbo ao PDF
type: docs
weight: 40
url: /pt/python-net/add-stamp/
description: Saiba como adicionar um carimbo às páginas PDF usando PdfFileStamp em Python.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Adicionar Carimbos de Texto ao PDF em Python
Abstract: Este artigo explica como adicionar conteúdo de carimbo a documentos PDF com Aspose.PDF for Python via .NET usando a fachada PdfFileStamp. Ele mostra como criar um carimbo, posicioná‑lo na página, controlar a rotação e a opacidade, e salvar o PDF atualizado.
---

Aspose.PDF for Python via .NET fornece o [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) fachada para adicionar conteúdo repetido às páginas PDF. Além de cabeçalhos, rodapés e números de página, você pode usá‑la para colocar carimbos baseados em texto em cada página de um documento.

## Adicionar o carimbo ao PDF

Depois que o carimbo é configurado, vincule o PDF de entrada a `PdfFileStamp`, adicione o selo, e salve o arquivo de saída. Isso aplica o selo configurado em todo o documento.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
