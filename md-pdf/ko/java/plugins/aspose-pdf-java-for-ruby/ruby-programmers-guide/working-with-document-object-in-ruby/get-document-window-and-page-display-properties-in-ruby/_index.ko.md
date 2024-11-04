---
title: 루비에서 문서 창 및 페이지 표시 속성 가져오기
type: docs
weight: 40
url: /java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 문서 창 및 페이지 표시 속성 가져오기

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 문서 창 및 페이지 표시 속성을 가져오려면, **GetDocumentWindow** 모듈을 호출하세요.

루비 코드

```java
# 문서 디렉토리 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 다양한 문서 속성을 가져옵니다.

# 문서 창의 위치 - 기본값: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# 주 독서 방향; 페이지의 위치를 결정합니다

# 나란히 표시될 때 - 기본값: L2R

puts "Direction :- " + doc.getDirection().to_s

# 창의 제목 표시줄에 문서 제목을 표시할지 여부.

# false일 경우, 제목 표시줄에 PDF 파일 이름이 표시됩니다 - 기본값: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# 첫 번째 표시된 페이지의 크기에 맞게 문서 창의 크기를 조정할지 여부 - 기본값: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# 뷰어 응용 프로그램의 메뉴 바를 숨길지 여부 - 기본값: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# 뷰어 응용 프로그램의 도구 모음을 숨길지 여부 - 기본값: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# 스크롤 바와 같은 UI 요소를 숨기고

# 페이지 콘텐츠만 표시할지 여부 - 기본값: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# 문서의 페이지 모드입니다. 전체 화면 모드를 종료할 때 문서를 어떻게 표시할지.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# 페이지 레이아웃, 예: 단일 페이지, 한 열

puts "PageLayout :-" + doc.getPageLayout().to_s

# 문서를 열 때 어떻게 표시할지.

puts "pageMode :-" + doc.getPageMode().to_s
```


## 코드 실행 다운로드

**문서 창 및 페이지 표시 속성 가져오기 (Aspose.PDF)**를 아래의 소셜 코딩 사이트 중 하나에서 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)