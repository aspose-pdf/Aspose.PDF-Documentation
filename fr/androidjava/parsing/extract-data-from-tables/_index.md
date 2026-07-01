---
title: Extraire les données du tableau du PDF
linktitle: Extraire les données du tableau
type: docs
weight: 40
url: /fr/androidjava/extract-data-from-table-in-pdf/
description: Apprenez comment extraire des données tabulaires à partir du PDF en utilisant Aspose.PDF for Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire les tableaux du PDF de manière programmatique

Extraire des tableaux à partir de PDFs n’est pas une tâche triviale car le tableau peut être créé de différentes manières.

Aspose.PDF for Android via Java dispose d’un outil qui facilite la récupération des tableaux. Pour extraire les données du tableau, vous devez suivre les étapes suivantes :

1. Ouvrir le document - instancier un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objet;
1. Créer un [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) objet.
1. Déterminez quelles pages doivent être analysées et appliquez [visiter](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) vers les pages souhaitées. Les données tabulaires seront analysées, et le résultat sera enregistré dans une liste de [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Nous pouvons obtenir cette liste via [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) méthode.
1. Pour obtenir les données, itérez à travers `TableList` et gérer la liste de [lignes absorbées](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) et la liste des cellules absorbées. Nous pouvons accéder à la première liste en appelant [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) méthode et à la seconde en appelant [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. Chaque [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contient [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Vous pouvez le traiter à vos propres fins.

L'exemple suivant montre l'extraction de tableau depuis toutes les pages :

```java
public void extractTable () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();

        File file=new File(fileStorage, "extracted-text.txt");
        FileOutputStream fileOutputStream;

        try {
            fileOutputStream=new FileOutputStream(file);

        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
        // Scan pages
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // Iterate through list of rows
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // Iterate through list of cell
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb=new StringBuilder();
                                for (TextSegment seg :
                                        (Iterable<? extends TextSegment>) fragment.getSegments())
                                    sb.append(seg.getText());
                                bw.write(sb.toString() + "|");
                            }
                        }
                        bw.newLine();
                    }
                } catch (IOException e) {
                    resultMessage.setText(e.getMessage());
                    return;
                }
            }
        }
        try {
            bw.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Extraire le tableau dans une zone spécifique de la page PDF

Chaque tableau absorbé a [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) propriété qui décrit la position du tableau sur la page.

Donc, si vous devez extraire des tableaux situés dans une région spécifique, vous devez travailler avec des coordonnées spécifiques.

L'exemple suivant montre comment extraire le tableau marqué avec l'annotation Square Annotation :

```java
public void extractMarkedTable () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.Page page=document.getPages().get_Item(1);

        com.aspose.pdf.AnnotationSelector annotationSelector=
                new com.aspose.pdf.AnnotationSelector(
                        new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

        List list=annotationSelector.getSelected();
        if (list.size() == 0) {
            resultMessage.setText("Marked tables not found..");
            return;
        }

        com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();
        absorber.visit(page);

        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            {
                boolean isInRegion=(squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                        && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                        && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                        && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

                if (isInRegion) {
                    File file=new File(fileStorage, "extracted-text.txt");
                    FileOutputStream fileOutputStream;

                    try {
                        fileOutputStream=new FileOutputStream(file);

                    } catch (FileNotFoundException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }

                    BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
                    try {
                        //Parse table
                        for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                            {
                                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                                    for (com.aspose.pdf.TextFragment fragment :
                                            cell.getTextFragments()) {
                                        bw.write(fragment.getText());
                                    }
                                    bw.write("|");
                                }
                                bw.newLine();
                            }
                        }
                        bw.close();
                        // -------------
                    } catch (IOException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }
                    resultMessage.setText(R.string.success_message);
                }
            }
        }
    }
```

## Extraire les données du tableau du PDF et les enregistrer dans un fichier CSV

L'exemple suivant montre comment extraire le tableau et le stocker sous forme de fichier CSV.
Pour voir comment convertir un PDF en feuille de calcul Excel, veuillez vous référer à [Convertir le PDF en Excel](/pdf/fr/java/convert-pdf-to-excel/) article.

```java
 public void extractTableSaveCSV () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // Instantiate ExcelSave Option object
        com.aspose.pdf.ExcelSaveOptions excelSave=new com.aspose.pdf.ExcelSaveOptions();
        excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);
        try {
            document.save(file.toString(), excelSave);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

