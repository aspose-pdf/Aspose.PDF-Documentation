---
title: Python에서 DOM을 사용하여 HTML 문자열 추가
linktitle: Python에서 DOM을 사용하여 HTML 문자열 추가
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: PDF 파일 형식 라이브러리와 함께 Python을 사용하여 DOM에 HTML 문자열을 추가하는 방법을 설명합니다.
---
## 
Python을 사용하여 PDF DOM에 HTML 문자열 추가



**Aspose.PDF Java for Python**을 사용하여 PDF 문서에 HTML 문자열을 추가하려면 **AddHtml** 모듈을 호출하기만 하면 됩니다.

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 HTML(Aspose.PDF) 추가**를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
