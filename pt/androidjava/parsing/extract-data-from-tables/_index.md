---
title: Extrair Dados de Tabela do PDF
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: /pt/androidjava/extract-data-from-table-in-pdf/
description: Aprenda como extrair dados tabulares de PDF usando Aspose.PDF for Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Tabelas de PDF programaticamente

Extrair tabelas de PDFs não é uma tarefa trivial porque a tabela pode ser criada de várias maneiras.

Aspose.PDF for Android via Java tem uma ferramenta que facilita a recuperação de tabelas. Para extrair os dados da tabela, você deve executar as seguintes etapas:

1. Abrir documento - instanciar um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objeto;
1. Create a [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) objeto.
1. Decida quais páginas serão analisadas e aplique [visitar](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) para as páginas desejadas. Os dados tabulares serão escaneados, e o resultado será salvo em uma lista de [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Podemos obter esta lista através [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) método.
1. Para obter os dados, itere através `TableList` e manipular lista de [linhas absorvidas](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) e lista de células absorvidas. Podemos acessar a primeira lista chamando [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) método e a segunda chamando [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contém [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Você pode processá-lo para seus próprios propósitos.

O exemplo a seguir mostra a extração de tabelas de todas as páginas:

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

## Extrair tabela em área específica da página PDF

Cada tabela absorvida tem [Retângulo](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) propriedade que descreve a posição da tabela na página.

Então, se você precisar extrair tabelas localizadas em uma região específica, terá que trabalhar com coordenadas específicas.

O exemplo a seguir mostra como extrair uma tabela marcada com Anotação Quadrada:

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

## Extrair dados de tabela de PDF e armazená‑los em arquivo CSV

O exemplo a seguir mostra como extrair a tabela e armazená‑la como arquivo CSV.
Para ver como converter PDF para planilha Excel, consulte [Converter PDF para Excel](/pdf/pt/java/convert-pdf-to-excel/) artigo.

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

