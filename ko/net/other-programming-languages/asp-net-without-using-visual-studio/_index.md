---
title: ASP.NET을 비주얼 스튜디오 없이 사용하기
type: docs
weight: 60
url: /ko/net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/ko/net/)을 사용하여 비주얼 스튜디오 없이 ASP.NET 페이지나 애플리케이션을 개발할 수 있습니다. 이 예제에서는 HTML과 C# 또는 VB.NET 코드를 하나의 .aspx 파일에 작성하는 방법을 소개합니다. 이 방법은 일반적으로 인스턴트 ASP.NET으로 알려져 있습니다.

{{% /alert %}}

## 구현 세부사항

{{% alert color="primary" %}}

샘플 웹 애플리케이션을 만들고 Aspose.PDF.dll을 웹사이트 디렉토리의 "Bin"이라는 디렉토리에 복사하세요 (*bin 폴더가 없다면 생성하세요*). 그런 다음 .aspx 페이지를 생성하고 다음 코드를 복사하세요.
이 예제는 [Aspose.PDF for .NET](/pdf/ko/net/)을 ASP.NET 페이지의 인라인 코드와 함께 사용하여 간단한 PDF 문서를 생성하는 방법을 보여줍니다.

{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title>Aspose.PDF for .NET을 사용한 인라인 ASP.NET</title>
    </head>
    <body>
        <h3>Aspose.PDF for .NET을 사용한 간단한 PDF 문서 생성</h3>
<%
    // 라이센스 설정
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // 문서 객체 초기화
    Document document = new Document();
    // 페이지 추가
    Page page = document.Pages.Add();
    // 새 페이지에 텍스트 추가
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
    // 업데이트된 PDF 저장
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```

