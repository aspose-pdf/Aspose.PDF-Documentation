---
title: Comment créer et convertir un fichier XML en PDF
linktitle: Comment créer et convertir un fichier XML en PDF
type: docs
weight: 30
url: /fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-06-18"
description: L'API PDF SharePoint est capable de créer et de convertir des fichiers XML au format PDF.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint est construit sur notre composant primé Aspose.PDF pour .NET. Aspose.PDF pour .NET offre des fonctionnalités remarquables, de la création d'un document PDF à partir de zéro à la manipulation de fichiers PDF existants. Parmi ces fonctionnalités, la conversion XML en PDF est l'une des excellentes fonctionnalités prises en charge par ce produit. Nous pensons donc qu'Aspose.PDF pour SharePoint sera également capable de convertir des fichiers XML en format PDF.

{{% /alert %}}

## **Création d'un fichier XML et conversion en PDF**

{{% alert color="primary" %}}

Pas à pas, cet article vous guide à travers le processus de création d'un fichier XML et de sa conversion en PDF :

1. [Créer un fichier XML](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Créer un modèle PDF](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Charger le modèle XML](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Spécifier le chemin du chemin source](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Spécifier les propriétés du fichier](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Exporter le fichier au format PDF](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Enregistrer le fichier PDF](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **Étape 1 : Créer un fichier XML**
Créez d'abord un fichier XML basé sur le modèle d'objet Document d'Aspose.PDF for .NET.

Selon le DOM d'Aspose.PDF for .NET, un document PDF contient une collection d'objets Section, et une Section contient un ou plusieurs éléments Paragraph. Le texte est un objet de niveau Paragraph et peut contenir un ou plusieurs segments. Ci-dessous, une chaîne de texte d'exemple est ajoutée à un objet Segment puis ajoutée à un objet Text. Enfin, l'élément Text est ajouté à la collection de paragraphes de l'objet Section.

**XML**

{{< highlight csharp >}}



\u003C?xml version=\u00221.0\u0022 encoding=\u0022utf-8\u0022 ?\u003E

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Bonjour le monde</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **Étape 2 : Créer le modèle PDF**
Avant de continuer, assurez‑vous que le serveur SharePoint Foundation 2010 est correctement installé et configuré sur le système où la conversion aura lieu.

1. Connectez‑vous au site SharePoint.
1. Sélectionnez **Site Action** et **All Items**.
1. Sélectionnez l’option **Create** et sélectionnez **PDF Template** dans la liste.
1. Saisissez un nom de modèle.
1. Cliquez sur **Create**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Étape 3 : Charger le modèle XML**
Une fois le modèle créé, chargez [le fichier XML](/pdf/fr/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):

1. Sur la page de modèle PDF, sélectionnez **Ajouter un nouvel élément**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Étape 4 : Spécifier le chemin du fichier source**
Dans la boîte de dialogue de téléchargement du document :

1. Cliquez sur **Parcourir** et localisez le fichier XML sur votre système. Vous pouvez activer la case à cocher pour écraser le fichier existant.
1. Appuyez sur le bouton **OK**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Étape 5 : Spécifier les propriétés du fichier**
Lorsque le fichier est chargé, ajoutez des informations dans les champs obligatoires (marqués d’un astérisque rouge : *).

Dans cet exemple, une description d’échantillon a été ajoutée et les champs suivants remplis :

1. Une brève description du document.
1. Saisissez **AllListTypes** pour le champ **Assigned List Types**.
1. Sélectionnez **List** dans le menu **Type**.
   Assurez‑vous que le statut reste **Active**.
1. Cliquez sur **Enregistrer** pour enregistrer les propriétés.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Étape 6 : Exporter en PDF**
Lorsque le fichier XML a été ajouté au modèle PDF :
Soit :

1. Cliquez avec le bouton droit sur le fichier test.xml.
1. Sélectionnez **Export to PDF** dans le menu.

Ou :

1. Sélectionnez **Aspose Tools** depuis les **Library Tools**.
1. Cliquez sur **Export**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Étape 7 : Enregistrez le document PDF**
1. Dans la boîte de dialogue Exporter vers PDF, sélectionnez **Template storage** (l’emplacement où le fichier source est stocké).
1. Sélectionnez le fichier à exporter dans le menu **Template name**.
1. Cliquez sur **Export to PDF** pour enregistrer le document PDF final.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Ouvrir le PDF**
Le document PDF a été enregistré et peut être ouvert. Dans l'image ci-dessous, notez la phrase "Hello World" qui était dans la balise {segment] du XML. Notez également que le producteur PDF est Aspose.PDF for SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
