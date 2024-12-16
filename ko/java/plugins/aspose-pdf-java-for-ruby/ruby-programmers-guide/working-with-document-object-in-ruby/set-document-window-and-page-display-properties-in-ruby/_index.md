---
title: Ruby에서 문서 창 및 페이지 표시 속성 설정
type: docs
weight: 100
url: /ko/java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 문서 창 및 페이지 표시 속성 설정

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서의 문서 창 및 페이지 표시 속성을 설정하려면, 간단히 **SetDocumentWindow** 모듈을 호출하십시오.

루비 코드

```java
# 문서 디렉토리 경로.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 다양한 문서 속성을 설정합니다.

# 문서 창의 위치 - 기본값: false

doc.setCenterWindow(true)

# 주요 읽기 순서; 페이지의 위치를 결정합니다.

# 나란히 표시될 때 - 기본값: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# 창의 제목 표시줄이 문서 제목을 표시할지 여부.

# false인 경우 제목 표시줄은 PDF 파일 이름을 표시합니다 - 기본값: false

doc.setDisplayDocTitle(true)

# 첫 번째 표시된 페이지 크기에 맞게 문서 창 크기를 조정할지 여부 - 기본값: false

doc.setFitWindow(true)

# 뷰어 애플리케이션의 메뉴 바를 숨길지 여부 - 기본값: false

doc.setHideMenubar(true)

# 뷰어 애플리케이션의 도구 바를 숨길지 여부 - 기본값: false

doc.setHideToolBar(true)

# 스크롤 바와 같은 UI 요소를 숨기고 페이지 내용만 표시할지 여부 - 기본값: false

doc.setHideWindowUI(true)

# 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서를 어떻게 표시할지.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# 페이지 레이아웃, 즉 단일 페이지, 한 열.

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# 문서를 열 때 어떻게 표시할지.

doc.setPageMode()

# 업데이트된 PDF 파일 저장

doc.save(data_dir + "Set Document Window.pdf")
```


## 코드 실행 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **문서 창 및 페이지 표시 속성 설정 (Aspose.PDF)**을 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)