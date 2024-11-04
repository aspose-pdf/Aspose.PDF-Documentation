---

title: Conversion d'un fichier en PDF via une activité de workflow  
type: docs  
weight: 50  
url: /sharepoint/converting-a-file-to-pdf-via-workflow-activity/  
lastmod: "2020-12-16"  
description: PDF SharePoint API peut être utilisé dans un workflow SharePoint qui convertit un document en PDF.  

---

{{% alert color="primary" %}}

Le support pour les workflows est une fonctionnalité clé de Microsoft Office SharePoint Server. Les workflows aident à automatiser le mouvement des documents selon une logique métier et à rationaliser le coût et le temps de l'organisation des documents. Cet article démontre comment utiliser Aspose.PDF pour SharePoint dans un workflow qui convertit un document en PDF.

{{% /alert %}}

## **Configuration d'un Workflow**

Cet exemple crée un workflow qui convertit tout nouvel élément dans une bibliothèque de documents au format PDF et le stocke dans une autre bibliothèque de documents. L'exemple utilise la bibliothèque **Documents personnels** comme bibliothèque source et le sous-dossier **Pdf** dans la bibliothèque **Documents partagés** comme bibliothèque de destination.

Aspose.PDF pour SharePoint prend en charge la conversion de fichiers HTML, texte et image.

### **Concevoir le Flux de Travail avec SharePoint Designer**

1. Ouvrez **SharePoint Designer** et connectez-vous au site où le flux de travail sera implémenté.
2. Sélectionnez **Flux de travail** dans **objets du site** puis ouvrez **Flux de liste**.
3. Sélectionnez la bibliothèque **Documents personnels** pour créer et attacher un nouveau flux de liste à la bibliothèque de documents.

   **Sélection de Documents personnels dans le menu**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)

4. Créez et attachez le flux de liste à la bibliothèque **Documents personnels** en tapant un nom et une description pour le flux de travail.
5. Cliquez sur **OK** pour terminer cette étape.

   **Création d'un flux de liste**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)

Un éditeur d'étapes de flux de travail apparaît. Ceci est utilisé pour définir les conditions et les actions pour les flux de travail. Ajoutez maintenant une action pour convertir un nouveau document en PDF sans condition, à partir de **Aspose Actions**.
1. Sélectionnez l'action **Convertir le fichier en PDF via Aspose.PDF** dans le menu **Action**.

   **Sélectionner une action**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Configurez les paramètres de l'action :
   1. Définissez le paramètre **ce dossier** sur le dossier de destination.
   1. Soit laissez les autres paramètres de l'action avec les valeurs par défaut, soit définissez-les à l'aide de la fenêtre des propriétés de l'action. La valeur par défaut pour le paramètre **Écraser** est faux.

      **L'Éditeur de Workflow**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Définir la bibliothèque de destination**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Définir les propriétés**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. Dans le menu **Workflow**, sélectionnez **Paramètres du Workflow**.
1. Sélectionnez **démarrer automatiquement le workflow lorsqu'un nouvel élément est créé** et désélectionnez les autres options dans **Options de démarrage**.

   **Définir les options de démarrage**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)

La conception du flux de travail est terminée.

1. Enregistrez et publiez le flux de travail pour le mettre en œuvre sur le site SharePoint.

### **Tester le flux de travail**

Pour tester le flux de travail :

1. Ouvrez le site SharePoint et téléchargez un nouveau document dans la bibliothèque de documents **Documents personnels**. Aspose.PDF pour SharePoint prend en charge la conversion de fichiers HTML, de fichiers texte et d'images (JPG, PNG, GIF, TIFF et BMP*) en PDF. Le flux de travail est configuré pour démarrer automatiquement lorsqu'un nouvel élément est créé, de sorte que les fichiers sont traités automatiquement.
1. Actualisez le navigateur. Le statut du flux de travail apparaît dans la colonne de flux de travail, **Aspose.PDF Workflow** dans ce cas.

   **Ajouter un document à la bibliothèque source**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Ouvrez la bibliothèque de documents de destination pour afficher le document converti. **Documents partagés/Pdf** est le chemin dans cet exemple.

   **La bibliothèque de destination**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)