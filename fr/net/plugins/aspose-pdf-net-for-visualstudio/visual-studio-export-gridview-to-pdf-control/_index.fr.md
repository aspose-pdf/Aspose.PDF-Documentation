---
title: Visual Studio Export GridView To PDF Control
type: docs
weight: 10
url: /net/visual-studio-export-gridview-to-pdf-control/
---

## Introduction

Export GridView To Pdf Control est un contrôle serveur ASP.NET qui permet d'exporter le contenu d'un GridView dans un document Pdf en utilisant [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx). Il ajoute un bouton **Exporter en Pdf** en haut du contrôle GridView. En cliquant sur le bouton, le contenu du contrôle GridView est exporté dynamiquement dans un document Pdf puis le fichier exporté est automatiquement téléchargé à l'emplacement sélectionné par l'utilisateur en quelques secondes.

### Fonctionnalités du module

Cette version initiale du contrôle offre les fonctionnalités suivantes :

- Obtenez une copie hors ligne de votre contenu GridView en ligne préféré pour l'édition, le partage et l'impression dans un document Pdf très populaire.
- Hérité du contrôle GridView ASP.NET par défaut et possède donc toutes ses fonctionnalités et propriétés.
- Fonctionne avec toutes les versions de .NET à partir de .NET 2.0.
- Capacité à personnaliser/localiser le texte du bouton Exporter.
- Capacité à personnaliser/localiser le texte du bouton d'exportation.
- Option pour exporter en mode Paysage si le contenu de GridView est plus large et ne rentre pas en mode Portrait par défaut
- Appliquer l'apparence de votre propre thème sur le bouton d'exportation en utilisant css.
- Option pour ajouter un titre personnalisé en haut du document exporté
- Option pour sauvegarder chaque document exporté sur le serveur à un chemin de disque configurable
- Option pour exporter la page courante ou toutes les pages lorsque la pagination est activée

## Exigences Système et Plateformes Supportées

### Exigences Système

Le contrôle Export GridView To Pdf pour Visual Studio peut être utilisé sur tout système disposant de IIS et du framework .NET 2.0 ou supérieur.

### Plateformes Supportées

Le contrôle Export GridView To Pdf pour Visual Studio est supporté sur toutes les versions de ASP.NET fonctionnant sur le framework .NET 2.0 ou supérieur. Vous pouvez utiliser n'importe quelle des versions suivantes de Visual Studio pour utiliser ce contrôle dans vos applications ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## Téléchargement
## Téléchargement

Vous pouvez télécharger le contrôle Export GridView To Pdf à partir de l'un des emplacements suivants

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## Installation

Il est très simple et facile d'installer le contrôle Export GridView To Pdf, veuillez suivre ces étapes simples

### **Pour Visual Studio 2010, 2012 et 2013**

1. Extrayez le fichier zip téléchargé, c'est-à-dire Aspose.PDF.GridViewExport_1.0.zip
1. Double-cliquez sur le fichier VSIX Aspose.PDF.GridViewExport.vsix
1. Une boîte de dialogue apparaîtra vous montrant les versions de Visual Studio disponibles et prises en charge installées sur votre machine
1. Sélectionnez celles auxquelles vous souhaitez ajouter le contrôle Export GridView To Pdf.
1. Cliquez sur Installer

Vous obtiendrez une boîte de dialogue de succès une fois l'installation terminée.

**Note :** Veuillez vous assurer de redémarrer Visual Studio pour que les modifications prennent effet.

### **Pour Visual Studio 2005, 2008 et les éditions Express**

Veuillez suivre ces étapes pour intégrer le contrôle Export GridView To Pdf dans Visual studio pour un glisser-déposer facile tout comme les autres contrôles ASP.NET
Veuillez suivre ces étapes pour intégrer le contrôle Export GridView To Pdf dans Visual Studio pour un glisser-déposer facile comme les autres contrôles ASP.NET

1. Extrayez le fichier zip téléchargé, i.e. Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Assurez-vous d'exécuter Visual Studio en tant qu'Administrateur

Dans le menu Outils, cliquez sur Choisir les éléments de la boîte à outils.

1. Cliquez sur Parcourir.
   La boîte de dialogue Ouvrir apparaît.
1. Naviguez jusqu'au dossier extrait et sélectionnez Aspose.PDF.GridViewExport.dll
1. Cliquez sur OK.

Lorsque vous ouvrez un contrôle aspx ou ascx dans la boîte à outils du côté gauche, vous verrez ExportGridViewToPdf sous l'onglet Général

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## Utilisation

Une fois installé, il est très facile de commencer à utiliser ce contrôle dans vos applications ASP.NET

|**Pour le framework .NET 4.0 et supérieur**|**Pour le framework .NET 2.0 et supérieur**|** |
| :- | :- | :- |
|Pour les applications fonctionnant sous le framework .NET 4.0 et supérieur dans Visual Studio 2010 et supérieur, vous devriez voir le contrôle **ExportGridViewToPdf** dans l'onglet **Aspose** de la barre d'outils comme indiqué ci-dessous.
|Pour les applications fonctionnant sous .NET framework 4.0 et plus dans Visual Studio 2010 et au-delà, vous devriez voir le contrôle **ExportGridViewToPdf** dans l'onglet **Aspose** de la barre d'outils comme indiqué ci-dessous.

### Ajout manuel du contrôle ExportGridViewToPdf

Si vous rencontrez des problèmes avec les méthodes ci-dessus qui utilisent la boîte à outils de Visual Studio, vous pouvez ajouter manuellement ce contrôle à votre application ASP.NET fonctionnant sur un framework .NET supérieur à 2.0

1. Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'Administrateur
1. Ajoutez une référence à **Aspose.PDF.GridViewExport.dll** disponible dans le package téléchargé extrait dans votre projet ASP.NET ou application web. Assurez-vous que votre application web/Visual Studio a un accès complet à ce dossier sinon vous pourriez obtenir une exception Accès refusé.
1. Ajoutez cette ligne en haut de la page, du contrôle ou de la MasterPage

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
<aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### FAQs

Questions fréquentes et problèmes que vous pourriez rencontrer en utilisant ce contrôle

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. Je ne vois pas le contrôle ExportGridViewToPdf dans la boîte à outils</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 et versions ultérieures</strong></p>
<ol><li>Assurez-vous d'avoir installé ce contrôle en utilisant le fichier d'extension VSIX trouvé dans le paquet téléchargé. Pour vérifier, allez dans Outils -> Extensions et mises à jour. Sous Installé, vous devriez voir 'Aspose Export Export GridView To Pdf Control'. Si vous ne le voyez pas, essayez de le réinstaller.</li>
<li>Assurez-vous que votre application web fonctionne sur le framework .NET 4.0 ou supérieur, pour les versions inférieures de .NET framework, veuillez vérifier la méthode alternative ci-dessus.</li>

<ol>
<li>Assurez-vous que votre application web fonctionne sous le framework .NET 4.0 ou supérieur, pour les versions antérieures du framework .NET, veuillez vérifier la méthode alternative ci-dessus.
Anciennes Versions de Visual Studio</li>
<li>Assurez-vous que vous avez manuellement ajouté ce contrôle à votre boîte à outils conformément aux instructions ci-dessus.</li>
</ol>

<div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
    <h3 itemprop="name" class="faq-q">2. Je reçois une erreur 'Accès refusé' lors de l'exécution de l'application</h3>
    <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
         <div itemprop="text" class="faq-a">
           <ol>
           <li>Si vous rencontrez ce problème en production, assurez-vous de copier à la fois Aspose.PDF.dll et Aspose.PDF.GridViewExport.dll dans votre dossier bin.</li>
           <li>Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'administrateur même si vous êtes déjà connecté en tant qu'administrateur.</li>
```

<li>Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'administrateur même si vous êtes déjà connecté en tant qu'administrateur.</li>
</ol>
</div>
</div>
</div>
</div>

### **Propriétés du Contrôle Aspose .NET Export GridView To Pdf**

Les propriétés suivantes sont exposées pour configurer et utiliser les fonctionnalités intéressantes fournies par ce contrôle

|**Nom de la Propriété**|**Type**|**Exemple/Valeurs Possibles**|**Description**|
| :- | :- | :- | :- |
|ExportButtonText|string|Exporter en Pdf|Vous pouvez utiliser cette propriété pour remplacer le texte par défaut existant|
|ExportButtonCssClass|string|btn btn-primary|Classe CSS qui est appliquée au div externe du bouton d'exportation. Pour appliquer css sur le bouton, vous pouvez utiliser .yourClass input|
|ExportInLandscape|bool|vrai ou faux|Si vrai, cela change l'orientation du document de sortie en paysage. Par défaut, c'est Portrait|
| | | | |
|ExportFileHeading|string|Exemple de Rapport d'Exportation GridView|Vous pouvez utiliser des balises html pour ajouter du style à votre en-tête|
|ExportOutputPathOnServer|string|c:/temp|Chemin du disque local sur le serveur où une copie de l'exportation est automatiquement enregistrée.|
```
|ExportOutputPathOnServer|string|c:/temp|Chemin local du disque sur le serveur où une copie de l'exportation est automatiquement sauvegardée.
|ExportDataSource|object|allRowsDataTable|Définit l'objet à partir duquel ce contrôle de liaison de données récupère sa liste d'éléments de données. L'objet doit contenir toutes les données qui doivent être exportées. Cette propriété est utilisée en complément de la propriété DataSource normale et est utile lorsque la pagination personnalisée est activée et que la page actuelle ne récupère que les lignes à afficher à l'écran.
|LicenseFilePath|string| |Chemin local sur le serveur pour le fichier de licence. Par exemple c:/inetpub/Aspose.PDF.lic|

Un exemple de contrôle Export GridView vers Pdf avec toutes les propriétés utilisées est montré ci-dessous

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Export to Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Example Report</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## Démo Vidéo

Veuillez consulter [la vidéo](https://www.youtube.com/watch?v=WNJ7T8u4JlM) ci-dessous pour voir le module en action.

### Support

Dès les premiers jours d'Aspose, nous savions que proposer de bons produits à nos clients ne serait pas suffisant. Nous devions également offrir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant qu'un problème technique ou une particularité du logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre des problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou qu'elle utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez signaler tout problème ou suggestion lié à ce Pdf en utilisant l'une des plateformes suivantes :

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - Q et A](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Microsoft Developer Network - Q et A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### Étendre et Contribuer

Aspose .NET Export GridView vers Pdf pour Visual Studio est open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à étendre les fonctionnalités selon leurs propres besoins.

#### Code Source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### Comment configurer le code source

Vous devez avoir les éléments suivants installés pour ouvrir et étendre le code source

- Visual Studio 2010

Veuillez suivre ces étapes simples pour commencer

1. Téléchargez/Clonez le code source.
1.
1.
1. Accédez au dernier code source que vous avez téléchargé et ouvrez **Aspose.PDF.GridViewExport.sln**

#### Vue d'ensemble du code source

Il y a trois projets dans la solution

- Aspose.PDF.GridViewExport - Contient le paquet VSIX et Server Pdf pour .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - GridView Pdf étendu pour .NET 2.0
- Aspose.PDF.GridViewExport.Website - Projet web pour tester le GridView Pdf exportable en Word


