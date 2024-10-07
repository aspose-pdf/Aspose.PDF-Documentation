---
title: Définir les métadonnées XMP d'un PDF existant
type: docs
weight: 20
url: /net/set-xmp-metadata-of-an-existing-pdf/
description: Cette section explique comment définir les métadonnées XMP d'un PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Pour définir les métadonnées XMP dans un fichier PDF, vous devez créer un objet [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Vous pouvez utiliser la méthode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) de la classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) pour ajouter différentes propriétés. Enfin, appelez la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de la classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). L'extrait de code suivant vous montre comment ajouter des métadonnées XMP dans un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Créer un objet PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Lier le fichier pdf à l'objet
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// Ajouter la date de création
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// Modifier la date des métadonnées
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// Ajouter l'outil de création
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Nom de l'outil de création");

// Supprimer la date de modification
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// Ajouter une propriété définie par l'utilisateur
// Étape #1 : enregistrer le préfixe de l'espace de noms et l'URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// Étape #2 : ajouter une propriété utilisateur avec le préfixe
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// Modifier la propriété définie par l'utilisateur
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// Enregistrer les métadonnées xmp dans le fichier pdf
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// Fermer l'objet
xmpMetaData.Close();
```