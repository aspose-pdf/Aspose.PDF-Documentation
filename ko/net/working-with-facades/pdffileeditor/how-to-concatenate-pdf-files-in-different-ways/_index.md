---
title: .NET 5를 사용하여 PDF 파일 병합하기
linktitle: PDF 병합하는 방법
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /ko/net/how-to-concatenate-pdf-files-in-different-ways/
description: 이 문서에서는 기존 PDF 파일을 단일 PDF 파일로 연결하는 가능한 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "Aspose.PDF for .NET의 새로운 기능을 통해 여러 PDF 파일을 단일 문서로 원활하게 병합할 수 있습니다. 이 기능은 개발자가 간단한 메서드 호출을 통해 원하는 만큼의 PDF를 연결할 수 있게 하여 PDF 관리 및 조작의 생산성을 향상시킵니다. 다양한 요구에 맞춘 다재다능한 접근 방식을 통해 ASP.NET 및 Windows 애플리케이션을 포함한 다양한 .NET 애플리케이션에 이 기능을 손쉽게 통합할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
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
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

이 문서에서는 [Aspose.PDF for .NET](/pdf/ko/net/) 구성 요소의 도움으로 여러 PDF 문서를 단일 PDF 문서로 [연결하는 방법](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)을 설명합니다. [Aspose.PDF for .NET](/pdf/ko/net/)는 이 작업을 매우 쉽게 만들어 줍니다.

{{% /alert %}}

해야 할 일은 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Concatenate](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드를 호출하는 것입니다. 그러면 모든 입력 PDF 파일이 함께 연결되고 단일 PDF 파일이 생성됩니다. PDF 파일 연결을 연습하기 위해 애플리케이션을 만들어 보겠습니다. Visual Studio.NET 2019를 사용하여 애플리케이션을 만들 것입니다.

{{% alert color="primary" %}}

Aspose.PDF for .NET는 ASP.NET 웹 애플리케이션이든 Windows 애플리케이션이든 .NET Framework에서 실행되는 모든 종류의 애플리케이션에서 사용할 수 있습니다.

{{% /alert %}}

## 다양한 방법으로 PDF 파일 연결하기

폼에는 PDF 파일을 탐색하기 위한 세 개의 텍스트 박스(textBox1, textBox2, textBox3)와 각각의 링크 레이블(linkLabel1, linkLabel2, linkLabel3)이 있습니다. "찾아보기" 링크 레이블을 클릭하면 PDF 파일(연결할 파일)을 선택할 수 있는 입력 파일 대화 상자(inputFileDialog1)가 나타납니다.

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

PDF 파일 연결을 위한 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스의 시연을 위해 Windows 폼 애플리케이션의 뷰가 표시됩니다.

![PDF 파일 연결하기](how-to-concatenate-pdf-files-in-different-ways_1.png)

PDF 파일을 선택하고 확인 버튼을 클릭하면 관련 텍스트 박스에 전체 파일 이름과 경로가 할당됩니다.

![PDF 파일 선택하기](how-to-concatenate-pdf-files-in-different-ways_2.png)

마찬가지로 아래와 같이 두 개 또는 세 개의 입력 PDF 파일을 선택할 수 있습니다:

![두 개 또는 세 개의 입력 PDF 파일 선택하기](how-to-concatenate-pdf-files-in-different-ways_3.png)

마지막 텍스트 박스(textBox4)는 출력 PDF 파일의 이름과 함께 생성될 위치 경로를 입력받습니다.

![출력 PDF 파일의 위치 경로](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate 메서드](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate() 메서드

Concatenate() 메서드는 세 가지 방법으로 사용할 수 있습니다. 각 방법을 자세히 살펴보겠습니다:

### 접근법 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

이 접근법은 두 개의 PDF 파일만 연결해야 할 경우에 적합합니다. 첫 번째 두 인수(firstInputFile 및 secInputFile)는 연결할 두 개의 입력 PDF 파일의 전체 파일 이름과 저장 경로를 제공합니다. 세 번째 인수(outputFile)는 출력 PDF 파일의 원하는 파일 이름과 경로를 제공합니다.

![파일 이름을 사용하여 두 개의 PDF 연결하기](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### 접근법 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

위의 접근법과 유사하게, 이 접근법도 두 개의 PDF 파일을 연결할 수 있습니다. 첫 번째 두 인수(firstInputStream 및 secInputStream)는 연결할 두 개의 입력 PDF 파일을 스트림(스트림은 비트/바이트의 배열)으로 제공합니다. 세 번째 인수(outputStream)는 원하는 출력 PDF 파일의 스트림 표현을 제공합니다.

![파일 스트림을 사용하여 두 개의 PDF 연결하기](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### 접근법 3

- Concatenate(Stream inputStreams[], Stream outputStream)

두 개 이상의 PDF 파일을 연결하려면 이 접근법이 최선의 선택입니다. 첫 번째 인수(inputStreams[])는 연결할 입력 PDF 파일을 스트림 배열의 형태로 제공합니다. 두 번째 인수(outputStream)는 원하는 출력 PDF 파일의 스트림 표현을 제공합니다.

![스트림 배열을 사용하여 여러 PDF 연결하기](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```