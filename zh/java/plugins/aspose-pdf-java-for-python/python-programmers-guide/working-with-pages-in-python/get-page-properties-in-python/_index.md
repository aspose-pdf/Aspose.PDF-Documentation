---
title: 在 Python 中获取页面属性
linktitle: 在 Python 中获取页面属性
type: docs
weight: 50
url: /java/get-page-properties-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中访问 PDF 文档中特定页面的属性以进行详细控制。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 获取 Pdf 文档的页面属性，只需调用 **GetPageProperties** 类即可。

```Python
doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf_document.getPages();

# get particular page
pdf_page = page_collection.get_Item(1);

# get page properties
print "ArtBox : Height = " + pdf_page.getArtBox().getHeight() + ", Width = " + pdf_page.getArtBox().getWidth() + ", LLX = " + pdf_page.getArtBox().getLLX() + ", LLY = " + pdf_page.getArtBox().getLLY() + ", URX = " + pdf_page.getArtBox().getURX() + ", URY = " + pdf_page.getArtBox().getURY()
print "BleedBox : Height = " + pdf_page.getBleedBox().getHeight() + ", Width = " + pdf_page.getBleedBox().getWidth() + ", LLX = " + pdf_page.getBleedBox().getLLX() + ", LLY = " + pdf_page.getBleedBox().getLLY() + ", URX = " + pdf_page.getBleedBox().getURX() + ", URY = " . pdf_page.getBleedBox().getURY()
print "CropBox : Height = " + pdf_page.getCropBox().getHeight() + ", Width = " + pdf_page.getCropBox().getWidth() + ", LLX = " + pdf_page.getCropBox().getLLX() + ", LLY = " + pdf_page.getCropBox().getLLY() + ", URX = " + pdf_page.getCropBox().getURX() + ", URY = " . pdf_page.getCropBox().getURY()
print "MediaBox : Height = " + pdf_page.getMediaBox().getHeight() + ", Width = " + pdf_page.getMediaBox().getWidth() + ", LLX = " + pdf_page.getMediaBox().getLLX() + ", LLY = " + pdf_page.getMediaBox().getLLY() + ", URX = " + pdf_page.getMediaBox().getURX() + ", URY = " . pdf_page.getMediaBox().getURY()
print "TrimBox : Height = " + pdf_page.getTrimBox().getHeight() + ", Width = " + pdf_page.getTrimBox().getWidth() + ", LLX = " + pdf_page.getTrimBox().getLLX() + ", LLY = " + pdf_page.getTrimBox().getLLY() + ", URX = " + pdf_page.getTrimBox().getURX() + ", URY = " . pdf_page.getTrimBox().getURY()
print "Rect : Height = " + pdf_page.getRect().getHeight() + ", Width = " + pdf_page.getRect().getWidth() + ", LLX = " + pdf_page.getRect().getLLX() + ", LLY = " + pdf_page.getRect().getLLY() + ", URX = " + pdf_page.getRect().getURX() + ", URY = " + pdf_page.getRect().getURY()
print "Page Number :- " + pdf_page.getNumber()
print "Rotate :-" + pdf_page.getRotate()

```

**下载运行代码**

从以下任何一个社交编码网站下载**获取页面属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetPageProperties/GetPageProperties.py)
