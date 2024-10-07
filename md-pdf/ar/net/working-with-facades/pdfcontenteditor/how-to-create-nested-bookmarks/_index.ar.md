---
title: إضافة الإشارات المرجعية إلى ملف PDF
type: docs
weight: 20
url: /net/how-to-create-nested-bookmarks/
description: يوضح هذا القسم كيفية إنشاء إشارات مرجعية متداخلة باستخدام فئة PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

الإشارات المرجعية تمنحك الخيار لتتبع/ربط صفحات معينة داخل مستند PDF. توفر فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) في [مساحة الأسماء Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) ميزة تتيح لك إنشاء إشارتك المرجعية الخاصة بطريقة متقدمة لكنها بديهية داخل ملف PDF موجود، في صفحة معينة أو في جميع الصفحات.

## تفاصيل التنفيذ

بخلاف إنشاء الإشارات المرجعية البسيطة، أحيانًا يكون لديك متطلب لإنشاء إشارة مرجعية في شكل فصول حيث تقوم بتعشيق الإشارات المرجعية الفردية داخل إشارات مرجعية للفصل بحيث عندما تنقر على علامة + للفصل، سترى الصفحات بالداخل عند توسع الإشارات المرجعية، كما هو موضح في الصورة أدناه.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("إشارة مرجعية 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // Saves the result PDF to file
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```