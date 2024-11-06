---
title: ASP - VBScript를 통한 COM Interop
type: docs
weight: 30
url: ko/net/asp-vbscript-via-com-interop/
---

## Prerequisites

{{% alert color="primary" %}}

    .NET을 통해 Aspose.pdf를 사용하는 방법에 대한 글을 확인해 주세요.

{{% /alert %}}

## Hello World! VB Script 예제

{{% alert color="primary" %}}

이것은 [Aspose.PDF for .NET](/pdf/net/)과 VBScript를 통한 COM Interop을 사용하여 샘플 텍스트가 포함된 PDF 파일을 생성하는 방법을 보여주는 간단한 ASP 애플리케이션입니다.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title>클래식 ASP 샘플에서 Aspose.PDF for .NET 사용</title>
    </head>
<body>

<h3>클래식 ASP와 VBScript를 사용하여 Aspose.PDF for .NET으로 샘플 PDF 문서 생성</h3>

<%

'라이센스 설정
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'빈 생성자를 호출하여 Pdf 인스턴스 생성
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Pdf 객체에 새로운 섹션 생성
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'섹션을 Pdf 객체에 추가
pdf.Sections.Add(pdfsection)

'텍스트 객체 생성
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'텍스트 객체에 텍스트 세그먼트 추가
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'세그먼트에 일부 내용 할당
seg1.Content = "ASP와 VBScript를 사용한 HelloWorld"

'단락에 세그먼트 추가 (빨간 텍스트 색상으로)
SampleText.Segments.Add(seg1)

'섹션의 단락 컬렉션에 텍스트 단락 추가
pdfsection.Paragraphs.Add(SampleText)

'PDF 문서 저장
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## VBScript를 사용하여 텍스트 추출

{{% alert color="primary" %}}
    이 VBScript 샘플은 COM Interop을 통해 기존 PDF 문서에서 텍스트를 추출합니다.
    매크로 'code'의 오류 렌더링 : lang 매개변수에 대해 지정된 값이 잘못되었습니다.
{{% /alert %}}
