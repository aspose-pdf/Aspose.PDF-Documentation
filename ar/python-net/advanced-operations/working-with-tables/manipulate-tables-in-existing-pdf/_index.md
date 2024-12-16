---
title: معالجة الجداول في ملفات PDF الموجودة
linktitle: معالجة الجداول
type: docs
weight: 40
url: /ar/python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "معالجة الجداول في ملفات PDF الموجودة",
    "alternativeHeadline": "كيفية تحديث محتوى الجداول في ملفات PDF الموجودة",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, python, معالجة الجداول",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## التعامل مع الجداول في ملف PDF موجود

إحدى أقدم الميزات المدعومة من قبل Aspose.PDF لـ Python عبر .NET هي قدراته على العمل مع الجداول ويوفر دعمًا كبيرًا لإضافة الجداول في ملفات PDF التي يتم إنشاؤها من الصفر أو أي ملفات PDF موجودة. في هذا الإصدار الجديد، قمنا بتنفيذ ميزة جديدة للبحث وتحليل الجداول البسيطة التي توجد بالفعل في صفحة من مستند PDF. توفر فئة جديدة تُسمى [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) هذه القدرات. استخدام TableAbsorber مشابه جدًا لفئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) الموجودة. يوضح مقتطف الشيفرة التالي الخطوات لتحديث المحتويات في خلية جدول معينة.

```python

    import aspose.pdf as ap

    # تحميل ملف PDF موجود
    pdf_document = ap.Document(input_file)
    # إنشاء كائن TableAbsorber للعثور على الجداول
    absorber = ap.text.TableAbsorber()
    # زيارة الصفحة الأولى مع المُمتص
    absorber.visit(pdf_document.pages[1])
    # الوصول إلى أول جدول في الصفحة، أول خلية وقطع النص فيها
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # تغيير نص أول قطعة نصية في الخلية
    fragment.text = "مرحبا بالعالم"
    pdf_document.save(output_file)
```


## استبدال الجدول القديم بآخر جديد في مستند PDF

في حال كنت بحاجة إلى العثور على جدول معين واستبداله بالجدول المطلوب، يمكنك استخدام [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) وهي طريقة من فئة [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) للقيام بذلك. يوضح المثال التالي كيفية استبدال الجدول داخل مستند PDF:

```python

    import aspose.pdf as ap

    # تحميل مستند PDF الحالي
    pdf_document = ap.Document(input_file)
    # إنشاء كائن TableAbsorber للعثور على الجداول
    absorber = ap.text.TableAbsorber()
    # زيارة الصفحة الأولى باستخدام الكائن absorber
    absorber.visit(pdf_document.pages[1])
    # الحصول على الجدول الأول في الصفحة
    table = absorber.table_list[0]
    # إنشاء جدول جديد
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("العمود 1")
    row.cells.add("العمود 2")
    row.cells.add("العمود 3")

    # استبدال الجدول بالجدول الجديد
    absorber.replace(pdf_document.pages[1], table, new_table)
    # حفظ المستند
    pdf_document.save(output_file)
```


## كيفية تحديد ما إذا كانت الجدول سوف ينكسر في الصفحة الحالية

يقوم هذا الكود بإنشاء مستند PDF يحتوي على جدول، ويحسب المساحة المتاحة على الصفحة، ويتحقق مما إذا كانت إضافة المزيد من الصفوف إلى الجدول ستؤدي إلى انكسار الصفحة بناءً على قيود المساحة. يتم حفظ النتيجة في ملف إخراج.

```python

    import aspose.pdf as ap

    # إنشاء كائن لفئة PDF
    pdf = ap.Document()
    # إضافة القسم إلى مجموعة أقسام مستند PDF
    page = pdf.pages.add()
    # إنشاء كائن جدول
    table1 = ap.Table()
    table1.margin.top = 300
    # إضافة الجدول إلى مجموعة الفقرات في القسم المطلوب
    page.paragraphs.add(table1)
    # تعيين عرض الأعمدة في الجدول
    table1.column_widths = "100 100 100"
    # تعيين الحدود الافتراضية للخلايا باستخدام كائن BorderInfo
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # إنشاء كائن MarginInfo وتعيين هوامشه اليسرى والسفلى واليمنى والعلوية
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # تعيين حشو الخلايا الافتراضي إلى كائن MarginInfo
    table1.default_cell_padding = margin
    # إذا زدت العداد إلى 17، سينكسر الجدول
    # لأنه لا يمكن استيعاب المزيد على هذه الصفحة
    for row_counter in range(0, 17):
        # إنشاء صفوف في الجدول ثم خلايا في الصفوف
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # الحصول على معلومات ارتفاع الصفحة
    page_height = pdf.page_info.height
    # الحصول على مجموع ارتفاع هوامش الصفحة العلوية والسفلية،
    # هامش الجدول العلوي وارتفاع الجدول.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # عرض معلومات ارتفاع الصفحة، وارتفاع الجدول، وهامش الجدول العلوي
    # ومعلومات هوامش الصفحة العلوية والسفلية
    print("PDF document Height = " + str(pdf.page_info.height) + "\nTop Margin Info = " + str(page.page_info.margin.top)
          + "\nBottom Margin Info = " + str(page.page_info.margin.bottom) + "\n\nTable-Top Margin Info = "
          + str(table1.margin.top) + "\nAverage Row Height = " + str(table1.rows[0].min_row_height) + " \nTable height "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nTotal Page Height ="
          + str(page_height) + "\nCummulative height including Table =" + str(total_objects_height))
    # التحقق مما إذا قمنا بطرح مجموع هامش الصفحة العلوي + هامش الصفحة السفلي
    # + هامش الجدول العلوي وارتفاع الجدول من ارتفاع الصفحة وهل هو أقل
    # من 10 (قد يكون ارتفاع الصف أكبر من 10)
    if (page_height - total_objects_height) <= 10:
        # إذا كانت القيمة أقل من 10، فقم بعرض الرسالة.
        # التي تظهر أن صفًا آخر لا يمكن وضعه وإذا أضفنا صفًا جديدًا
        # سينكسر الجدول. يعتمد ذلك على قيمة ارتفاع الصف.
        print("Page Height - Objects Height < 10, so table will break")
    # حفظ مستند pdf
    pdf.save(output_file)
```


## إضافة عمود متكرر في الجدول

في فئة [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)، يمكنك تعيين [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) الذي سيكرر الصفوف إذا كان الجدول طويلًا جدًا عموديًا ويمتد إلى الصفحة التالية. ومع ذلك، في بعض الحالات، تكون الجداول عريضة جدًا بحيث لا تتناسب مع صفحة واحدة وتحتاج إلى الاستمرار إلى الصفحة التالية. لتحقيق هذا الغرض، قمنا بتطبيق خاصية [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) في فئة [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/). يؤدي تعيين هذه الخاصية إلى انقسام الجدول إلى الصفحة التالية عموديًا وتكرار عدد الأعمدة المعطى في بداية الصفحة التالية. يُظهر مقتطف الشيفرة التالي استخدام خاصية [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties):

```python

    import aspose.pdf as ap

    # إنشاء مستند جديد
    doc = ap.Document()
    page = doc.pages.add()
    # إنشاء جدول خارجي يشغل الصفحة بالكامل
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # إنشاء كائن جدول سيتم تضمينه داخل outerTable الذي سينقسم داخل نفس الصفحة
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # إضافة outerTable إلى فقرات الصفحة
    # إضافة جدولي إلى outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # إضافة صف الرأس
    row = my_table.rows.add()
    row.cells.add("رأس 1")
    row.cells.add("رأس 2")
    row.cells.add("رأس 3")
    row.cells.add("رأس 4")
    row.cells.add("رأس 5")
    row.cells.add("رأس 6")
    row.cells.add("رأس 7")
    row.cells.add("رأس 11")
    row.cells.add("رأس 12")
    row.cells.add("رأس 13")
    row.cells.add("رأس 14")
    row.cells.add("رأس 15")
    row.cells.add("رأس 16")
    row.cells.add("رأس 17")
    for row_counter in range(0, 6):
        # إنشاء صفوف في الجدول ثم خلايا في الصفوف
        row1 = my_table.rows.add()
        row1.cells.add("عمود " + str(row_counter) + ", 1")
        row1.cells.add("عمود " + str(row_counter) + ", 2")
        row1.cells.add("عمود " + str(row_counter) + ", 3")
        row1.cells.add("عمود " + str(row_counter) + ", 4")
        row1.cells.add("عمود " + str(row_counter) + ", 5")
        row1.cells.add("عمود " + str(row_counter) + ", 6")
        row1.cells.add("عمود " + str(row_counter) + ", 7")
        row1.cells.add("عمود " + str(row_counter) + ", 11")
        row1.cells.add("عمود " + str(row_counter) + ", 12")
        row1.cells.add("عمود " + str(row_counter) + ", 13")
        row1.cells.add("عمود " + str(row_counter) + ", 14")
        row1.cells.add("عمود " + str(row_counter) + ", 15")
        row1.cells.add("عمود " + str(row_counter) + ", 16")
        row1.cells.add("عمود " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python عبر .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "بريطانيا",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF للبايثون عبر .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>