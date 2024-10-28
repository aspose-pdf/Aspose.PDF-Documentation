---
title: WebForms DataGridView를 PDF로 렌더링
linktitle: WebForms DataGridView를 PDF로 렌더링
type: docs
weight: 20
url: /net/render-webforms-datagridview-to-pdf/
description: 이 예제는 Aspose.PDF 라이브러리를 사용하여 WebForm을 PDF로 렌더링하는 방법을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF/Aspose.HTML을 사용하여 WebForm을 PDF로 내보내는 방법

### 소개

일반적으로 WebForm을 PDF 문서로 변환하기 위해 추가 도구가 필요합니다. 이 예제는 Aspose.PDF 라이브러리를 사용하여 WebForm을 PDF로 렌더링하는 방법을 보여줍니다. 이 예제에는 _GridView 컨트롤을 PDF 문서로 렌더링하는 방법을 보여주는 Aspose Export GridView To Pdf Control도 포함되어 있습니다._

## WebForm을 PDF로 렌더링하는 방법

WebForm을 PDF로 렌더링하기 위한 원래 아이디어는 [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)에서 상속받은 헬퍼 클래스를 생성하고, Render 메소드를 오버라이딩하는 것입니다.

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // PDF 문서를 위한 웹 페이지 렌더링
    }
    else
    {
        // 브라우저에서 웹 페이지 렌더링
        base.Render(writer);
    }
}
```
HTML을 PDF로 렌더링하는 데 사용할 수 있는 Aspose 도구는 두 가지가 있습니다:

- Aspose.PDF for .NET
- Aspose Export GridView 컨트롤 (Aspose.PDF 기반)

## 소스 파일

이 샘플에는 2개의 데모 보고서가 있습니다.

- _Default.aspx_ 는 Aspose.PDF를 사용하여 PDF로 내보내기를 보여줍니다.
- _Report2.aspx_ 는 Aspose Export GridView 컨트롤을 사용하여 PDF로 내보내기를 보여줍니다. (Aspose.PDF 기반)

## 추가 파일

`Helpers\PdfPage.cs` - Aspose.PDF API 사용 방법을 보여주는 헬퍼 클래스를 포함하고 있습니다.

Aspose.Pdf.GridViewExport 프로젝트는 `Report2.aspx`에서 GridView 컨트롤을 확장하여 보여줍니다.
