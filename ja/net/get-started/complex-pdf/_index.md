---
title: 複雑なPDFの作成
linktitle: 複雑なPDFの作成
type: docs
weight: 60
url: /ja/net/complex-pdf-example/
description: Aspose.PDF for NETを使用すると、画像、テキストフラグメント、およびテーブルを含む複雑なドキュメントを作成できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/ja/net/hello-world-example/)の例では、C# と Aspose.PDF を使用してPDFドキュメントを作成するための簡単な手順を示しました。この記事では、C# と Aspose.PDF for .NETを使用して、より複雑なドキュメントを作成する方法を見ていきます。例として、旅客フェリーサービスを運営する架空の会社のドキュメントを取り上げます。
このドキュメントには、画像、2つのテキストフラグメント（ヘッダーと段落）、およびテーブルが含まれます。このようなドキュメントを構築するために、DOMベースのアプローチを使用します。詳細はセクション[Basics of DOM API](/pdf/ja/net/basics-of-dom-api/)で読むことができます。

ゼロからドキュメントを作成する場合、以下の手順に従う必要があります：

1.
1. ドキュメントオブジェクトに[ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page)を追加します。これで、ドキュメントには1ページが含まれるようになります。
1. ページに[画像](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index)を追加します。
1. ヘッダー用に[テキストフラグメント](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)を作成します。ヘッダーにはArialフォント、フォントサイズ24pt、中央揃えを使用します。
1. ページの[段落](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)にヘッダーを追加します。
1. 説明用に[テキストフラグメント](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)を作成します。説明にはArialフォント、フォントサイズ24pt、中央揃えを使用します。
1. ページの段落に（説明）を追加します。
1. テーブルを作成し、テーブルのプロパティを追加します。
1. ページの[段落](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)に（テーブル）を追加します。
1. ドキュメント「Complex.pdf」を保存します。

このコードスニペットは[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。
以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // ドキュメントオブジェクトを初期化
            Document document = new Document();
            // ページを追加
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // 画像を追加
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // ヘッダーを追加
            var header = new TextFragment("2020年秋の新しいフェリールート");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 説明を追加
            var descriptionText = "訪問者はオンラインでチケットを購入する必要があり、1日のチケットは5,000枚に限定されています。フェリーサービスは半分のキャパシティで運行され、スケジュールも縮小されています。列ができることを予想してください。";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // テーブルを追加
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("出発都市");
            headerRow.Cells.Add("出発島");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

