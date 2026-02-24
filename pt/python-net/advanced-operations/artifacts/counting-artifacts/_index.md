---
title: Contagem de Artefatos de um Tipo Específico em Python via .NET
linktitle: Contagem de Artefatos
type: docs
weight: 40
url: /pt/python-net/counting-artifacts/
description: Este artigo ilustra como inspecionar artefatos de paginação em um documento PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando Artefatos em PDF usando Python
Abstract: Artefatos de paginação, como marcas d'água, fundos, cabeçalhos e rodapés, são comumente usados em documentos PDF para fornecer estrutura, branding e identificação. Este exemplo demonstra como inspecionar e contar esses artefatos programaticamente usando Aspose.PDF para Python via .NET. Ao filtrar artefatos em uma página e agrupá-los por subtipo, os desenvolvedores podem analisar rapidamente a composição do documento e verificar a presença de elementos específicos. O código fornecido ilustra como abrir um PDF, extrair artefatos de paginação da primeira página, contar cada subtipo e exibir os resultados, oferecendo uma abordagem prática para auditoria e validação de documentos.
---

## Contagem de Artefatos de um Tipo Específico

Inspecione e conte artefatos de paginação em um PDF [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python via .NET. Artefatos de paginação incluem elementos como marcas d'água, fundos, cabeçalhos e rodapés que são aplicados às páginas para layout e propósitos de identificação. Ao filtrar objetos [`Artefato`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) em uma [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) e agrupá-los por subtipo (`Artifact.ArtifactSubtype`), os desenvolvedores podem analisar rapidamente a estrutura do documento e verificar a presença de elementos específicos.

Para calcular a contagem total de artefatos de um tipo específico (por exemplo, o número total de marcas d'água), use o código a seguir. O exemplo filtra a coleção de [`Artefatos`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página (uma [`ColeçãoDeArtefatos`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) por [`TipoDeArtefato`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) e então conta os subtipos (`Artifact.ArtifactSubtype`).

1. Abra o documento PDF (veja [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtre artefatos de paginação usando a coleção de [`Artefatos`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página.
1. Conte os artefatos por subtipo (`Artifact.ArtifactSubtype`).
1. Imprima os resultados.

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

