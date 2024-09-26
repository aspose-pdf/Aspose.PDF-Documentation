---
title: ASP - JScript를 통한 COM Interop
type: docs
weight: 40
url: /net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

이것은 [Aspose.PDF for .NET](/pdf/net/)과 JScript를 통해 COM Interop을 사용하여 PDF 파일에 간단한 텍스트 문자열을 추가하는 방법을 보여주는 간단한 ASP 애플리케이션입니다.

{{% /alert %}}

예제:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> ASP 클래식 샘플에서 Aspose.PDF for .NET 사용</title>
    </head>
    <body>
        <h3>ASP 클래식과 JScript로 Aspose.PDF for .NET을 사용하여 샘플 PDF 문서 생성</h3>
<%
// 라이선스 설정
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// 빈 생성자 호출로 Pdf 인스턴스 생성
var pdf = Server.CreateObject("Aspose.PDF.Document");

// PDF 객체에서 새 페이지 생성
var pdfpage = pdf.Pages.Add();

// 텍스트 프래그먼트 객체 생성
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// 프래그먼트에 내용 할당
sampleText.Text = "HelloWorld using ASP and JScript";

// 섹션의 단락 컬렉션에 텍스트 단락 추가
pdfpage.Paragraphs.Add(sampleText);

// PDF 문서 저장
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```
{{% /alert %}}
