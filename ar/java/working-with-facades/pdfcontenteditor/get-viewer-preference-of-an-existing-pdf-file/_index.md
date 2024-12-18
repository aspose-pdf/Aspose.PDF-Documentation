---
title: الحصول على تفضيلات العارض لملف PDF موجود
type: docs
weight: 70
url: /ar/java/get-viewer-preference-of-an-existing-pdf-file/
description: يوضح هذا القسم كيفية العمل مع Aspose.PDF Facades باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## الحصول على تفضيلات العارض لملف PDF موجود

فئة [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) تمثل أوضاع عرض ملفات PDF؛ على سبيل المثال، وضع نافذة المستند في وسط الشاشة، إخفاء شريط القوائم لتطبيق العارض، إلخ.

لكي نقرأ الإعدادات نستخدم 'getViewerPreference'. هذه الطريقة تعيد متغيرًا حيث يتم حفظ جميع الإعدادات.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // تغيير تفضيلات العارض
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("CenterWindow");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Menu bar hided");
        }
```