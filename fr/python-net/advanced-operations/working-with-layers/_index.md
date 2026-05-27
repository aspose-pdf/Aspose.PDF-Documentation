---
title: Travailler avec les calques PDF en Python
linktitle: Travailler avec les calques PDF
type: docs
weight: 50
url: /fr/python-net/working-with-pdf-layers/
description: Apprenez comment ajouter, verrouiller, extraire, aplatir et fusionner des calques PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérez les calques PDF avec Python
Abstract: Cet article explique comment travailler avec les couches PDF (Groupes de contenu optionnel) en utilisant Aspose.PDF for Python via .NET. Apprenez comment ajouter des couches, verrouiller la visibilité des couches, extraire le contenu d'une couche, aplatir le contenu en couches et fusionner les couches en une seule.
---

Les calques PDF, également appelés Groupes de contenu optionnel (OCG), vous permettent d'organiser le contenu en groupes visuels séparés qui peuvent être affichés ou masqués dans les visionneuses PDF compatibles. Dans Aspose.PDF, les opérations sur les calques sont construites autour de la [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

Avec Aspose.PDF for Python via .NET, vous pouvez:

- Ajouter plusieurs calques à une page.
- Verrouiller et déverrouiller les calques pour contrôler le comportement de visibilité.
- Extraire les calques dans des fichiers ou flux distincts.
- Aplatir le contenu en couches dans la page.
- Fusionner plusieurs calques en un seul calque.

## Ajouter des calques à un PDF

Cet exemple crée un PDF avec trois calques. Il utilise un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), ajoute un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), et ajoute [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) objets à cette page.

1. Créer un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et ajoutez un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Créer et ajouter la couche rouge.
1. Créer et ajouter la couche verte.
1. Créer et ajouter la couche bleue.
1. Enregistrez le document PDF.

Le PDF résultant contiendra trois calques distincts : une ligne rouge, une ligne verte et une ligne bleue. Chaque calque peut être activé ou désactivé dans les lecteurs PDF qui prennent en charge le contenu en calques.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## Verrouiller un calque PDF

Cet exemple ouvre un PDF, verrouille un calque spécifique sur la première page et enregistre le fichier mis à jour.

Verrouiller une couche empêche les utilisateurs de modifier l’état de visibilité de cette couche dans les visionneuses PDF prises en charge. Les couches sont accessibles depuis une page et gérées via la collection de couches de la page.

Méthodes et propriétés disponibles :

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) verrouille le calque.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) déverrouille le calque.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) renvoie l'état actuel du verrou.

1. Ouvrez le document PDF.
1. Accédez à la première page du PDF.
1. Vérifiez si la page a des calques.
1. Obtenez la première couche et verrouillez‑la.
1. Enregistrez le PDF mis à jour.

Si le PDF contient des calques, le premier calque sera verrouillé, garantissant que son état de visibilité ne puisse pas être modifié par l'utilisateur. Si aucun calque n'est trouvé, un message est affiché à la place.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## Extraire les éléments de calque PDF

Cet exemple utilise la bibliothèque Aspose.PDF for Python via .NET pour extraire les couches individuelles de la première page d'un document PDF et enregistrer chaque couche comme un fichier PDF distinct en utilisant [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

Pour créer un nouveau PDF à partir d’une couche, le fragment de code suivant peut être utilisé :

1. Charger le PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Accéder aux calques sur la page 1 jusqu’à [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Vérifiez si les calques existent.
1. Parcourir les calques et enregistrer chacun d'eux.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

Il est possible d'extraire les éléments de calque du PDF et de les enregistrer dans un nouveau flux de fichier PDF.

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Aplatir un PDF à calques

Ce script utilise Aspose.PDF for Python via .NET pour aplatir tous les calques de la première page d'un document PDF. L'aplatissement fusionne le contenu visuel de chaque calque en un calque unique, ce qui facilite l'impression, le partage ou l'archivage sans perdre la fidélité visuelle ou les données spécifiques aux calques. L'opération est réalisée avec [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Chargez le document PDF.
1. Accédez aux calques de la page 1.
1. Vérifiez si les calques existent.
1. Aplatir chaque calque avec `layer.flatten(True)`.
1. Enregistrez le document modifié.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## Fusionner tous les calques d'un PDF en un seul

Cet extrait de code utilise Aspose.PDF pour fusionner tous les calques de la première page d'un PDF en un seul calque unifié avec un nom personnalisé en utilisant [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Chargez le document PDF.
1. Accédez à la page 1 et récupérez ses calques.
1. Vérifiez si les calques existent.
1. Définir un nouveau nom de calque.
1. Fusionnez les calques en un seul.
1. Enregistrez le document.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## Sujets liés à la couche

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Travailler avec des tables dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-tables/)
- [Ajouter des pages PDF en Python](/pdf/fr/python-net/add-pages/)
