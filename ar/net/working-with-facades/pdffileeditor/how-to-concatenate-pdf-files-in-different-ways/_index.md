---
title: دمج ملفات PDF باستخدام .NET 5 
linktitle: كيفية دمج PDF
type: docs
weight: 75
url: /ar/net/how-to-concatenate-pdf-files-in-different-ways/
description: يوضح هذا المقال الطرق الممكنة لدمج أي عدد من ملفات PDF الموجودة في ملف PDF واحد.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

يصف هذا المقال كيفية [دمج](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) مستندات PDF متعددة في مستند PDF واحد بمساعدة [Aspose.PDF for .NET](/pdf/ar/net/). يجعل [Aspose.PDF for .NET](/pdf/ar/net/) هذه المهمة سهلة للغاية.

{{% /alert %}}

كل ما عليك فعله هو استدعاء طريقة [دمج](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) وسيتم دمج جميع ملفات PDF المدخلة الخاصة بك معًا وسيتم إنشاء ملف PDF واحد. لنقم بإنشاء تطبيق لممارسة دمج ملفات PDF. سنقوم بإنشاء تطبيق باستخدام Visual Studio.NET 2019.

{{% alert color="primary" %}}

يمكن استخدام Aspose.PDF for .NET في أي نوع من التطبيقات التي تعمل على .NET Framework سواء كان تطبيق ويب ASP.NET أو تطبيق ويندوز.

{{% /alert %}}

## كيفية دمج ملفات PDF بطرق مختلفة

في النموذج، هناك ثلاثة صناديق نصية (textBox1, textBox2, textBox3) تحتوي على تسميات الروابط الخاصة بها (linkLabel1, linkLabel2, linkLabel3) لتصفح ملفات PDF. عند النقر على "تصفح" في تسمية الرابط، سيظهر مربع حوار إدخال ملف (inputFileDialog1) الذي سيمكننا من اختيار ملفات PDF (للدمج).

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

يتم عرض واجهة تطبيق نموذج ويندوز لعرض فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) لدمج ملفات PDF.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

بعد اختيار ملف PDF والضغط على زر OK، يتم تخصيص الاسم الكامل للملف مع المسار إلى مربع النص المرتبط.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

وبالمثل، يمكننا اختيار ملفين أو ثلاثة ملفات PDF للإدخال لدمجها كما هو موضح أدناه:

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

سيأخذ مربع النص الأخير (textBox4) مسار الوجهة لملف PDF الناتج باسمه حيث سيتم إنشاء هذا الملف الناتج.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## دالة Concatenate()

يمكن استخدام دالة Concatenate() بثلاث طرق. دعونا نلقي نظرة أقرب على كل منها:

### الطريقة 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

هذه الطريقة جيدة فقط إذا كنت بحاجة لدمج ملفي PDF فقط. أول حجتين (firstInputFile و secInputFile) توفران الأسماء الكاملة للملفات مع مسار التخزين الخاص بملفي PDF اللذين سيتم دمجهما. الحجة الثالثة (outputFile) توفر اسم الملف المطلوب مع المسار الخاص بملف PDF الناتج.

![دمج ملفي PDF باستخدام أسماء الملفات](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### النهج 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

مماثل للنهج أعلاه، هذا النهج يسمح أيضًا بدمج ملفي PDF. أول وسيطين (firstInputStream و secInputStream) يوفران ملفي PDF المدخلين كتيارات (التيار هو مجموعة من البتات/البايتات) التي سيتم دمجها. الوسيط الثالث (outputStream) يوفر تمثيل التيار لملف PDF المطلوب كخرج.

![دمج ملفي PDF باستخدام تيارات الملفات](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdf1,pdf2,outputPDF);
  outputPDF.Close();
}
```

### النهج الثالث

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

إذا كنت ترغب في دمج أكثر من ملفي PDF، فإن هذا النهج سيكون خيارك الأمثل. First argument (inputStreams[]) يوفر ملفات PDF المدخلة في شكل مصفوفة من التدفقات التي سيتم دمجها. Second argument (outputStream) يوفر تمثيل التدفق لملف PDF المطلوب.

![دمج ملفات PDF متعددة باستخدام مصفوفة من التدفقات](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream pdf3 = new FileStream(textBox3.Text,FileMode.Open);
  Stream[] pdfStreams = new Stream[]{pdf1,pdf2,pdf3};
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdfStreams,outputPDF);
  outputPDF.Close();
}
```