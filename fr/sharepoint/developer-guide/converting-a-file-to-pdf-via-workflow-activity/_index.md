---
title: Conversion d'un fichier en PDF via une activité de flux de travail
linktitle: Conversion d'un fichier en PDF via une activité de flux de travail
type: docs
weight: 50
url: /fr/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: L'API PDF SharePoint peut être utilisée dans un flux de travail SharePoint qui convertit un document en PDF.
---

{{% alert color="primary" %}}

La prise en charge des flux de travail est une fonctionnalité clé de Microsoft Office SharePoint Server. Les flux de travail aident à automatiser le déplacement des documents selon la logique métier et à rationaliser le coût et le temps d'organisation des documents. Cet article montre comment utiliser Aspose.PDF for SharePoint dans un flux de travail qui convertit un document en PDF.

{{% /alert %}}
## **Configurer un flux de travail**

Cet exemple crée un flux de travail qui convertit tout nouvel élément d'une bibliothèque de documents au format PDF et le stocke dans une autre bibliothèque de documents. L'exemple utilise la bibliothèque **Personal Documents** comme bibliothèque source et le sous-dossier **Pdf** dans la bibliothèque **Shared Documents** comme bibliothèque de destination.

Aspose.PDF for SharePoint prend en charge la conversion des fichiers HTML, texte et image.

### **Concevoir le flux de travail à l'aide de SharePoint Designer**

1. Ouvrez **SharePoint Designer** et connectez-vous au site où le flux de travail sera implémenté.
1. Sélectionnez **Workflows** dans **site objects** puis ouvrez **List Workflow**.
1. Sélectionnez la bibliothèque **Personal Documents** pour créer et attacher un nouveau flux de travail de liste à la bibliothèque de documents.

   **Sélection de Personal Documents dans le menu**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. Créez et attachez le flux de travail de liste à la bibliothèque **Personal Documents** en saisissant un nom et une description du flux de travail.
1. Cliquez sur **OK** pour terminer cette étape.

   **Création d'un workflow de liste**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



Un éditeur d'étape de workflow apparaît. Il est utilisé pour définir les conditions et les actions des workflows. Ajoutez maintenant une action pour convertir un nouveau document en PDF sans aucune condition, depuis **Aspose Actions**.

1. Sélectionnez l'action **Convert file to PDF via Aspose.PDF** dans le menu **Action**.

   **Sélection d'une action**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. Configurez les paramètres de l'action :
   1. Définissez le paramètre **ce dossier** sur le dossier de destination.
   1. Laissez soit les autres paramètres d'action avec leurs valeurs par défaut, soit définissez‑les en utilisant la fenêtre des propriétés d'action. La valeur par défaut du paramètre **Overwrite** est false.

      **L'éditeur de flux de travail**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**Définition de la bibliothèque de destination**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**Définition des propriétés**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. Du menu **Workflow**, sélectionnez **Paramètres du flux de travail**.
1. Sélectionnez **démarrer le flux de travail automatiquement lorsqu'un nouvel élément est créé** et désactivez les autres options de **Options de démarrage**.

   **Définir les options de démarrage**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



La conception du flux de travail est terminée.

1. Enregistrez et publiez le flux de travail pour le mettre en œuvre sur le site SharePoint.

### **Tester le flux de travail**

Pour tester le flux de travail :

1. Ouvrez le site SharePoint et téléversez un nouveau document dans la bibliothèque de documents **Personal Documents**.
   Aspose.PDF for SharePoint prend en charge la conversion des fichiers HTML, des fichiers texte et des images (JPG, PNG, GIF, TIFF et BMP*) en PDF. Le workflow est configuré pour démarrer automatiquement lorsqu'un nouvel élément est créé, de sorte que les fichiers sont traités automatiquement.
1. Actualisez le navigateur.
   Le statut du workflow apparaît dans la colonne workflow, **Aspose.PDF Workflow** dans ce cas.

   **Ajout d'un document à la bibliothèque source**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. Ouvrez la bibliothèque de documents de destination pour voir le document converti. **Shared Documents/Pdf** est le chemin dans cet exemple.

   **La bibliothèque de destination**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

