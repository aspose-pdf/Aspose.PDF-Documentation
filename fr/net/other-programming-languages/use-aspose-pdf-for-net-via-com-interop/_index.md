---
title: Aspose.PDF for .NET via COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/use-aspose-pdf-for-net-via-com-interop/
description: Découvrez comment utiliser Aspose.PDF for .NET via COM Interop pour une intégration transparente avec des applications non-.NET.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET prend désormais en charge une intégration transparente avec divers langages de programmation via COM Interop, permettant aux développeurs d'utiliser ses puissantes capacités de manipulation de PDF en dehors du cadre .NET. Cette fonctionnalité améliore la flexibilité en transformant les objets Aspose.PDF en objets COM, simplifiant les interactions avec le code non géré tout en maintenant des performances élevées grâce aux techniques de liaison précoce et tardive.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

Les informations dans ce sujet s'appliquent aux scénarios où vous souhaitez utiliser [Aspose.PDF for .NET](/pdf/fr/net/) via COM Interop dans l'un des langages de programmation suivants :

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Travailler avec COM Interop

Aspose.PDF for .NET s'exécute sous le contrôle du .NET Framework et cela s'appelle du code géré. Le code écrit dans tous les langages ci-dessus s'exécute en dehors du .NET Framework et cela s'appelle du code non géré. L'interaction entre le code non géré et Aspose.PDF se produit via la fonctionnalité .NET appelée COM Interop.

Les objets Aspose.PDF sont des objets .NET, mais lorsqu'ils sont utilisés via COM Interop, ils apparaissent comme des objets COM dans votre langage de programmation. Par conséquent, il est préférable de s'assurer que vous savez comment créer et utiliser des objets COM dans votre langage de programmation, avant de commencer à utiliser [Aspose.PDF for .NET](/pdf/fr/net/).

{{% alert color="primary" %}}

- Dans le monde COM, nous distinguons le serveur COM et le client COM. Le serveur COM stocke les classes COM tandis que le client COM demande au serveur COM des instances de classes, c'est-à-dire des objets COM.
- Le client COM ou simplement l'application cliente peut connaître le contenu de la classe COM ou être totalement inconscient de ses méthodes et propriétés. Par conséquent, l'application cliente peut découvrir la structure de la classe COM lors de la compilation/construction ou uniquement pendant l'exécution. Le processus de "découverte" est connu sous le nom de liaison et nous avons donc **liaison précoce** et **liaison tardive**.
- en bref, la classe COM est comme une boîte noire et pour travailler avec elle, une bibliothèque de types est nécessaire, ce fichier binaire a une description des méthodes, propriétés de la classe COM et tout langage de haut niveau qui prend en charge le travail avec des objets COM a souvent une expression de syntaxe pour ajouter une bibliothèque de types, par exemple, c'est [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) en C++.
- la bibliothèque de types est utilisée pour la liaison précoce.
- un objet COM peut exposer ses méthodes et propriétés de deux manières : par le biais d'une **interface de dispatch** (dispinterface) et dans sa **vtable** (table des fonctions virtuelles).
- au sein de l'**interface de dispatch**, chaque méthode et propriété est identifiée par un membre unique ; ce membre est l'identifiant de dispatch de la fonction (ou **DispID**).
- **vtable** est simplement un ensemble de pointeurs vers des fonctions que l'interface de classe COM prend en charge.
- un objet qui expose ses méthodes par les deux interfaces prend en charge une **interface duale**.
- il y a des avantages aux deux types de liaison. La liaison précoce vous offre des performances accrues et une vérification de syntaxe à la compilation. La liaison tardive est la plus avantageuse lorsque vous écrivez des clients que vous souhaitez rendre ***compatibles avec les futures versions*** de votre classe COM. Avec la liaison tardive, les informations de la bibliothèque de types ne sont pas "câblées" dans votre client, vous pouvez donc avoir une plus grande confiance que votre client peut fonctionner avec les futures versions de la classe COM sans modifications de code.
- le mécanisme de liaison tardive a un grand avantage : si le créateur de la DLL COM décide de publier une nouvelle version, avec une disposition d'interface de fonction différente, tout code appelant ces méthodes ne plantera pas à moins que les méthodes ne soient plus disponibles ; même si la **vtable** est différente, la liaison tardive parvient à découvrir les nouveaux DISPIDs et à appeler les méthodes appropriées.
{{% /alert %}}

Voici les sujets que vous devrez éventuellement maîtriser :
{{% alert color="primary" %}}

- Utilisation des objets COM dans votre langage de programmation. Consultez la documentation de votre langage de programmation et les sujets spécifiques au langage plus loin dans cette documentation.

- Travailler avec des objets COM exposés par .NET COM Interop. Voir [Interopérer avec du code non géré](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) et [Exposer des composants du .NET Framework à COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) dans MSDN.

- Modèle d'objet de document Aspose.PDF. Voir [Guide du programmeur Aspose.PDF](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) et [Référence API](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## Enregistrer Aspose.PDF for .NET avec COM Interop

Vous devez installer Aspose.PDF for .NET et vous assurer qu'il est enregistré avec COM Interop (en vous assurant qu'il peut être appelé depuis du code non géré).

{{% alert color="primary" %}}

Pour enregistrer Aspose.PDF for .NET pour COM Interop manuellement :

1. Dans le menu **Démarrer**, sélectionnez **Tous les programmes**, puis **Microsoft Visual Studio**, **Outils Visual Studio** et enfin **Invite de commandes Visual Studio**.
1. Entrez la commande pour enregistrer l'assembly :
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Attention, /codebase est nécessaire uniquement si Aspose.PDF.dll n'est pas dans le GAC, l'utilisation de cette option fait que regasm met le chemin de l'assembly dans le registre.

{{% alert color="primary" %}}

regasm.exe est un outil inclus dans le SDK du .NET Framework. Tous les outils du SDK du .NET Framework se trouvent dans le répertoire *\Microsoft .NET\Framevork\<FrameworkVersion>*, par exemple *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Si vous utilisez Visual Studio .NET :
Dans le menu **Démarrer**, sélectionnez **Programmes**, suivi de **Visual Studio 2022**, enfin, **Invite de commandes pour développeurs VS 2022**.
Cela exécute une invite de commandes avec toutes les variables d'environnement nécessaires définies.

{{% /alert %}}

### ProgIDs

ProgID signifie "identifiant programmatique". C'est le nom d'une classe COM utilisée pour créer un objet. Les ProgIDs se composent du nom de la bibliothèque "Aspose.PDF" et du nom de la classe.

### Bibliothèque de types

{{% alert color="primary" %}}

Si votre langage de programmation (par exemple Visual Basic ou Delphi) vous permet de référencer une bibliothèque de types COM, alors ajoutez une référence à Aspose.PDF.tlb et pour voir toutes les classes, méthodes, propriétés et énumérations de Aspose.PDF for .NET dans votre navigateur d'objets.

Pour générer un fichier TLB :

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Création d'objets COM

La création d'un objet COM est similaire à la création d'un objet .NET normal :

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

Une fois créé, vous pouvez accéder aux méthodes et propriétés de l'objet, comme s'il s'agissait d'un objet COM :

```vb
'Add page to the document
document.Pages.Add()
```

Certaines méthodes ont des surcharges et elles seront exposées par COM Interop avec un suffixe numérique ajouté, sauf pour la toute première méthode qui reste inchangée. Par exemple, les surcharges de la méthode Document.Save deviennent Document.Save, Document.Save_2, et ainsi de suite.

Pour plus d'informations, consultez les articles spécifiques au langage plus loin dans cette documentation.

## Création d'une assembly wrapper

Si vous devez utiliser de nombreuses classes, méthodes et propriétés de Aspose.PDF for .NET, envisagez de créer une assembly wrapper (en utilisant C# ou tout autre langage de programmation .NET). Les assemblies wrapper aident à éviter d'utiliser Aspose.PDF for .NET directement depuis du code non géré.

Une bonne approche consiste à développer une assembly .NET qui référence Aspose.PDF for .NET et fait tout le travail avec, et n'expose qu'un ensemble minimal de classes et de méthodes au code non géré. Votre application devrait alors fonctionner uniquement avec votre bibliothèque wrapper.

Réduire le nombre de classes et de méthodes que vous devez invoquer via COM Interop simplifie le projet. Utiliser des classes .NET via COM Interop nécessite souvent des compétences avancées.