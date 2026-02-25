---
title: Exemple de Hello World avec Python
linktitle: Exemple Hello World
type: docs
weight: 20
url: /fr/python-net/hello-world-example/
description: Cet exemple montre comment créer un document PDF simple contenant le texte Hello World en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemple Hello World via Python
Abstract: Cet article fournit un exemple Hello World utilisant la bibliothèque Aspose.PDF pour Python via .NET afin de créer un document PDF. L'exemple montre les étapes de base de l'utilisation de l'API Aspose.PDF en générant un PDF contenant le texte "Hello World!". Le processus consiste à instancier un objet `Document`, ajouter une `Page`, créer un objet `TextFragment`, définir les propriétés du texte telles que la taille de la police et la couleur, et utiliser un `TextBuilder` pour ajouter le texte à la page. Le PDF résultant est ensuite enregistré sous le nom "HelloWorld_out.pdf". L'article inclut un extrait complet de code Python illustrant ces étapes, servant de guide d'introduction à l'utilisation de la bibliothèque.
---

Un "Hello World" exemple montre la syntaxe la plus simple et le programme le plus simple dans n'importe quel langage de programmation. Les développeurs sont initiés à la syntaxe de base du langage en apprenant comment afficher "Hello World" sur l'écran de l'appareil. Par conséquent, nous commencerons traditionnellement notre prise en main de notre bibliothèque avec cela.

Dans cet article, nous créons un document PDF contenant le texte "Hello World!". Après avoir installé **Aspose.PDF for Python via .NET** dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

Le fragment de code ci-dessous suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Ajouter une [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Définir les couleurs du texte
1. Créer un Text Builder
1. Ajouter le [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à la Page
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) le document PDF résultant

Le fragment de code suivant est un programme "Hello World" qui démontre la fonctionnalité d'Aspose.PDF pour Python via l'API .NET.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
