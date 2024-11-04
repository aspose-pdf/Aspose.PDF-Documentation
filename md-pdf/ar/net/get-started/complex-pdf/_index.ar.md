---
title: إنشاء PDF معقد
linktitle: إنشاء PDF معقد
type: docs
weight: 60
url: /net/complex-pdf-example/
description: يتيح لك Aspose.PDF لـ NET إنشاء مستندات أكثر تعقيداً تحتوي على صور وأجزاء نصية وجداول في مستند واحد.
aliases:
    - /net/complex-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

أظهر مثال [مرحباً، العالم](/pdf/net/hello-world-example/) خطوات بسيطة لإنشاء مستند PDF باستخدام C# و Aspose.PDF. في هذا المقال، سنلقي نظرة على إنشاء مستند أكثر تعقيداً باستخدام C# و Aspose.PDF لـ .NET. كمثال، سنأخذ مستنداً من شركة وهمية تعمل في خدمات العبّارات الركابية.
سيحتوي مستندنا على صورة، وجزأين نصيين (الرأس والفقرة)، وجدول. لبناء مثل هذا المستند، سنستخدم نهج DOM. يمكنك قراءة المزيد في قسم [أساسيات واجهة برمجة التطبيقات DOM](/pdf/net/basics-of-dom-api/).

إذا كنا ننشئ مستنداً من الصفر فإننا نحتاج إلى اتباع خطوات معينة:

1.
1.
1. قم بإضافة [صفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى كائن المستند. وبذلك، سيكون لدينا الآن صفحة واحدة.
1. قم بإضافة [صورة](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) إلى الصفحة.
1. قم بإنشاء [جزء نصي](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) للعنوان. للعنوان سنستخدم خط Arial بحجم الخط 24pt ومحاذاة في الوسط.
1. أضف العنوان إلى [الفقرات](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) الصفحة.
1. قم بإنشاء [جزء نصي](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) للوصف. للوصف سنستخدم خط Arial بحجم الخط 24pt ومحاذاة في الوسط.
1. أضف (الوصف) إلى فقرات الصفحة.
1. قم بإنشاء جدول وأضف خصائص الجدول.
1. أضف (الجدول) إلى [الفقرات](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) الصفحة.
1. احفظ المستند "Complex.pdf".

يعمل الشفرة البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // تهيئة كائن المستند
            Document document = new Document();
            // إضافة صفحة
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // إضافة صورة
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // إضافة رأس
            var header = new TextFragment("مسارات العبارات الجديدة في خريف 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // إضافة وصف
            var descriptionText = "يجب على الزوار شراء التذاكر عبر الإنترنت والتذاكر محدودة بـ 5000 تذكرة في اليوم. تعمل خدمة العبارات بنصف الطاقة وبجدول مخفض. توقع الانتظار.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // إضافة جدول
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("يغادر المدينة");
            headerRow.Cells.Add("يغادر الجزيرة");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

