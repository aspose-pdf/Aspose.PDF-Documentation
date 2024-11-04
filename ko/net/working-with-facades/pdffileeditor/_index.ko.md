---
title: PdfFileEditor 클래스
type: docs
weight: 10
url: /net/pdffileeditor-class/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades와 작업하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서 작업에는 다양한 기능이 포함됩니다. PDF 파일의 페이지를 관리하는 것은 이 작업의 중요한 부분입니다. Aspose.PDF.Facaded는 이 목적을 위해 `PdfFileEditor` 클래스를 제공합니다.

PdfFileEditor 클래스에는 개별 페이지를 조작하는 데 도움이 되는 메서드가 포함되어 있으며, 이 클래스는 페이지의 내용을 편집하거나 조작하지 않습니다. 새 페이지를 삽입하거나 기존 페이지를 삭제하고 페이지를 분할하거나 PdfFileEditor를 사용하여 페이지의 배치를 지정할 수 있습니다.

이 클래스에서 제공하는 기능은 파일 편집, PDF 배치 및 분할의 세 가지 주요 카테고리로 나눌 수 있습니다. 아래에서 이 섹션들을 자세히 논의할 것입니다:

## 파일 편집

이 섹션에 포함할 수 있는 기능은 삽입, 추가, 삭제, 연결 및 추출입니다. 새 페이지를 지정된 위치에 삽입하려면 Insert 메서드를 사용하거나, 파일의 끝에 페이지를 추가할 수 있습니다. 또한, 삭제할 페이지 번호를 포함하는 정수 배열을 지정하여 Delete 메서드를 사용하여 파일에서 원하는 수의 페이지를 삭제할 수 있습니다. Concatenate 메서드는 여러 PDF 파일에서 페이지를 결합하는 데 도움이 됩니다. Extract 메서드를 사용하여 원하는 수의 페이지를 추출하고, 이 페이지들을 다른 PDF 파일이나 메모리 스트림에 저장할 수 있습니다.

이 섹션에서는 이 클래스의 기능을 탐구하고, 그 메서드의 목적을 설명합니다.

- [PDF 문서 결합](/pdf/net/concatenate-pdf-documents/)
- [PDF 페이지 추출](/pdf/net/extract-pdf-pages/)
- [PDF 페이지 삽입](/pdf/net/insert-pdf-pages/)
- [PDF 페이지 삭제](/pdf/net/delete-pdf-pages/)

## 페이지 나누기 사용

페이지 나누기는 문서의 흐름을 재조정할 수 있는 특별한 기능입니다.

- [기존 PDF의 페이지 나누기](/pdf/net/page-break-in-existing-pdf/)

## PDF 배치

배치란 인쇄 전에 페이지를 올바르게 배열하는 과정입니다. `PdfFileEditor`는 이 목적을 위해 두 가지 메소드를 제공합니다. 즉, `MakeBooklet`과 `MakeNUp`입니다. MakeBooklet 메소드는 페이지를 정리하여 인쇄 후 접거나 제본하기 쉽게 도와주며, MakeNUp 메소드는 PDF 파일의 한 페이지에 여러 페이지를 인쇄할 수 있도록 합니다.

- [PDF의 소책자 만들기](/pdf/net/make-booklet-of-pdf/)
- [PDF 파일의 NUp 만들기](/pdf/net/make-nup-of-pdf-files/)

## 분할

분할 기능을 사용하면 기존 PDF 파일을 여러 부분으로 나눌 수 있습니다. PDF 파일의 앞부분이나 뒷부분을 분할할 수 있습니다. PdfFileEditor는 분할을 위한 다양한 방법을 제공하므로 파일을 개별 페이지나 여러 페이지 세트로 분할할 수도 있습니다.

- [PDF 페이지 분할](/pdf/net/split-pdf-pages/)