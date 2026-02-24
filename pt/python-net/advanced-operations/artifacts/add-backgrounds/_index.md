---
title: Trabalhando com fundos como artefatos com Python
linktitle: Adicionando fundos
type: docs
weight: 20
url: /pt/python-net/add-backgrounds/
description: Adicione uma imagem de fundo ao seu arquivo PDF com Python. Use a classe BackgroundArtifact.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar fundo a PDF com Python
Abstract: Este artigo discute o uso de imagens de fundo em documentos PDF usando Aspose.PDF para Python via .NET. Destaca a capacidade de adicionar marcas d'água ou designs sutis aos documentos utilizando a classe `BackgroundArtifact`, que permite a incorporação de imagens de fundo em objetos de página individuais. O artigo fornece um exemplo de código prático que demonstra como implementar esse recurso. O processo envolve criar um novo documento PDF, adicionar uma página, criar um objeto `BackgroundArtifact`, definir uma imagem de fundo e acrescentar o artefato de fundo à coleção de artefatos da página. Finalmente, o documento modificado é salvo como um arquivo PDF. Esta técnica permite uma apresentação visual aprimorada dos documentos PDF.
---

As imagens de fundo podem ser usadas para adicionar uma marca d'água ou outro design sutil aos documentos. No Aspose.PDF para Python via .NET, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O trecho de código a seguir mostra como adicionar uma imagem de fundo às páginas PDF usando o objeto BackgroundArtifact com Python.

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```


