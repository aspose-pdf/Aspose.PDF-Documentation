```
---
title: 删除注释（外观）
type: docs
weight: 10
url: /net/delete-annotations/
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfAnnotationEditor 类删除注释。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从现有 PDF 文件中删除所有注释

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 允许您删除现有 PDF 文件中的所有注释。
``` 首先，创建一个 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，调用 [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) 方法删除文件中的所有注释，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段展示了如何从 PDF 文件中删除所有注释。

```csharp
   public static void DeleteAllAnnotations()
        {
            // 打开文档
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // 删除所有注释
            annotationEditor.DeleteAnnotations();
            // 保存更新后的 PDF
        }   
```
## 删除指定类型的所有注释

您可以使用 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 类，从现有的 PDF 文件中删除指定类型的所有注释。 为了做到这一点，您需要创建一个[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor)对象，并使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)方法绑定输入的PDF文件。之后，调用[DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations)方法，并使用字符串参数，从文件中删除所有注释；字符串参数表示要删除的注释类型。最后，使用[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)方法保存更新后的PDF文件。以下代码片段向您展示了如何按指定的注释类型删除所有注释。

```csharp
    public static void DeleteAnnotation()
        {
            // 打开文档
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("请输入编号:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // 保存更新后的PDF
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```