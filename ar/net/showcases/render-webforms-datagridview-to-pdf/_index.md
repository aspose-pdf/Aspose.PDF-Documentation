---
title: تحويل WebForms DataGridView إلى PDF
linktitle: تحويل WebForms DataGridView إلى PDF
type: docs
weight: 20
url: ar/net/render-webforms-datagridview-to-pdf/
description: توضح هذه العينة كيفية استخدام مكتبة Aspose.PDF لتقديم WebForm إلى PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية تصدير WebForm إلى PDF باستخدام Aspose.PDF/Aspose.HTML

### مقدمة

عمومًا، لتحويل WebForm إلى مستند PDF يستخدم أدوات إضافية. توضح هذه العينة كيفية استخدام مكتبة Aspose.PDF لتقديم WebForm إلى PDF. يتضمن هذا العينة أيضًا تحكم Aspose Export GridView To Pdf لإظهار كيفية تقديم _GridView control إلى مستند PDF._

## كيفية تقديم WebForm إلى PDF

الفكرة الأصلية لتقديم WebForm إلى PDF هي إنشاء فئة مساعدة، ترث من [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)، وتجاوز طريقة Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // تقديم صفحة الويب لمستند PDF
    }
    else
    {
        // تقديم صفحة الويب في المتصفح
        base.Render(writer);
    }
}
```
هناك أداتان من Aspose يمكن استخدامهما لتحويل HTML إلى PDF:

- Aspose.PDF لـ .NET
- تحكم Aspose Export GridView (يعتمد على Aspose.PDF)

## ملفات المصدر

في هذا العينة لدينا تقريرين تجريبيين.

- _Default.aspx_ يوضح التصدير إلى PDF باستخدام Aspose.PDF
- _Report2.aspx_ يوضح التصدير إلى PDF باستخدام تحكم Aspose Export GridView (يعتمد على Aspose.PDF)

## ملفات إضافية

`Helpers\PdfPage.cs` - يحتوي على فئة مساعدة، تظهر كيفية استخدام واجهة برمجة تطبيقات Aspose.PDF.

مشروع Aspose.Pdf.GridViewExport يحتوي على تحكم GridView الموسع للعرض في `Report2.aspx`

