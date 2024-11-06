---
title: PDFファイルからリンクを抽出する
linktitle: リンクの抽出
type: docs
weight: 30
url: ja/java/extract-links/
description: JavaでPDFからリンクを抽出します。このトピックでは、AnnotationSelectorクラスを使用してリンクを抽出する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルからリンクを抽出する

リンクはPDFファイル内で注釈として表現されるため、リンクを抽出するには、すべての[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation)オブジェクトを抽出します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトを作成します。
1. リンクを抽出したい[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)を取得します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector)クラスを使用して、指定されたページからすべての[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)オブジェクトを抽出します。

1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) オブジェクトを Page オブジェクトの Accept メソッドに渡します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) オブジェクトの [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) メソッドを使用して、選択されたすべてのリンク注釈を IList オブジェクトに取得します。

次のコードスニペットは、PDF ファイルからリンクを抽出する方法を示しています。

```java
    public static void ExtractLinksFromThePDFFile() {        
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("注釈の位置: " + annot.getRect());
        }
                
        // 更新されたリンクを持つ文書を保存する
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```