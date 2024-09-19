---
title:  Extraire des données d'AcroForm en utilisant C#
linktitle:  Extraire des données d'AcroForm
type: docs
weight: 50
url: /net/extract-data-from-acroform/
description: Aspose.PDF permet d'extraire facilement les données des champs de formulaire des fichiers PDF. Apprenez à extraire des données des AcroForms et à les enregistrer au format JSON, XML ou FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire les champs de formulaire d'un document PDF

En plus de vous permettre de générer des champs de formulaire et de remplir des champs de formulaire, Aspose.PDF pour .NET facilite l'extraction des données des champs de formulaire ou des informations sur les champs de formulaire des fichiers PDF.

Dans le code exemple ci-dessous, nous démontrons comment parcourir chaque page d'un PDF pour extraire des informations sur tous les AcroForm du PDF ainsi que les valeurs des champs de formulaire. Ce code exemple suppose que vous ne connaissez pas le nom des champs de formulaire à l'avance.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Obtenir les valeurs de tous les champs
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Nom du champ : {0} ", formField.PartialName);
        Console.WriteLine("Valeur : {0} ", formField.Value);
    }
}
```
Si vous connaissez le nom des champs de formulaire dont vous souhaitez extraire les valeurs, vous pouvez utiliser l'indexeur dans la collection Documents.Form pour récupérer rapidement ces données. Regardez en bas de cet article pour un exemple de code sur comment utiliser cette fonction.

## Récupérer la valeur d'un champ de formulaire par titre

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire de la collection Form de l'objet Document. Cet exemple sélectionne un TextBoxField et récupère sa valeur en utilisant la propriété Value.

## Extraire les champs de formulaire d'un document PDF en JSON

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## Extraire les données vers XML à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode ExportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe Form puis appeler la méthode ExportXml en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et supprimer l'objet Form. Le fragment de code suivant vous montre comment exporter des données vers un fichier XML.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// Ouvrir le document
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// Créer un fichier xml.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// Exporter les données
form.ExportXml(xmlOutputStream);
// Fermer le flux de fichier
xmlOutputStream.Close();

// Fermer le document
form.Dispose();
```
## Exporter des données vers FDF à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier FDF à partir du fichier PDF en utilisant la méthode ExportFdf. Pour exporter des données vers FDF, vous devez créer un objet de la classe Form puis appeler la méthode ExportFdf en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode Save de la classe Form. Le fragment de code suivant vous montre comment exporter des données vers un fichier FDF.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Ouvrir le document
form.BindPdf(dataDir + "input.pdf");

// Créer un fichier fdf.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Exporter les données
form.ExportFdf(fdfOutputStream);

// Fermer le flux de fichier
fdfOutputStream.Close();

// Enregistrer le document mis à jour
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## Exporter des données vers XFDF à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier XFDF à partir du fichier PDF en utilisant la méthode ExportXfdf. Pour exporter des données vers XFDF, vous devez créer un objet de la classe Form puis appeler la méthode ExportXfdf en utilisant l'objet FileStream. Enfin, vous pouvez enregistrer le fichier PDF en utilisant la méthode Save de la classe Form. Le fragment de code suivant vous montre comment exporter des données vers un fichier XFDF.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Ouvrir le document
form.BindPdf(dataDir + "input.pdf");

// Créer un fichier xfdf.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Exporter les données
form.ExportXfdf(xfdfOutputStream);

// Fermer le flux de fichier
xfdfOutputStream.Close();

// Enregistrer le document mis à jour
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

