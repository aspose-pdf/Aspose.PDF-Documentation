---
title: PDFドキュメントからテーブルを抽出する
linktitle: テーブルを抽出する
type: docs
weight: 20
url: /net/extract-table-from-existing-pdf-document/
description: Aspose.PDF for .NETは、PDFドキュメントに含まれるテーブルに対して様々な操作を行うことができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFドキュメントからテーブルを抽出する",
    "alternativeHeadline": "PDFファイルからテーブルを抽出する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, dotnet, テーブルを抽出する",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-table-from-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-table-from-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETは、PDFドキュメントに含まれるテーブルに対して様々な操作を行うことができます。"
}
</script>
次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## PDFから表を抽出する

```csharp
public static void Extract_Table()
{
    // ソースPDFドキュメントを読み込む
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(@"c:\tmp\the_worlds_cities_in_2018_data_booklet 7.pdf");           
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {
                    TextFragment textfragment = new TextFragment();
                    TextFragmentCollection textFragmentCollection = cell.TextFragments;
                    foreach (TextFragment fragment in textFragmentCollection)
                    {
                        string txt = "";
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            txt += seg.Text;
                        }
                        Console.WriteLine(txt);
                    }
                }
            }
        }
    }
}
```
## 画像としてテーブルの枠を抽出する

ページの境界線はパス描画操作です。したがって、Pdf->Html処理ロジックは描画命令を実行し、テキストの背後に背景を配置します。したがって、ロジックを繰り返すには、コンテンツオペレーターを手動で処理し、グラフィックスを自分で描画する必要があります。また、次のコードスニペットはさまざまなPDFファイルで正確に機能しない場合があることに注意してくださいが、問題が発生した場合は、お気軽にお問い合わせください。このコードは特定のPDFファイル用に開発されました。次のコードスニペットは、PDFドキュメントから画像としてテーブルの境界を抽出する手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document(dataDir + "input.pdf");

Stack graphicsState = new Stack();
System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap((int)doc.Pages[1].PageInfo.Width, (int)doc.Pages[1].PageInfo.Height);
System.Drawing.Drawing2D.GraphicsPath graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
// デフォルトのctm行列値は1,0,0,1,0,0です
System.Drawing.Drawing2D.Matrix lastCTM = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, 0);
// System.Drawingの座標系は左上基準ですが、pdfの座標系は左下基準なので、反転行列を適用する必要があります
System.Drawing.Drawing2D.Matrix inversionMatrix = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, (float)doc.Pages[1].PageInfo.Height);
System.Drawing.PointF lastPoint = new System.Drawing.PointF(0, 0);
System.Drawing.Color fillColor = System.Drawing.Color.FromArgb(0, 0, 0);
System.Drawing.Color strokeColor = System.Drawing.Color.FromArgb(0, 0, 0);

using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bitmap))
{
    gr.SmoothingMode = SmoothingMode.HighQuality;
    graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

    // すべてのコンテンツコマンドを処理します
    foreach (Operator op in doc.Pages[1].Contents)
    {
        Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
        Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
        Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
        Aspose.Pdf.Operators.MoveTo opMoveTo = op as Aspose.Pdf.Operators.MoveTo;
        Aspose.Pdf.Operators.LineTo opLineTo = op as Aspose.Pdf.Operators.LineTo;
        Aspose.Pdf.Operators.Re opRe = op as Aspose.Pdf.Operators.Re;
        Aspose.Pdf.Operators.EndPath opEndPath = op as Aspose.Pdf.Operators.EndPath;
        Aspose.Pdf.Operators.Stroke opStroke = op as Aspose.Pdf.Operators.Stroke;
        Aspose.Pdf.Operators.Fill opFill = op as Aspose.Pdf.Operators.Fill;
        Aspose.Pdf.Operators.EOFill opEOFill = op as Aspose.Pdf.Operators.EOFill;
        Aspose.Pdf.Operators.SetRGBColor opRGBFillColor = op as Aspose.Pdf.Operators.SetRGBColor;
        Aspose.Pdf.Operators.SetRGBColorStroke opRGBStrokeColor = op as Aspose.Pdf.Operators.SetRGBColorStroke;

        if (opSaveState != null)
        {
            // 前の状態を保存し、現在の状態をスタックの先頭にプッシュします
            graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opRestoreState != null)
        {
            // 現在の状態を破棄し、以前の状態を復元します
            graphicsState.Pop();
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opCtm != null)
        {
            System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
                (float)opCtm.Matrix.A,
                (float)opCtm.Matrix.B,
                (float)opCtm.Matrix.C,
                (float)opCtm.Matrix.D,
                (float)opCtm.Matrix.E,
                (float)opCtm.Matrix.F);

            // 現在の行列を状態行列と乗算します
            ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opMoveTo != null)
        {
            lastPoint = new System.Drawing.PointF((float)opMoveTo.X, (float)opMoveTo.Y);
        }
        else if (opLineTo != null)
        {
            System.Drawing.PointF linePoint = new System.Drawing.PointF((float)opLineTo.X, (float)opLineTo.Y);
            graphicsPath.AddLine(lastPoint, linePoint);

            lastPoint = linePoint;
        }
        else if (opRe != null)
        {
            System.Drawing.RectangleF re = new System.Drawing.RectangleF((float)opRe.X, (float)opRe.Y, (float)opRe.Width, (float)opRe.Height);
            graphicsPath.AddRectangle(re);
        }
        else if (opEndPath != null)
        {
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opRGBFillColor != null)
        {
            fillColor = opRGBFillColor.getColor();
        }
        else if (opRGBStrokeColor != null)
        {
            strokeColor = opRGBStrokeColor.getColor();
        }
        else if (opStroke != null)
        {
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.DrawPath(new System.Drawing.Pen(strokeColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opFill != null)
        {
            graphicsPath.FillMode = FillMode.Winding;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opEOFill != null)
        {
            graphicsPath.FillMode = FillMode.Alternate;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
    }
}
dataDir = dataDir + "ExtractBorder_out.png";
bitmap.Save(dataDir, ImageFormat.Png);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

