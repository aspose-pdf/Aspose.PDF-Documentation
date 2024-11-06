---
title: 既存のPDFにTOCを追加する（Python）
type: docs
weight: 20
url: ja/java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントにTOCを追加するには、**AddToc**クラスを呼び出すだけです。

```python

# PDFドキュメントを開きます。
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# PDFファイルの最初のページにアクセスします
toc_page = doc.getPages().insert(1)

# TOC情報を表すオブジェクトを作成します
toc_info = self.TocInfo()
title = self.TextFragment("目次")
title.getTextState().setFontSize(20)

# TOCのタイトルを設定します
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# TOC要素として使用される文字列オブジェクトを作成します
titles = ["最初のページ", "2ページ目"]

i = 0;
while (i < 2):

# Headingオブジェクトを作成します
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Headingオブジェクトの宛先ページを指定します
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# 宛先ページ
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# 宛先座標
segment2.setText(titles[i])

# TOCを含むページにHeadingを追加します
toc_page.getParagraphs().add(heading2)

i +=1;

# PDFドキュメントを保存します
doc.save(self.dataDir + "TOC.pdf")

print "TOCを正常に追加しました。出力ファイルを確認してください。"
```


**コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Add TOC (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)