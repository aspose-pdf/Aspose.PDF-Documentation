---
title: Vérifier les limites de forme dans les graphiques PDF avec Python
linktitle: Vérifier les limites de forme
type: docs
weight: 70
url: /fr/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Apprenez comment valider les limites de forme dans les collections de graphiques PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validez les limites de forme des graphiques dans les fichiers PDF à l'aide de Python
Abstract: Cet article montre comment valider les limites de forme dans les collections de Graph avec Aspose.PDF for Python via .NET. Il couvre la configuration de BoundsCheckMode, la détection des formes hors limites et la gestion sécurisée des exceptions de limites.
---

## Vérifier les limites de forme dans un Graph

Lorsque vous ajoutez des formes à un [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), vous pouvez activer la validation des limites pour garantir que chaque forme s'adapte à la zone du graphique.

Utilisez [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) définir le comportement lorsqu'une forme est hors de portée. Dans cet exemple, `THROW_EXCEPTION_IF_DOES_NOT_FIT` est utilisé pour lever une exception.

Suivez les étapes ci-dessous:

1. Créer un nouveau PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ajouter un [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Créer un [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) et l'ajouter à la page.
1. Créer un [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) qui dépasse les limites du graphique.
1. Définir le mode de vérification des limites sur `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Ajoutez le rectangle et gérez l’exception.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## Remarques

- Utilisez `THROW_EXCEPTION_IF_DOES_NOT_FIT` lorsque la validation stricte de la mise en page est requise.
- Pour un comportement permissif, choisissez‑en un autre `BoundsCheckMode` option basée sur vos besoins de mise en page.

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Ajouter des formes rectangulaires au PDF en Python](/pdf/fr/python-net/add-rectangle/)
- [Ajouter des formes de ligne au PDF en Python](/pdf/fr/python-net/add-line/)
- [Ajouter des formes elliptiques au PDF en Python](/pdf/fr/python-net/add-ellipse/)
