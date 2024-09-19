---
title: Extraire les polices de PDF C#
linktitle: Extraire les polices de PDF
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
description: Utilisez la bibliothèque Aspose.PDF pour .NET pour extraire toutes les polices intégrées de votre document PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Si vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode FontUtilities.GetAllFonts() fournie dans la classe Document. Veuillez vérifier le morceau de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

Le morceau de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

