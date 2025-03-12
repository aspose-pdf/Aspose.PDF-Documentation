---
title: Utilisation du générateur de documents PDF OneClick
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/using-oneclick-pdf-document-generator/
description: Apprenez à utiliser Aspose.PDF OneClick PDF Document Generator dans Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Débloquez une génération de documents sans faille dans Microsoft Dynamics avec le générateur de documents PDF OneClick d'Aspose.PDF. Cette fonctionnalité innovante permet aux utilisateurs de créer des modèles PDF personnalisables directement dans le CRM, de générer efficacement des documents d'un simple clic et d'intégrer facilement des boutons OneClick dans des formulaires pour un accès simplifié. Améliorez vos capacités de gestion des données et augmentez votre productivité avec cet outil puissant",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Créer un modèle et l'ajouter dans le CRM

- Ouvrez Word et créez un modèle.
- Insérez des champs MailMerge pour les données provenant du CRM.

![Insérer des champs MailMerge](using-oneclick-pdf-document-generator_1.png)

- Assurez-vous que le nom du champ correspond exactement au champ du CRM.
- Les modèles sont spécifiques à une utilisation avec une entité individuelle.

![Modèle de démonstration](using-oneclick-pdf-document-generator_2.png)

- Une fois le modèle créé, ouvrez l'entité de configuration OneClick PDF dans le CRM et créez un nouvel enregistrement.
- Donnez le nom du modèle, sélectionnez l'entité pour laquelle le modèle est défini et attachez le document créé dans la pièce jointe.

![Sélectionner le modèle](using-oneclick-pdf-document-generator_3.png)

## Générer un document à partir du bouton de la barre d'outils

- Ouvrez l'enregistrement où vous souhaitez générer le document. (Assurez-vous qu'un modèle est déjà attaché dans la configuration pour cette entité)
- Cliquez sur le bouton OneClick PDF dans la barre d'outils.

![Cliquez sur OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- Dans la fenêtre contextuelle : sélectionnez le modèle, le nom du fichier et l'action, puis cliquez sur Générer.
- Vérifiez le fichier téléchargé ou les notes, en fonction de la sélection.

## Configurer les boutons OneClick et les utiliser

- Pour utiliser le bouton OneClick directement depuis le formulaire, ouvrez la personnalisation du formulaire.
- Insérez WebResource où vous souhaitez ajouter des boutons OneClick.
- Sélectionnez OpenButtonPage dans WebResource et donnez-lui un nom.
- Configurez les boutons dans le champ de données dans l'exemple suivant.

![Propriétés de WebResource](using-oneclick-pdf-document-generator_5.png)

- Utilisez une ligne séparée pour chaque bouton et utilisez la syntaxe suivante :
  - Syntaxe : Nom du modèle |<Action : Télécharger/Note>|Nom du fichier de sortie
  - Exemple : Démo|Télécharger|Mon fichier téléchargé
- Enregistrez et publiez la personnalisation.
- Le bouton est disponible sur le formulaire.

![Le bouton est disponible sur le formulaire](using-oneclick-pdf-document-generator_6.png)