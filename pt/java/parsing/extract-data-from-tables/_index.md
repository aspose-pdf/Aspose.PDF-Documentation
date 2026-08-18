---
title: Extraia dados de tabela em PDF com Java
linktitle: Extrair dados da tabela
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Aprenda como extrair dados de tabela de arquivos PDF com Aspose.PDF para Java e exportar tabelas detectadas para processamento posterior.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair dados de tabela em PDF via Java
Abstract: Este artigo explica como extrair e processar dados de tabela de documentos PDF com Aspose.PDF para Java. Ele mostra como digitalizar páginas com `TableAbsorber`, ler linhas e células de tabelas detectadas, limitar a extração a uma região anotada específica e exportar o resultado para Excel.
---
## Extraia tabelas de PDF

Usar `TableAbsorber` para localizar tabelas em cada página e percorrer linhas, células, fragmentos de texto e segmentos de texto.

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) exemplo.
1. Iterar pelo documento [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos porque as tabelas são detectadas página por página.
1. Crie um [Absorvedor de mesa](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) para cada página e chamada `visit(page)` para preencher a lista de tabelas detectadas.
1. Iterar através do detectado [Tabela Absorvida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [Linha Absorvida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [Célula Absorvida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), e `TextSegment` objetos.
1. Construa o texto da linha extraído do conteúdo do fragmento e imprima os dados da tabela.

```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Extraia uma tabela de uma área marcada específica

Este exemplo encontra uma anotação quadrada, compara seu retângulo com cada tabela detectada e gera apenas tabelas dentro da região marcada.

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) exemplo.
1. Obtenha o alvo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e localize o quadrado [Anotação](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) que marca a região de extração.
1. Crie um [Absorvedor de mesa](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) e ligue `visit(page)` para detectar tabelas nessa página.
1. Compare cada detectado [Tabela Absorvida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) com os limites do retângulo de anotação.
1. Iterar através da correspondência [Linha Absorvida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) e [Célula Absorvida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) objetos e reconstruir o texto da linha.
1. Imprima os dados da tabela apenas para a região marcada.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Exportar tabelas para Excel

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) exemplo.
1. Criar [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para a exportação.
1. Defina o formato de saída do Excel para `XLSX` portanto, o layout da tabela detectado é escrito como uma pasta de trabalho do Excel.
1. Chamar `document.save(outputFile.toString(), excelSave)` para exportar o documento em formato Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
