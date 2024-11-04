---
title: 更新 PDF 中的链接
linktitle: 更新链接
type: docs
weight: 20
url: /java/update-links/
description: 以编程方式更新 PDF 中的链接。本指南介绍如何在 Java 语言中更新 PDF 中的链接。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 更新 PDF 文件中的链接

如在 PDF 文件中添加超链接中所述，[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 类可以在 PDF 文件中添加链接。还有一个类似的类用于从 PDF 文件内部获取现有链接。如果需要更新现有链接，请使用此方法。要更新现有链接：

1. 加载一个 PDF 文件。
1. 转到 PDF 文件中的特定页面。
1. 使用 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction) 对象的 Destination 属性指定链接目标。

1. 目标页面是使用 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) 构造函数指定的。

### 将链接目标设置为同一文档中的页面

以下代码片段向您展示了如何更新 PDF 文件中的链接，并将其目标设置为文档的第二页。

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // 从文档的第一页获取第一个链接注释
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // 修改链接：更改链接目标
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // 指定链接对象的目标
        // 表示显示页面与坐标 (left, top) 定位在窗口左上角的显式目标，
        // 并且页面内容按缩放因子放大。
        // 第一个参数是目标页码。
        // 第二个是左坐标
        // 第三个是顶部坐标
        // 第四个参数是在显示相应页面时的缩放因子。使用 2 表示页面将以 200% 缩放显示
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // 保存带有更新链接的文档
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### 设置链接目标为网页地址

要更新超链接以指向网页地址，需实例化 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) 对象，并将其传递给 LinkAnnotation 的 Action 属性。以下代码片段展示了如何在 PDF 文件中更新链接并将其目标设置为网页地址。

```java
    public static void SetLinkDestinationToWebAddress() {        
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // 从文档的第一页获取第一个链接注释
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // 修改链接：更改链接动作并将目标设置为网页地址
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // 保存带有更新链接的文档
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### 将链接目标设置为另一个 PDF 文件

以下代码片段展示了如何在 PDF 文件中更新链接并将其目标设置为另一个 PDF 文件。

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // 下一行更新目标，不更新文件
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // 下一行更新文件
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // 保存带有更新链接的文档
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### 更新 LinkAnnotation 文本颜色

链接注释不包含文本。
 相反，文本被放置在标注下的页面内容中。因此，要更改文本的颜色，请替换页面文本的颜色，而不是尝试更改标注的颜色。以下代码片段显示了如何更新PDF文件中链接标注的颜色。

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // 加载PDF文件
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // 搜索标注下的文本
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // 更改文本颜色。
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // 保存更新了链接的文档
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```