---
title: Concatenate les documents PDF en C#
linktitle: Concatenate les documents PDF
type: docs
weight: 20
url: /fr/net/concatenate-pdf-documents/
description: Cette section explique comment concaténer des documents PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **Aperçu**

Cet article explique comment fusionner, combiner ou concaténer différents fichiers PDF en un seul PDF en utilisant C#. Il couvre des sujets tels que :

- [Fusionner des fichiers PDF en C#](#concatenate-pdf-files-using-file-paths)
- [Combiner des fichiers PDF en C#](#concatenate-pdf-files-using-file-paths)

- [Fusionner plusieurs fichiers PDF en un seul PDF en C#](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Combiner plusieurs fichiers PDF en un seul PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Fusionner tous les fichiers PDF dans un dossier](#concatenating-all-pdf-files-in-particular-folder)
- [C# Combiner tous les fichiers PDF dans un dossier](#concatenating-all-pdf-files-in-particular-folder)
- [C# Fusionner des fichiers PDF en utilisant des chemins de fichiers](#concatenate-pdf-files-using-file-paths)
- [C# Combiner des fichiers PDF en utilisant des flux](#concatenate-array-of-pdf-files-using-streams)
- [C# Concatenation de tous les fichiers PDF dans un dossier](#concatenate-pdf-files-in-folder)

## Concatenation de fichiers PDF en utilisant des chemins de fichiers

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) est la classe dans [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) qui vous permet de concaténer plusieurs fichiers PDF. Vous pouvez non seulement concaténer des fichiers en utilisant FileStreams, mais aussi en utilisant MemoryStreams. Dans cet article, le processus de concaténation des fichiers en utilisant MemoryStreams sera expliqué puis montré à l'aide de l'extrait de code.

La méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) peut être utilisée pour concaténer deux fichiers PDF. La méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) vous permet de passer trois paramètres : premier PDF d'entrée, second PDF d'entrée, et PDF de sortie. Le PDF de sortie final contient les deux fichiers PDF d'entrée.

L'extrait de code C# suivant vous montre comment concaténer des fichiers PDF en utilisant des chemins de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

Dans certains cas, lorsqu'il y a beaucoup de signets, les utilisateurs peuvent les désactiver en réglant CopyOutlines sur false et améliorer les performances de la concaténation.
## Concaténer plusieurs fichiers PDF en utilisant des MemoryStreams

La méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) prend les fichiers PDF source et le fichier PDF de destination comme paramètres. Ces paramètres peuvent être soit des chemins vers les fichiers PDF sur le disque, soit des MemoryStreams. Maintenant, pour cet exemple, nous allons d'abord créer deux flux de fichiers pour lire les fichiers PDF à partir du disque. Ensuite, nous convertirons ces fichiers en tableaux d'octets. Ces tableaux d'octets des fichiers PDF seront convertis en MemoryStreams. Une fois que nous aurons extrait les MemoryStreams des fichiers PDF, nous pourrons les transmettre à la méthode de concaténation et les fusionner en un seul fichier de sortie.

Le code C# suivant vous montre comment concaténer plusieurs fichiers PDF en utilisant des MemoryStreams :

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Concaténer un tableau de fichiers PDF en utilisant les chemins de fichiers

Si vous souhaitez concaténer plusieurs fichiers PDF, vous pouvez utiliser la surcharge de la méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), qui vous permet de passer un tableau de fichiers PDF. Le résultat final est enregistré sous la forme d'un fichier fusionné créé à partir de tous les fichiers du tableau. Le code C# suivant vous montre comment concaténer un tableau de fichiers PDF en utilisant les chemins de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Concaténer un tableau de fichiers PDF en utilisant des flux

La concaténation d'un tableau de fichiers PDF ne se limite pas uniquement aux fichiers résidant sur le disque. Vous pouvez également concaténer un tableau de fichiers PDF à partir de flux. Si vous souhaitez concaténer plusieurs fichiers PDF, vous pouvez utiliser la surcharge appropriée de la méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Tout d'abord, vous devez créer un tableau de flux d'entrée et un flux pour le PDF de sortie, puis appeler la méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). La sortie sera enregistrée dans le flux de sortie. Le fragment de code C# suivant vous montre comment concaténer un tableau de fichiers PDF en utilisant des flux.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Concaténer tous les fichiers Pdf dans un dossier particulier

Vous pouvez même lire tous les fichiers Pdf dans un dossier particulier à l'exécution et les concaténer, sans même connaître les noms des fichiers. Fournissez simplement le chemin du répertoire, qui contient les documents PDF, que vous souhaitez concaténer.

Veuillez essayer d'utiliser le snippet de code C# suivant pour réaliser cette fonctionnalité.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Concaténer les formulaires PDF et garder les noms des champs uniques

La classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dans l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre la capacité de concaténer les fichiers PDF. Maintenant, si les fichiers Pdf à concaténer contiennent des champs de formulaire avec des noms de champ similaires, Aspose.PDF offre la possibilité de conserver les champs dans le fichier Pdf résultant comme uniques et vous pouvez également spécifier le suffixe pour rendre les noms de champ uniques. La propriété [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) de [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) en tant que true rendra les noms de champ uniques lorsque les formulaires Pdf sont concaténés. De plus, la propriété [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) de PdfFileEditor peut être utilisée pour spécifier le format défini par l'utilisateur du suffixe qui est ajouté au nom du champ pour le rendre unique lorsque les formulaires sont concaténés. Cette chaîne doit contenir la sous-chaîne `%NUM%` qui sera remplacée par des chiffres dans le fichier résultant.

Veuillez consulter l'extrait de code simple suivant pour réaliser cette fonctionnalité.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## Concaténer des fichiers PDF et créer une table des matières

## Concaténer des fichiers PDF

Veuillez consulter l'extrait de code suivant pour obtenir des informations sur la façon de fusionner les fichiers PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### Insérer une page blanche

Une fois les fichiers PDF fusionnés, nous pouvons insérer une page blanche au début du document sur laquelle nous pouvons créer une table des matières. Pour accomplir cette exigence, nous pouvons charger le fichier fusionné dans l'objet **Document** et nous devons appeler la méthode Page.Insert(...) pour insérer une page blanche.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### Ajouter des tampons de texte

Pour créer une table des matières, nous devons ajouter des tampons de texte sur la première page en utilisant les objets [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). Stamp classe fournit la méthode `BindLogo(...)` pour ajouter [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) et nous pouvons également spécifier l'emplacement pour ajouter ces tampons de texte en utilisant la méthode `SetOrigin(..)`. Dans cet article, nous concaténons deux fichiers PDF, donc nous devons créer deux objets de tampon de texte pointant vers ces documents individuels.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### Créer des liens locaux

Nous devons maintenant ajouter des liens vers les pages à l'intérieur du fichier concaténé. Pour répondre à cette exigence, nous pouvons utiliser la méthode `CreateLocalLink(..)` de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Dans l'extrait de code suivant, nous avons passé Transparent comme 4ème argument pour que le rectangle autour du lien ne soit pas visible.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### Code complet

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}

## Concaténer des fichiers PDF dans un dossier

La classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dans l'espace de noms Aspose.Pdf.Facades vous offre la possibilité de concaténer le fichier PDF. Vous pouvez même lire tous les fichiers Pdf dans un dossier particulier à l'exécution et les concaténer, sans même connaître les noms des fichiers. Il suffit de fournir le chemin du répertoire, qui contient les documents PDF, que vous souhaitez concaténer.

Veuillez essayer d'utiliser le code C# suivant pour réaliser cette fonctionnalité avec Aspose.PDF :

```csharp
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Récupérer les noms de tous les fichiers Pdf dans un répertoire particulier
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Obtenir la date actuelle du système et définir son format
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Obtenir l'heure actuelle du système et définir son format
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Définir la valeur pour le document Pdf résultant final
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Instancier l'objet PdfFileEditor
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Appeler la méthode Concatenate de l'objet PdfFileEditor pour concaténer tous les fichiers d'entrée
// En un seul fichier de sortie
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```