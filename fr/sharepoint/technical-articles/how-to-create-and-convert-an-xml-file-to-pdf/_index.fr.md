---
title: Comment créer et convertir un fichier XML en PDF
type: docs
weight: 30
url: /sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API est capable de créer et de convertir des fichiers XML en format PDF.
---

{{% alert color="primary" %}}

Aspose.PDF pour SharePoint est basé sur notre composant primé Aspose.PDF pour .NET. Aspose.PDF pour .NET offre des fonctionnalités remarquables allant de la création de documents PDF à partir de zéro à la manipulation de fichiers PDF existants. Parmi ces fonctionnalités, la conversion de XML en PDF est l'une des grandes fonctionnalités prises en charge par ce produit. Nous croyons donc qu'Aspose.PDF pour SharePoint sera également capable de convertir des fichiers XML en format PDF.

{{% /alert %}}

## **Création d'un fichier XML et conversion en PDF**

{{% alert color="primary" %}}

Étape par étape, cet article vous guide à travers le processus de création d'un fichier XML et sa conversion en PDF :
1. [Créer un fichier XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Créer un modèle PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Charger le modèle XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Spécifiez le chemin vers le chemin source](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Spécifiez les propriétés du fichier](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Exporter le fichier en PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Enregistrer le fichier PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **Étape 1 : Créer un fichier XML**
Créez d'abord un fichier XML basé sur le modèle d'objet de document Aspose.PDF pour .NET.

Selon le DOM d'Aspose.PDF pour .NET, un document PDF contient une collection d'objets Section, et une Section contient un ou plusieurs éléments Paragraph.
 Text est un objet de niveau paragraphe et peut contenir un ou plusieurs segments. Ci-dessous, une chaîne de texte exemple est ajoutée à un objet Segment et ajoutée à un objet Text. Enfin, l'élément Text est ajouté à la collection de paragraphes de l'objet Section.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Bonjour le monde</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **Étape 2 : Créer un modèle PDF**
Avant de continuer, assurez-vous que le serveur SharePoint Foundation 2010 est correctement installé et configuré sur le système où la conversion aura lieu.

1. Connectez-vous au site SharePoint.
1. Sélectionnez **Action du site** et **Tous les éléments**.
1. Sélectionnez l'option **Créer** et sélectionnez **Modèle PDF** dans la liste.
1. Entrez un nom de modèle.
1. Cliquez sur **Créer**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Étape 3 : Charger le modèle XML**

Une fois le modèle créé, chargez [le fichier XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. Sur la page de modèle PDF, sélectionnez **Ajouter un nouvel élément**.

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Étape 4 : Spécifier le chemin du fichier source**
Dans la boîte de dialogue de téléchargement du document :

1. Cliquez sur **Parcourir** et localisez le fichier XML sur votre système. Vous pouvez activer la case à cocher pour l'option d'écrasement du fichier existant.
1. Appuyez sur le bouton **OK**.

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Étape 5 : Spécifier les propriétés du fichier**
Lorsque le fichier est chargé, ajoutez des informations dans les champs obligatoires (marqués d'un astérisque rouge : *).

Pour cet exemple, une description d'échantillon a été ajoutée et les champs suivants complétés :

1. Une brève description du document.
1. Entrez **AllListTypes** pour le champ **Types de liste assignés**.
1. Sélectionnez **Liste** dans le menu **Type**.
   Assurez-vous que le statut reste **Actif**.
1. Cliquez sur **Enregistrer** pour sauvegarder les propriétés.

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Étape 6 : Exporter en PDF**

Lorsque le fichier XML a été ajouté au modèle PDF :
Soit :

1. Faites un clic droit sur le fichier test.xml.
1. Sélectionnez **Exporter en PDF** dans le menu.

Ou :

1. Sélectionnez **Outils Aspose** dans les **Outils de la bibliothèque**.
1. Cliquez sur **Exporter**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Étape 7 : Enregistrer le document PDF**
1. Dans la boîte de dialogue Exporter en PDF, sélectionnez **Stockage des modèles** (l'emplacement où le fichier source est stocké).
1. Sélectionnez le fichier à exporter dans le menu **Nom du modèle**.
1. Cliquez sur **Exporter en PDF** pour enregistrer le document PDF final.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Ouvrir le PDF**
Le document PDF a été enregistré et peut être ouvert. Dans l'image ci-dessous, notez la phrase "Hello World" qui était dans la balise {segment] dans le XML. Notez également que le producteur de PDF est Aspose.PDF pour SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}