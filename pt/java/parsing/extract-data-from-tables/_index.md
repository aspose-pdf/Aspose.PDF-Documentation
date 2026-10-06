---
title: Extrair Dados da Tabela em PDF com Java
linktitle: Extrair Dados da Tabela
type: docs
weight: 40
url: /pt/java/extract-data-from-table-in-pdf/
description: Aprenda como extrair dados de tabelas de arquivos PDF com Aspose.PDF for Java e exportar tabelas detectadas para processamento adicional.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Extrair Dados da Tabela em PDF via Java
Abstract: Este artigo explica como extrair e processar dados de tabela de documentos PDF com Aspose.PDF for Java. Ele mostra como analisar páginas com `TableAbsorber`, ler linhas e células de tabelas detectadas, limitar a extração a uma região anotada específica e exportar o resultado para Excel.
---
## Extrair tabelas de PDF

Usar `TableAbsorber` para encontrar tabelas em cada página e iterar pelas linhas, células, fragmentos de texto e segmentos de texto.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Iterar através do documento [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos porque as tabelas são detectadas página por página.
1. Crie um [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) para cada página e chamar `visit(page)` para preencher a lista de tabelas detectadas.
1. Iterar pelos detectados [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), e `TextSegment` objetos.
1. Construa o texto da linha extraída a partir do conteúdo do fragmento e imprima os dados da tabela.

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

## Extrair uma tabela de uma área marcada específica

Este exemplo encontra uma anotação quadrada, compara seu retângulo com cada tabela detectada e exibe apenas as tabelas dentro da região marcada.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Obtenha o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e localize o quadrado [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) que marca a região de extração.
1. Crie um [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) e chamar `visit(page)` para detectar tabelas nessa página.
1. Compare cada detectado [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) com os limites do retângulo da anotação.
1. Iterar através da correspondência [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) e [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) objetos e reconstruir o texto da linha.
1. Imprimir os dados da tabela apenas para a região marcada.

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

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para a exportação.
1. Defina o formato de saída do Excel como `XLSX` portanto, o layout da tabela detectado é gravado como uma pasta de trabalho do Excel.
1. Chamada `document.save(outputFile.toString(), excelSave)` para exportar o documento no formato Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
