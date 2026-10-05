---
title: "Java での PDF のテーブルからデータの抽出"
linktitle: "テーブルからデータの抽出"
type: docs
weight: 40
url: /ja/java/extract-data-from-table-in-pdf/
description: Aspose.PDF for Java を使用して PDF ファイルからテーブルデータを抽出し、検出されたテーブルをさらに処理できるようにエクスポートする方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF のテーブルからデータの抽出方法"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメントからテーブルデータを抽出および処理する方法を説明します。`TableAbsorber` を使用してページをスキャンし、検出されたテーブルから行とセルを読み取り、特定の注釈領域に抽出を限定し、結果を Excel にエクスポートする方法を示します。"
---
## PDF からテーブルの抽出

`TableAbsorber` を使用して、各ページのテーブルを検出し、行、セル、テキストフラグメント、テキストセグメントを反復処理します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. ドキュメントの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを反復処理してください。テーブルはページ単位で検出されるためです。
1. 各ページごとに [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) を作成し、`visit(page)` を呼び出して検出されたテーブルリストを埋めてください。
1. 検出された [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/)、[AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/)、[AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/)、[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)、および `TextSegment` オブジェクトを反復処理してください。
1. フラグメントの内容から抽出した行テキストを構築し、テーブルデータを出力してください。

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

## 特定のマークされた領域からの表の抽出

この例では、四角形の注釈を見つけ、その矩形を検出された各表と比較し、マークされた領域内の表のみを出力します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. ターゲットの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得し、抽出領域を示す四角形の [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) を見つけてください。
1. [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) を作成し、そのページ上のテーブルを検出するために `visit(page)` を呼び出してください。
1. 検出された各 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) の [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を、注釈の矩形境界と比較してください。
1. 一致する [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) および [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) オブジェクトを反復処理し、行テキストを再構築してください。
1. マークされた領域のテーブル データのみを印刷してください。

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

## テーブルを Excel にエクスポート

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. エクスポート用に [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成してください。
1. Excel の出力形式を `XLSX` に設定してください。これにより、検出されたテーブルレイアウトが Excel ブックとして書き込まれます。
1. `document.save(outputFile.toString(), excelSave)` を呼び出して、ドキュメントを Excel 形式でエクスポートしてください。

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
