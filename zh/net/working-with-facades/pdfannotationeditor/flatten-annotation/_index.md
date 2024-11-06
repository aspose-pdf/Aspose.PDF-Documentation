---
title: 从PDF到XFDF的扁平化注释
type: docs
weight: 40
url: zh/net/flatten-annotation/
description: 本节解释如何使用Aspose.PDF Facades将PDF文件中的注释导出为XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

扁平化过程意味着当注释从文档中移除时，其可视表示保持不变。扁平化的注释仍然可见，但不再可由用户或应用程序编辑。例如，这可以用于将注释永久应用于文档或使无法显示注释的查看器能看到注释。如果未指定，导出将保留所有注释。

选择此选项时，您的注释将作为PDF标准注释包含在导出的PDF中。

查看下一个代码片段中如何使用 [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) 方法。

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```