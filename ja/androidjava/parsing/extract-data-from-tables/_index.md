---
title: PDFから表データを抽出する 
linktitle: 表データの抽出
type: docs
weight: 40
url: /ja/androidjava/extract-data-from-table-in-pdf/
description: Aspose.PDF for Android via Javaを使用してPDFから表形式データを抽出する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## プログラムでPDFから表を抽出する

PDFから表を抽出することは簡単な作業ではありません。なぜなら、表はさまざまな方法で作成される可能性があるからです。

Aspose.PDF for Android via Javaには、表を簡単に取得するためのツールがあります。表データを抽出するには、次の手順を実行する必要があります：

1. ドキュメントを開く - [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトをインスタンス化します;
1. [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) オブジェクトを作成します。

1. 分析するページを決定し、[visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)を希望するページに適用します。表形式のデータがスキャンされ、結果は[AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable)のリストに保存されます。このリストは[getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--)メソッドを通じて取得できます。
2. データを取得するには、`TableList`を反復処理し、[吸収された行](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow)のリストと吸収されたセルのリストを処理します。最初のリストには[getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--)メソッドを呼び出すことでアクセスでき、2番目のリストには[getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--)メソッドを呼び出すことでアクセスできます。

1. 各[AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell)には[TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection)が含まれています。これを自分の目的に合わせて処理することができます。

次の例は、すべてのページからテーブルを抽出する方法を示しています:

```java
public void extractTable () {
        // ドキュメントを開く
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
        // ページをスキャン
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // 行のリストを反復処理
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // セルのリストを反復処理
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


## PDFページの特定エリアからテーブルを抽出する

各吸収されたテーブルには、ページ上のテーブルの位置を説明する[Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle)プロパティがあります。

したがって、特定の領域にあるテーブルを抽出する必要がある場合は、特定の座標で作業する必要があります。

次の例は、四角形注釈でマークされたテーブルを抽出する方法を示しています:

```java
public void extractMarkedTable () {
        // ドキュメントを開く
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
            resultMessage.setText("マークされたテーブルが見つかりませんでした。");
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
                        // テーブルを解析する
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


## PDFからテーブルデータを抽出してCSVファイルに保存する

次の例は、テーブルを抽出してCSVファイルとして保存する方法を示しています。PDFをExcelスプレッドシートに変換する方法については、[PDFをExcelに変換する](/pdf/ja/java/convert-pdf-to-excel/)記事を参照してください。

```java
 public void extractTableSaveCSV () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // ExcelSave Optionオブジェクトをインスタンス化
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