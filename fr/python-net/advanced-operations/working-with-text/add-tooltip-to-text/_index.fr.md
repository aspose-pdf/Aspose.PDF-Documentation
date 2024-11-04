---
title: PDF Tooltip en utilisant Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: /python-net/pdf-tooltip/
description: Apprenez à ajouter une info-bulle au fragment de texte dans un PDF en utilisant Python et Aspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip en utilisant Python",
    "alternativeHeadline": "Ajouter une info-bulle PDF au texte",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, ajouter info-bulle pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vente",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vente",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vente",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Apprenez à ajouter une info-bulle au fragment de texte dans un PDF en utilisant Python et Aspose.PDF"
}
</script>


## Ajouter une Info-bulle au Texte Recherché en ajoutant un Bouton Invisible

Ce code montre comment ajouter des info-bulles à des fragments de texte spécifiques dans un document PDF en utilisant Aspose.PDF. Les info-bulles s'affichent lorsque le curseur de la souris survole le texte correspondant.

Le code suivant vous montrera comment réaliser cette fonctionnalité :

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Déplacez le curseur de la souris ici pour afficher une info-bulle")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "Déplacez le curseur de la souris ici pour afficher une info-bulle très longue"
        )
    )
    document.save(output_pdf)

    # Ouvrir le document avec le texte
    document = ap.Document(output_pdf)
    # Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
    absorber = ap.text.TextFragmentAbsorber(
        "Déplacez le curseur de la souris ici pour afficher une info-bulle"
    )
    # Accepter l'absorbeur pour les pages du document
    document.pages.accept(absorber)
    # Obtenir les fragments de texte extraits
    text_fragments = absorber.text_fragments

    # Boucler à travers les fragments
    for fragment in text_fragments:
        # Créer un bouton invisible à la position du fragment de texte
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # La valeur de alternate_name sera affichée comme info-bulle par une application de visualisation
        field.alternate_name = "Info-bulle pour le texte."
        # Ajouter le champ de bouton au document
        document.form.add(field)

    # Ensuite, un exemple d'info-bulle très longue
    absorber = ap.text.TextFragmentAbsorber(
        "Déplacez le curseur de la souris ici pour afficher une info-bulle très longue"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Définir un texte très long
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # Enregistrer le document
    document.save(output_pdf)
```


## Créer un bloc de texte caché et l'afficher au survol de la souris

Ce snippet de code Python montre comment ajouter du texte flottant à un document PDF, qui apparaît lorsque le curseur de la souris survole une zone spécifique.

Tout d'abord, un nouveau document PDF est créé, et un paragraphe contenant le texte "Déplacez le curseur de la souris ici pour afficher le texte flottant" est ajouté. Le document est ensuite enregistré.

Ensuite, le document enregistré est rouvert, et un objet TextAbsorber est créé pour trouver le fragment de texte précédemment ajouté. Ce fragment de texte est ensuite utilisé pour définir la position et les caractéristiques du champ de texte flottant.

Un objet TextBoxField est créé pour représenter le champ de texte flottant, et ses propriétés telles que la position, la valeur, le statut en lecture seule, et la visibilité sont configurées en conséquence. De plus, un nom unique et des caractéristiques d'apparence sont attribués au champ.

Le champ de texte flottant est ajouté au formulaire du document, et un champ de bouton invisible est créé à la position du fragment de texte original.
 Les événements HideAction sont assignés au champ de bouton, spécifiant que le champ de texte flottant doit apparaître lorsque le curseur de la souris entre dans sa proximité et disparaître lorsque le curseur en sort.

Enfin, le champ de bouton est ajouté au formulaire du document, et le document modifié est enregistré.

Cet extrait de code fournit une méthode pour créer des éléments de texte flottants interactifs dans un document PDF en utilisant Aspose.PDF pour Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Déplacez le curseur de la souris ici pour afficher le texte flottant")
    )
    document.save(output_pdf)

    # Ouvrir le document avec du texte
    document = ap.Document(output_pdf)
    # Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
    absorber = ap.text.TextFragmentAbsorber(
        "Déplacez le curseur de la souris ici pour afficher le texte flottant"
    )
    # Accepter l'absorbeur pour les pages du document
    document.pages.accept(absorber)
    # Obtenir le premier fragment de texte extrait
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # Créer un champ de texte caché pour le texte flottant dans le rectangle spécifié de la page
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # Définir le texte à afficher comme valeur du champ
    floating_field.value = 'Ceci est le "champ de texte flottant".'
    # Nous recommandons de rendre le champ 'readonly' pour ce scénario
    floating_field.read_only = True
    # Définir le drapeau 'hidden' pour rendre le champ invisible à l'ouverture du document
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # Définir un nom de champ unique n'est pas nécessaire mais autorisé
    floating_field.partial_name = "FloatingField_1"

    # Définir les caractéristiques de l'apparence du champ n'est pas nécessaire mais améliore
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # Ajouter le champ de texte au document
    document.form.add(floating_field)
    # Créer un bouton invisible à la position du fragment de texte
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # Créer une nouvelle action de masquage pour le champ spécifié (annotation) et le drapeau d'invisibilité.
    # (Vous pouvez également référer le champ flottant par le nom si vous l'avez spécifié ci-dessus.)
    # Ajouter des actions à l'entrée/sortie de la souris sur le champ de bouton invisible

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # Ajouter le champ de bouton au document
    document.form.add(button_field)

    # Enregistrer le document
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>