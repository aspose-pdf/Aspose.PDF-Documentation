---
title: Extraire les données de table à partir d'un PDF 
linktitle: Extraire les données de table
type: docs
weight: 40
url: fr/java/extract-data-from-table-in-pdf/
description: Apprenez à extraire les données tabulaires d'un PDF en utilisant Aspose.PDF pour Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire des tables d'un PDF par programmation

Extraire des tables des PDFs n'est pas une tâche triviale car la table peut être créée de différentes manières.

Aspose.PDF pour Java dispose d'un outil pour faciliter la récupération des tables. Pour extraire les données de table, vous devez effectuer les étapes suivantes :

1. Ouvrir le document - instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. Créer un objet [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. Décidez quelles pages doivent être analysées et appliquez [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) aux pages souhaitées. Les données tabulaires seront scannées, et le résultat sera enregistré dans une liste de [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Nous pouvons obtenir cette liste via la méthode [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Pour obtenir les données, itérez à travers `TableList` et gérez la liste des [lignes absorbées](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) et la liste des cellules absorbées. Nous pouvons accéder à la première liste en appelant la méthode [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) et à la seconde en appelant la méthode [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Chaque [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contient des [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Vous pouvez les traiter pour vos propres besoins.

L'exemple suivant montre l'extraction de table depuis toutes les pages :

```java
public static void Extract_Table() {
    // Charger le document PDF source        
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // Analyser les pages
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Table");
            // Itérer à travers la liste des lignes
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // Itérer à travers la liste des cellules
                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                    for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                        StringBuilder sb = new StringBuilder();
                        for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                            sb.append(seg.getText());
                        System.out.print(sb.toString() + "|");
                    }
                }
                System.out.println();
            }
        }
    }
}
```


## Extraire une table dans une zone spécifique de la page PDF

Chaque table absorbée a la propriété [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--) qui décrit la position de la table sur la page.

Donc, si vous avez besoin d'extraire des tables situées dans une région spécifique, vous devez travailler avec des coordonnées spécifiques.

L'exemple suivant montre comment extraire une table marquée avec une annotation carrée :

```java
public static void Extract_Marked_Table() {
    // Charger le document PDF source
    String filePath = "<... entrer le chemin vers le fichier pdf ici ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("Tables marquées non trouvées..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```


## Extraire les Données de Table d'un PDF et les stocker dans un fichier CSV

L'exemple suivant montre comment extraire une table et la stocker sous forme de fichier CSV.
Pour voir comment convertir un PDF en feuille de calcul Excel, veuillez vous référer à l'article [Convertir un PDF en Excel](/pdf/java/convert-pdf-to-excel/).

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // Charger le document PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Instancier un objet ExcelSave Option
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // Enregistrer la sortie au format XLS
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```