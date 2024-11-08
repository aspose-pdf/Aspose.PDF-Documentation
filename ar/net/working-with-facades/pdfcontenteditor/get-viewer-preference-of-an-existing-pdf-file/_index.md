---
title: الحصول على تفضيلات العارض لملف PDF
type: docs
weight: 70
url: /ar/net/get-viewer-preference-of-an-existing-pdf-file/
description: يوضح هذا القسم كيفية الحصول على تفضيلات العارض لملف PDF موجود باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## الحصول على تفضيلات العارض لملف PDF موجود

تمثل فئة [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) أوضاع عرض ملفات PDF؛ على سبيل المثال، وضع نافذة المستند في وسط الشاشة، إخفاء شريط القوائم للتطبيق العارض إلخ.

من أجل قراءة الإعدادات نستخدم فئة [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). تُرجع هذه الطريقة متغيرًا حيث يتم حفظ جميع الإعدادات.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Change Viewer Preferences
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Menu bar hided");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Page Mode Full Screen");
        }
```