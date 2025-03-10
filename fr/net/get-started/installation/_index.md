---
title: Comment installer Aspose.PDF for .NET
linktitle: Installation
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/installation/
description: Cette section montre une description du produit et des instructions pour installer Aspose.PDF for .NET par vous-même, ainsi que l'utilisation de NuGet.
lastmod: "2024-09-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Install Aspose.PDF for .NET",
    "alternativeHeadline": "Seamless PDF Creation with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET est un composant puissant qui permet aux développeurs de générer et de manipuler des documents PDF par programmation sans dépendre d'Adobe Acrobat. Avec le support de l'insertion d'éléments complexes tels que des tableaux, des images et des polices personnalisées, ainsi que des fonctionnalités de sécurité robustes et une intégration transparente via NuGet, cet outil polyvalent améliore la productivité et l'efficacité dans les applications .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Aspose.PDF, PDF documents, .NET component, NuGet installation, C# API, Temporary License, multithread safe, eval version limitations, .NET Core support, font installation",
    "wordcount": "1214",
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
    "url": "/net/installation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/installation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Composant Aspose.PDF C#

{{% alert color="primary" %}}

**Aspose.PDF est un composant .NET** conçu pour permettre aux développeurs de créer des documents PDF, qu'ils soient simples ou complexes, à la volée par programmation. Aspose.PDF for .NET permet aux développeurs d'insérer des tableaux, des graphiques, des images, des hyperliens, des polices personnalisées - et plus encore - dans des documents PDF. De plus, il est également possible de compresser des documents PDF. Aspose.PDF for .NET offre d'excellentes fonctionnalités de sécurité pour développer des documents PDF sécurisés. Et la caractéristique la plus distincte de Aspose.PDF for .NET est qu'il prend en charge la création de documents PDF à la fois via une API et à partir de modèles XML.

{{% /alert %}}

## Description du produit

**Aspose.PDF for .NET** est un composant .NET robuste qui permet aux développeurs de créer des documents PDF à partir de zéro sans utiliser Adobe Acrobat. Il fournit une interface de programmation d'application (API) simple qui est facile à apprendre et à utiliser.

**Aspose.PDF for .NET** est implémenté en utilisant C# géré et peut être utilisé avec n'importe quel langage .NET comme C#, VB.NET et J# etc. Il peut être intégré à tout type d'application, que ce soit une application Web ASP.NET ou une application Windows.

Pour que les développeurs puissent se lancer rapidement, Aspose.PDF for .NET fournit des démonstrations entièrement fonctionnelles et des exemples de travail écrits en C#. Grâce à ces démonstrations, les développeurs peuvent rapidement découvrir les fonctionnalités offertes par Aspose.PDF for .NET.

Le composant rapide et léger crée des documents PDF efficacement et aide votre application à mieux fonctionner. Aspose.PDF for .NET est le premier choix de nos clients lors de la création de documents PDF en raison de son prix, de ses performances exceptionnelles et de son excellent support.

**Aspose.PDF for .NET** est sécurisé multithread tant qu'un seul thread travaille sur un document à la fois. Il est courant d'avoir un thread travaillant sur un document. Différents threads peuvent travailler en toute sécurité sur différents documents en même temps.

## Déclaration

Tous les composants Aspose .NET nécessitent un ensemble de permissions de confiance totale. La raison en est que les composants Aspose .NET doivent accéder aux paramètres du registre, aux fichiers système autres que le répertoire virtuel pour certaines opérations comme l'analyse des polices, etc. De plus, les composants Aspose .NET sont basés sur des classes système .NET de base qui nécessitent également un ensemble de permissions de confiance totale dans de nombreux cas.

Les fournisseurs de services Internet hébergeant plusieurs applications de différentes entreprises appliquent généralement un niveau de sécurité de confiance moyenne. Dans le cas de .NET 2.0, ce niveau de sécurité impose les contraintes suivantes :

- **OleDbPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas utiliser le fournisseur de données OLE DB géré ADO.NET pour accéder aux bases de données.
- **EventLogPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas accéder au journal des événements Windows.
- **ReflectionPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas utiliser la réflexion.
- **RegistryPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas accéder au registre.
- **WebPermission est restreint.** Cela signifie que votre application ne peut communiquer qu'avec une adresse ou une plage d'adresses que vous définissez dans l'élément `<trust>`.
- **FileIOPermission est restreint.** Cela signifie que vous ne pouvez accéder qu'aux fichiers dans la hiérarchie de répertoires virtuels de votre application.
En raison des raisons spécifiées ci-dessus, les composants Aspose .NET ne peuvent pas être utilisés sur des serveurs accordant un ensemble de permissions autre que la confiance totale.

## Installation

### Évaluer Aspose.PDF for .NET

Vous pouvez facilement télécharger Aspose.PDF for .NET pour évaluation. Le téléchargement d'évaluation est le même que le téléchargement acheté. La version d'évaluation devient simplement sous licence lorsque vous ajoutez quelques lignes de code pour appliquer la licence.

La version d'évaluation d'Aspose.PDF (sans licence spécifiée) fournit l'intégralité des fonctionnalités du produit. Cependant, elle a deux limitations : elle insère un filigrane d'évaluation et seules les quatre premières pages de tout document peuvent être visualisées/éditées.

{{% alert color="primary" %}}

Si vous souhaitez tester Aspose.PDF for .NET sans les limitations de la version d'évaluation, vous pouvez également demander une Licence Temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une Licence Temporaire ?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

### Installer Aspose.PDF for .NET via NuGet

NuGet est un système de gestion de packages gratuit et open source axé sur les développeurs pour la plateforme .NET, visant à simplifier le processus d'incorporation de bibliothèques tierces dans une application .NET pendant le développement. C'est une extension de Visual Studio qui facilite l'ajout, la suppression et la mise à jour de bibliothèques et d'outils dans des projets Visual Studio utilisant le .NET Framework. Une bibliothèque ou un outil peut facilement être partagé avec d'autres développeurs en créant un package NuGet et en le stockant dans un dépôt NuGet. Lorsque vous installez le package, NuGet copie les fichiers dans votre solution et effectue automatiquement les modifications nécessaires, telles que l'ajout de références et la modification de vos fichiers app.config ou web.config. Si vous décidez de supprimer la bibliothèque, NuGet supprime les fichiers et inverse toutes les modifications qu'il a apportées à votre projet afin qu'aucun encombrement ne reste.

### Référencer Aspose.PDF for .NET

#### Installer le package en utilisant la Console du Gestionnaire de Packages

- Ouvrez votre application .NET dans Visual Studio.
- Dans le menu Outils, sélectionnez **Gestionnaire de Packages NuGet** puis **Console du Gestionnaire de Packages**.
- Tapez la commande `Install-Package Aspose.PDF` pour installer la dernière version complète, ou tapez la commande `Install-Package Aspose.PDF -prerelease` pour installer la dernière version incluant des correctifs.
- Appuyez sur `Entrée`.

#### Mettre à jour le package en utilisant la Console du Gestionnaire de Packages

Si vous avez déjà référencé le composant via NuGet, suivez ces étapes pour mettre à jour la référence à la dernière version :

- Ouvrez votre application .NET dans Visual Studio.
- Dans le menu Outils, sélectionnez **Gestionnaire de Packages NuGet** puis **Console du Gestionnaire de Packages**.
- Tapez la commande `Update-Package Aspose.PDF` pour référencer la dernière version complète, ou tapez la commande `Update-Package Aspose.PDF -prerelease` pour installer la dernière version incluant des correctifs.

#### Installer le Package en utilisant l'Interface Graphique du Gestionnaire de Packages

Suivez ces étapes pour référencer le composant en utilisant l'interface graphique du gestionnaire de packages :

- Ouvrez votre application .NET dans Visual Studio.

- Dans le menu Projet, sélectionnez **Gérer les Packages NuGet**.

![Installation_step](../images/install_step.png)

- Sélectionnez l'onglet **Broswe**.

![Installation_step1](../images/install_step1.png)

- Tapez Aspose.PDF dans la zone de recherche pour trouver Aspose.PDF for .NET.

- Cliquez sur Installer/Mise à jour à côté de la dernière version de Aspose.PDF for .NET.

![Installation_step2](../images/Install_step2.png)

- Et cliquez sur Accepter dans la fenêtre contextuelle.

![Installation_step3](../images/Install_step3.png)

![Installation](../images/install.gif)

### Travailler avec des DLL .NET Core dans un environnement non-Windows

Comme Aspose.PDF for .NET fournit un support .NET Standard 2.0 (support .NET Core 2.0), il peut être utilisé dans des applications Core fonctionnant dans des systèmes d'exploitation de type Linux. Nous travaillons constamment à améliorer le support .NET Core dans notre API. Cependant, il y a certaines opérations suivantes que nous recommandons à nos clients d'effectuer, afin d'obtenir de meilleurs résultats lors de l'utilisation des fonctionnalités de Aspose.PDF for .NET :

Veuillez installer :

- le package libgdiplus
- le package avec des polices compatibles Microsoft : **ttf-mscorefonts-installer**. (par exemple, `sudo apt-get install ttf-mscorefonts-installer`)
Ces polices doivent être placées dans le répertoire "/usr/share/fonts/truetype/msttcorefonts" car Aspose.PDF for .NET scanne ce dossier sur les systèmes d'exploitation de type Linux. Si le système d'exploitation a un autre dossier/répertoire par défaut pour les polices, vous devez utiliser la ligne de code suivante avant d'effectuer toute opération utilisant Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<user's path to ms fonts>"));
```

#### Configurer Aspose.PDF for .NET dans Visual Studio Code
- Installer le SDK .NET

1. Visitez le site officiel [Microsoft .NET](https://dotnet.microsoft.com/download).
2. Téléchargez le dernier SDK .NET.
3. Exécutez l'installateur.
4. Ouvrez un terminal et vérifiez l'installation en exécutant :
```bash
dotnet --version
```

- Installer Visual Studio Code

1. Allez sur https://code.visualstudio.com/.
2. Téléchargez la version appropriée pour votre système d'exploitation.

- Installer les extensions VS Code requises

1. Ouvrez Visual Studio Code.
2. Cliquez sur l'icône de vue des extensions (icône carrée dans la barre latérale gauche).
3. Recherchez et installez les extensions suivantes :
   - "C#" par Microsoft
   - "C# Dev Kit" par Microsoft
   - ".NET Core Test Explorer" (optionnel, mais recommandé)

- Créer un nouveau projet .NET

1. Ouvrez Visual Studio Code
2. Allez dans Terminal > Nouveau Terminal
3. Naviguez jusqu'à votre répertoire de projet souhaité
```bash
# Create a new console application
dotnet new console -n AsposePDFNetDemo
# Navigate into the project directory
cd AsposePDFNetDemo
```

- Ajouter le package NuGet

```bash
# Install Aspose.PDF package
dotnet add package Aspose.PDF
```

- Vérifier l'installation du package

1. Ouvrez le fichier `.csproj`
2. Confirmez que la référence au package Aspose.PDF est ajoutée :
```xml
<ItemGroup>
  <PackageReference Include="Aspose.PDF" Version="x.x.x" />
</ItemGroup>
```

- Créer une configuration de débogage

1. Appuyez sur Ctrl+Shift+P (Cmd+Shift+P sur Mac).
2. Tapez ">.NET: Générer des actifs pour la construction et le débogage".
3. Sélectionnez votre projet.
4. Créez ou modifiez `.vscode/launch.json` :
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net7.0/AsposePDFNetDemo.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "stopAtEntry": false
        }
    ]
}
```

- Écrire le code d'exemple dans Program.cs

Remplacez le contenu de `Program.cs` par :
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
using System;
using Aspose.Pdf;
using Aspose.Pdf.Text;

class Program 
{
    static void Main(string[] args)
    {
        // Activate your license, you can comment out these codelines to use library in Evaluation mode
        var license = new Aspose.Pdf.License();
        license.SetLicense("Aspose.PDF.NET.lic");

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            
            // Create a text fragment
            var textFragment = new Aspose.Pdf.Text.TextFragment("Hello, Aspose.PDF for .NET!");
            textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
            
            // Add text to the page
            page.Paragraphs.Add(textFragment);
            
            // Save PDF document
            document.Save("sample.pdf");
        }
    }
}
```

- Construire et exécuter

```bash
dotnet restore
dotnet build
dotnet run
```