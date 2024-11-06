---
title: Obtenir les métadonnées XMP d'un fichier PDF
type: docs
weight: 30
url: fr/net/get-xmp-metadata-of-an-existing-pdf-file/
description: Cette section explique comment obtenir les métadonnées XMP d'un PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Pour obtenir les métadonnées XMP d'un fichier PDF, vous devez créer un objet [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Vous pouvez passer des propriétés spécifiques de métadonnées XMP à l'objet [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) pour obtenir leurs valeurs. Le code suivant vous montre comment obtenir les métadonnées XMP d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Créer un objet PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Lier le fichier PDF à l'objet
xmpMetaData.BindPdf( dataDir + "input.pdf");

// Obtenir les propriétés des métadonnées XMP
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```