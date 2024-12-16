---
title: 从PDF文件中提取链接
linktitle: 提取链接
type: docs
weight: 30
url: /zh/java/extract-links/
description: 使用Java从PDF中提取链接。本主题向您解释如何使用AnnotationSelector类提取链接。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文件中提取链接

链接在PDF文件中表示为注释，因此要提取链接，需要提取所有[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation)对象。

1. 创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象。
2. 获取您想要从中提取链接的[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)。
3. 使用[AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector)类从指定页面中提取所有[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)对象。

1. 将 [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) 对象传递给 Page 对象的 Accept 方法。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) 对象的 [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) 方法，将所有选定的链接注释获取到一个 IList 对象中。

以下代码片段向您展示如何从 PDF 文件中提取链接。

```java
    public static void ExtractLinksFromThePDFFile() {        
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("注释位置: " + annot.getRect());
        }
                
        // 保存具有更新链接的文档
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```