---
title: Travailler avec les calques PDF à l'aide de Python
linktitle: Travailler avec les calques PDF
type: docs
weight: 50
url: /fr/python-net/work-with-pdf-layers/
description: Cet article explique comment verrouiller un calque PDF, extraire les éléments d’un calque PDF, aplatir un PDF à calques et fusionner tous les calques d’un PDF en un seul.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment gérer, verrouiller, extraire, aplatir et fusionner les calques PDF en Python
Abstract: Cet article explique comment travailler avec les calques PDF en Python à l’aide d’Aspose.PDF pour .NET, y compris le verrouillage des calques, l’extraction des éléments de calque, l’aplatissement des PDF à calques et la fusion des calques.
---

Les calques PDF permettent à un document de contenir plusieurs ensembles de contenu qui peuvent être affichés ou masqués sélectivement. Chaque calque peut inclure du texte, des images ou des graphiques, et les utilisateurs peuvent les activer ou les désactiver selon les besoins. Les calques sont particulièrement utiles dans les documents complexes où le contenu doit être organisé ou séparé. Les exemples ci‑dessous utilisent les API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) et manipulent les objets [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) via la collection `layers` de la page.

## Verrouiller un calque PDF

Avec Aspose.PDF pour Python via .NET, vous pouvez ouvrir un PDF (voir [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)), verrouiller un [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) spécifique sur la première [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) et enregistrer le document avec les modifications.

Méthodes et propriétés disponibles sur l’objet [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) :

- `layer.lock()` – Verrouille le calque. (voir [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – Déverrouille le calque. (voir [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – Retourne l’état de verrouillage actuel. (voir [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. Ouvrez le document PDF (voir [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Récupérez la première page à l’aide de la collection [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) du document (voir [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. Sélectionnez le [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) à verrouiller depuis `page.layers`.
1. Appelez `layer.lock()` pour empêcher les utilisateurs de modifier la visibilité du calque.
1. Enregistrez le document mis à jour en utilisant [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Extraire les éléments d’un calque PDF

Aspose.PDF vous permet d’extraire chaque [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) d’une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) et de l’enregistrer comme un fichier PDF séparé.

Pour créer un nouveau PDF à partir d’un calque, le fragment de code suivant peut être utilisé (la collection `layers` est accessible via `Page.layers`) :

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

Vous pouvez également enregistrer les calques dans un flux :

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## Aplatir un PDF à calques

L’aplatissement rend un [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) permanent sur la page, supprimant sa fonctionnalité de bascule.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

Le paramètre `cleanup_content_stream` contrôle la suppression des marqueurs de groupe de contenu optionnel (marqueurs OCG). Le définir sur `False` accélère l’aplatissement. Consultez la méthode [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) pour plus de détails.

## Fusionner tous les calques du PDF en un seul

Vous pouvez fusionner tous les calques (ou des spécifiques) en un nouveau [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) unique (l’API de fusion se trouve sur l’objet [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).

Méthodes de l’objet [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) :

- `page.merge_layers(new_layer_name)` — fusionne tous les calques sous un nouveau nom de calque (voir [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — fusionne en utilisant un ID de groupe de contenu optionnel personnalisé (voir [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
