---
title: Extraer Datos de Tabla de PDF
linktitle: Extraer Datos de Tabla
type: docs
weight: 40
url: /es/androidjava/extract-data-from-table-in-pdf/
description: Aprenda a extraer datos tabulares de PDF usando Aspose.PDF para Android a través de Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer Tablas de PDF programáticamente

Extraer tablas de archivos PDF no es una tarea trivial porque la tabla puede ser creada de diversas maneras.

Aspose.PDF para Android a través de Java tiene una herramienta para facilitar la recuperación de tablas. Para extraer datos de tabla, debe realizar los siguientes pasos:

1. Abrir documento - instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
2. Crear un objeto [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. Decida qué páginas se van a analizar y aplique [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) a las páginas deseadas. Los datos tabulares serán escaneados y el resultado se guardará en una lista de [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Podemos obtener esta lista a través del método [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Para obtener los datos, itere a través de `TableList` y maneje la lista de [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) y la lista de celdas absorbidas. Podemos acceder a la primera lista llamando al método [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) y a la segunda llamando al método [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contiene [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Puede procesarlo para sus propios propósitos.

El siguiente ejemplo muestra la extracción de tablas de todas las páginas:

```java
public void extractTable () {
        // Abrir documento
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
        // Escanear páginas
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // Iterar a través de la lista de filas
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // Iterar a través de la lista de celdas
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


## Extraer tabla en un área específica de la página PDF

Cada tabla absorbida tiene la propiedad [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) que describe la posición de la tabla en la página.

Por lo tanto, si necesitas extraer tablas ubicadas en una región específica, debes trabajar con coordenadas específicas.

El siguiente ejemplo muestra cómo extraer una tabla marcada con Anotación Cuadrada:

```java
public void extractMarkedTable () {
        // Abrir documento
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
            resultMessage.setText("Tablas marcadas no encontradas..");
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
                        //Analizar tabla
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


## Extraer Datos de Tablas de PDF y almacenarlos en un archivo CSV

El siguiente ejemplo muestra cómo extraer una tabla y almacenarla como un archivo CSV. Para ver cómo convertir un PDF a una hoja de cálculo de Excel, consulte el artículo [Convertir PDF a Excel](/pdf/es/java/convert-pdf-to-excel/).

```java
 public void extractTableSaveCSV () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // Instanciar objeto de opción de guardado en Excel
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