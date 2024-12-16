---
title: تعيين تفضيلات العارض لملف PDF موجود
type: docs
weight: 60
url: /ar/java/set-viewer-preference-of-an-existing-pdf-file/
description: يوضح هذا القسم كيفية العمل مع Aspose.PDF Facades باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## تعيين تفضيلات العارض لملف PDF موجود

فئة [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) تمثل أوضاع عرض ملفات PDF؛ على سبيل المثال، وضع نافذة المستند في وسط الشاشة، إخفاء شريط قوائم تطبيق العارض، إلخ.

تسمح لك طريقة [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) في فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) بتغيير تفضيلات العارض.
 من أجل القيام بذلك، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) وربط ملف PDF المدخل باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-).

بعد ذلك، يمكنك استدعاء طريقة [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) لتعيين أي تفضيل. أخيرًا، يجب عليك حفظ ملف PDF المحدث باستخدام طريقة الحفظ. يوضح لك مقتطف الشيفرة التالي كيفية تغيير تفضيلات العارض في ملف PDF موجود.

على سبيل المثال، نحن نحدد المعامل [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) الذي يمكننا من توسيط النافذة، بعد إزالة شريط الأدوات العلوي باستخدام [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) ومع [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) لفتح وضع الشاشة الكاملة.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // تغيير تفضيلات العارض
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```