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

Use `TableAbsorber` para localizar tabelas em cada página e percorrer linhas, células, fragmentos de texto e segmentos de texto.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere através dos objetos do documento [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) porque as tabelas são detectadas página por página.
1. Crie um [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) para cada página e chame `visit(page)` para preencher a lista de tabelas detectadas.
1. Itere através dos objetos detectados [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) e `TextSegment`.
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

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenha o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e localize o quadrado [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) que marca a região de extração.
1. Crie um [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) e chame `visit(page)` para detectar tabelas nessa página.
1. Compare cada [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) detectado com os limites do retângulo de anotação.
1. Itere através dos objetos [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) e [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) correspondentes e reconstrua o texto da linha.
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

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para a exportação.
1. Defina o formato de saída do Excel como `XLSX` para que o layout da tabela detectado seja escrito como uma pasta de trabalho do Excel.
1. Chame `document.save(outputFile.toString(), excelSave)` para exportar o documento em formato Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
