---
title: PDF内のテーブルからデータを抽出するC#
linktitle: テーブルからデータを抽出する
type: docs
weight: 40
url: /net/extract-data-from-table-in-pdf/
description: Aspose.PDF for .NET を使用してPDFから表データを抽出する方法を学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFからプログラムでテーブルを抽出する

PDFからテーブルを抽出することは、テーブルがさまざまな方法で作成されているため、簡単な作業ではありません。

Aspose.PDF for .NETには、テーブルを簡単に取得するためのツールがあります。テーブルデータを抽出するには、次の手順を実行する必要があります：

1. ドキュメントを開く - [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトをインスタンス化します。
1. [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) オブジェクトを作成します。
1. `TableList`は[AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable)のリストです。日付を取得するには、`TableList`を反復処理し、[RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist)と[CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)を扱います。
1. 各[AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell)には[TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments)コレクションが含まれています。これを自分の目的で処理できます。

以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

以下の例は、すべてのページから表を抽出する方法を示しています：

```csharp
public static void Extract_Table()
{
    // Load source PDF document
    var filePath="<... enter path to pdf file here ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## PDFページの特定の領域の表を抽出する

各吸収された表には、ページ上の表の位置を記述する[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle)プロパティがあります。

したがって、特定の領域に位置する表を抽出する必要がある場合、特定の座標で作業する必要があります。

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

次の例は、四角注釈でマークされた表を抽出する方法を示しています：

```csharp
public static void Extract_Marked_Table()
{
    // PDFドキュメントのソースを読み込む
    var filePath="<... PDFファイルへのパスをここに入力 ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## PDFから表データを抽出し、CSVファイルに保存する

次の例は、表を抽出してCSVファイルとして保存する方法を示しています。
PDFをExcelスプレッドシートに変換する方法については、[PDFをExcelに変換する](/pdf/net/convert-pdf-to-excel/)記事を参照してください。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
public static void Extract_Table_Save_CSV()
{
    // 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください

    // PDF文書をロード
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // ExcelSave Option オブジェクトをインスタンス化
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // 出力をXLS形式で保存
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
