---
title: PythonでのAspose.PDF for .NETの使用
linktitle: Pythonとの統合
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ja/net/python-net/
description: このチュートリアルでは、PythonでPDFファイルを作成および変更するさまざまな方法を探ります。
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Aspose.PDF for .NET with Python",
    "alternativeHeadline": "Integrate Aspose.PDF for .NET with Python Effortlessly",
    "abstract": "PythonとのAspose.PDF for .NETの強力な統合を発見し、ユーザーが簡単にPDFドキュメントをシームレスに作成および変更できるようにします。この機能は、テキスト、画像、テーブルの追加などの機能を示しながら、Python環境での.NETライブラリの強力な機能を活用して、シンプルおよび複雑なPDFを生成するための簡単な例を提供します。この革新的な統合により、PDFの操作と生成の新しい可能性を効率的に開きます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "681",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/python-net/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/python-net/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

この記事では、Pythonとの統合を使用してPDFを作成する短い例を説明します。

## 前提条件

PythonでAspose.PDF for .NETを使用するには、次の`requirments.txt`を使用してください：

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

また、`Aspose.PDF.dll`を希望のフォルダーに配置する必要があります。

## Pythonを使用したシンプルなPDFの作成

作業するために、[PythonNet](https://github.com/pythonnet/pythonnet)をアプリケーションに統合し、いくつかの設定を行う必要があります。

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```

### シンプルなドキュメントの生成

クラシックなテキスト「Hello, world」を使用してシンプルなPDFを作成しましょう。詳細な説明については、[このページ](https://docs.aspose.com/pdf/net/hello-world-example/)を参照してください。

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Create PDF document
        document = Document()
        # Add page
        page = document.Pages.Add()
        # Add text to new page
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Create TextBuilder object
        textBuilder = TextBuilder(page)

        # Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment)

        # Save PDF document
        document.Save("HelloWorld_out.pdf")
```

## Pythonを使用した複雑なPDFの作成

次の例では、画像とテーブルを含む複雑なPDFドキュメントを作成する方法を示します。この例は、[次のページ](https://docs.aspose.com/pdf/net/complex-pdf-example/)に基づいています。

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... skipped ...

    # Make a Complex Document
    def run_complex(self):

        # Create PDF document
        document = Document()
        # Add page
        page = document.Pages.Add()

        # Add image
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Add Header
        header = TextFragment("New ferry routes in Fall 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Add description
        descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
        Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)

        # Add table
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Departs City")
        headerRow.Cells.Add("Departs Island")

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

        # Save PDF document
        document.Save(self.dataDir + "Complex.pdf")
```

## WindowsでPDF生成を実行する方法

このスニペットは、Windows PCで上記の例を実行する方法を示しています。`class HelloWorld`が`example_get_started.py`ファイルにあると仮定しています。
Aspose.PDF for .NETの試用版を実行する場合は、`license_path`として空の文字列を渡す必要があります。

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```