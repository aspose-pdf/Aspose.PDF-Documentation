---
title: Go를 사용하여 PDF의 배경 색상을 설정합니다
linktitle: 배경 색상 설정
type: docs
weight: 80
url: /ko/go-cpp/set-background-color/
description: Go를 사용하여 PDF 파일의 배경 색상을 설정합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 사용하여 PDF의 배경 색상을 설정합니다
Abstract: Aspose.PDF for Go via C++는 PDF 페이지의 배경 색상을 설정하는 기능을 제공하여 개발자가 문서의 모양을 사용자 지정할 수 있도록 합니다. 이 기능은 페이지 전체 배경에 단색을 적용할 수 있게 하여 문서의 시각적 표현을 향상시킵니다. 개발자는 RGB 또는 CMYK와 같은 표준 색상 모델을 사용하여 색상 값을 쉽게 지정할 수 있습니다. 문서에는 자세한 지침과 코드 샘플이 제공되어 개발자가 C++ 애플리케이션 내에서 배경 색상 사용자 지정을 효과적으로 구현할 수 있도록 돕습니다.
SoftwareApplication: go-cpp
---

1. 제공된 코드 스니펫은 Go에서 Aspose.PDF 라이브러리를 사용하여 PDF 파일의 배경 색상을 설정하는 방법을 보여줍니다.
1. 그 [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) 이 메서드는 지정된 PDF 파일을 메모리로 로드하여, 모양이나 내용 수정과 같은 추가 조작을 가능하게 합니다.
1. 그 [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) 이 메서드는 PDF 문서에 새로운 배경색을 적용합니다. RGB 값은 사용자가 문서의 시각적 스타일을 맞춤 설정할 수 있게 해줍니다.
1. 그 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method는 업데이트된 PDF를 새 이름으로 저장합니다.

이 코드는 브랜드 보고서 생성, 워터마크 추가 또는 여러 문서에 걸친 시각적 일관성 향상과 같이 PDF 맞춤화를 자동화해야 하는 애플리케이션에 이상적입니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```