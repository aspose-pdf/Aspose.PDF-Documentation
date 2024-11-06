---
title: استخراج فقرة من PDF بلغة C#
linktitle: استخراج فقرة من PDF
type: docs
weight: 20
url: ar/net/extract-paragraph-from-pdf/
description: هذا المقال يصف كيفية استخدام أداة ParagraphAbsorber - أداة خاصة في Aspose.PDF لاستخراج النصوص من مستندات PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من مستند PDF على شكل فقرات

يمكننا الحصول على النص من مستند PDF من خلال البحث عن نص معين (باستخدام "النص العادي" أو "التعبيرات العادية") من صفحة واحدة أو المستند بأكمله، أو يمكننا الحصول على النص الكامل لصفحة واحدة، نطاق صفحات أو المستند بأكمله.
يمكننا الحصول على نص من مستند PDF عن طريق البحث عن نص معين (باستخدام "نص عادي" أو "تعبيرات منتظمة") من صفحة واحدة أو المستند بأكمله، أو يمكننا الحصول على النص الكامل لصفحة واحدة، أو مجموعة من الصفحات أو المستند بأكمله.

**1- برسم حدود الأقسام والفقرات على صفحة PDF:**

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraph()
{
    // مسار دليل المستندات
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    Document doc = new Document(dataDir + "input.pdf");
    Page page = doc.Pages[2];

    ParagraphAbsorber absorber = new ParagraphAbsorber();
    absorber.Visit(page);

    PageMarkup markup = absorber.PageMarkups[0];

    foreach (MarkupSection section in markup.Sections)
    {
        DrawRectangleOnPage(section.Rectangle, page);
        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            DrawPolygonOnPage(paragraph.Points, page);
        }
    }

    doc.Save(dataDir + "output_out.pdf");
}

private static void DrawRectangleOnPage(Rectangle rectangle, Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(2));
    page.Contents.Add(
        new Aspose.Pdf.Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}

private static void DrawPolygonOnPage(Point[] polygon, Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(1));
    page.Contents.Add(new Aspose.Pdf.Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}
```
**2- من خلال تكرار مجموعة الفقرات والحصول على نصوصها:**

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// فتح ملف PDF موجود
Document doc = new Document(dataDir + "input.pdf");
// استحداث ParagraphAbsorber
ParagraphAbsorber absorber = new ParagraphAbsorber();
absorber.Visit(doc);

foreach (PageMarkup markup in absorber.PageMarkups)
{
    int i = 1;
    foreach (MarkupSection section in markup.Sections)
    {
        int j = 1;

        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            StringBuilder paragraphText = new StringBuilder();

            foreach (List<TextFragment> line in paragraph.Lines)
            {
                foreach (TextFragment fragment in line)
                {
                    paragraphText.Append(fragment.Text);
                }
                paragraphText.Append("\r\n");
            }
            paragraphText.Append("\r\n");

            Console.WriteLine("الفقرة {0} من القسم {1} في الصفحة {2}:", j, i, markup.Number);
            Console.WriteLine(paragraphText.ToString());

            j++;
        }
        i++;
    }
}
```

