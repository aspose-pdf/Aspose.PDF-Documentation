---
title: Travailler avec les opérateurs PDF en Python
linktitle: Travailler avec les opérateurs
type: docs
weight: 90
url: /fr/python-net/working-with-operators/
description: Apprenez comment utiliser les opérateurs PDF de bas niveau en Python pour une manipulation précise du flux de contenu et le contrôle graphique.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilisez les opérateurs PDF de bas niveau pour le contrôle du flux de contenu en Python
Abstract: Cet article explique comment travailler avec les opérateurs PDF de bas niveau dans Aspose.PDF for Python via .NET. Apprenez à manipuler les flux de contenu directement, à positionner les graphiques avec précision à l'aide des classes d'opérateurs, et à supprimer les objets dessinés des pages PDF dans les workflows Python.
---

## Introduction aux opérateurs PDF et à leur utilisation

Un opérateur est un mot‑clé PDF spécifiant une action à exécuter, comme le dessin d’une forme graphique sur la page. Un mot‑clé d'opérateur se distingue d'un objet nommé par l'absence d'un caractère slash initial (2Fh). Les opérateurs n'ont de sens que à l'intérieur du flux de contenu.

Un flux de contenu est un objet de flux PDF dont les données sont constituées d'instructions décrivant les éléments graphiques à peindre sur une page. Plus de détails sur les opérateurs PDF peuvent être trouvés dans le [Spécification PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Utilisez cette page lorsque vous avez besoin d'un contrôle direct sur les flux de contenu PDF en Python, comme placer des graphiques à des coordonnées exactes, encapsuler les changements d'état des graphiques, ou supprimer des opérateurs de dessin spécifiques d'une page.

## Ajouter des images avec des classes d'opérateurs

Utilisez des classes d'opérateurs bas-niveau lorsque vous devez placer le contenu d'image très précisément dans le flux d'une page PDF sans vous reposer sur des abstractions de mise en page de niveau supérieur.

Cette méthode offre un contrôle granulaire sur le placement des images dans un PDF en manipulant directement le flux de contenu avec des opérateurs graphiques de bas niveau. Elle est particulièrement utile lorsque le positionnement précis et la transformation des images sont nécessaires, comme :

- ajouter des filigranes ou des logos à des emplacements spécifiques.
- superposer des images sur un contenu existant avec un alignement précis.
- mettre en œuvre des mises en page personnalisées qui ne sont pas réalisables avec des abstractions de haut niveau.

En utilisant des opérateurs tels que GSave, ConcatenateMatrix, Do et GRestore, les développeurs peuvent garantir que les images sont rendues avec précision et sans effets secondaires inattendus sur le reste du contenu de la page.

- Le [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) l'opérateur enregistre l'état graphique actuel du PDF.
- Le [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (concatenate matrix) l'opérateur est utilisé pour définir comment une image doit être placée sur la page PDF.
- Le [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) l'opérateur dessine l'image sur la page.
- Le [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) l'opérateur restaure l'état graphique.

Pour ajouter une image dans un fichier PDF :

1. Ouvrez le document PDF
1. Définir les coordonnées de placement de l'image
1. Accéder à la page cible
1. Charger l'image dans un Stream
1. Enregistrer l'état graphique actuel
1. Créer un rectangle et une matrice de transformation
1. Appliquer la matrice de transformation
1. Dessiner l'image
1. Restaurer l'état graphique précédent
1. Enregistrer le document PDF modifié

Le fragment de code suivant montre comment utiliser les opérateurs PDF:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Dessiner XForm sur Page en utilisant des opérateurs

Cet exemple utilise la puissance des XForms et des opérateurs graphiques pour réutiliser efficacement le contenu graphique au sein d'un PDF. En encapsulant l'image dans un XForm, elle peut être dessinée plusieurs fois sans dupliquer les données de l'image, ce qui entraîne des tailles de fichier plus petites et des performances améliorées. Cette approche est particulièrement bénéfique lorsque :

- la même image ou le même graphique doit apparaître plusieurs fois dans un document.

- Un contrôle précis du placement et de la transformation des graphiques est requis.

- L'optimisation du PDF pour les performances et la taille est une priorité.

En gérant l'état graphique avec GSave et GRestore, et en utilisant des matrices de transformation avec ConcatenateMatrix, cette technique garantit que chaque graphique est rendu correctement et de manière indépendante.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Supprimer les objets graphiques à l'aide des classes d'opérateurs

L'extrait de code suivant montre comment supprimer les graphiques. Veuillez noter que si le fichier PDF contient des libellés textuels pour les graphiques, ils pourraient persister dans le fichier PDF en utilisant cette approche. Par conséquent, recherchez les opérateurs graphiques pour une méthode alternative afin de supprimer ces images.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## Sujets associés

- [Opérations PDF avancées en Python](/pdf/fr/python-net/advanced-operations/)
- [Travailler avec les pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Travailler avec des images dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-images/)
- [Travailler avec les graphiques PDF en Python](/pdf/fr/python-net/working-with-graphs/)
