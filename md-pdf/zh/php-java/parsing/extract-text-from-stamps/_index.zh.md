---
title: 从印章中提取文本
type: docs
weight: 60
url: /php-java/extract-text-from-stamps/
---

## 从印章注释中提取文本

Aspose.PDF for PHP via Java 允许您从印章注释中提取文本。为了从 PDF 的印章注释中提取文本，可以使用以下步骤。

1. 加载 PDF 文档
1. 获取文档的所需页面
1. 创建 StampAnnotation 类的新实例
1. 创建 AnnotationSelector 类的新实例并传递印章注释给它
1. 在页面上接受注释选择器
1. 获取选定的印章注释
1. 创建 TextAbsorber 类的新实例
1. 获取第一个印章注释
1. 获取印章注释的正常外观
1. 使用文本吸收器访问外观
1. 从文本吸收器中获取提取的文本
1. 关闭文档

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```