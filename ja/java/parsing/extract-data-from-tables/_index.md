---
title: "Java での PDF のテーブルからデータの抽出"
linktitle: "テーブルからデータの抽出"
type: docs
weight: 40
url: /ja/java/extract-data-from-table-in-pdf/
description: Aspose.PDF for Java を使用して PDF ファイルからテーブルデータを抽出し、検出されたテーブルをさらに処理できるようにエクスポートする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF のテーブルからデータを抽出する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントからテーブル データを抽出および処理する方法を説明します。`TableAbsorber` を使用してページをスキャンし、検出されたテーブルから行とセルを読み取り、特定の注釈領域に抽出を限定し、結果を Excel にエクスポートする方法を示します。
---
## PDF からテーブルの抽出

使用 `TableAbsorber` 各ページのテーブルを見つけ、行、セル、テキストフラグメント、テキストセグメントを反復処理します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. ドキュメントを繰り返し処理する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) テーブルがページごとに検出されるため、objects。
1. 作成 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 各ページごとに呼び出す `visit(page)` 検出されたテーブルリストを埋めるために。
1. 検出されたものを反復処理する [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)、そして `TextSegment` オブジェクト。
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

## 特定のマークされた領域から表の抽出

この例では、四角形の注釈を見つけ、その矩形を検出された各表と比較し、マークされた領域内の表のみを出力します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. ターゲットを取得 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして四角形を見つける [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 抽出領域を示す。
1. 作成 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) そして呼び出す `visit(page)` そのページ上のテーブルを検出するために。
1. 検出された各項目を比較 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 注釈の矩形境界と共に。
1. 一致するものを反復処理する [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) および [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) オブジェクトを処理し、行テキストを再構築してください。
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

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) エクスポート用に。
1. Excel の出力形式を設定 `XLSX` したがって、検出されたテーブルレイアウトはExcelブックとして書き込まれます。
1. 呼び出す `document.save(outputFile.toString(), excelSave)` ドキュメントをExcel形式でエクスポートしてください。

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
