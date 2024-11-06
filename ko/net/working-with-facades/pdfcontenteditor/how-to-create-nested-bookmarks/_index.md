---
title: PDF 파일에 북마크 추가하기
type: docs
weight: 20
url: ko/net/how-to-create-nested-bookmarks/
description: 이 섹션은 PdfContentEditor 클래스를 사용하여 중첩 북마크를 만드는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

북마크를 사용하면 PDF 문서 내 특정 페이지를 추적하거나 링크할 수 있습니다. [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)의 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) 클래스는 기존 PDF 파일 내에서 주어진 페이지 또는 모든 페이지에 정교하면서도 직관적인 방식으로 자신의 북마크를 생성할 수 있는 기능을 제공합니다.

## 구현 세부사항

단순한 북마크 생성 외에도, 때때로 개별 북마크를 챕터 북마크 안에 중첩시켜 챕터의 + 기호를 클릭하면 북마크가 확장되면서 내부의 페이지를 볼 수 있도록 챕터 형태로 북마크를 생성해야 할 때가 있습니다. 아래 그림과 같이 말입니다.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("북마크 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // 결과 PDF를 파일로 저장
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```