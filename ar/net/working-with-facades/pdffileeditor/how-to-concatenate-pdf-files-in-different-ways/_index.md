---
title: دمج ملفات PDF باستخدام .NET 5
linktitle: كيفية دمج PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /ar/net/how-to-concatenate-pdf-files-in-different-ways/
description: يشرح هذا المقال الطرق الممكنة لدمج أي عدد من ملفات PDF الموجودة في ملف PDF واحد.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "قم بدمج عدة ملفات PDF في مستند واحد بسلاسة مع الوظيفة الجديدة في Aspose.PDF for .NET. تتيح هذه الميزة للمطورين دمج أي عدد من ملفات PDF من خلال استدعاءات طرق بسيطة، مما يعزز الإنتاجية في إدارة PDF والتلاعب به. قم بدمج هذه القدرة بسهولة في تطبيقات .NET المختلفة، بما في ذلك تطبيقات ASP.NET وتطبيقات Windows، مع أساليب متعددة تلبي احتياجات مختلفة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
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
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسهل، ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

يصف هذا المقال كيفية [دمج](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) عدة مستندات PDF في مستند PDF واحد بمساعدة [Aspose.PDF for .NET](/pdf/ar/net/) المكون. يجعل [Aspose.PDF for .NET](/pdf/ar/net/) هذه المهمة سهلة للغاية.

{{% /alert %}}

كل ما عليك فعله هو استدعاء طريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) وسيتم دمج جميع ملفات PDF المدخلة الخاصة بك معًا وسيتم إنشاء ملف PDF واحد. دعنا ننشئ تطبيقًا لممارسة دمج ملفات PDF. سنقوم بإنشاء تطبيق باستخدام Visual Studio.NET 2019.

{{% alert color="primary" %}}

يمكن استخدام Aspose.PDF for .NET في أي نوع من التطبيقات التي تعمل على إطار عمل .NET سواء كانت تطبيق ويب ASP.NET أو تطبيق Windows.

{{% /alert %}}

## كيفية دمج ملفات PDF بطرق مختلفة

في النموذج، هناك ثلاثة صناديق نصية (textBox1، textBox2، textBox3) تحتوي على تسميات روابطها الخاصة (linkLabel1، linkLabel2، linkLabel3) لتصفح ملفات PDF. عند النقر على "تصفح" رابط التسمية، سيظهر مربع حوار إدخال ملف (inputFileDialog1) يمكّننا من اختيار ملفات PDF (التي سيتم دمجها).

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

يظهر عرض تطبيق نموذج Windows لتوضيح فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) لدمج ملفات PDF.

![دمج ملفات PDF](how-to-concatenate-pdf-files-in-different-ways_1.png)

بعد اختيار ملف PDF والنقر على زر OK. يتم تعيين الاسم الكامل للملف مع المسار إلى صندوق النص المعني.

![اختر ملف PDF](how-to-concatenate-pdf-files-in-different-ways_2.png)

وبالمثل، يمكننا اختيار ملفين أو ثلاثة ملفات PDF مدخلة للدمج كما هو موضح أدناه:

![اختر ملفين أو ثلاثة ملفات PDF مدخلة](how-to-concatenate-pdf-files-in-different-ways_3.png)

سيأخذ صندوق النص الأخير (textBox4) مسار الوجهة لملف PDF الناتج مع اسمه حيث سيتم إنشاء هذا الملف الناتج.

![مسار الوجهة لملف PDF الناتج](how-to-concatenate-pdf-files-in-different-ways_4.png)

![طريقة الدمج](how-to-concatenate-pdf-files-in-different-ways_5.png)

## طريقة Concatenate()

يمكن استخدام طريقة Concatenate() بثلاث طرق. دعنا نلقي نظرة فاحصة على كل منها:

### الطريقة 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

تكون هذه الطريقة جيدة فقط إذا كنت بحاجة إلى دمج ملفين PDF فقط. توفر الحجتان الأوليان (firstInputFile و secInputFile) الأسماء الكاملة للملفات مع مسار تخزينهما لملفي PDF المدخلين اللذين سيتم دمجهما. توفر الحجة الثالثة (outputFile) الاسم المطلوب مع مسار ملف PDF الناتج.

![دمج ملفين PDF باستخدام أسماء الملفات](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### الطريقة 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

على غرار الطريقة السابقة، تتيح هذه الطريقة أيضًا دمج ملفين PDF. توفر الحجتان الأوليان (firstInputStream و secInputStream) ملفي PDF المدخلين كتيارات (التيار هو مصفوفة من البتات/البايتات) التي سيتم دمجها. توفر الحجة الثالثة (outputStream) تمثيل التيار لملف PDF الناتج المطلوب.

![دمج ملفين PDF باستخدام تيارات الملفات](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### الطريقة 3

- Concatenate(Stream inputStreams[], Stream outputStream)

إذا كنت ترغب في دمج أكثر من ملفين PDF، فإن هذه الطريقة ستكون خيارك النهائي. توفر الحجة الأولى (inputStreams[]) ملفات PDF المدخلة في شكل مصفوفة من التيارات التي سيتم دمجها. توفر الحجة الثانية (outputStream) تمثيل التيار لملف PDF الناتج المطلوب.

![دمج عدة ملفات PDF باستخدام مصفوفة من التيارات](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```