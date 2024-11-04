---
title: إنشاء إشارات مرجعية لجميع الصفحات (واجهات)
type: docs
weight: 10
url: /java/create-bookmark/
description: يشرح هذا القسم كيفية إنشاء إشارات مرجعية باستخدام Aspose.PDF Facades باستخدام فئة PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إنشاء إشارات مرجعية لجميع الصفحات (واجهات)

لإنشاء إشارات مرجعية لجميع الصفحات، تحتاج إلى استخدام طريقة createBookmarks بدون أي معلمات. تسمح لك فئة PdfBookmarEditor بإنشاء إشارات مرجعية لجميع صفحات ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة PdfBookmarkEditor وربط ملف PDF المدخل باستخدام طريقة bindPdf. ثم، عليك استدعاء طريقة createBookmarks وحفظ ملف PDF الناتج باستخدام طريقة save.

يظهر لك مقطع الشيفرة التالي:

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## إنشاء إشارات مرجعية لجميع الصفحات مع الخصائص (واجهات)

تسمح لك فئة PdfBookmarEditor بإنشاء إشارات مرجعية لجميع صفحات ملف PDF وتحديد الخصائص (اللون، العريض، المائل).
 يمكنك القيام بذلك بمساعدة طريقة createBookmarks. أولاً، تحتاج إلى إنشاء كائن من فئة PdfBookmarkEditor وربط ملف PDF المدخل باستخدام طريقة bindPdf. بعد ذلك، يجب عليك استدعاء طريقة createBookmarks وحفظ ملف PDF الناتج باستخدام طريقة save.

يظهر لك مقتطف الشيفرة التالي كيفية إنشاء إشارات مرجعية لجميع الصفحات مع الخصائص.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}