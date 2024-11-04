---
title: 从PDF文件到XFDF的扁平化注释（facades）
type: docs
weight: 40
url: /java/flatten-annotation/
description: 本节解释了如何使用Aspose.PDF Facades将注释从PDF文件导出到XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

扁平化过程意味着当注释从文档中移除时，其视觉表示保持不变。扁平化的注释仍然可见，但不再可由您的用户或应用程序编辑。例如，这可以用于永久性地将注释应用于您的文档，或使无法显示注释的查看器仍然可以看到注释。如果未指定，导出将保持所有注释原样。

当选择此选项时，您的注释将作为PDF标准注释包含在导出的PDF中。

查看在下面的代码片段中如何使用[flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--)方法。

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // 设置应用修订
        flattenSettings.setCallEvents(false); // 设置不调用事件
        flattenSettings.setHideButtons(true); // 设置隐藏按钮
        flattenSettings.setUpdateAppearances(true); // 设置更新外观
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```