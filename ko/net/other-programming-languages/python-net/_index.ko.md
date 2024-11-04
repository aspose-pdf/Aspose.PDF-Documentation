---
title: Aspose.PDF for .NET을 Python과 함께 사용하기
linktitle: Python과의 통합
type: docs
weight: 100
url: /net/python-net/
description: 이 튜토리얼에서는 Python에서 PDF 파일을 생성하고 수정하는 다양한 방법을 탐구합니다.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

이 글은 Aspose.PDF for .NET을 Python과 통합하여 PDF를 생성하는 방법에 대한 간단한 예제를 설명합니다.

## 필수 조건

Python에서 Aspose.PDF for .NET을 사용하려면 다음 `requirments.txt`를 사용하세요:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

또한, 원하는 폴더에 `Aspose.PDF.dll`을 넣어야 합니다.

## Python을 사용하여 간단한 PDF 생성하기

작업을 위해 [PythonNet](https://github.com/pythonnet/pythonnet)을 우리 애플리케이션에 통합하고 몇 가지 설정을 해야 합니다.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### 간단한 문서 생성하기

간단한 PDF를 만들어 "Hello, world"라는 클래식한 텍스트를 넣어봅시다. 자세한 설명은 [이 페이지](https://docs.aspose.com/pdf/net/hello-world-example/)를 참조하세요.

```python
class HelloWorld(object):
    def __init__(self, licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # 문서 객체 초기화
        document = Document()
        # 페이지 추가
        page = document.Pages.Add()
        # 새 페이지에 텍스트 추가
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # TextBuilder 객체 생성
        textBuilder = TextBuilder(page)

        # PDF 페이지에 텍스트 조각을 추가
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Python을 사용하여 복잡한 PDF 생성하기

다음 예제는 이미지와 표가 있는 복잡한 PDF 문서를 생성하는 방법을 보여줍니다. 이 예제는 [다음 페이지](https://docs.aspose.com/pdf/net/complex-pdf-example/)를 기반으로 합니다.

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... 생략 ...

    # 복잡한 문서 만들기
    def run_complex(self):

        # 문서 객체 초기화
        document = Document()
        # 페이지 추가
        page = document.Pages.Add()

        # 이미지 추가
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # 헤더 추가
        header = TextFragment("2020년 가을 새로운 페리 노선")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # 설명 추가
        descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 하루에 5,000장으로 제한됩니다. \
        페리 서비스는 절반의 용량으로 운영되며 일정이 축소되었습니다. 대기열을 예상하세요."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)

        # 표 추가
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("출발 도시")
        headerRow.Cells.Add("출발 섬")

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
## Windows에서 PDF 생성 실행 방법

이 스니펫은 Windows PC에서 위의 예제를 실행하는 방법을 보여줍니다. `class HelloWorld`가 `example_get_started.py` 파일에 위치하고 있다고 가정했습니다.
Aspose.PDF for .NET의 평가판을 실행하는 경우, `license_path`로 빈 문자열을 전달해야 합니다.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
