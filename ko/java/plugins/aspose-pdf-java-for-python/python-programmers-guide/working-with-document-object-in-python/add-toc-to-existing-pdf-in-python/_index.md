---
title: Python에서 기존 PDF에 목차 추가
linktitle: Python에서 기존 PDF에 목차 추가
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-python/
description: 간편한 탐색을 위해 Aspose.PDF를 사용하여 Python의 기존 PDF 문서에 목차(TOC)를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서에 목차를 추가하려면 **AddToc** 클래스를 호출하기만 하면 됩니다.


```python

# Open a pdf document.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get access to first page of PDF file
toc_page = doc.getPages().insert(1)

# Create object to represent TOC information
toc_info = self.TocInfo()
title = self.TextFragment("Table Of Contents")
title.getTextState().setFontSize(20)

# Set the title for TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Create string objects which will be used as TOC elements
titles = ["First page", "Second page"]

i = 0;
while (i < 2):

# Create Heading object
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Specify the destination page for heading object
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Destination page
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Destination coordinate
segment2.setText(titles[i])

# Add heading to page containing TOC
toc_page.getParagraphs().add(heading2)

i +=1;

# Save PDF Document
doc.save(self.dataDir + "TOC.pdf")

print "Added TOC Successfully, please check the output file."
```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 В **TOC 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)
