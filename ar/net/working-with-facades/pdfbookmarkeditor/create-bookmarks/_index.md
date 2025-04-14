---
title: إنشاء إشارات مرجعية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/create-bookmarks/
description: يشرح هذا القسم كيفية إنشاء إشارات مرجعية لملف PDF الخاص بك باستخدام Aspose.PDF Facades من خلال استخدام فئة PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "تقديم وظيفة الإشارات المرجعية في Aspose.PDF for .NET، المصممة لتعزيز التنقل في PDF من خلال السماح للمستخدمين بإنشاء إشارات مرجعية لصفحات كاملة، أو صفحات محددة، أو نطاقات من الصفحات مع خصائص قابلة للتخصيص. تتيح هذه الميزة تنظيم مستندات PDF بسلاسة، مما يسهل الوصول إلى المحتوى وإدارته بشكل فعال. سواء كنت بحاجة إلى إضافة إشارات مرجعية بسيطة أو إشارات مرجعية فرعية معقدة، توفر فئة Aspose.PDF PdfBookmarkEditor الأدوات اللازمة لتحسين تجربتك مع PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1124",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/create-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إنشاء إشارات مرجعية لجميع الصفحات

لإنشاء إشارات مرجعية لجميع الصفحات، تحتاج إلى استخدام [CreateBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) بدون أي معلمات. تتيح لك فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) إنشاء إشارات مرجعية لجميع صفحات ملف PDF. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، يجب عليك استدعاء طريقة [CreateBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك المقتطف البرمجي التالي كيفية إنشاء إشارات مرجعية.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarksAll.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks();
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarksOfAllPages_out.pdf");
    }
} 
```

## إنشاء إشارات مرجعية لجميع الصفحات مع الخصائص

تتيح لك فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) إنشاء إشارات مرجعية لجميع صفحات ملف PDF وتحديد الخصائص (اللون، الغامق، المائل). يمكنك القيام بذلك بمساعدة طريقة [CreateBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، يجب عليك استدعاء طريقة [CreateBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك المقتطف البرمجي التالي كيفية إنشاء إشارات مرجعية لجميع الصفحات مع الخصائص.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPagesWithProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarks-PagesProperties.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks(System.Drawing.Color.Green, true, true);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarks-PagesProperties_out.pdf");
    }
}
```

## إنشاء إشارة مرجعية لصفحة معينة

يمكنك إنشاء إشارة مرجعية لصفحة معينة في ملف PDF موجود باستخدام طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). تأخذ هذه الطريقة وسيطين: عنوان الإشارة المرجعية ورقم الصفحة. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، يجب عليك استدعاء طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك المقتطف البرمجي التالي كيفية إنشاء إشارة مرجعية لصفحة معينة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarkOfAParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Create bookmark of a particular page
        bookmarkEditor.CreateBookmarkOfPage("Bookmark Name", 2);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmark-Page_out.pdf");
    }
}
```

## إنشاء إشارات مرجعية لنطاق من الصفحات

تتيح لك فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) إنشاء إشارات مرجعية لنطاق من الصفحات. يمكنك استخدام طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) مع وسيطين: قائمة الإشارات المرجعية (قائمة عناوين الإشارات المرجعية) وقائمة الصفحات (قائمة الصفحات التي تريد إنشاء إشارات مرجعية لها). أولاً، تحتاج إلى إنشاء كائن من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.facade/bindpdf/methods/3). ثم، يجب عليك استدعاء طريقة [CreateBookmarkOfPage](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) وحفظ ملف PDF الناتج باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك المقتطف البرمجي التالي كيفية إنشاء إشارات مرجعية لنطاق من الصفحات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfARangeOfPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Bookmark name list
        string[] bookmarkList = { "First" };
        // Page list
        int[] pageList = { 1 };
        // Create bookmark of a range of pages
        bookmarkEditor.CreateBookmarkOfPage(bookmarkList, pageList);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarkPageRange_out.pdf");
    }
}
```

## إضافة إشارة مرجعية في ملف PDF موجود

يمكنك إضافة إشارة مرجعية في ملف PDF موجود باستخدام فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor). لإنشاء الإشارة المرجعية، تحتاج إلى إنشاء كائن [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark) وتعيين الخصائص المطلوبة للإشارة المرجعية. بعد ذلك، تحتاج إلى تمرير كائن [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark) إلى طريقة [CreateBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor). أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك المقتطف البرمجي التالي كيفية إضافة الإشارة المرجعية في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmark
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.PageNumber = 1;
    bookmark.Title = "New Bookmark";
    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```

## إضافة إشارة مرجعية فرعية في ملف PDF موجود

يمكنك إضافة إشارات مرجعية فرعية في ملف PDF موجود باستخدام فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor). لإضافة إشارات مرجعية فرعية، تحتاج إلى إنشاء كائنات [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark). يمكنك إضافة كائنات [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark) الفردية إلى كائن [Bookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmarks). تحتاج أيضًا إلى إنشاء كائن [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark) وتعيين خاصية [ChildItem](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark/properties/childitem) إلى كائن [Bookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmarks). ثم تحتاج إلى تمرير هذا الكائن [Bookmark](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark) مع [ChildItem](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/bookmark/properties/childitem) إلى طريقة [CreateBookmarks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save) من فئة [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor). يوضح لك المقتطف البرمجي التالي كيفية إضافة إشارات مرجعية فرعية في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmarks
    var bookmarks = new Aspose.Pdf.Facades.Bookmarks();
    var childBookmark1 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark1.PageNumber = 1;
    childBookmark1.Title = "First Child";
    var childBookmark2 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark2.PageNumber = 2;
    childBookmark2.Title = "Second Child";
    bookmarks.Add(childBookmark1);
    bookmarks.Add(childBookmark2);
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.Action = "GoTo";
    bookmark.PageNumber = 1;
    bookmark.Title = "Parent";
    bookmark.ChildItems = bookmarks;
    // Create PdfBookmarkEditor class
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddChildBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```