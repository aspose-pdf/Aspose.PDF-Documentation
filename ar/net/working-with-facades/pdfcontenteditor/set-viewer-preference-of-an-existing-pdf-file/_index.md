---
title: تعيين تفضيل العارض لملف PDF
type: docs
weight: 60
url: /ar/net/set-viewer-preference-of-an-existing-pdf-file/
description: يوضح هذا القسم كيفية تعيين تفضيل العارض لملف PDF موجود باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## تعيين تفضيل العارض لملف PDF موجود

تمثل فئة [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) أوضاع عرض ملفات PDF؛ على سبيل المثال، وضع نافذة المستند في وسط الشاشة، إخفاء شريط القوائم لتطبيق العارض، إلخ.

تسمح لك طريقة [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) في فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) بتغيير تفضيل العارض. ```
من أجل القيام بذلك، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

بعد ذلك، يمكنك استدعاء طريقة [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) لتعيين أي تفضيل. وأخيراً، يجب عليك حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). يوضح لك مقطع الشيفرة التالي كيفية تغيير تفضيل العارض في ملف PDF موجود.

على سبيل المثال، نحدد المعامل [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) الذي نستخدمه لمركز النافذة، بعد إزالة شريط الأدوات العلوي باستخدام [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) ومع [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) لفتح وضع الشاشة الكاملة.
```
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // تغيير تفضيلات العارض
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // يحفظ ملف PDF الناتج إلى ملف
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```