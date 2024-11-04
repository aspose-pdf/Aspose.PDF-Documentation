---
title: .NET 5를 사용하여 PDF 파일 병합
linktitle: PDF 병합하는 방법
type: docs
weight: 75
url: /net/how-to-concatenate-pdf-files-in-different-ways/
description: 이 문서는 기존의 여러 PDF 파일을 하나의 PDF 파일로 연결하는 가능한 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

이 문서는 [Aspose.PDF for .NET](/pdf/net/) 컴포넌트를 사용하여 여러 PDF 문서를 하나의 PDF 문서로 [연결](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)하는 방법을 설명합니다. [Aspose.PDF for .NET](/pdf/net/)은 이 작업을 매우 쉽게 만들어 줍니다.

{{% /alert %}}

당신이 해야 할 일은 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드를 호출하는 것뿐이며, 모든 입력 PDF 파일이 함께 연결되고 하나의 PDF 파일이 생성됩니다. 응용 프로그램을 만들어 PDF 파일 연결을 연습해 보겠습니다. 우리는 Visual Studio.NET 2019를 사용하여 응용 프로그램을 만들 것입니다.

{{% alert color="primary" %}}

Aspose.PDF for .NET은 .NET Framework에서 실행되는 모든 종류의 응용 프로그램에서 사용할 수 있습니다. 그것이 ASP.NET 웹 응용 프로그램이든 Windows 응용 프로그램이든 상관없이 사용할 수 있습니다.

{{% /alert %}}

## 다양한 방법으로 PDF 파일 연결하기

양식에는 각각 PDF 파일을 탐색하기 위한 링크 레이블(linkLabel1, linkLabel2, linkLabel3)을 가진 세 개의 텍스트 상자(textBox1, textBox2, textBox3)가 있습니다. "탐색" 링크 레이블을 클릭하면 입력 파일 대화 상자(inputFileDialog1)가 나타나서 PDF 파일(연결할 파일)을 선택할 수 있게 됩니다.

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

PDF 파일 연결을 위한 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 데모를 위한 윈도우 폼 응용 프로그램의 뷰가 표시됩니다.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

PDF 파일을 선택하고 확인 버튼을 클릭하면, 경로와 함께 전체 파일 이름이 관련 텍스트 박스에 할당됩니다.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

마찬가지로, 아래와 같이 두 개 또는 세 개의 입력 PDF 파일을 선택하여 연결할 수 있습니다:

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

마지막 텍스트 박스(textBox4)는 출력 PDF 파일이 생성될 이름과 함께 출력 파일의 대상 경로를 가져옵니다.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate() 메소드

Concatenate() 메소드는 세 가지 방법으로 사용할 수 있습니다. 각 방법을 자세히 살펴보겠습니다:

### 접근 방법 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

이 접근 방법은 두 개의 PDF 파일만 연결해야 할 때 적합합니다. 첫 번째 두 인수 (firstInputFile 및 secInputFile)는 연결할 두 입력 PDF 파일의 저장 경로와 함께 전체 파일 이름을 제공합니다. 세 번째 인수 (outputFile)는 출력 PDF 파일의 원하는 파일 이름과 경로를 제공합니다.

![파일 이름을 사용하여 두 개의 PDF 연결](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### 접근 방식 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

위의 접근 방식과 유사하게 이 접근 방식도 두 개의 PDF 파일을 결합할 수 있습니다. ```
첫 번째 두 인수(firstInputStream 및 secInputStream)는 연결할 두 개의 입력 PDF 파일을 스트림(스트림은 비트/바이트의 배열)으로 제공합니다. 세 번째 인수(outputStream)는 원하는 출력 PDF 파일의 스트림 표현을 제공합니다.
```

![Concatenate two PDFs using File Streams](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdf1,pdf2,outputPDF);
  outputPDF.Close();
}
```

### 접근 방식 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

두 개 이상의 PDF 파일을 연결하려는 경우 이 접근 방식이 최종 선택이 될 것입니다. 첫 번째 인수 (inputStreams[])는 연결할 PDF 파일을 스트림 배열의 형태로 제공합니다. 두 번째 인수 (outputStream)는 원하는 출력 PDF 파일의 스트림 표현을 제공합니다.

![여러 PDF를 스트림 배열을 사용하여 연결](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream pdf3 = new FileStream(textBox3.Text,FileMode.Open);
  Stream[] pdfStreams = new Stream[]{pdf1,pdf2,pdf3};
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdfStreams,outputPDF);
  outputPDF.Close();
}
```