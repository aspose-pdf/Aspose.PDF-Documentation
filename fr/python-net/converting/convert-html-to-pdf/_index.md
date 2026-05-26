---
title: Convertir HTML en PDF en Python
linktitle: Convertir HTML en fichier PDF
type: docs
weight: 40
url: /fr/python-net/convert-html-to-pdf/
lastmod: "2026-05-22"
description: Apprenez comment convertir HTML et MHTML en PDF en Python avec Aspose.PDF for Python via .NET, y compris les paramètres de médias CSS, les polices intégrées et la sortie Tagged PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir HTML en PDF en Python avec Aspose.PDF
Abstract: Cet article explique comment convertir des fichiers HTML et MHTML en PDF en utilisant Aspose.PDF for Python via .NET. Il couvre le flux de travail de base HTML-to-PDF et montre comment contrôler le rendu avec les types de médias, la priorité des règles de page CSS, les polices intégrées, la sortie mono‑page et la génération de structure logique pour des PDF balisés accessibles.
---

## Conversion de HTML en PDF avec Python

**Aspose.PDF for Python via .NET** vous permet de convertir des documents HTML existants en PDF avec des options de rendu flexibles. Vous pouvez affiner la génération de la sortie pour qu’elle corresponde à votre mise en page, votre style, vos exigences d’accessibilité et d’archivage.

## Convertir le HTML en PDF

L'exemple Python suivant montre le flux de travail de base pour convertir un document HTML en PDF.

1. Créer une instance de [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) classe.
1. Initialiser un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet avec le fichier HTML source.
1. Enregistrez le document PDF de sortie en appelant `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Conversions associées

- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) lorsque vous avez besoin d'une sortie prête pour le Web à partir de fichiers PDF existants.
- [Convertir d'autres formats de fichier en PDF](/pdf/fr/python-net/convert-other-files-to-pdf/) pour les flux de travail de conversion EPUB, XPS, texte et PostScript.
- [Convertir les images en PDF](/pdf/fr/python-net/convert-images-format-to-pdf/) lorsque votre contenu source est basé sur des images plutôt que sur du balisage HTML.

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**

Aspose présente l'application en ligne [HTML en PDF](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez tester la qualité de conversion et le résultat.

[![Aspose.PDF Conversion HTML en PDF à l'aide de l'application](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Convertir HTML en PDF en utilisant le type de média

Cet exemple montre comment convertir un fichier HTML en PDF à l'aide d'options de rendu spécifiques.

1. Créer une instance de [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) classe.
1. Définir `html_media_type` pour appliquer des règles CSS destinées aux mises en page écran ou impression, telles que `HtmlMediaType.SCREEN` ou `HtmlMediaType.PRINT`.
1. Charger le HTML dans un `ap.Document` en utilisant les options de chargement.
1. Enregistrez le document au format PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Priorisez le CSS `@page` règle lors de la conversion HTML en PDF

Certains documents utilisent [le `@page` règle](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) pour la mise en page. Si ces styles entrent en conflit avec d’autres paramètres, vous pouvez contrôler la priorité avec `is_priority_css_page_rule`.

1. Créer une instance de [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) classe.
1. Définir `is_priority_css_page_rule = False` laisser d'autres styles prévaloir sur `@page` règles.
1. Charger le HTML dans un `ap.Document` avec les options configurées.
1. Enregistrez le document au format PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Convertir le HTML en PDF avec des polices intégrées

Cet exemple montre comment convertir un fichier HTML en PDF tout en incorporant les polices. Si vous avez besoin que le PDF de sortie préserve la typographie d'origine, définissez `is_embed_fonts` à `True`.

1. Créer `HtmlLoadOptions()` pour configurer la conversion HTML en PDF.
1. Définir `is_embed_fonts = True` intégrer les polices utilisées dans le HTML directement dans le PDF.
1. Charger le HTML dans un `ap.Document` avec ces options.
1. Enregistrez le document au format PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Rendre le contenu HTML sur une seule page PDF

Cet exemple montre comment convertir un fichier HTML en un PDF d'une seule page en utilisant Aspose.PDF for Python via .NET. Utilisez le `is_render_to_single_page` propriété lorsque vous souhaitez que le contenu HTML complet soit rendu sur une page continue.

1. Créer une instance de `HtmlLoadOptions()` pour configurer le processus de conversion.
1. Activer `is_render_to_single_page` afficher le contenu HTML complet sur une seule page.
1. Chargez le document avec les options configurées dans un `ap.Document`.
1. Enregistrez le résultat sous forme de fichier PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## Créer une structure logique à partir des balises HTML

La structure logique, également appelée Tagged PDF, préserve la hiérarchie sémantique du HTML d'origine, telle que les titres, les paragraphes et les listes. Cela rend le PDF résultant plus accessible, consultable et adapté aux flux de travail de documents structurés.

En activant la structure logique pendant la conversion, le DOM HTML est mappé dans un arbre de balises PDF plutôt que d'être rendu uniquement en tant que contenu visuel.

Pour répondre aux exigences d'accessibilité, un PDF doit inclure des éléments de structure logique qui définissent l'ordre de lecture, fournissent un texte alternatif pour les lecteurs d\'écran et préservent la hiérarchie du contenu.

> La qualité de la structure logique dans le PDF de sortie dépend directement de la qualité du balisage HTML d'origine. Un HTML mal structuré ou invalide peut entraîner un balisage incomplet ou inexact dans le PDF converti.

1. Créez une instance de HtmlLoadOptions pour contrôler la façon dont le HTML est converti.
1. Activez le balisage sémantique afin que le PDF contienne des éléments structurés.
1. Ouvrez le fichier HTML en utilisant les options configurées.
1. Enregistrez le PDF structuré.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## Convertir MHTML en PDF

Cet exemple montre comment convertir un fichier MHT ou MHTML en document PDF en utilisant Aspose.PDF for Python via .NET avec des dimensions de page spécifiques.

1. Créer une instance de `ap.MhtLoadOptions()` pour configurer le traitement des fichiers MHTML.
1. Définissez différents paramètres, tels que la taille de la page.
1. Initialisez le document avec le fichier d'entrée et les options de chargement configurées.
1. Enregistrez le document résultant au format PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
