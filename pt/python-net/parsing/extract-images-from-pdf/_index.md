---
title: Extrair Imagens de PDF usando Python
linktitle: Extrair Imagens de PDF
type: docs
weight: 20
url: /pt/python-net/extract-images-from-the-pdf-file/
description: Como extrair parte da imagem de um PDF usando Aspose.PDF para Python
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Extrair Imagens de PDF via Python
Abstract: Este artigo oferece um guia conciso sobre a extração de imagens incorporadas de um documento PDF usando Python. O processo envolve três etapas principais - carregar o documento PDF, acessar o recurso de imagem e salvar a imagem em um arquivo. O trecho de código utiliza a biblioteca Aspose.PDF para facilitar essas operações. Inicialmente, o documento PDF é carregado a partir de um caminho especificado, e a imagem desejada é acessada dos recursos da primeira página. Finalmente, a imagem é salva em um arquivo de saída especificado usando uma operação de E/S de arquivos, permitindo análises adicionais, edição ou reutilização em outros documentos.
---

Este trecho de código extrai imagens incorporadas de um documento PDF para análise separada, edição ou reutilização em outros documentos:

1. Carregar o Documento PDF
1. Acessar o Recurso de Imagem
1. Salvar a Imagem em um Arquivo

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

