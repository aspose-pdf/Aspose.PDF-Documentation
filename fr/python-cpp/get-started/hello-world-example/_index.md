---
title: Exemple de Hello World en utilisant le langage Python
linktitle: Exemple de Hello World
type: docs
weight: 20
url: fr/python-cpp/hello-world-example/
description: Cet exemple montre comment créer un document PDF simple "Hello, World!" en utilisant Aspose.PDF pour Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exemple de Hello World en utilisant le langage Python",
    "alternativeHeadline": "Exemple Aspose.PDF Python (via C++)",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, Python, génération de documents",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe Doc Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet exemple montre comment créer un document PDF simple en utilisant Aspose.PDF pour Python.",
    "articleBody": "Un cas d'utilisation simple peut aider à démontrer les fonctionnalités d'un langage de programmation ou d'un logiciel. Cela se fait généralement avec un exemple de \"Hello World\".\n\nAspose.PDF pour Python via C++ est une puissante API PDF qui permet aux développeurs de créer, manipuler et convertir des documents PDF dans leurs applications Python. Il prend en charge le travail avec divers formats de fichiers tels que PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX et les formats de fichiers image. Dans cet article, nous allons vous montrer comment créer un document PDF avec le texte \"Hello World!\" en utilisant l'API Aspose.PDF. Vous devez installer Aspose.PDF pour Python via C++ dans votre environnement avant d'exécuter l'exemple de code suivant.\n1. Importez le module AsposePdfPython.\n2. Créez un nouvel objet document PDF en utilisant la fonction document_create.\n3. Obtenez la collection des pages du document en utilisant la fonction document_get_pages.\n4. Ajoutez une nouvelle page à la collection de pages en utilisant la fonction page_collection_add_page.\n5. Obtenez la collection des paragraphes de la page en utilisant la fonction page_get_paragraphs.\n6. Créez un nouvel objet image en utilisant la fonction image_create.\n7. Définissez le nom de fichier de l'objet image sur \"sample.jpg\" en utilisant la fonction image_set_file.\n8. Ajoutez l'objet image à la collection de paragraphes en utilisant la fonction paragraphs_add_image.\n9. Enregistrez le document dans un fichier nommé \"document.pdf\" en utilisant la fonction document_save.\n10. Fermez le handle du document en utilisant la fonction close_handle."
}
</script>


A simple use case can help to demonstrate the features of a programming language or software. This is usually done with a "Hello World" example.

Aspose.PDF pour Python via C++ est une API PDF puissante qui permet aux développeurs de créer, manipuler et convertir des documents PDF dans leurs applications Python. Il prend en charge le travail avec divers formats de fichiers tels que PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX et formats de fichiers image. Dans cet article, nous vous montrerons comment créer un document PDF avec le texte "Hello World!" en utilisant l'API Aspose.PDF. Vous devez installer Aspose.PDF pour Python via C++ dans votre environnement avant d'exécuter l'exemple de code suivant.

1. Importer le module `AsposePdfPython`.
1. Créer un nouvel objet document PDF en utilisant la fonction `document_create`.
1. Obtenez la collection de pages du document en utilisant la fonction `document_get_pages`.
1. Ajouter une nouvelle page à la collection de pages en utilisant la fonction `page_collection_add_page`.

1. Obtenez la collection de paragraphes de la page en utilisant la fonction `page_get_paragraphs`.
1. Créer un nouvel objet image en utilisant la fonction `image_create`.
1. Définir le nom de fichier de l'objet image sur "sample.jpg" en utilisant la fonction `image_set_file`.
1. Ajouter l'objet image à la collection de paragraphes en utilisant la fonction `paragraphs_add_image`.
1. Sauvegarder le document dans un fichier nommé "document.pdf" en utilisant la fonction `document_save`.
1. Fermer le handle du document en utilisant la fonction `close_handle`.

Le snippet de code suivant est un programme Hello World qui montre comment fonctionne Aspose.PDF pour Python via C++.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```