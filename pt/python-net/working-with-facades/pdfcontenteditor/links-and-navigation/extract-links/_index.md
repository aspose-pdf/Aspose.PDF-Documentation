---
title: Extrair Links
type: docs
weight: 70
url: /pt/python-net/extract-links/
description: Este exemplo vincula um PDF de entrada, extrai todos os links e imprime suas coordenadas e URIs (se disponíveis).
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair Links de um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como extrair todos os links de um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como identificar e recuperar links da web ou outros links acionáveis incorporados no PDF.
---

Os PDFs frequentemente contêm elementos interativos, como links da web, links de documento e ações personalizadas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode extrair programaticamente todas as anotações de link de um PDF. Isso permite que você inspecione ou processe os links, por exemplo, para validar URLs ou analisar padrões de navegação em um documento.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Extrair todos os links usando 'extract_link()'.
1. Iterar pelos links extraídos.
1. Verificar se um link é um LinkAnnotation e se sua ação é um GoToURIAction.
1. Imprimir as coordenadas do retângulo e a URI.
1. Exibir uma mensagem se nenhum link for encontrado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```
