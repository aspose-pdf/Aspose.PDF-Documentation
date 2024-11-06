---
title: Exemple de Hello World en utilisant Python
linktitle: Exemple de Hello World
type: docs
weight: 20
url: fr/python-net/hello-world-example/
description: Cet exemple démontre comment créer un document PDF simple avec le texte Hello World en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Un exemple "Hello World" montre la syntaxe la plus simple et le programme le plus simple dans n'importe quel langage de programmation donné. Les développeurs sont initiés à la syntaxe de base du langage de programmation en apprenant comment imprimer "Hello World" sur l'écran de l'appareil. Par conséquent, nous commencerons traditionnellement notre connaissance de notre bibliothèque par cela.

Dans cet article, nous créons un document PDF contenant le texte "Hello World!". Après avoir installé **Aspose.PDF pour Python via .NET** dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

L'extrait de code ci-dessous suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Ajouter une [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Ajouter TextFragment à la collection de [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) le document PDF résultant

Le code suivant est un programme "Hello World" pour démontrer le fonctionnement d'Aspose.PDF pour Python via l'API .NET.

```python

    import aspose.pdf as ap

    # Initialiser l'objet document
    document = ap.Document()
    # Ajouter une page
    page = document.pages.add()
    # Initialiser l'objet textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Ajouter le fragment de texte à la nouvelle page
    page.paragraphs.add(text_fragment)
    # Enregistrer le PDF mis à jour
    document.save("output.pdf")
```