---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
weight: 10
url: /fr/net/aspose-pdf-editor/
description: Aspose.PDF pour .NET démontre que l'éditeur PDF HTML5 est un éditeur PDF basé sur le web et open source.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Qu'est-ce que l'éditeur PDF HTML5 par Aspose.PDF pour .NET ?

L'éditeur PDF HTML5 par Aspose.PDF pour .NET est un éditeur PDF basé sur le web et open source qui permet aux utilisateurs de créer, éditer et convertir des fichiers PDF en ligne et les utilisateurs peuvent facilement intégrer l'éditeur dans leurs propres applications web pour visualiser et éditer des fichiers PDF. L'éditeur PDF HTML5 est développé en utilisant HTML5, jQuery Ajax, ASP.NET, Bootstrap et le backend est alimenté par Aspose.PDF pour .NET. L'interface utilisateur de l'éditeur est très simple pour une compréhension facile et l'amélioration des fonctionnalités selon les exigences des utilisateurs.

![Image](../images/aspose-pdf-editor.png)

## Fonctionnalités

Actuellement, il prend en charge les fonctionnalités suivantes :

- Créer de nouveaux fichiers PDF
- Chargement et visualisation de fichiers PDF
- Chargement de fichiers PDF et d'images depuis Dropbox
- Chargement de fichiers PDF et d'images depuis Dropbox
- Exportation de fichiers PDF vers différents formats de fichiers
- Ajout ou Fusion de fichiers PDF
- Insertion de nouvelles pages
- Suppression de pages
- Déplacement de pages dans un fichier PDF
- Insertion de texte dans un PDF
- Surlignage de texte dans un PDF
- Rotation du texte inséré dans un PDF
- Recherche de texte dans un PDF
- Remplacement de texte dans un PDF
- Insertion d'images
- Redimensionnement de la signature et des images
- Glisser et positionner les éléments insérés
- Chargement de fichiers PDF avec des champs de formulaire
- Remplissage des champs de formulaire à l'aide de l'éditeur
- Sauvegarde et exportation de PDF avec les données des champs de formulaire
- Surlignage des champs de formulaire requis
- Ajout de pièces jointes aux fichiers PDF
- Chargement des pièces jointes à partir du fichier PDF d'entrée
- Téléchargement des fichiers de pièces jointes
- Suppression des fichiers de pièces jointes
- Signature de PDF à l'aide du dessin à main levée

## Configuration système

Comme l'éditeur PDF HTML5 est une application Web .NET développée en utilisant ASP.NET, C#, HTML5, jQuery, Javascript. Vous aurez besoin de l'environnement système suivant pour configurer l'éditeur PDF HTML5 de votre côté.

- Visual Studio 2010 (ou supérieur)
- .NET Framework 3.5 (ou supérieur)
- Aspose.PDF pour .NET
- Aspose.PDF pour .NET
- jQuery 2.0.3
- Bootstrap 3.2.0

Vous pouvez utiliser l'un des navigateurs suivants pour exécuter l'application de votre côté :

- Mozilla Firefox (recommandé)
- Internet Explorer (version 9 ou ultérieure)
- Google Chrome
- Apple Safari

## Support

Nous, chez Aspose, nous assurons de fournir le meilleur soutien possible à nos clients / utilisateurs pour leurs requêtes de toute nature, qu'elles soient techniques ou commerciales. Veuillez utiliser les liens ci-dessous pour toute question liée aux licences et ventes ou pour toute question technique.

# Guide du développeur de l'éditeur PDF

## Créer de nouveaux fichiers PDF

En plus de modifier les documents PDF existants, l'éditeur PDF Html5 prend également en charge la création de nouveaux fichiers PDF à partir de zéro que vous pouvez réaliser en utilisant l'option Créer un nouveau fichier de la barre de menu. En utilisant cette fonctionnalité, vous pouvez créer un PDF vierge dans l'éditeur, ajouter du texte/des images et l'enregistrer dans le format souhaité. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Créer un nouveau fichier" est cliqué sur la page**

Lorsque vous cliquez sur l'élément de menu "Créer un nouveau fichier", la méthode onNewFileClicked est appelée dans le fichier Editor.js.
Lorsque vous cliquez sur l'élément de menu "Créer un nouveau fichier", la méthode onNewFileClicked est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête Ajax au serveur pour la méthode CreateNewFile.**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode onNewFileClicked, elle appelle la méthode CreateNewFile dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous avec le code source de la méthode CreateNewFile. Elle efface toutes les données existantes concernant le fichier précédemment chargé en utilisant la méthode ResetData.

**Création d'un nouveau fichier PDF en utilisant Aspose.PDF pour .NET**

Après avoir effacé les données en utilisant la méthode ResetData, la méthode CreateNewFile crée un nouveau fichier PDF en utilisant la classe Document d'Aspose.PDF pour .NET.
Comme vous pouvez le voir dans l'onglet ci-dessous, l'objet Document génère un fichier avec une page vide. Après que le fichier est généré sur le serveur, le fichier est converti en image en utilisant la méthode ImageConverter pour être chargé sur le canvas.

**Chargement du fichier résultant sur le canvas.**

Après que le fichier est converti en image côté serveur, le contrôle est renvoyé à la méthode onNewFileClicked dans Editor.js.
Après que le fichier a été converti en image côté serveur, le contrôle est renvoyé à la méthode onNewFileClicked dans Editor.js.

## Exportation de PDF vers différents formats de fichiers

L'éditeur PDF HTML5 prend en charge l'exportation de fichiers PDF vers différents formats de fichiers, que vous pouvez réaliser en utilisant l'option Exporter le fichier depuis la barre de menu. En utilisant cette fonctionnalité, vous pouvez exporter le fichier PDF vers le format souhaité. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Exporter le fichier" est cliqué sur la page.**

Lorsque vous cliquez sur l'élément de menu "Exporter le fichier", vous pouvez choisir le format d'exportation dans la liste. Après avoir sélectionné le format d'exportation, la méthode "ExportFile" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête serveur Ajax pour la méthode btnFileExport_Click**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode "ExportFile". Il envoie une requête à la méthode serveur btnFileExport_Click avec un paramètre de format de fichier dans le fichier CanvasSave.aspx.cs.

**La méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous.
Voir l'onglet Canvas.aspx.cs ci-dessous.

**Exporter le fichier à télécharger sur le navigateur client**

Après que le fichier soit généré sur le serveur, le contrôle est renvoyé à la méthode ExportFile dans Editor.js d'où le fichier est envoyé au navigateur pour que l'utilisateur puisse le télécharger en utilisant la méthode ExportToBrowser.

## Ajout ou fusion de fichiers PDF

L'éditeur PDF Html5 prend en charge l'ajout ou la fusion de fichiers PDF que vous pouvez réaliser en utilisant l'option Ajouter un fichier de la barre de menu. En utilisant cette fonctionnalité, vous pouvez ajouter le fichier PDF à votre fichier d'entrée. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Ajouter un fichier" est cliqué sur la page.**

Lorsque vous cliquez sur l'élément de menu "Ajouter un fichier", vous pouvez télécharger le fichier en utilisant le dialogue de téléchargement de fichier. Après que le fichier soit téléchargé, la méthode "fileSelected" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête au serveur pour la méthode ProcessRequest**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode "fileSelected".
Voir l'onglet Editor.js ci-dessous pour le code source de la méthode "fileSelected".

**Méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous. En fonction du paramètre de formulaire passé, le fichier à ajouter est sauvegardé sur le serveur et la méthode "AppendFile" est appelée. La méthode AppendFile, ajoute le fichier téléchargé en utilisant Aspose.PDF pour .NET, convertit le fichier résultant en image et renvoie le contrôle à la méthode "fileSelected" dans Editor.js

**Mettre à jour le contenu du canevas après avoir ajouté le fichier**

Après que le fichier soit généré sur le serveur, le contrôle est renvoyé à la méthode "fileSeleceted" dans Editor.js qui met à jour le contenu de l'éditeur.

## Téléverser un fichier PDF local

L'éditeur PDF HTML5 prend en charge le téléversement de fichiers PDF depuis une machine locale en utilisant l'option Ouvrir depuis l'ordinateur dans la barre de menu. En utilisant cette fonctionnalité, vous pouvez ouvrir un fichier PDF existant et effectuer des modifications sur votre fichier PDF. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Ouvrir depuis l'ordinateur" est cliqué sur la page.**
**HTML - "Ouvrir depuis l'ordinateur" est cliqué sur la page.**

Lorsque vous cliquez sur "Ouvrir depuis l'ordinateur", vous pouvez télécharger le fichier d'entrée en utilisant la boîte de dialogue de téléchargement de fichiers. Après que le fichier soit téléchargé, la méthode "fileSelected" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête serveur pour la méthode ProcessRequest**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode "fileSelected". Le fichier est posté au serveur et la méthode "ProcessRequest" est appelée dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous. En fonction du paramètre de formulaire passé, le fichier à télécharger est sauvegardé sur le serveur, réinitialise les données en utilisant la méthode "ResetData" et la méthode "ImageConverter" est appelée. La méthode ImageConverter, convertit le fichier téléchargé en images en utilisant Aspose.PDF pour .NET et retourne le contrôle à la méthode "fileSelected" dans Editor.js

**Mettre à jour le contenu du canvas après le téléchargement du fichier**

Après que le fichier soit généré sur le serveur, le contrôle est renvoyé à la méthode "fileSeleceted" dans Editor.js qui met à jour le contenu de l'éditeur, c'est-à-dire
Après que le fichier est généré sur le serveur, le contrôle est renvoyé à la méthode "fileSeleceted" dans Editor.js qui met à jour le contenu de l'éditeur.

## Ajout de page dans un fichier PDF

En utilisant Html5 PDF Editor, vous pouvez ajouter de nouvelles pages dans les fichiers PDF en utilisant l'option Ajouter une page de la barre de menu. En utilisant cette fonctionnalité, vous pouvez ajouter une page blanche à votre fichier PDF. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Ajouter Page" est cliqué sur la page**

Lorsque vous cliquez sur l'élément de menu "Ajouter Page", la méthode "AddPage" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête Ajax au serveur pour la méthode AddPage_Click.**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode AddPage, il appelle la méthode AddPage_Click dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gère les requêtes du serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous avec le code source de la méthode AddPage_Click.
## Suppression de page d'un fichier PDF

En utilisant l'éditeur PDF Html5, vous pouvez supprimer une page des fichiers PDF en utilisant l'option Supprimer Page de la barre de menu. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Supprimer Page" est cliqué sur la page**

Lorsque vous cliquez sur l'élément de menu "Supprimer Page", la méthode DeletePage est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête Ajax au serveur pour la méthode DeletePage_Click.**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode DeletePage, elle appelle la méthode DeletePage_Click dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous avec le code source de la méthode DeletePage_Click. Elle supprime la page sélectionnée du fichier PDF en utilisant la méthode Delete de la collection Aspose.PDF.Document.Page.

**Mise à jour du contenu éditorial**

Après avoir supprimé la page du fichier PDF, le contrôle est ensuite renvoyé à la méthode DeletePage dans le fichier Editor.js qui met à jour la numérotation des pages, supprime toutes les collections associées à la page supprimée en utilisant la méthode updateIndexesDelete.
Après avoir supprimé la page du fichier PDF, le contrôle est ensuite renvoyé à la méthode DeletePage dans le fichier Editor.js qui met à jour la numérotation des pages, supprime toutes les collections associées à la page supprimée en utilisant la méthode updateIndexesDelete.

## Déplacer des pages dans un fichier PDF

En utilisant l'éditeur PDF Html5, vous pouvez déplacer des pages dans des fichiers PDF en utilisant l'option Déplacer la page depuis la barre de menu. Une fois que vous appuyez sur l'élément de menu Déplacer la page, une boîte de dialogue d'entrée s'affiche pour spécifier le nouvel emplacement de la page sélectionnée. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça marche ?

**HTML - L'élément de menu "Déplacer la page" est cliqué sur la page**

Lorsque vous cliquez sur l'élément de menu "Déplacer la page", une boîte de dialogue d'entrée s'affiche pour obtenir le nouvel emplacement de la page sélectionnée. Après avoir fourni le numéro de la page et appuyé sur le bouton "Déplacer", la méthode "Move" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête Ajax au serveur pour la méthode MovePages.**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode Move, qui appelle la méthode MovePage et transmet les détails comme déplacer de, déplacer vers, liste des pages à la méthode MovePages dans le fichier CanvasSave.aspx.cs.
Voir l'onglet Editor.js ci-dessous pour le code source de la méthode Move, qui appelle la méthode MovePage et qui passe les détails comme déplacer de, déplacer vers, liste des pages à la méthode MovePages dans le fichier CanvasSave.aspx.cs.

**La méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous avec le code source de la méthode MovePages. Elle utilise la collection Aspose.PDF.Document.Pages pour déplacer les pages.

**Mise à jour du contenu en cours d'édition**

Après avoir déplacé la page, le contrôle est ensuite renvoyé à la méthode MovePage dans le fichier Editor.js qui met à jour les indices des pages et les informations liées aux différentes collections dans l'éditeur en utilisant la méthode MoveUpdate.

## Insérer du texte dans un fichier PDF

En utilisant l'éditeur PDF Html5, vous pouvez insérer du texte dans des fichiers PDF en utilisant l'option Mode Texte dans la barre de menu. Une fois que vous sélectionnez l'élément de menu Mode Texte et cliquez sur un emplacement de l'éditeur où vous souhaitez ajouter le texte, une boîte de dialogue d'entrée s'affiche pour saisir et formater le texte désiré comme indiqué ci-dessous :

Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.
Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça marche ?

**HTML - L'élément de menu "Mode Texte" est sélectionné sur la page**

Lorsque vous sélectionnez l'élément de menu "Mode Texte" et cliquez à l'endroit souhaité sur l'éditeur pour insérer du texte dans un fichier PDF, une boîte de dialogue s'affiche pour recueillir le texte que vous souhaitez insérer sur la page. Après avoir fourni le texte et appuyé sur le bouton "OK", la méthode "saveTextFromArea" est appelée dans le fichier Editor.js.

**Javascript - Obtenir le texte saisi depuis la boîte de dialogue et l'afficher dans l'éditeur.**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode saveTextFromArea, qui obtient le texte de la boîte de dialogue et l'affiche dans l'éditeur. De plus, elle enregistre les données dans la collection de formes qui est utilisée plus tard côté serveur pour insérer le texte dans le fichier PDF. Vous pouvez vérifier le code source de la méthode saveFile qui est appelée lorsque le fichier est enregistré.

**Méthode web ASP.NET gère les requêtes serveur**

Comme mentionné ci-dessus, le texte sera effectivement inséré dans notre fichier PDF source lorsque nous effectuerons l'opération de sauvegarde qui utilise la méthode GetTextStamp pour créer le tampon de texte à insérer dans le fichier PDF.
Comme mentionné ci-dessus, le texte sera en fait inséré dans notre fichier PDF source lorsque nous effectuerons l'opération de sauvegarde qui utilise la méthode GetTextStamp pour créer le tampon de texte à insérer dans le fichier PDF.

## Mettre en surbrillance le texte dans un fichier PDF

En utilisant l'éditeur PDF Html5, vous pouvez mettre en surbrillance le texte dans les fichiers PDF en utilisant l'option Mode Surbrillance du menu. Une fois que vous sélectionnez l'élément de menu Mode Surbrillance, vous pouvez mettre en surbrillance n'importe quel texte et zone à l'aide de l'outil de surbrillance rectangulaire. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Mode Surbrillance" est sélectionné sur la page**

Lorsque vous sélectionnez l'élément de menu "Mode Surbrillance", vous pouvez dessiner une surbrillance rectangulaire autour de n'importe quel texte ou élément dans votre fichier PDF. La mise en œuvre de ce processus peut être vue dans la méthode "tools.rect" dans le fichier Editor.js.

**Javascript - Dessiner un rectangle de surbrillance sur l'éditeur.**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode tool.rect, qui permet à l'utilisateur de dessiner un rectangle de surbrillance à n'importe quel endroit sur l'éditeur.
Voir l'onglet Editor.js ci-dessous pour le code source de la méthode tool.rect, qui permet à l'utilisateur de dessiner un rectangle de mise en évidence à n'importe quel endroit de l'éditeur.

**La méthode web ASP.NET gère les requêtes serveur**

Comme mentionné ci-dessus, la mise en évidence est réellement insérée dans notre fichier PDF source lorsque nous effectuons l'opération de sauvegarde qui utilise la méthode GetImageStamp pour insérer le timbre d'image dans le fichier PDF source à l'emplacement spécifié sur l'éditeur. Voir l'onglet Canvas.aspx.cs ci-dessous avec le code source de la méthode GetImageStamp. Il utilise la classe Aspose.PDF.ImageStamp pour insérer le rectangle de mise en évidence dans le fichier PDF.

## Recherche de texte dans un fichier PDF

En utilisant l'éditeur PDF Html5, vous pouvez rechercher du texte dans des fichiers PDF en utilisant l'option Recherche de texte dans la barre de menu. Une fois que vous cliquez sur l'élément de menu Recherche de texte, une boîte de dialogue s'affiche pour saisir le texte à rechercher comme indiqué ci-dessous :

En fournissant le texte et en appuyant sur rechercher, toutes les instances du mot recherché seront mises en évidence comme indiqué ci-dessous :

### Comment ça fonctionne ?

**HTML - L'élément de menu "Recherche de texte" est cliqué sur la page**
**HTML - L'élément de menu "Rechercher du texte" est cliqué sur la page**

Lorsque vous cliquez sur l'élément de menu "Rechercher du texte", une boîte de dialogue s'ouvre pour saisir le texte que vous souhaitez rechercher. Après avoir entré le texte et appuyé sur le bouton de recherche, la méthode "Déplacer" est appelée, qui vérifie si l'opération de changement de page ou l'opération de recherche est effectuée, puis elle appelle la méthode performSearch dans le fichier Editor.js.

**jQuery - Envoyer une requête serveur Ajax pour la méthode SearchData**

Voir l'onglet Editor.js ci-dessous pour le code source de la méthode performSearch, qui obtient le texte entré et une requête à la méthode serveur SearchData dans le fichier _CanvasSave.aspx.cs_.

**Méthode web ASP.NET gère les requêtes serveur**

Voir l'onglet _Canvas.aspx.cs_ ci-dessous.
Voyez l'onglet _Canvas.aspx.cs_ ci-dessous.

## Remplacement de texte dans un fichier PDF

En utilisant l'éditeur PDF Html5, vous pouvez remplacer le texte existant dans les fichiers PDF en utilisant l'option Remplacer le texte depuis la barre de menu. Une fois que vous cliquez sur l'élément de menu Remplacer le texte, une boîte de dialogue s'affiche pour saisir le texte à rechercher et à remplacer.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Remplacer le texte" est cliqué sur la page**

Lorsque vous cliquez sur l'élément de menu "Remplacer le texte", une boîte de dialogue de saisie s'affiche pour entrer le texte à rechercher et remplacer. Après avoir entré le texte et appuyé sur le bouton Remplacer, la méthode "ReplaceText" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête serveur Ajax pour la méthode ReplaceText**

Voyez l'onglet Editor.js ci-dessous pour le code source de la méthode ReplaceText, qui obtient le texte saisi depuis la boîte de dialogue de texte et une requête à la méthode serveur ReplaceText dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gère les requêtes serveur**

Voyez l'onglet Canvas.aspx.cs ci-dessous.
## Chargement d'un fichier PDF avec des champs de formulaire

En utilisant l'éditeur PDF Html5, vous pouvez charger et travailler avec un fichier PDF contenant des champs de formulaire. Une fois le fichier avec les champs de formulaire chargé dans l'éditeur, tous les champs de formulaire sont chargés pour l'édition. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Ouvrir depuis l'ordinateur" est cliqué sur la page.**

Lorsque vous cliquez sur l'élément de menu "Ouvrir depuis l'ordinateur", vous pouvez télécharger le fichier d'entrée contenant les champs de formulaire en utilisant la boîte de dialogue de téléchargement de fichier. Après le téléchargement du fichier, la méthode "fileSelected" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une demande serveur pour la méthode ProcessRequest**

Le fichier est posté sur le serveur et la méthode "ProcessRequest" est appelée dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gère les demandes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous.
Voir l'onglet Canvas.aspx.cs ci-dessous.

**Chargement des champs de formulaire sur le canevas**

Voir l'onglet Editor.js ci-dessous, la méthode manageFields dans Editor.js est utilisée pour générer tous les champs sur le canevas en fonction des informations renvoyées par le côté serveur. Elle dessine les contrôles de champs HTML en utilisant les informations de type et de localisation du côté serveur sur le canevas.

## Mise en évidence des champs de formulaire requis

En utilisant Html5 PDF Editor, vous pouvez mettre en évidence les champs de formulaire requis dans l'éditeur. Une fois le fichier contenant les champs de formulaire chargé dans l'éditeur, tous les champs de formulaire requis sont mis en évidence pour aider les utilisateurs à les éditer. Dans notre prochaine section, nous discuterons des détails techniques derrière cette fonctionnalité.

### Comment ça fonctionne ?

**HTML - L'élément de menu "Ouvrir depuis l'ordinateur" est cliqué sur la page.**

Lorsque vous cliquez sur l'élément de menu "Ouvrir depuis l'ordinateur", vous pouvez télécharger le fichier d'entrée contenant les champs de formulaire à l'aide de la boîte de dialogue de téléchargement de fichiers. Après que le fichier soit téléchargé, la méthode "fileSelected" est appelée dans le fichier Editor.js.

**jQuery - Envoyer une requête serveur pour la méthode ProcessRequest**
**jQuery - Envoyer une requête serveur pour la méthode ProcessRequest**

Le fichier est posté sur le serveur et la méthode "ProcessRequest" est appelée dans le fichier CanvasSave.aspx.cs.

**Méthode web ASP.NET gérant les requêtes serveur**

Voir l'onglet Canvas.aspx.cs ci-dessous. En fonction du paramètre du formulaire passé, le fichier à télécharger est enregistré sur le serveur, la méthode ImageConverter convertit le fichier téléchargé en images et la méthode "CheckFields" est appelée. Cette méthode utilise la classe Aspose.PDF.InteractiveFeatures.Forms pour vérifier tous les champs du formulaire et collecter les informations concernant les champs, c’est-à-dire le Type de Champ, l'Emplacement, etc. Après avoir obtenu les détails de tous les champs du formulaire, nous obtenons l'information si un champ du formulaire est requis en utilisant la méthode Aspose.PDF.Facades.IsRequiredField et renvoie la collection de champs à la méthode ImageConverter. La méthode ImageConverter renvoie le contrôle à la méthode "fileSelected" dans Editor.js

**Chargement des champs de formulaire sur le canevas**

Voir l'onglet Editor.js ci-dessous, la méthode manageFields dans Editor.js est utilisée pour générer tous les champs sur le canevas en fonction des informations renvoyées du côté serveur.
Voir l'onglet Editor.js ci-dessous, la méthode manageFields dans Editor.js est utilisée pour générer tous les champs sur le canevas en fonction des informations renvoyées par le serveur.
