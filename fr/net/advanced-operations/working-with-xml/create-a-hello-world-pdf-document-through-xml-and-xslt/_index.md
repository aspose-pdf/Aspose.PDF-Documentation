---
title: Création de PDF à partir de XML en utilisant XSLT
linktitle: Créer un PDF à partir de XML en utilisant XSLT
type: docs
weight: 10
url: /fr/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: La bibliothèque C# offre la possibilité de convertir un fichier XML en document PDF en exigeant que le fichier XML d'entrée suive le schéma Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Création de PDF à partir de XML en utilisant XSLT",
    "alternativeHeadline": "Comment créer un PDF à partir de XML en utilisant XSLT",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, c#, créer pdf xml, pdf avec xslt",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2022-02-04",
    "description": "La bibliothèque C# offre la possibilité de convertir un fichier XML en document PDF en exigeant que le fichier XML d'entrée suive le schéma Aspose.PDF."
}
</script>
The following code snippet also work with [Aspose.PDF.Drawing](/pdf/fr/net/drawing/) library.

Parfois, vous pouvez avoir des fichiers XML existants contenant des données d'application et vous souhaitez générer un rapport PDF en utilisant ces fichiers. Vous pouvez utiliser XSLT pour transformer votre document XML existant en un document XML compatible avec Aspose.Pdf, puis générer un fichier PDF. Il y a 3 étapes pour générer un PDF en utilisant XML et XSLT.

Veuillez suivre ces étapes pour convertir un fichier XML en un document PDF en utilisant XSLT :

* Créez une instance de la classe PDF qui représente un document PDF
* Si vous avez acheté une licence, vous devez également intégrer le code pour utiliser cette licence avec l'aide de la classe License dans l'espace de noms Aspose.Pdf
* Liez les fichiers XML et XSLT d'entrée à l'instance de la classe PDF en appelant sa méthode BindXML
* Enregistrez le XML lié avec l'instance PDF en tant que document PDF

## Fichier XML d'entrée

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Fichier XSLT d'entrée

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

---
id: docker
title: Docker
sidebar_label: Docker
slug: /docker
---

Docker est un outil conçu pour faciliter la création, le déploiement et l'exécution d'applications en utilisant des conteneurs. Les conteneurs permettent à un développeur de regrouper une application avec toutes les parties dont elle a besoin, telles que des bibliothèques et d'autres dépendances, et de les expédier toutes sous forme d'un seul paquet.

## Introduction

Docker est une plateforme logicielle qui vous permet de créer, tester et déployer des applications rapidement. Docker regroupe le logiciel avec toutes ses bibliothèques et dépendances dans un conteneur, et ce conteneur peut être déployé sur n'importe quel hôte Docker.

## Avantages de Docker

- **Portabilité**: Les conteneurs Docker peuvent s'exécuter sur n'importe quelle machine qui prend en charge Docker sans aucune modification.
- **Isolation**: Chaque conteneur s'exécute dans son propre environnement, ce qui permet une meilleure gestion des dépendances et des versions.
- **Efficacité**: Docker utilise moins de ressources système que les machines virtuelles, ce qui permet une utilisation plus efficace des ressources système.

## Concepts clés

- **Image**: Une image Docker est un modèle en lecture seule avec les instructions pour créer un conteneur Docker. Souvent, une image est basée sur une autre image, avec quelques personnalisations supplémentaires.
- **Conteneur**: Un conteneur est une instance en cours d'exécution d'une image Docker. Un conteneur est le processus en cours d'exécution et l'environnement isolé dans lequel il s'exécute.
- **Dockerfile**: Un Dockerfile est un fichier texte qui contient toutes les commandes qu'un utilisateur pourrait appeler sur la ligne de commande pour assembler une image.

## Commandes Docker de base

Voici quelques commandes Docker de base pour vous aider à démarrer:

- `docker build`: Cette commande construit une image à partir d'un Dockerfile et d'un contexte.
- `docker run`: Cette commande exécute un conteneur à partir d'une image Docker.
- `docker pull`: Cette commande télécharge une image depuis un registre Docker.
- `docker push`: Cette commande pousse une image vers un registre Docker.
- `docker ps`: Cette commande liste les conteneurs Docker en cours d'exécution.

## Conclusion

Docker est un outil puissant qui peut grandement simplifier le processus de développement, de déploiement et d'exécution des applications. En utilisant des conteneurs, les développeurs peuvent s'assurer que leurs applications fonctionneront de manière cohérente, quel que soit l'environnement dans lequel elles sont déployées.
```
