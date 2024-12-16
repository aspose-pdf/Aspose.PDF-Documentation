---
title: العمل مع الحافظة في PDF
linktitle: الحافظة
type: docs
weight: 40
url: /ar/cpp/portfolio/
description: إنشاء حافظة PDF باستخدام Aspose.PDF لـ C++. يجب عليك استخدام ملف Microsoft Excel ومستند Word وملف صورة لإنشاء حافظة PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية إنشاء حافظة PDF

تسمح Aspose.PDF بإنشاء مستندات حافظة PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). أضف ملفًا إلى كائن Document.Collection بعد الحصول عليه باستخدام فئة [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). عندما تتم إضافة الملفات، استخدم طريقة الحفظ في فئة Document لحفظ مستند الحافظة.

المثال التالي يستخدم ملف Microsoft Excel ومستند Word وملف صورة لإنشاء حافظة PDF.

الكود أدناه ينتج الحافظة التالية.

### حافظة PDF تم إنشاؤها باستخدام Aspose.PDF


![حافظة PDF تم إنشاؤها باستخدام Aspose.PDF لـ C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // إنشاء كائن المستند
    auto pdfDocument = MakeObject<Document>();

    // إنشاء كائن مجموعة المستندات
    pdfDocument->set_Collection(MakeObject<Collection>());

    // الحصول على الملفات لإضافتها إلى الحافظة
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // توفير وصف للملفات
    excel->set_Description(u"ملف إكسل");
    word->set_Description(u"ملف وورد");
    image->set_Description(u"ملف صورة");

    // إضافة الملفات إلى مجموعة المستندات
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // حفظ مستند الحافظة
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```


## استخراج الملفات من حافظة PDF

PDF Portfolios تسمح لك بتجميع المحتوى من مجموعة متنوعة من المصادر (على سبيل المثال، ملفات PDF، Word، Excel، JPEG) في حاوية واحدة موحدة. تحتفظ الملفات الأصلية بهوياتها الفردية ولكن يتم تجميعها في ملف PDF Portfolio. يمكن للمستخدمين فتح كل ملف مكون وقراءته وتعديله وتنسيقه بشكل مستقل عن الملفات المكونة الأخرى.

يسمح Aspose.PDF بإنشاء مستندات PDF Portfolio باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). كما يوفر القدرة على استخراج الملفات من محفظة PDF.

يظهر لك مقتطف الشيفرة التالي الخطوات لاستخراج الملفات من محفظة PDF.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // فتح مستند
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // الحصول على مجموعة الملفات المضمنة
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // التكرار عبر الملفات الفردية للملف
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // حفظ الملف المستخرج في بعض المواقع
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // إغلاق كائن التدفق
    fileStream->Close();
    }
}
```

![استخراج الملفات من محفظة PDF](working-with-pdf-portfolio_2.jpg)

## إزالة الملفات من محفظة PDF

من أجل حذف/إزالة الملفات من محفظة PDF، حاول استخدام أسطر الكود التالية.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // تحميل محفظة PDF المصدر
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```