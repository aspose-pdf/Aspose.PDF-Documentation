---
title: PDFからテーブルデータを抽出
linktitle: テーブルデータの抽出
type: docs
weight: 40
url: ja/java/extract-data-from-table-in-pdf/
description: Aspose.PDF for Javaを使用してPDFから表形式データを抽出する方法を学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## プログラムでPDFからテーブルを抽出

PDFからテーブルを抽出することは簡単な作業ではありません。なぜなら、テーブルはさまざまな方法で作成できるからです。

Aspose.PDF for Javaには、テーブルを簡単に取得するためのツールがあります。テーブルデータを抽出するには、次の手順を実行する必要があります。

1. ドキュメントを開く - [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトをインスタンス化する;
1. [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) オブジェクトを作成する。

1. 分析するページを決定し、目的のページに[visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)を適用します。表形式のデータがスキャンされ、その結果が[AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable)のリストに保存されます。このリストは[getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--)メソッドを通じて取得できます。

1. データを取得するには、`TableList`を反復処理し、[absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow)のリストと吸収されたセルのリストを扱います。最初のリストには[getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--)メソッドを呼び出すことでアクセスでき、2番目のリストには[getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--)メソッドを呼び出すことでアクセスできます。

1. 各[AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell)には[TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection)が含まれています。これを自分の目的で処理することができます。

次の例は、すべてのページからテーブルを抽出する方法を示しています:

```java
public static void Extract_Table() {
    // ソースPDFドキュメントをロード
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // ページをスキャン
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Table");
            // 行のリストを繰り返す
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // セルのリストを繰り返す
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


## PDFページの特定エリアからテーブルを抽出する

各吸収されたテーブルは、ページ上のテーブルの位置を示す[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--)プロパティを持っています。

したがって、特定の領域にあるテーブルを抽出する必要がある場合は、特定の座標で作業する必要があります。

次の例は、四角形の注釈でマークされたテーブルを抽出する方法を示しています：

```java
public static void Extract_Marked_Table() {
    // ソースPDFドキュメントを読み込む
    String filePath = "<... enter path to pdf file here ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("マークされたテーブルが見つかりません。");
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


## PDFからテーブルデータを抽出しCSVファイルに保存

次の例は、テーブルを抽出してCSVファイルとして保存する方法を示しています。
PDFをExcelスプレッドシートに変換する方法については、[PDFをExcelに変換する](/pdf/java/convert-pdf-to-excel/)記事を参照してください。

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // PDFドキュメントをロード
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // ExcelSaveオプションオブジェクトをインスタンス化
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // 出力をXLS形式で保存
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```