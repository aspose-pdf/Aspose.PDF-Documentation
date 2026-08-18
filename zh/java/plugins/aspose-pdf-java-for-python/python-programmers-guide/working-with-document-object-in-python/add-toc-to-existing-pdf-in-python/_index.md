---
title: 使用 Python 将目录添加到现有 PDF
linktitle: 使用 Python 将目录添加到现有 PDF
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-python/
description: 了解如何使用 Aspose.PDF 将目录 (TOC) 添加到 Python 中的现有 PDF 文档中，以便于导航。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 在 Pdf 文档中添加 TOC，只需调用 **AddToc** 类即可。

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

**下载运行代码**

从以下任何一个社交编码网站下载**添加目录 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)
