---
title: إضافة كائن مستطيل إلى ملف PDF
linktitle: إضافة مستطيل
type: docs
weight: 50
url: /cpp/add-rectangle/
description: يشرح هذا المقال كيفية إنشاء كائن مستطيل إلى ملف PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن مستطيل

يدعم Aspose.PDF لـ C++ ميزة إضافة كائنات الرسم البياني (مثل الرسم البياني، الخط، المستطيل إلخ.) إلى مستندات PDF. كما تحصل على ميزة إضافة كائن [مستطيل](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) حيث تقدم أيضًا ميزة ملء كائن المستطيل بلون معين، التحكم في ترتيب الطبقات، إضافة تعبئة بلون متدرج وما إلى ذلك.

أولاً، دعونا ننظر إلى إمكانية إنشاء كائن مستطيل.

اتبع الخطوات أدناه:

1. قم بإنشاء [مستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF جديد

1. أضف [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) إلى مجموعة الصفحات في ملف PDF

1.
``` أضف [Text fragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) إلى مجموعة الفقرات الخاصة بنسخة الصفحة

1. قم بإنشاء نسخة [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)

1. قم بتعيين الحدود لكائن [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. قم بإنشاء نسخة Rectangle

1. أضف كائن [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) إلى مجموعة الأشكال الخاصة بكائن Graph

1. أضف كائن الرسم إلى مجموعة الفقرات الخاصة بنسخة الصفحة

1. أضف [Text fragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) إلى مجموعة الفقرات الخاصة بنسخة الصفحة

1. واحفظ ملف PDF الخاص بك

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // إنشاء كائن الرسم بأبعاد مماثلة لتلك المحددة لكائن المستطيل
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // هل يمكننا تغيير موضع كائن الرسم
                IsChangePosition = false,
                // تعيين موضع الإحداثي الأيسر لكائن الرسم
                Left = x,
                // تعيين موضع الإحداثي العلوي لكائن الرسم
                Top = y
            };
            // أضف مستطيل داخل "كائن الرسم"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // تعيين لون تعبئة المستطيل
            rect.GraphInfo.FillColor = color;
            // لون كائن الرسم
            rect.GraphInfo.Color = color;
            // أضف المستطيل إلى مجموعة الأشكال الخاصة بكائن الرسم
            graph.Shapes.Add(rect);
            // تعيين Z-Index لكائن المستطيل
            graph.ZIndex = zindex;
            // أضف كائن الرسم إلى مجموعة الفقرات الخاصة بكائن الصفحة
            page.Paragraphs.Add(graph);
        }
```
![إنشاء مستطيل](create_rectangle.png)

## إنشاء كائن مستطيل مملوء

يوفر Aspose.PDF for C++ أيضًا ميزة ملء كائن المستطيل بلون معين.

يُظهر مقتطف الشيفرة التالي كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) مملوء بالألوان.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // إنشاء مثيل للمستند
            var doc = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = doc.Pages.Add();
            // إنشاء مثيل للرسم
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // إضافة كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة
            page.Paragraphs.Add(graph);

            // إنشاء مثيل للمستطيل
            var rect = new Rectangle(100, 100, 200, 120);

            // تحديد لون التعبئة لكائن الرسم
            rect.GraphInfo.FillColor = Color.Red;

            // إضافة كائن المستطيل إلى مجموعة الأشكال في كائن الرسم
            graph.Shapes.Add(rect);

            // حفظ ملف PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

انظر إلى نتيجة المستطيل الممتلئ بلون صلب:

![مستطيل ممتلئ](fill_rectangle.png)

## إضافة رسم بتعبئة متدرجة

يدعم Aspose.PDF for C++ ميزة إضافة كائنات الرسوم إلى مستندات PDF وأحيانًا يكون من الضروري تعبئة كائنات الرسوم بلون متدرج. لتعبئة كائنات الرسوم بلون متدرج، نحتاج إلى ضبط setPatterColorSpace مع كائن gradientAxialShading كما يلي.

يُظهر مقتطف الشيفرة التالي كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) الذي يتم تعبئته بلون متدرج.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // إنشاء مثيل للمستند
            var doc = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = doc.Pages.Add();
            // إنشاء مثيل للرسم
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // إضافة كائن الرسم إلى مجموعة الفقرات لمثيل الصفحة
            page.Paragraphs.Add(graph);
            // إنشاء مثيل للمستطيل
            var rect = new Rectangle(0, 0, 300, 300);
            // تحديد لون التعبئة لكائن الرسم
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن الرسم
            graph.Shapes.Add(rect);

            // حفظ ملف PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![مستطيل متدرج](gradient.png)

## إنشاء مستطيل مع قناة اللون ألفا

يدعم Aspose.PDF لـ C+++ ملء كائن المستطيل بلون معين. يمكن أن يحتوي كائن المستطيل أيضًا على قناة لون ألفا لإعطاء مظهر شفاف. يوضح مقتطف الكود التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) مع قناة لون ألفا.

يمكن أن تخزن بكسلات الصورة معلومات حول شفافيتها جنبًا إلى جنب مع قيمة اللون. يسمح ذلك بإنشاء صور بمناطق شفافة أو شبه شفافة.

بدلاً من جعل اللون شفافًا، يخزن كل بكسل معلومات حول مدى شفافيته. تُسمى بيانات الشفافية هذه قناة ألفا وعادةً ما تُخزن بعد قنوات الألوان للبكسل.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // إنشاء مثيل وثيقة
            var doc = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = doc.Pages.Add();
            // إنشاء مثيل رسم بياني
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // إضافة كائن الرسم البياني إلى مجموعة الفقرات في مثيل الصفحة
            page.Paragraphs.Add(graph);
            // إنشاء مثيل مستطيل
            var rect = new Rectangle(100, 100, 200, 120);
            // تحديد لون التعبئة لكائن الرسم البياني
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن الرسم البياني
            graph.Shapes.Add(rect);

            // إنشاء كائن مستطيل ثاني
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // إضافة مثيل الرسم البياني إلى مجموعة الفقرات لكائن الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## التحكم في ترتيب Z للمستطيل

يدعم Aspose.PDF for C++ ميزة إضافة كائنات الرسم (على سبيل المثال الرسم، الخط، المستطيل، إلخ) إلى مستندات PDF. عند إضافة أكثر من نسخة من نفس الكائن داخل ملف PDF، يمكننا التحكم في عرضها بتحديد ترتيب Z. يُستخدم ترتيب Z أيضًا عندما نحتاج إلى عرض الكائنات فوق بعضها البعض.

يعرض مقتطف الشيفرة التالي خطوات عرض كائنات [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) فوق بعضها البعض.

```csharp
 public static void AddRectangleZOrder()
        {
            // إنشاء كائن من فئة Document
            Document doc1 = new Document();
            /// إضافة صفحة لمجموعة الصفحات في ملف PDF
            Page page1 = doc1.Pages.Add();
            // تعيين حجم صفحة PDF
            page1.SetPageSize(375, 300);
            // تعيين الهامش الأيسر لكائن الصفحة كـ 0
            page1.PageInfo.Margin.Left = 0;
            // تعيين الهامش العلوي لكائن الصفحة كـ 0
            page1.PageInfo.Margin.Top = 0;
            // إنشاء مستطيل جديد بلون أحمر، وترتيب Z كـ 0 وأبعاد معينة
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // إنشاء مستطيل جديد بلون أزرق، وترتيب Z كـ 0 وأبعاد معينة
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // إنشاء مستطيل جديد بلون أخضر، وترتيب Z كـ 0 وأبعاد معينة
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // حفظ ملف PDF الناتج
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

![التحكم في ترتيب الطبقات](control.png)