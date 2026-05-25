---
title: Extrair fontes de PDF via Python
linktitle: Extrair fontes de PDF
type: docs
weight: 30
url: /pt/python-net/extract-fonts-from-pdf/
description: Use a biblioteca Aspose.PDF for Python para extrair todas as fontes incorporadas do seu documento PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair fontes de PDF usando Python
Abstract: Este artigo explica como inspecionar as fontes usadas em um documento PDF com Aspose.PDF for Python. Ele mostra como abrir um PDF com a classe Document, chamar font_utilities.get_all_fonts() para recuperar os objetos de fonte disponíveis e percorrer os resultados para ler os nomes das fontes para análise, auditoria ou fluxos de trabalho de processamento de documentos.
---

Usar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para abrir o PDF e chamar `font_utilities.get_all_fonts()` para recuperar tudo disponível [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) objetos referenciados pelo documento. Isso é útil ao auditar fontes incorporadas, verificar a disponibilidade de fontes antes da conversão ou analisar os recursos do documento.

1. Abra o PDF de origem como um `Document`.
1. Chamar `document.font_utilities.get_all_fonts()` para obter a coleção de fontes.
1. Iterar sobre o retornado `Font` objetos.
1. Leia e imprima cada `font.font_name` valor.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
