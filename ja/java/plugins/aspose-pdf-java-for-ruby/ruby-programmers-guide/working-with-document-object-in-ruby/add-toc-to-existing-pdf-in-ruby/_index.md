---
title: "Ruby での 既存のPDFに目次の追加"
linktitle: "Ruby での 既存のPDFに目次の追加"
type: docs
weight: 30
url: /ja/java/add-toc-to-existing-pdf-in-ruby/
description: Aspose.PDF を使用して、Rubyで既存のPDFに目次を追加し、文書のナビゲーションを向上させる方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - 目次の追加

<ins>PDF ドキュメントに TOC を追加するには、**Aspose.PDF Java for Ruby** を使用し、単に **AddToc** モジュールを呼び出します。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get access to first page of PDF file

toc_page = doc.getPages().insert(1)

# Create object to represent TOC information

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Table Of Contents")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Set the title for TOC

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Create string objects which will be used as TOC elements

titles = Array["First page", "Second page"]

i = 0

while i < 2

В В В  # Create Heading object

В В В  heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

В В В  segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

В В В  heading2.setTocPage(toc_page)

В В В  heading2.getSegments().add(segment2)

В В В  # Specify the destination page for heading object

В В В  heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

В В В  # Destination page

В В В  heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

В В В  # Destination coordinate

В В В  segment2.setText(titles[i])

В В В  # Add heading to page containing TOC

В В В  toc_page.getParagraphs().add(heading2)

В В В  i +=1

end

# Save PDF Document

doc.save(data_dir + "TOC.pdf")

puts "Added TOC Successfully, please check the output file."
```

## <ins> **実行コードのダウンロード**

ダウンロードВ **TOC を追加 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)
