---
title: Aspose.PDF for .NETをPythonで使用する
linktitle: Pythonとの統合
type: docs
weight: 100
url: /net/python-net/
description: このチュートリアルでは、PythonでPDFファイルを作成および変更するさまざまな方法を探ります。
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

この記事では、Aspose.PDF for .NETとPythonを統合してPDFを作成する方法について短い例を説明します。

## 前提条件

PythonでAspose.PDF for .NETを使用するには、以下の`requirments.txt`を使用してください：

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

また、希望のフォルダに`Aspose.PDF.dll`を配置する必要があります。

## Pythonを使用したシンプルなPDFの作成

作業を進めるために、[PythonNet](https://github.com/pythonnet/pythonnet)をアプリケーションに統合し、いくつかの設定を行う必要があります。

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### シンプルなドキュメントを生成する

シンプルなPDFを、クラシカルなテキスト「Hello, world」を用いて作成しましょう。詳しい説明については、[このページ](https://docs.aspose.com/pdf/net/hello-world-example/)を参照してください。

```python
class HelloWorld(object):
    def __init__(self, licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # ドキュメントオブジェクトを初期化
        document = Document()
        # ページを追加
        page = document.Pages.Add()
        # 新しいページにテキストを追加
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # TextBuilderオブジェクトを作成
        textBuilder = TextBuilder(page)

        # PDFページにテキストフラグメントを追加
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Pythonを使用して複雑なPDFを作成する

次の例は、画像や表を含む複雑なPDFドキュメントを作成する方法を示しています。この例は、[次のページ](https://docs.aspose.com/pdf/net/complex-pdf-example/)に基づいています。

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... 省略 ...

    # 複雑なドキュメントを作成する
    def run_complex(self):

        # ドキュメントオブジェクトを初期化
        document = Document()
        # ページを追加
        page = document.Pages.Add()

        # 画像を追加
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # ヘッダーを追加
        header = TextFragment("2020年秋の新しいフェリールート")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # 説明を追加
        descriptionText = "訪問者はオンラインでチケットを購入する必要があり、チケットは1日に5,000枚に限定されています。\
        フェリーサービスは定員の半分で運行され、スケジュールも縮小されています。列を予想してください。"
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # テーブルを追加
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("出発都市")
        headerRow.Cells.Add("出発島")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## WindowsでPDF生成を実行する方法

このスニペットは、上記の例をWindows PCで実行する方法を示しています。`class HelloWorld`が`example_get_started.py`ファイルに位置していると仮定します。
Aspose.PDF for .NETの試用版を実行する場合、`license_path`として空の文字列を渡す必要があります。

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
