---
title: 从印章提取文本
type: docs
weight: 60
url: /java/extract-text-from-stamps/
---

## 从印章注释中提取文本

Aspose.PDF for Java 允许您从印章注释中提取文本。为了从 PDF 中的印章注释中提取文本，可以使用以下步骤。

1. 创建一个 Document 类对象
1. 从页面的注释列表中获取所需的注释
1. 定义一个新的 TextAbsorber 类对象
1. 使用 TextAbsorber 的 visit 方法获取文本

```java
Document doc = new Document(dataDir+"test.pdf");
Annotation item = doc.getPages().get_Item(1).getAnnotations().get_Item(3);
if (item instanceof StampAnnotation ) {
   StampAnnotation annot = (StampAnnotation) item;
   TextAbsorber ta = new TextAbsorber();
   XForm ap = annot.getNormalAppearance();
   ta.visit(ap);
   System.out.println(ta.getText());
}
```