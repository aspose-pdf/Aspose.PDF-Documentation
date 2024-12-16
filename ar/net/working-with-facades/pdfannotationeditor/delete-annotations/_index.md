---
title: حذف التعليقات التوضيحية (الواجهات)
type: docs
weight: 10
url: /ar/net/delete-annotations/
description: يشرح هذا القسم كيفية حذف التعليقات التوضيحية باستخدام Aspose.PDF Facades باستخدام فئة PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## حذف جميع التعليقات التوضيحية من ملف PDF موجود

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) يسمح لك بحذف جميع التعليقات التوضيحية من ملف PDF الموجود. 
أولاً، قم بإنشاء كائن [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) واربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، قم باستدعاء طريقة [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) لحذف جميع التعليقات التوضيحية من الملف، ثم استخدم طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لحفظ ملف PDF المحدث. يوضح لك مقطع الشيفرة التالي كيفية حذف جميع التعليقات التوضيحية من ملف PDF.

```csharp
   public static void DeleteAllAnnotations()
        {
            // Open document
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // Delete all annoations
            annotationEditor.DeleteAnnotations();
            // Save updated PDF
        }   
    
```
```
## حذف جميع التعليقات التوضيحية حسب النوع المحدد

يمكنك استخدام فئة [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) لحذف جميع التعليقات التوضيحية، حسب نوع التعليق التوضيحي المحدد، من ملف PDF الموجود. من أجل القيام بذلك، تحتاج إلى إنشاء كائن [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، قم باستدعاء طريقة [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) مع وسيط نصي لحذف جميع التعليقات التوضيحية من الملف؛ الوسيط النصي يمثل نوع التعليق التوضيحي المراد حذفه. أخيرًا، استخدم طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لحفظ ملف PDF المحدث. يوضح لك مقتطف الشيفرة التالي كيفية حذف جميع التعليقات التوضيحية بواسطة نوع التعليق التوضيحي المحدد.

```csharp
    public static void DeleteAnnotation()
        {
            // فتح المستند
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("يرجى إدخال الرقم:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // حفظ ملف PDF المحدث
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```