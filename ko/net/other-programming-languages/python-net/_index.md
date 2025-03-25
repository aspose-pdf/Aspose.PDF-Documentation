---
title: Python에서 Aspose.PDF for .NET 사용하기
linktitle: Python과의 통합
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ko/net/python-net/
description: 이 튜토리얼에서는 Python에서 PDF 파일을 생성하고 수정하는 다양한 방법을 탐색합니다.
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
    "abstract": "Python과의 Aspose.PDF for .NET의 강력한 통합을 발견하여 사용자가 PDF 문서를 쉽게 생성하고 수정할 수 있도록 합니다. 이 기능은 텍스트, 이미지 및 테이블 추가와 같은 기능을 보여주며, Python 환경에서 .NET 라이브러리의 강력한 기능을 활용하여 간단하고 복잡한 PDF를 생성하기 위한 직관적인 예제를 제공합니다. 이 혁신적인 통합을 통해 PDF 조작 및 생성을 효율적으로 위한 새로운 가능성을 열어보세요.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

이 문서에서는 Python과의 통합을 통해 PDF를 생성하는 방법에 대한 짧은 예제를 설명합니다.

## 전제 조건

Python에서 Aspose.PDF for .NET을 사용하려면 다음 `requirments.txt`를 사용하세요:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

또한, 원하는 폴더에 `Aspose.PDF.dll`을 넣어야 합니다.

## Python을 사용하여 간단한 PDF 생성하기

작업을 위해 [PythonNet](https://github.com/pythonnet/pythonnet)을 애플리케이션에 통합하고 몇 가지 설정을 해야 합니다.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```

### 간단한 문서 생성

클래식 텍스트 "Hello, world"로 간단한 PDF를 만들어 보겠습니다. 더 자세한 설명은 [이 페이지](https://docs.aspose.com/pdf/net/hello-world-example/)를 참조하세요.

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

## Python을 사용하여 복잡한 PDF 생성하기

다음 예제는 이미지와 테이블이 포함된 복잡한 PDF 문서를 생성하는 방법을 보여줍니다. 이 예제는 [다음 페이지](https://docs.aspose.com/pdf/net/complex-pdf-example/)를 기반으로 합니다.

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

## Windows에서 PDF 생성 실행하기

이 코드 조각은 Windows PC에서 위의 예제를 실행하는 방법을 보여줍니다. `class HelloWorld`가 `example_get_started.py` 파일에 위치한다고 가정했습니다.
Aspose.PDF for .NET의 평가판 버전을 실행하는 경우 `license_path`에 빈 문자열을 전달해야 합니다.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```