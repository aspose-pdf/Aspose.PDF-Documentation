---
title: Module d'importation PDF Umbraco
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/umbraco-pdf-import-module/
description: Apprenez à installer et à utiliser le module d'importation PDF Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Umbraco PDF Import Module",
    "alternativeHeadline": "Umbraco Module Simplifies PDF Content Import Process",
    "abstract": "Le module d'importation PDF Umbraco permet aux développeurs d'importer facilement du contenu PDF dans leurs sites Web Umbraco sans avoir besoin de logiciels supplémentaires. Cet add-on open-source puissant simplifie la gestion des documents en fournissant une interface conviviale pour récupérer et afficher instantanément le contenu PDF, améliorant ainsi l'efficacité de la gestion de contenu au sein des applications .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "950",
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
    "url": "/net/umbraco-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/umbraco-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Introduction

**Aspose.PDF for .NET** est un composant de création et de manipulation de documents PDF qui permet à vos applications .NET de lire, écrire et manipuler des documents PDF existants sans utiliser Adobe Acrobat. Il vous permet également de créer des formulaires et de gérer les champs de formulaire intégrés dans un document PDF.

**Aspose.PDF for .NET** est abordable et offre une incroyable richesse de fonctionnalités, y compris des options de compression PDF ; création et manipulation de tableaux ; prise en charge des objets graphiques ; fonctionnalité de lien hypertexte étendue ; contrôles de sécurité avancés ; gestion de polices personnalisées ; intégration avec des sources de données ; ajout ou suppression de signets ; création de tables des matières ; ajout, mise à jour, suppression de pièces jointes et d'annotations ; importation ou exportation de données de formulaire PDF ; ajout, remplacement ou suppression de texte et d'images ; division, concaténation, extraction ou insertion de pages ; transformation de pages en image ; impression de documents PDF et bien plus encore.

### **Fonctionnalités du module**

L'importation PDF Umbraco est un add-on open source de [Aspose](http://www.aspose.com/) qui permet aux développeurs de récupérer/lire le contenu de n'importe quel document PDF sans nécessiter d'autres logiciels. Cet add-on démontre la puissante fonctionnalité d'importation fournie par [Aspose.PDF](https://products.aspose.com/pdf/net/). Il ajoute un simple contrôle de navigateur de fichiers et un bouton **Importer depuis PDF** sur la page où l'add-on est ajouté. En cliquant sur le bouton, le contenu du document est récupéré à partir du fichier et affiché immédiatement à l'écran.

## Exigences système et plateformes prises en charge

### **Exigences système**

Pour configurer le module d'importation PDF Aspose .NET pour Umbraco, vous devez répondre aux exigences suivantes :

- Umbraco 6.0+.

N'hésitez pas à nous contacter si vous souhaitez installer ce module sur d'autres versions d'Umbraco.

### **Plateformes prises en charge**

Le module est pris en charge sur toutes les versions de

- Umbraco fonctionnant sur ASP.NET 4.0.

## Téléchargement

Vous pouvez télécharger Aspose .NET Pdf Import pour Umbraco à partir de l'un des emplacements suivants :

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases).
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads).
- [Umbraco](https://our.umbraco.com/packages/developer-tools/import-from-pdf-using-asposepdf/).

## Installation

Une fois téléchargé, veuillez suivre ces étapes pour installer ce package dans votre site Web Umbraco :

1. Connectez-vous à la section **Développeur** d'Umbraco, par exemple <http://www.myblog.com/umbraco/>.
1. Dans l'arborescence, développez le dossier **Packages**.
   À partir d'ici, il existe deux façons d'installer un package : sélectionnez **Installer un package local** ou parcourez le **Dépôt de packages Umbraco.**.
1. Si vous installez un **package local**, ne décompressez pas le package mais chargez le zip dans Umbraco.
1. Suivez les instructions à l'écran.

**Remarque :** Vous pouvez rencontrer une erreur ‘Longueur de requête maximale dépassée’ lors de l'installation. Vous pouvez facilement résoudre ce problème en mettant à jour la valeur ‘maxRequestLength’ dans votre fichier web.config Umbraco.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## Utilisation

Après avoir installé le macro, il est très simple de commencer à l'utiliser sur votre site Web :

1. Assurez-vous d'être connecté à la section **Développeur** d'Umbraco, par exemple <http://www.myblog.com/umbraco/>.
1. Cliquez sur **Paramètres** dans la liste des sections en bas à gauche de l'écran.
1. Développez le nœud **Modèles** et sélectionnez le modèle auquel vous souhaitez ajouter le macro, par exemple un article de blog.
1. Sélectionnez la position dans le modèle sélectionné où vous souhaitez placer le bouton.
1. Cliquez sur **Insérer Macro** dans le ruban supérieur.
1. Dans **Choisir un macro**, sélectionnez le macro installé et cliquez sur **OK**.

Vous avez ajouté avec succès le modèle. Un bouton intitulé **Importer depuis Pdf** apparaît maintenant sur toutes les pages créées à l'aide de ce modèle. Quiconque peut simplement cliquer sur le bouton et importer le contenu d'un document PDF.

## Démonstration vidéo

Veuillez consulter [la vidéo](https://www.youtube.com/watch?v=zmZTJ86B25E) ci-dessous pour voir le module en action.

## Support, Extension et Contribution

### Support

Dès les premiers jours d'Aspose, nous savions que donner simplement de bons produits à nos clients ne suffirait pas. Nous devions également fournir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant qu'un problème technique ou une particularité du logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre des problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Quiconque utilise notre produit, qu'il l'ait acheté ou qu'il utilise une évaluation, mérite notre pleine attention et respect.

Vous pouvez signaler tout problème ou suggestion lié aux modules Aspose.PDF .NET pour Umbraco en utilisant l'une des plateformes suivantes :

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open).

### Étendre et Contribuer

Aspose .NET PDF Import pour Umbraco est open source et son code source est disponible sur les principaux sites de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à étendre la fonctionnalité selon leurs propres besoins.

#### Code source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants :

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src).

#### Comment configurer le code source

Vous devez avoir les éléments suivants installés pour ouvrir et étendre le code source :

- Visual Studio 2010 ou supérieur.

Veuillez suivre ces étapes simples pour commencer :

1. Téléchargez/cloner le code source.
1. Ouvrez Visual Studio 2010 et choisissez **Fichier** > **Ouvrir le projet**.
1. Parcourez le dernier code source que vous avez téléchargé et ouvrez **Aspose.Import from PDF.sln**.