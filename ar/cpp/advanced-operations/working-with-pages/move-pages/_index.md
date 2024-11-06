---
title: نقل صفحات PDF برمجيًا C++
linktitle: نقل صفحات PDF
type: docs
weight: 20
url: ar/cpp/move-pages/
description: حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## نقل صفحة من مستند PDF إلى آخر

يعتبر نقل صفحات PDF في المستند مهمة مثيرة وشائعة.
يشرح هذا الموضوع كيفية نقل صفحة من مستند PDF إلى نهاية مستند آخر باستخدام C++.
لنقل صفحة يجب علينا:

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ملف PDF المصدر.
1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [إضافة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) الصفحة إلى المستند الوجهة.
1. حفظ ملف PDF الناتج باستخدام طريقة Save.
1. [احذف](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) الصفحة في المستند المصدر.  
1. احفظ ملف PDF المصدر باستخدام طريقة الحفظ Save.

يوضح لك مقتطف الشفرة التالي كيفية نقل صفحة واحدة.

```cpp
void MovePage()
{
    // افتح المستند
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // احفظ ملف الإخراج
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## نقل مجموعة من الصفحات من وثيقة PDF إلى أخرى

1. أنشئ كائن فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ملف PDF المصدر.  
1. حدد مصفوفة بأرقام الصفحات التي سيتم نقلها.  
1. ترجم المستند إلى اللغة العربية كما يلي:

قم بتشغيل حلقة عبر المصفوفة:
1. احصل على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [أضف](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) الصفحة إلى مستند الوجهة.
1. احفظ ملف PDF الناتج باستخدام طريقة Save.
1. [احذف](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) الصفحة في المستند المصدر.
1. احفظ ملف PDF المصدر باستخدام طريقة Save.

يظهر لك مقطع الشفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```cpp
void MoveBunchPages()
{
    // افتح المستند
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // احفظ الملفات الناتجة
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## نقل صفحة إلى موقع جديد في مستند PDF الحالي

1. قم بإنشاء كائن فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ملف PDF المصدر.
2. احصل على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
3. [أضف](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) الصفحة إلى الموقع الجديد (على سبيل المثال إلى النهاية).
4. [احذف](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) الصفحة في الموقع السابق.
5. احفظ ملف الـ PDF الناتج باستخدام طريقة Save.

```cpp
void MovePagesInOnePDF()
{
    // Open document
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // Save output file
    srcDocument->Save(dstFileName);
}
```