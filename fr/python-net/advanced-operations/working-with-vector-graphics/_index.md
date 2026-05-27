---
title: Travailler avec les graphiques vectoriels en Python
linktitle: Travailler avec les graphiques vectoriels
type: docs
weight: 100
url: /fr/python-net/working-with-vector-graphics/
description: Apprenez comment extraire, déplacer, supprimer et copier des graphiques vectoriels entre les pages PDF en utilisant GraphicsAbsorber en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilisez GraphicsAbsorber pour inspecter et manipuler les graphiques vectoriels PDF en Python
Abstract: Cet article explique comment travailler avec des graphiques vectoriels dans Aspose.PDF for Python via .NET en utilisant la classe GraphicsAbsorber. Apprenez comment extraire des éléments vectoriels des pages PDF, les déplacer ou les supprimer, et copier des graphiques entre les pages avec un contrôle de bas niveau dans les workflows Python.
---

[Aspose.PDF for Python via .NET](/pdf/fr/python-net/) fournit le [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) classe pour accéder et manipuler les graphiques vectoriels déjà présents dans une page PDF. Appelez la `visit` méthode sur n'importe quelle page pour extraire les chemins, les formes et d'autres opérateurs graphiques, puis déplacer, supprimer ou copier ces éléments selon les besoins.

Utilisez cette page lorsque vous devez inspecter ou modifier des éléments de dessin vectoriel intégrés dans un PDF existant, plutôt que de dessiner de nouvelles formes à partir de zéro.

## Extraction de graphiques

L'extraction est le point de départ de toutes les tâches de graphisme vectoriel. `GraphicsAbsorber` lit le flux de contenu d’une page et expose chaque élément graphique avec sa référence de page, sa position et ses opérateurs bruts.

1. Ouvrez le document PDF.
1. Créer un [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) instance.
1. Appel `visit` sur la page cible à remplir `elements`.
1. Itérer sur `elements` pour inspecter la position et le nombre d'opérateurs.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` fait partie du `aspose.pdf.vector` namespace et est spécialement conçu pour interagir avec les graphiques vectoriels dans les flux de contenu PDF.

## Graphiques animés

Après extraction, définissez un nouveau `position` sur chaque élément pour le repositionner sur la même page. Enveloppez les mises à jour dans `suppress_update` / `resume_update` appels pour regrouper les écritures du flux de contenu en une seule opération et éviter les rafraîchissements redondants.

1. Ouvrez le document PDF.
1. Créer un `GraphicsAbsorber` et appeler `visit` sur la page cible.
1. Appel `suppress_update` mettre en pause les écritures du flux de contenu.
1. Mettre à jour le `position` de chaque élément.
1. Appel `resume_update` pour valider tous les changements en une seule fois.
1. Enregistrez le document modifié.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Suppression des graphiques

Pour supprimer des éléments vectoriels spécifiques d'une page, filtrez par position ou rectangle englobant, puis supprimez-les. Aspose.PDF for Python propose deux approches selon que vous souhaitiez supprimer les éléments en ligne ou les collecter d'abord.

### Méthode 1 : suppression en ligne à l’aide de la bordure du rectangle

Cette approche vérifie la position de chaque élément par rapport à un rectangle et appelle `element.remove()` directement à l'intérieur de la boucle. Utilisez-le lorsque vous souhaitez un code concis et que vous n'avez pas besoin d'examiner l'ensemble des éléments supprimés par la suite.

1. Ouvrez le document PDF.
1. Créer un `GraphicsAbsorber` et appeler `visit` sur la page cible.
1. Définir la cible [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Appel `suppress_update` mettre en pause les écritures du flux de contenu.
1. Itérer `elements`, appelant `remove()` sur chaque élément dont la position se trouve à l'intérieur du rectangle.
1. Appel `resume_update` pour valider les suppressions.
1. Enregistrez le document modifié.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Méthode 2 : Collecter les éléments d'abord, puis les supprimer

Cette approche rassemble les éléments correspondants dans un `GraphicElementCollection` et transmet la collection à `page.delete_graphics`. Utilisez-le lorsque vous devez examiner ou consigner ce qui sera supprimé avant de valider la suppression.

1. Ouvrez le document PDF.
1. Créer un `GraphicsAbsorber` et appeler `visit` sur la page cible.
1. Définissez le rectangle cible.
1. Itérer `elements` et ajouter des éléments correspondants à un `GraphicElementCollection`.
1. Appel `page.contents.suppress_update` mettre en pause les écritures du flux de contenu.
1. Appel `page.delete_graphics` avec la collection.
1. Appel `page.contents.resume_update` pour valider les suppressions.
1. Enregistrez le document modifié.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Ajout de graphiques à une autre page

Les éléments vectoriels extraits d’une page peuvent être placés sur n’importe quelle autre page du même document. Deux méthodes sont disponibles : ajouter les éléments un par un, ou transmettre l’ensemble complet en un seul appel.

### Méthode 1 : ajouter les éléments individuellement

Utilisez cette méthode lorsque vous avez besoin d'un contrôle élément par élément, comme le filtrage ou la transformation d'éléments individuels avant de les placer sur la page de destination.

1. Ouvrez le document PDF.
1. Créer un `GraphicsAbsorber` et appeler `visit` sur la page source.
1. Ajoutez une nouvelle page de destination au document.
1. Appel `page_2.contents.suppress_update` mettre en pause les écritures du flux de contenu.
1. Appel `element.add_on_page(page_2)` pour chaque élément.
1. Appel `page_2.contents.resume_update` pour valider toutes les ajouts.
1. Enregistrez le document modifié.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Méthode 2 : Ajouter toute la collection en une fois

Utilisez cette méthode lorsque vous souhaitez copier tous les éléments extraits vers une page en une seule opération, sans itérer manuellement.

1. Ouvrez le document PDF.
1. Créer un `GraphicsAbsorber` et appeler `visit` sur la page source.
1. Ajoutez une nouvelle page de destination au document.
1. Appel `page_2.contents.suppress_update` mettre en pause les écritures du flux de contenu.
1. Appel `page_2.add_graphics` avec le complet `elements` collection.
1. Appel `page_2.contents.resume_update` pour valider toutes les ajouts.
1. Enregistrez le document modifié.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Sujets associés

- [Opérations PDF avancées en Python](/pdf/fr/python-net/advanced-operations/)
- [Travailler avec les graphiques PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Travailler avec les opérateurs PDF en Python](/pdf/fr/python-net/working-with-operators/)
- [Travailler avec les pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
