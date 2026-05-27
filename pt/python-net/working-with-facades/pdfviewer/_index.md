---
title: Classe PdfViewer
type: docs
weight: 135
url: /pt/python-net/pdfviewer-class/
description: Aprenda como usar a classe PdfViewer no Aspose.PDF for Python via .NET para decodificar todas as páginas PDF, decodificar uma página específica e inspecionar metadados de PDF relacionados ao visualizador.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decodifique páginas PDF e inspecione dados do visualizador em Python com PdfViewer
Abstract: Este artigo explica como usar a fachada PdfViewer no Aspose.PDF for Python via .NET para tarefas de decodificação de páginas e inspeção relacionadas ao visualizador. Aprenda como decodificar todas as páginas PDF, renderizar uma página específica e inspecionar propriedades como contagem de páginas, tipo de coordenada e resolução.
---

Aspose.PDF for Python via .NET fornece o [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) fachada para trabalhar com visualização de PDF e cenários de decodificação de página. Um caso de uso comum é converter páginas de PDF em objetos de imagem que podem então ser salvos no disco.

## Crie um auxiliar PdfViewer reutilizável

Antes de decodificar páginas ou ler propriedades relacionadas ao visualizador, crie um pequeno auxiliar que inicializa e retorna um `PdfViewer` instância. Isso mantém os exemplos abaixo autossuficientes e deixa claro como o objeto visualizador é criado antes de ser associado a um documento PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## Decodificar todas as páginas PDF

usar `decode_all_pages()` quando você deseja converter cada página do PDF em uma imagem separada. As imagens das páginas retornadas podem então ser salvas uma a uma em um diretório de saída.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## Decodificar uma página PDF específica

usar `decode_page()` quando você precisa de apenas uma página do documento. Isso é útil ao gerar pré-visualizações, miniaturas ou exportações específicas de página.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## Inspecionar Metadados do PDF

O `inspect_pdf_metadata` A função demonstra como abrir um documento PDF e recuperar metadados básicos relacionados ao visualizador usando o Aspose.PDF. Ela se concentra em extrair informações que descrevem como o documento é interpretado e exibido, em vez de seu conteúdo.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
