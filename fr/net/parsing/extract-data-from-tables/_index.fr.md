---
title: Extraire des données de tableau dans un PDF avec C#
linktitle: Extraire des données de tableau
type: docs
weight: 40
url: /net/extract-data-from-table-in-pdf/
description: Apprenez à extraire des données tabulaires à partir d'un PDF en utilisant Aspose.PDF pour .NET en C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire des tableaux d'un PDF de manière programmatique

Extraire des tableaux des PDF n'est pas une tâche facile car les tableaux peuvent être créés de diverses manières.

Aspose.PDF pour .NET dispose d'un outil pour faciliter la récupération des tableaux. Pour extraire les données d'un tableau, vous devez effectuer les étapes suivantes :

1. Ouvrir le document - instancier un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ;
1. Créer un objet [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. `TableList` est une liste de [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Pour obtenir la date, itérez à travers `TableList` et gérez [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) et [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)
1. Chaque [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) contient une collection de [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Vous pouvez la traiter selon vos besoins.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

L'exemple suivant montre l'extraction de tableaux de toutes les pages :

```csharp
public static void Extract_Table()
{
    // Charger le document PDF source
    var filePath="<... entrez le chemin vers le fichier pdf ici ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Extraire une table dans une zone spécifique d'une page PDF

Chaque table absorbée possède une propriété [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) qui décrit la position de la table sur la page.

Ainsi, si vous avez besoin d'extraire des tables situées dans une région spécifique, vous devez travailler avec des coordonnées spécifiques.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

L'exemple suivant montre comment extraire une table marquée avec une annotation carrée :

```csharp
public static void Extract_Marked_Table()
{
    // Charger le document PDF source
    var filePath="<... entrez le chemin du fichier pdf ici ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Extraire les données des tableaux d'un PDF et les stocker dans un fichier CSV

L'exemple suivant montre comment extraire un tableau et le stocker sous forme de fichier CSV.
Pour voir comment convertir un PDF en feuille de calcul Excel, veuillez consulter l'article [Convertir un PDF en Excel](/pdf/net/convert-pdf-to-excel/).

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void Extract_Table_Save_CSV()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Charger le document PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instancier l'objet option de sauvegarde Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // Sauvegarder la sortie au format XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
