---
title: 파이썬에서 문서 창 및 페이지 표시 속성 가져오기
type: docs
weight: 30
url: /ko/java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 문서 창 및 페이지 표시 속성을 가져오려면 **GetDocumentWindow** 클래스를 호출하십시오.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 다양한 문서 속성 가져오기
# 문서 창의 위치 - 기본값: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# 주요 읽기 순서; 나란히 표시될 때 페이지의 위치 결정 - 기본값: L2R
print "Direction :- " + str(doc.getDirection())

# 창의 제목 표시줄에 문서 제목을 표시할지 여부.
# false이면 제목 표시줄에 PDF 파일 이름이 표시됨 - 기본값: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# 문서 창의 크기를 첫 번째 표시된 페이지의 크기에 맞추어 조정할지 여부 - 기본값: false
print "FitWindow :- " + str(doc.getFitWindow())

# 뷰어 애플리케이션의 메뉴 막대를 숨길지 여부 - 기본값: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# 뷰어 애플리케이션의 도구 막대를 숨길지 여부 - 기본값: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# 스크롤 막대와 같은 UI 요소를 숨기고 페이지 내용만 표시할지 여부 - 기본값: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서를 표시하는 방법.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# 페이지 레이아웃, 즉 단일 페이지, 한 열
print "PageLayout :-" + str(doc.getPageLayout())

# 문서를 열 때 표시되는 방법.
print "pageMode :-" + str(doc.getPageMode())
```


**실행 코드 다운로드**

**문서 창 및 페이지 표시 속성 가져오기 (Aspose.PDF)**를 아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)