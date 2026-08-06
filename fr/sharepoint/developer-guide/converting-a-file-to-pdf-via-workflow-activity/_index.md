---
title: Converting a File to PDF via Workflow Activity
linktitle: Conversion d'un fichier en PDF via une activité de workflow
type: docs
weight: 50
url: /fr/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: PDF SharePoint API can be used in a SharePoint workflow that converts a document to PDF.
---

{{% alert color="primary" %}}

La prise en charge des flux de travail est une fonctionnalité clé de Microsoft Office SharePoint Server. Les flux de travail aident à automatiser le mouvement des documents selon la logique métier et à rationaliser le coût et le temps d'organisation des documents. Cet article montre comment utiliser Aspose.PDF pour SharePoint dans un flux de travail qui convertit un document au format PDF.

{{% /alert %}}

## Configuration d'un flux de travail

This example creates a workflow that converts any new item in a document library to PDF format and stores it in another document library. The example users the **Personal Documents** library as the source library and the **Pdf** sub-folder in the **Shared Documents** library as the destination library.

Aspose.PDF pour SharePoint prend en charge la conversion de fichiers HTML, texte et image.

### Concevoir le flux de travail à l'aide de SharePoint Designer

1. Ouvrez **SharePoint Designer** et connectez-vous au site sur lequel le flux de travail sera implémenté.
1. Sélectionnez **Workflows** à partir des **objets de site**, puis ouvrez **List Workflow**.
1. Sélectionnez la bibliothèque **Documents personnels** pour créer et joindre un nouveau flux de travail de liste à la bibliothèque de documents.

   **Selecting Personal Documents from the menu**

![Converting file to PDF via Workflow Activity_1](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. Créez et attachez le flux de travail de liste à la bibliothèque **Documents personnels** en saisissant un nom et une description du flux de travail.
1. Cliquez sur **OK** pour terminer cette étape.

   **Création d'un workflow de liste**

![Converting file to PDF via Workflow Activity_2](converting-a-file-to-pdf-via-workflow-activity_2.png)

Un éditeur d'étape de workflow apparaît. Ceci est utilisé pour définir les conditions et les actions pour les flux de travail. Ajoutez maintenant une action pour convertir un nouveau document en PDF sans aucune condition, à partir de **Aspose Actions**.

1. Sélectionnez l'action **Convertir le fichier en PDF via Aspose.PDF** dans le menu **Action**.

   **Sélection et action**

![Converting file to PDF via Workflow Activity_3](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Configurez les paramètres de l'action :
   1. Définissez le paramètre **ce dossier** sur le dossier de destination.
   1. Laissez les autres paramètres d'action comme valeurs par défaut ou définissez-les à l'aide de la fenêtre des propriétés de l'action. La valeur par défaut du paramètre **Overwrite** est false.

      **L'éditeur de flux de travail**

![Converting file to PDF via Workflow Activity_4](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Définition de la bibliothèque de destination**

![Converting file to PDF via Workflow Activity_5](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Définition des propriétés**

![Converting file to PDF via Workflow Activity_6](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. Dans le menu **Workflow**, sélectionnez **Paramètres du workflow**.
1. Sélectionnez **démarrer automatiquement le flux de travail lors de la création d'un nouvel élément** et désactivez les autres options dans **Options de démarrage**.

   **Définition des options de démarrage**

![Converting file to PDF via Workflow Activity_7](converting-a-file-to-pdf-via-workflow-activity_7.png)

La conception du workflow est terminée.

1. Enregistrez et publiez le workflow pour l'implémenter sur le site SharePoint.

### Testez le flux de travail

Pour tester le flux de travail :

1. Ouvrez le site SharePoint et téléchargez un nouveau document dans la bibliothèque de documents **Documents personnels**.
   Aspose.PDF pour SharePoint prend en charge la conversion de fichiers HTML, de fichiers texte et d'images (JPG, PNG, GIF, TIFF et BMP*) en PDF. Le flux de travail est configuré pour démarrer automatiquement lorsqu'un nouvel élément est créé, de sorte que les fichiers sont traités automatiquement.
1. Actualisez le navigateur.
   L'état du flux de travail apparaît dans la colonne du flux de travail, **Aspose.PDF Workflow** dans ce cas.

   **Ajout d'un document à la bibliothèque source**

![Converting file to PDF via Workflow Activity_8](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Ouvrez la bibliothèque de documents de destination pour afficher le document converti. **Documents partagés/Pdf** est le chemin dans cet exemple.

   **La bibliothèque de destination**

![Converting file to PDF via Workflow Activity_9](converting-a-file-to-pdf-via-workflow-activity_9.png)

