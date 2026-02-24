---
title: Comptage des artefacts d'un type particulier en Python via .NET
linktitle: Comptage des artefacts
type: docs
weight: 40
url: /fr/python-net/counting-artifacts/
description: Cet article montre comment inspecter les artefacts de pagination dans un document PDF à l'aide d'Aspose.PDF pour Python via .NET.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comptage des artefacts dans PDF avec Python
Abstract: Les artefacts de pagination tels que les filigranes, les arrière-plans, les en-têtes et les pieds de page sont couramment utilisés dans les documents PDF pour fournir une structure, une identité visuelle et une identification. Cet exemple montre comment inspecter et compter ces artefacts de manière programmatique à l'aide d'Aspose.PDF pour Python via .NET. En filtrant les artefacts sur une page et en les regroupant par sous‑type, les développeurs peuvent analyser rapidement la composition du document et vérifier la présence d'éléments spécifiques. Le code fourni illustre comment ouvrir un PDF, extraire les artefacts de pagination de la première page, compter chaque sous‑type et afficher les résultats, offrant ainsi une approche pratique de l'audit et de la validation de documents.
---

## Comptage des artefacts d'un type particulier

Inspectez et comptez les artefacts de pagination dans un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) à l'aide d'Aspose.PDF pour Python via .NET. Les artefacts de pagination comprennent des éléments tels que les filigranes, les arrière-plans, les en-têtes et les pieds de page qui sont appliqués aux pages pour le mise en page et l'identification. En filtrant les objets [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) sur une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) et en les regroupant par sous‑type (`Artifact.ArtifactSubtype`), les développeurs peuvent analyser rapidement la structure du document et vérifier la présence d'éléments spécifiques.

Pour calculer le nombre total d'artefacts d'un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant. L'exemple filtre la collection [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page (une [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) par [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties), puis compte les sous‑types (`Artifact.ArtifactSubtype`).

1. Ouvrez le document PDF (voir [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtrez les artefacts de pagination à l'aide de la collection [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Comptez les artefacts par sous‑type (`Artifact.ArtifactSubtype`).
1. Affichez les résultats.

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

