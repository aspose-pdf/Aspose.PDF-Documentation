---
title: PDF에서 글꼴 추출 C#
linktitle: PDF에서 글꼴 추출
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
description: Aspose.PDF for. NET 라이브러리를 사용하여 PDF 문서에서 모든 내장 글꼴을 추출하세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서에서 모든 글꼴을 가져오고 싶다면, Document 클래스에서 제공하는 FontUtilities.GetAllFonts() 메소드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 글꼴을 가져오기 위해 다음 코드 스니펫을 확인하세요:

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

