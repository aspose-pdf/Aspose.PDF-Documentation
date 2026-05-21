---
title: Extrair imagens de PDF usando Python
linktitle: Extrair imagens de PDF
type: docs
weight: 20
url: /pt/python-net/extract-images-from-the-pdf-file/
description: Aprenda como extrair imagens incorporadas de arquivos PDF com Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair imagens de PDF via Python
Abstract: Este artigo explica como extrair imagens incorporadas de um documento PDF com Aspose.PDF for Python. Ele abrange a abertura do PDF de origem com a classe Document, o acesso a uma imagem da coleção de recursos da página e a gravação da XImage extraída em um arquivo externo para reutilização, inspeção ou processamento subsequente.
---

Usar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para abrir o PDF, então acessar os recursos da página para recuperar um [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) objeto e salvá-lo como um arquivo separado. Essa abordagem é útil quando você precisa reutilizar imagens, inspecionar ativos extraídos ou criar fluxos de trabalho de processamento de imagens a partir do conteúdo PDF.

1. Abra o PDF como um `Document`.
1. Acesse o recurso de imagem da página de destino.
1. Recuperar o necessário `XImage` da coleção de imagens da página.
1. Salve a imagem extraída em um arquivo de saída.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
