---
title: Convertir d’autres formats de fichiers en PDF avec Python
linktitle: Convertir d’autres formats de fichiers en PDF
type: docs
weight: 80
url: /fr/python-net/convert-other-files-to-pdf/
lastmod: "2026-05-22"
description: Apprenez à convertir les fichiers EPUB, Markdown, PCL, XPS, PostScript, XML et LaTeX en PDF avec Python en utilisant Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Comment convertir d'autres formats de fichiers en PDF en Python
Abstract: Cet article fournit un guide complet sur la conversion de divers formats de fichiers en PDF en utilisant Python, en tirant parti des capacités d'Aspose.PDF for Python via .NET. Le document décrit les processus de conversion pour plusieurs formats, notamment EPUB, Markdown, PCL, Texte, XPS, PostScript, XML, XSL-FO et LaTeX/TeX. Chaque section propose des extraits de code spécifiques et des instructions pour mettre en œuvre ces conversions. L'article souligne l'utilité des fonctionnalités d'Aspose.PDF, telles que les options de chargement adaptées à chaque type de fichier, afin d'assurer une conversion précise et efficace. De plus, il met en avant la disponibilité d'applications de conversion en ligne pour que les utilisateurs puissent explorer la fonctionnalité directement. Le guide sert de ressource pratique pour les développeurs souhaitant intégrer des capacités de conversion PDF dans leurs applications Python.
---

Cet article explique comment **convertir différents types de fichiers en PDF à l'aide de Python**. Il couvre les sujets suivants.

## Convertir OFD en PDF

OFD signifie Open Fixed-layout Document (également appelé format Open Fixed Document). C’est une norme nationale chinoise (GB/T 33190-2016) pour les documents électroniques, présentée comme une alternative au PDF.

Étapes Convertir OFD en PDF en Python:

1. Configurez les options de chargement OFD en utilisant OfdLoadOptions().
1. Chargez le document OFD.
1. Enregistrer au format PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir LaTeX/TeX en PDF

Le format de fichier LaTeX est un format de fichier texte avec balisage dans le dérivé LaTeX de la famille de langages TeX et LaTeX est un format dérivé du système TeX. LaTeX (ˈleɪtæk/lay-tek ou lah-tek) est un système de préparation de documents et un langage de balisage de documents. Il est largement utilisé pour la communication et la publication de documents scientifiques dans de nombreux domaines, y compris les mathématiques, la physique et l’informatique. Il joue également un rôle clé dans la préparation et la publication de livres et d’articles contenant du matériel multilingue complexe, tel que le coréen, le japonais, les caractères chinois et l’arabe, y compris les éditions spéciales.

LaTeX utilise le programme de composition TeX pour formater sa sortie, et il est lui‑même écrit dans le langage macro TeX.

{{% alert color="success" %}}
**Essayez de convertir LaTeX/TeX en PDF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["LaTex en PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité avec lesquelles cela fonctionne.

[![Aspose.PDF Conversion LaTeX/TeX en PDF avec App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Étapes pour convertir TEX en PDF en Python :

1. Configurez les options de chargement LaTeX en utilisant LatexLoadOptions().
1. Chargez le document LaTeX.
1. Enregistrer au format PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir EPUB en PDF

**Aspose.PDF for Python via .NET** vous permet de simplement convertir des fichiers EPUB en format PDF.

EPUB (abrégé de publication électronique) est une norme libre et ouverte d'e‑book du International Digital Publishing Forum (IDPF). Les fichiers ont l’extension .epub. EPUB est conçu pour du contenu réajustable, ce qui signifie qu’un lecteur EPUB peut optimiser le texte pour un dispositif d’affichage particulier.

<abbr title="electronic publication">EPUB</abbr> Il prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les sociétés de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.La version EPUB 3 est également approuvée par le Book Industry Study Group (BISG), une association leader du commerce du livre pour les meilleures pratiques normalisées, la recherche, l'information et les événements, pour l'emballage du contenu.

{{% alert color="success" %}}
**Essayez de convertir EPUB en PDF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["EPUB en PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité avec lesquelles cela fonctionne.

[![Aspose.PDF Conversion EPUB en PDF avec l'application](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Étapes pour convertir EPUB en PDF en Python :

1. Chargez le Document EPUB avec EpubLoadOptions().
1. Convertir EPUB en PDF.
1. Imprimer la confirmation.

Le fragment de code suivant vous montre comment convertir des fichiers EPUB au format PDF avec Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Convertir le Markdown en PDF

**Cette fonctionnalité est prise en charge à partir de la version 19.6 ou supérieure.**

{{% alert color="success" %}}
**Essayer de convertir Markdown en PDF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["Markdown en PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité avec lesquelles cela fonctionne.

[![Aspose.PDF Conversion de Markdown en PDF avec l'application](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Cet extrait de code d'Aspose.PDF for Python via .NET aide à convertir des fichiers Markdown en PDF, permettant un meilleur partage de documents, la préservation du formatage et la compatibilité d'impression.o

L'extrait de code suivant montre comment utiliser cette fonctionnalité avec la bibliothèque Aspose.PDF :

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Convertir PCL en PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) est un langage d'imprimante Hewlett‑Packard développé pour accéder aux fonctionnalités d'imprimante standard. Les niveaux PCL 1 à 5e/5c sont des langages basés sur des commandes utilisant des séquences de contrôle qui sont traitées et interprétées dans l'ordre de leur réception. Au niveau consommateur, les flux de données PCL sont générés par un pilote d'impression. La sortie PCL peut également être générée facilement par des applications personnalisées.

{{% alert color="success" %}}
**Essayer de convertir PCL en PDF en ligne**

Aspose.PDF for for .NET vous présente une application en ligne ["PCL en PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité avec lesquelles cela fonctionne.

[![Aspose.PDF Conversion PCL en PDF avec l'application](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Pour permettre la conversion de PCL en PDF, Aspose.PDF possède la classe [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) qui est utilisé pour initialiser l'objet LoadOptions. Par la suite, cet objet est passé comme argument lors de l'initialisation de l'objet Document et il aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le fragment de code suivant montre le processus de conversion d'un fichier PCL au format PDF.

Étapes Convertir PCL en PDF en Python :

1. Options de chargement pour PCL en utilisant PclLoadOptions().
1. Chargez le document.
1. Enregistrer au format PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir le texte préformaté en PDF

**Aspose.PDF for Python via .NET** prend en charge la fonctionnalité de conversion de texte brut et de fichiers texte préformatés au format PDF.

Convertir du texte en PDF signifie ajouter des fragments de texte à la page PDF. En ce qui concerne les fichiers texte, nous traitons de 2 types de texte : le pré-formatage (par exemple, 25 lignes de 80 caractères chacune) et le texte non formaté (texte brut). Selon nos besoins, nous pouvons contrôler cette addition nous-mêmes ou la confier aux algorithmes de la bibliothèque.

{{% alert color="success" %}}
**Essayer de convertir le TEXTE en PDF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["Texte en PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité avec lesquelles cela fonctionne.

[![Aspose.PDF Conversion TEXTE en PDF avec App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Étapes pour convertir le TEXT en PDF en Python :

1. Lire le fichier texte d'entrée ligne par ligne.
1. Configurez une police à espacement fixe (Courier New) pour un alignement de texte cohérent.
1. Créer un nouveau PDF Document et ajouter la première page avec des marges personnalisées et des paramètres de police.
1. Itérer à travers les lignes du fichier texte Pour simuler une machine à écrire, nous utilisons la police 'monospace_font' de taille 12.
1. Limiter la création de pages à 4 pages.
1. Enregistrez le PDF final dans le chemin spécifié.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir PostScript en PDF

Cet exemple montre comment convertir un fichier PostScript en document PDF à l'aide d'Aspose.PDF for Python via .NET.

1. Créez une instance de 'PsLoadOptions' pour interpréter correctement le fichier PS.
1. Chargez le fichier 'PostScript' dans un objet Document en utilisant les options de chargement.
1. Enregistrez le document au format PDF à l'emplacement de sortie souhaité.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir XPS en PDF

**Aspose.PDF for Python via .NET** prise en charge de la fonctionnalité de conversion <abbr title="XML Paper Specification">XPS</abbr> fichiers au format PDF. Consultez cet article pour résoudre vos tâches.

Le type de fichier XPS est principalement associé à la XML Paper Specification de Microsoft Corporation. La XML Paper Specification (XPS), anciennement nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft visant à intégrer la création et la visualisation de documents dans son système d'exploitation Windows.

Le fragment de code suivant montre le processus de conversion d'un fichier XPS en format PDF avec Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir le format XPS en PDF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["XPS en PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité avec lesquelles cela fonctionne.

[![Aspose.PDF Conversion XPS en PDF avec App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convertir XSL-FO en PDF

Le fragment de code suivant peut être utilisé pour convertir un XSLFO au format PDF avec Aspose.PDF for Python via .NET :

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Convertir XML avec XSLT en PDF

Cet exemple montre comment convertir un fichier XML en PDF en le transformant d'abord en HTML à l'aide d'un modèle XSLT, puis en chargeant le HTML dans Aspose.PDF.

1. Créez une instance de 'HtmlLoadOptions' pour configurer la conversion HTML vers PDF.
1. Chargez le fichier HTML transformé dans un objet Document Aspose.PDF.
1. Enregistrez le document au format PDF à l'emplacement de sortie spécifié.
1. Supprimez le fichier HTML temporaire après une conversion réussie.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Conversions associées

- [Convertir HTML en PDF](/pdf/fr/python-net/convert-html-to-pdf/) pour les scénarios de conversion HTML et MHTML.
- [Convertir les formats d'image en PDF](/pdf/fr/python-net/convert-images-format-to-pdf/) lorsque vos entrées sont PNG, JPEG, TIFF, SVG ou d’autres images.
- [Convertir le PDF en d’autres formats](/pdf/fr/python-net/convert-pdf-to-other-files/) si vous avez également besoin de conversions inverses telles que PDF vers EPUB, Markdown ou texte.
