---
title: ضبط حجم الصورة باستخدام C++
linktitle: ضبط حجم الصورة
type: docs
weight: 80
url: ar/cpp/set-image-size/
description: يصف هذا القسم كيفية ضبط حجم الصورة في ملف PDF باستخدام مكتبة C++.
lastmod: "2021-12-18"
---

من الممكن ضبط حجم الصورة التي يتم إضافتها إلى ملف PDF. لضبط الحجم، يمكنك استخدام خصائص [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) و[FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) الخاصة بـ[Aspose.Pdf.Image Class](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

يوضح مقطع الشفرة التالي كيفية ضبط حجم الصورة:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // إنشاء كائن Document
    auto document = MakeObject<Document>();
    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();
    // إنشاء مثيل للصورة
    auto img = MakeObject<Image>();
    // ضبط عرض وارتفاع الصورة بالنقاط
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // ضبط نوع الصورة كـ SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // مسار الملف المصدر
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // ضبط خصائص الصفحة
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // حفظ ملف PDF الناتج
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```