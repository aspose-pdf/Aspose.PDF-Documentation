---
title: إضافة إجراءات الإشارات المرجعية إلى ملف PDF موجود
type: docs
weight: 20
url: /ar/java/adding-bookmark-actions/
description: يشرح هذا القسم كيفية إضافة إجراءات الإشارات المرجعية إلى ملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تقدم فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) الموجودة تحت الحزمة com.aspose.pdf.facades المرونة لإضافة إجراءات الإشارات المرجعية إلى ملف PDF. يمكنك إنشاء رابط بالإجراءات التسلسلية المقابلة لتنفيذ عنصر قائمة في عارض PDF. توفر هذه الفئة أيضًا ميزة لإنشاء إجراءات إضافية لأحداث المستند.

يوضح المثال البرمجي التالي كيفية إضافة إجراء إشارة مرجعية إلى مستند PDF.
 إذا قمت بالنقر فوق هذا التبويب، يتم تنفيذ الإجراء المطلوب. بمساعدة علامة مرجعية، عند النقر عليها، نقوم بتنفيذ الإجراء المطلوب. ثم ننشئ [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-)، نحدد معلمات النص، الألوان، نشير إلى اسم العلامة المرجعية، وأيضًا نشير إلى رقم الصفحة. يتم تنفيذ الإجراء الأخير باستخدام "GoTo"، مما يسمح لك بالانتقال من أي مكان إلى الصفحة التي نحتاجها.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // يحفظ ملف PDF الناتج
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```