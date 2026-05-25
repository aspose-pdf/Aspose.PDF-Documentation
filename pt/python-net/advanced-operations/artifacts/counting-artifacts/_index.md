---
title: Contar Artefatos PDF em Python
linktitle: Contando Artefatos
type: docs
weight: 40
url: /pt/python-net/counting-artifacts/
description: Aprenda como inspecionar e contar artefatos de paginação em documentos PDF usando Python com Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando Artefatos em PDF usando Python
Abstract: Artefatos de paginação, como marcas d'água, planos de fundo, cabeçalhos e rodapés, são comumente usados em documentos PDF para fornecer estrutura, identidade visual e identificação. Este exemplo demonstra como inspecionar e contar esses artefatos programaticamente usando Aspose.PDF for Python via .NET. Ao filtrar artefatos em uma página e agrupá-los por subtipo, os desenvolvedores podem analisar rapidamente a composição do documento e verificar a presença de elementos específicos. O código fornecido ilustra como abrir um PDF, extrair artefatos de paginação da primeira página, contar cada subtipo e exibir os resultados, oferecendo uma abordagem prática para auditoria e validação de documentos.
---

## Contando Artefatos de um Tipo Particular

Inspecione e conte artefatos de paginação em um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python via .NET. Artefatos de paginação incluem elementos como marcas d'água, fundos, cabeçalhos e rodapés que são aplicados às páginas para fins de layout e identificação. Ao filtrar [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) objetos em um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) e agrupando-os por subtipo (`Artifact.ArtifactSubtype`), os desenvolvedores podem analisar rapidamente a estrutura do documento e verificar a presença de elementos específicos.

Para calcular a contagem total de artefatos de um tipo específico (por exemplo, o número total de marcas d'água), use o código a seguir. O exemplo filtra a página [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) coleção (an [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) by [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) e então conta subtipos (`Artifact.ArtifactSubtype`).

1. Abra o documento PDF (veja [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtre artefatos de paginação usando o 'da página [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) coleção.
1. Contar artefatos por subtipo (`Artifact.ArtifactSubtype`).
1. Imprima os resultados.

```python

from os import path
from collections import Counter
import sys
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## Tópicos de Artefatos Relacionados

- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
- [Adicionar marcas d'água ao PDF em Python](/pdf/pt/python-net/add-watermarks/)
- [Adicionar fundos PDF em Python](/pdf/pt/python-net/add-backgrounds/)
- [Adicionar numeração Bates ao PDF em Python](/pdf/pt/python-net/add-bates-numbering/)
